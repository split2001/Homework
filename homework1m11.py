from PIL import Image, ImageFilter
import requests
import matplotlib.pyplot as plt
import cv2


class MyImage:

    def __init__(self, name, url):
        self.url = url
        self.name = name

    def get_image(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            with open(self.name, 'wb') as f:
                f.write(r.content)

    def image_filter(self):
        image = Image.open(self.name)
        blurred_image = image.filter(ImageFilter.SMOOTH_MORE)
        blurred_image.save(self.name)

    def resize(self):
        image = Image.open(self.name)
        image = image.resize((600, 400))
        image.save(self.name)

    def histogram(self):
        image_obj = cv2.imread(self.name)
        plt.axis("on")
        plt.title(self.name)
        plt.imshow(cv2.cvtColor(image_obj, cv2.COLOR_BGR2RGB))
        plt.show()
        blue_color = cv2.calcHist([image_obj], [0], None, [256], [0, 256])
        red_color = cv2.calcHist([image_obj], [1], None, [256], [0, 256])
        green_color = cv2.calcHist([image_obj], [2], None, [256], [0, 256])
        plt.title("Histogram of all RGB Colors")
        plt.plot(blue_color, color="blue")
        plt.plot(green_color, color="green")
        plt.plot(red_color, color="red")
        plt.show()


img = MyImage('img1.jpg', 'https://puzzleit.ru/files/puzzles/144/144348/_original.jpg')
img.get_image()
img.image_filter()
img.resize()
img.histogram()
