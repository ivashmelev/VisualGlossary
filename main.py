from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class GlossaryApp(App):
    def build(self):
        background=AnchorLayout(anchor_x="left", anchor_y="center")
        alphabet=GridLayout(cols=6,  size_hint=[.5, .5], spacing=5)
        alphabetData=["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        # obj={"A":"dist"}
        def callback(instance):
            print("Button")

        for x in range(26):
            btn=Button(text=alphabetData[x], size_hint=[.05, .05])
            alphabet.add_widget( btn )

            # if alphabetData[x]==0: Отбор вызовов

            btn.bind(on_press=callback)

        

        background.add_widget( alphabet )
        
        return(background)


if __name__ == "__main__":
    GlossaryApp().run()