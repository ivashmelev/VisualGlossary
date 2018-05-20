from kivy.app import App
from kivy.uix.image import Image

class PhotoalbomApp(App):
    def build(self):
        img=Image( source="ImageDatabase/agel.jpg", size_hint=[.5, .5])

        image_A_1={"agel":"ImageDatabase/agel.jpg"}

        literal_A=[image_A_1]
        

        return img

PhotoalbomApp().run()
