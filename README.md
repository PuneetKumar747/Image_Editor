# **🖼️ Flask Image Editor & Filter App** 🎨  

A **Flask-based web application** that allows users to **upload, edit, and download images** with various transformations and filters such as **cropping, rotating, blurring, flipping, and pencil sketch effects**.  

This lightweight and easy-to-use app lets you apply **real-time image filters** through a simple web interface.  

---

## **🚀 Features**  

✅ **Upload Images** – Supports both **file uploads** and **image URLs**.  

✅ **Apply Filters & Transformations** –  
   - 📏 **Crop** – Select a specific region of an image.  
   - 🔄 **Rotate** – Rotate images by a custom angle.  
   - 🎨 **Blur** – Apply a Gaussian blur effect with adjustable intensity.  
   - ✏️ **Pencil Sketch** – Convert an image into a **sketch-style drawing**.  
   - 🖼️ **Flip** – Mirror an image **horizontally or vertically**.  

✅ **Live Preview** – See the filtered image before downloading.  

✅ **Download Processed Images** – Save your edited images in **PNG, JPEG, or other formats**.  

---

## **⚙️ Tech Stack**  

| **Technology**      | **Usage** |
|--------------------|-------------|
| 🐍 **Flask (Python)** | Backend framework |
| 🖼️ **Pillow (PIL)** | Image processing (cropping, blurring, sketch effect) |
| 🔗 **Requests** | Fetch images from URLs |
| 🏗 **HTML, CSS, Jinja** | Web UI templates |
| 📡 **Base64 Encoding** | Image processing & transfer |
| 🌍 **Bootstrap (Optional)** | Responsive UI styling |

---

## **📥 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/PuneetKumar747/Flask_Image_Editor.git
cd Flask-Image-Editor
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**  
```bash
python app.py
```
- Open your browser and go to:  
  ```bash
  http://127.0.0.1:5000
  ```

---

## **🎯 How to Use**  

1️⃣ **Upload an Image** – Choose a file or enter an image URL.  
2️⃣ **Select a Filter** – Crop, Rotate, Blur, Sketch, Flip, etc.  
3️⃣ **Apply the Transformation** – See the edited image.  
4️⃣ **Download the Processed Image** – Save it in your preferred format.  

---

## **🛠️ Contributing**  

Want to improve this project?  

1. **Fork** the repository.  
2. **Create a new branch** (`git checkout -b feature-newFeature`).  
3. **Commit your changes** (`git commit -m "Added new feature"`).  
4. **Push to GitHub** (`git push origin feature-newFeature`).  
5. **Open a Pull Request** and describe your changes.  

---

