from PIL import Image

def resize_image(size1, size2):
    image = Image.open('Python-Projects/resizer_project/profile_picture.jpg')
    print(f'Current size : {image.size}')
    resized_image = image.resize((size1, size2))
    resized_image.save(f'Python-Projects/resizer_project/resized_profile_picture_{str(size1)}_{str(size2)}.jpg')

inputSize1 = int(input("Enter the width you want the picture to be: "))
inputSize2 = int(input("Enter the length you want the picture to be: "))

resize_image(inputSize1, inputSize2)