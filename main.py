from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# from photoalbom import PhotoalbomApp

class GlossaryApp(App):
    def build(self):
        background=AnchorLayout(anchor_x="center", anchor_y="center")
        alphabet=GridLayout(cols=6,  size_hint=[.8, .8], spacing=5)
        alphabetData=["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        list_image_A={1:"ImageDatabase/agel.jpg", 2:"ImageDatabase/apricot.jpg"}
        list_image_B={1:"ImageDatabase/baker.jpg", 2:"ImageDatabase/builder.jpg"}
        # obj={"A":"dist"}
        # def callback(instance):

            # PhotoalbomApp().run()
        def words_A(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_A[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( img )
            next_img.bind(on_press=words_A_2)
            # background.remove_widget( next_img )

        def words_A_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_A[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al.add_widget( next_img )
            background.add_widget( al )
            next_img.bind(on_press=exit_img)

        def words_B(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_B[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( img )
            next_img.bind(on_press=words_B_2)
            # background.remove_widget( next_img )

        def words_B_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_B[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al.add_widget( next_img )
            background.add_widget( al )
            next_img.bind(on_press=exit_img)
            
            

        def exit_img(instance):
            print("Выход")
            background.clear_widgets()
            background.add_widget(alphabet)

        for x in range(len(alphabetData)):
            btn=Button(text=alphabetData[x], size_hint=[.05, .05])
            alphabet.add_widget( btn )
            
            if(btn.text=="A"):
                btn.bind(on_press=words_A)

            if(btn.text=="B"):
                btn.bind(on_press=words_B)

        
        
        

        
            

            # btn.bind(on_press=callback)

        

        background.add_widget( alphabet )
        
        return(background)


if __name__ == "__main__":
    GlossaryApp().run()