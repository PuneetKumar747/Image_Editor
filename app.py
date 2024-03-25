from flask import Flask, render_template, request, redirect, url_for, Response
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import io
import base64
import requests

app = Flask(__name__)

def pencil_sketch_filter(image):
    # Convert image to grayscale
    gray_image = image.convert('L')
    
    # Invert the grayscale image
    inverted_image = ImageOps.invert(gray_image)
    
    # Apply Gaussian blur to the inverted image
    blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Invert the blurred image
    final_image = ImageOps.invert(blurred_image)
    
    return final_image



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
        img = pencil_sketch_filter(img)  # Apply colorful sketch filter
    # images[i] = img
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')  # Save as PNG format
    img_byte_array.seek(0)

    # Convert image bytes to base64 encoded string
    encoded_img = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

    return render_template('result.html', result_image=encoded_img)

@app.route('/download', methods=['POST'])
def download():
    # Get image data and format from form submission
    image_data = request.form['image']
    format = request.form['format']

    # Decode base64 image data
    img_bytes = base64.b64decode(image_data)

    # Create file-like object from image data
    img_io = io.BytesIO(img_bytes)

    # Set content type based on format
    content_type = f'image/{format}'
    
    # Define default filename if not provided
    filename = 'filtered_image'
    if 'filename' in request.form:
        filename = request.form['filename']

    # Return the file data as a response
    return Response(img_io, mimetype=content_type, headers={'Content-Disposition': f'attachment;filename={filename}.{format}'})

if __name__ == '__main__':
    app.run(debug=True)
