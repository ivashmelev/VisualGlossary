from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class GlossaryApp(App):
    def build(self):
        background=AnchorLayout()
        alphabet=GridLayout(cols=6, size_hint=[.5, .5], spacing=5)
        alphabetData=["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        for x in range(26):
            alphabet.add_widget( Button(text=alphabetData[x], size_hint=[.05, .05] ) )
        

        background.add_widget( alphabet )
        
        return(background)

    

if __name__ == "__main__":
    GlossaryApp().run()