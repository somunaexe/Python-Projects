from PIL import Image

def resize_image():
    image = Image.open('Python-Projects/resizer_project/profile_picture.jpg')
    print(f'Current size : {image.size}')
    resized_image = image.resize((500, 500))
    resized_image.save('Python-Projects/resizer_project/resized_profile_picture.jpg')

resize_image()