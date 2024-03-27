from PIL import Image as PILImage
from tkinter import *
from tkinter import filedialog

gui = Tk()
gui.geometry('250x170')
gui.title('Encription and Decription')

def encrypt_image():
    input_image_path = filedialog.askopenfilename(filetypes=[('jpeg file', '*.jpeg')])
    key_text = (key1.get("1.0", 'end-1c'))
    try:
        key = int(key_text)  # Converting the key text to an integer
        if key < 1 or key > 255:
            raise ValueError("Key must be between 1 and 255")
    except ValueError:
        print("Error: Key must be an integer between 1 and 255")
        return
    
    
    input_image = PILImage.open(input_image_path)
    input_image = input_image.convert("RGB")
    
    encrypted_image = PILImage.new(input_image.mode, input_image.size)
    
    width, height = input_image.size
    
    for x in range(width):
        for y in range(height):

            pixel = input_image.getpixel((x, y))
            encrypted_pixel = tuple([(p ^ key) for p in pixel])  #encrypting or decrypring using XOR operation
            encrypted_image.putpixel((x, y), encrypted_pixel)
    
    
    output_image_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[('jpeg file', '*.jpeg')])
    encrypted_image.save(output_image_path)



b1 = Button(gui, text='Encrypt', command=encrypt_image)
b1.place(x=70, y=100)
b2 = Button(gui, text='Decrypt', command=encrypt_image)
b2.place(x=70, y=130)

key1 = Text(gui, height=3, width=10)
key1.place(x=70, y=40)

gui.mainloop()
