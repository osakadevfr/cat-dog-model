import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np

# Load the trained model
model = load_model("cd_model.h5")
IMG_SIZE = (128, 128)

# Prediction function
def predict_image(img_path):
    img = keras_image.load_img(img_path, target_size=IMG_SIZE)
    img_array = keras_image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        return f"🐶 That's a mofo'king DOG! ({prediction:.2f})"
    else:
        return f"🐱 That's a CAT. ({1 - prediction:.2f})"

# GUI setup
def choose_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        img = Image.open(file_path).resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        result = predict_image(file_path)
        result_label.config(text=result)

# Window
root = tk.Tk()
root.title("Cat or Mofo'king Dog Classifier")
root.geometry("300x400")
root.configure(bg="#222222")

# Button
btn = tk.Button(root, text="Pick Image", command=choose_image, font=("Arial", 14), bg="#333", fg="#fff")
btn.pack(pady=20)

# Image display
image_label = tk.Label(root, bg="#222")
image_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="#00FF00", bg="#222")
result_label.pack(pady=10)

root.mainloop()
