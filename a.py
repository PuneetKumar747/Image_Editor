from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import io
import base64

app = Flask(__name__)

def colorful_sketch_filter(image):
    # Convert image to grayscale
    gray_image = ImageOps.grayscale(image)
    
    # Invert the grayscale image
    inverted_image = ImageOps.invert(gray_image)
    
    # Apply Gaussian blur to the inverted image
    blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Blend the blurred image with the original image using color dodge
    sketch_image = Image.new('RGB', image.size)
    for x in range(image.width):
        for y in range(image.height):
            original_color = image.getpixel((x, y))  # Retrieve color from original image
            sketch_color = blurred_image.getpixel((x, y))  # Retrieve color from blurred image
            r = min(int(original_color[0] + (original_color[0] * (sketch_color / 255))), 255)
            g = min(int(original_color[1] + (original_color[1] * (sketch_color / 255))), 255)
            b = min(int(original_color[2] + (original_color[2] * (sketch_color / 255))), 255)
            sketch_image.putpixel((x, y), (r, g, b))
    
    return sketch_image






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    img = Image.open(io.BytesIO(file.read()))
    
    filter_type = request.form['filter']
    if filter_type == 'crop':
        left = int(request.form['left'])
        right = int(request.form['right'])
        top_val = int(request.form['top'])
        bottom = int(request.form['bottom'])
        
        # Add padding to the crop area (e.g., 20% of the image height)
        padding = int(0.2 * img.height)  # Adjust the padding percentage as needed
        
        # Ensure crop dimensions are within the bounds of the image
        left = max(0, left)
        top_val = max(0, top_val - padding)  # Adjust top value to include padding
        right = min(img.width, right)
        bottom = min(img.height, bottom)
        
        # Validate crop dimensions
        if left >= right or top_val >= bottom:
            return "Invalid crop dimensions. Please ensure that the crop area is within the bounds of the image."
        
        img = img.crop((left, top_val, right, bottom))
    elif filter_type == 'rotate':
        angle = int(request.form['angle'])
        img = img.rotate(angle)
    elif filter_type == 'blur':
        intensity = int(request.form['intensity'])
        img = img.filter(ImageFilter.GaussianBlur(radius=intensity))
    elif filter_type == 'sketch':
        img = colorful_sketch_filter(img)  # Apply colorful sketch filter
    
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')  # Save as PNG format
    img_byte_array.seek(0)

    # Convert image bytes to base64 encoded string
    encoded_img = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return render_template('result.html', result_image=encoded_img)

if __name__ == '__main__':
    app.run(debug=True)
