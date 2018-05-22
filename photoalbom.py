from kivy.app import App
from kivy.uix.image import Image

class PhotoalbomApp(App):
    def build(self):
        image_A_1={1:"ImageDatabase/agel.jpg"}
        literal_A=[image_A_1]
        img=Image( source=image_A_1[1], size_hint=[.5, .5])

        

        
        

        return img

# PhotoalbomApp().run()
