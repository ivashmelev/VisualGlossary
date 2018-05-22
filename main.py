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
        list_image_C={1:"ImageDatabase/composer.jpg", 2:"ImageDatabase/croissant.jpg"}
        list_image_D={1:"ImageDatabase/doctor.jpg", 2:"ImageDatabase/donut.jpg"}
        list_image_E={1:"ImageDatabase/Eagle.jpg", 2:"ImageDatabase/eggs.jpg"}
        list_image_F={1:"ImageDatabase/fountain.jpg", 2:"ImageDatabase/furious.jpg"}
        list_image_G={1:"ImageDatabase/gloves.jpg", 2:"ImageDatabase/guitar.jpg"}
        list_image_H={1:"ImageDatabase/hairdresser.jpg", 2:"ImageDatabase/ham.jpg"}
        list_image_I={1:"ImageDatabase/ice cream.jpg", 2:"ImageDatabase/island.jpg"}
        list_image_J={1:"ImageDatabase/jam.jpg", 2:"ImageDatabase/judge.jpg"}
        list_image_K={1:"ImageDatabase/Kiwi.jpg", 2:"ImageDatabase/Knee.jpg"}
        list_image_L={1:"ImageDatabase/lawyer.jpg", 2:"ImageDatabase/lemon.jpg"}
        list_image_M={1:"ImageDatabase/milk.jpg", 2:"ImageDatabase/muffin.jpg"}
        list_image_N={1:"ImageDatabase/nervous.jpg", 2:"ImageDatabase/nurse.jpg"}
        list_image_O={1:"ImageDatabase/oil.jpg", 2:"ImageDatabase/oyster.jpg"}
        list_image_P={1:"ImageDatabase/pancakes.jpg", 2:"ImageDatabase/piano.jpg"}
        list_image_Q={1:"ImageDatabase/Quail.jpg", 2:"ImageDatabase/queue.jpg"}
        list_image_R={1:"ImageDatabase/restaurant.jpg", 2:"ImageDatabase/room.jpg"}
        list_image_S={1:"ImageDatabase/sausages.jpg", 2:"ImageDatabase/sound.jpg"}
        list_image_T={1:"ImageDatabase/tea.jpg", 2:"ImageDatabase/toast.jpg"}
        list_image_U={1:"ImageDatabase/unhappy.jpg", 2:"ImageDatabase/uniform.jpg"}
        list_image_V={1:"ImageDatabase/vet.jpg", 2:"ImageDatabase/volcano.jpg"}
        list_image_W={1:"ImageDatabase/whiskey.jpg", 2:"ImageDatabase/wine.jpg"}
        list_image_X={1:"ImageDatabase/Xerox.jpg"}
        list_image_Y={1:"ImageDatabase/Yacht.jpg", 2:"ImageDatabase/youngster.jpg"}
        list_image_Z={1:"ImageDatabase/zebra.jpg", 2:"ImageDatabase/zoo.jpg"}
        
        
        
        
        
        
        
        
        
        
        
        # obj={"A":"dist"}
        # def callback(instance):

            # PhotoalbomApp().run()
        def words_A(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Agel", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_A[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
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
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Apricot", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_B(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Baker", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_B[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
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
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Builder", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_C(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Composer", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_C[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_C_2)
            # background.remove_widget( next_img )

        def words_C_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_C[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Croissant", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_D(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Doctor", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_D[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_D_2)
            # background.remove_widget( next_img )

        def words_D_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_D[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Donut", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_E(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Eagle", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_E[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_E_2)
            # background.remove_widget( next_img )

        def words_E_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_E[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Eggs", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_F(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Fountain", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_F[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_F_2)
            # background.remove_widget( next_img )

        def words_F_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_F[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Furious", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_G(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Gloves", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_G[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_G_2)
            # background.remove_widget( next_img )

        def words_G_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_G[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Guitar", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_H(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Hairdresser", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_H[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_H_2)
            # background.remove_widget( next_img )

        def words_H_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_H[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Ham", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)
        
        def words_I(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Ice-cream", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_I[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_I_2)
            # background.remove_widget( next_img )

        def words_I_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_I[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Island", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_J(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Jam", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_J[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_J_2)
            # background.remove_widget( next_img )

        def words_J_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_J[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Judge", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_K(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Kiwi", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_K[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_K_2)
            # background.remove_widget( next_img )

        def words_K_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_K[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Knee", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_L(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Lawyer", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_L[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_L_2)
            # background.remove_widget( next_img )

        def words_L_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_L[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Lemon", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_M(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Milk", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_M[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_M_2)
            # background.remove_widget( next_img )

        def words_M_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_M[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Muffin", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_N(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Nervous", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_N[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_N_2)
            # background.remove_widget( next_img )

        def words_N_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_N[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Nurse", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_O(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Oil", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_O[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_O_2)
            # background.remove_widget( next_img )

        def words_O_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_O[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Oyster", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_P(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Pancakes", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_P[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_P_2)
            # background.remove_widget( next_img )

        def words_P_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_P[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Piano", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_Q(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Quail", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_Q[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_Q_2)
            # background.remove_widget( next_img )

        def words_Q_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_Q[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Queue", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_R(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Restaurant", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_R[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_R_2)
            # background.remove_widget( next_img )

        def words_R_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_R[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Room", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_S(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Sausages", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_S[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_S_2)
            # background.remove_widget( next_img )

        def words_S_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_S[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Sound", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_T(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Tea", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_T[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_T_2)
            # background.remove_widget( next_img )

        def words_T_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_T[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Toast", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_U(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Unhappy", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_U[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_U_2)
            # background.remove_widget( next_img )

        def words_U_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_U[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Uniform", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_V(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Vet", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_V[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_V_2)
            # background.remove_widget( next_img )

        def words_V_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_V[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Volcano", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_W(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Whiskey", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_W[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_W_2)
            # background.remove_widget( next_img )

        def words_W_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_W[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Wine", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_X(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Xerox", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_X[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=exit_img)
            # background.remove_widget( next_img )

        def words_Y(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Yacht", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_Y[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_Y_2)
            # background.remove_widget( next_img )

        def words_Y_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_Y[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Youngster", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
            next_img.bind(on_press=exit_img)

        def words_Z(instance):
            print ("Первое")
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Zebra", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            next_img=Button(text="next", size_hint=[.1, .1])
            al.add_widget( next_img )
            img=Image( source=list_image_Z[1], size_hint=[.8, .8])
            background.remove_widget( alphabet )
            background.add_widget( al )
            background.add_widget( al_top )
            background.add_widget( img )
            next_img.bind(on_press=words_Z_2)
            # background.remove_widget( next_img )

        def words_Z_2(instance):
            print ("Второе")
            background.clear_widgets()
            img=Image( source=list_image_Z[2], size_hint=[.8, .8])
            background.add_widget( img )
            next_img=Button(text="next", size_hint=[.1, .1])
            al = AnchorLayout(anchor_x="center", anchor_y="bottom", padding=10)
            al_top = AnchorLayout(anchor_x="center", anchor_y="top", padding=10)
            label=Label(text="Zoo", size_hint=[.3, .3], font_size=35, bold=True)
            al_top.add_widget( label )
            al.add_widget( next_img )
            background.add_widget( al )
            background.add_widget( al_top )
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

            elif(btn.text=="B"):
                btn.bind(on_press=words_B)

            elif(btn.text=="C"):
                btn.bind(on_press=words_C)

            elif(btn.text=="D"):
                btn.bind(on_press=words_D)

            elif(btn.text=="E"):
                btn.bind(on_press=words_E)
            
            elif(btn.text=="F"):
                btn.bind(on_press=words_F)

            elif(btn.text=="G"):
                btn.bind(on_press=words_G)

            elif(btn.text=="H"):
                btn.bind(on_press=words_H)

            elif(btn.text=="I"):
                btn.bind(on_press=words_I)

            elif(btn.text=="J"):
                btn.bind(on_press=words_J)

            elif(btn.text=="K"):
                btn.bind(on_press=words_K)

            elif(btn.text=="L"):
                btn.bind(on_press=words_L)

            elif(btn.text=="M"):
                btn.bind(on_press=words_M)

            elif(btn.text=="N"):
                btn.bind(on_press=words_N)

            elif(btn.text=="O"):
                btn.bind(on_press=words_O)

            elif(btn.text=="P"):
                btn.bind(on_press=words_P)

            elif(btn.text=="Q"):
                btn.bind(on_press=words_Q)

            elif(btn.text=="R"):
                btn.bind(on_press=words_R)

            elif(btn.text=="S"):
                btn.bind(on_press=words_S)

            elif(btn.text=="T"):
                btn.bind(on_press=words_T)

            elif(btn.text=="U"):
                btn.bind(on_press=words_U)

            elif(btn.text=="V"):
                btn.bind(on_press=words_V)
            
            elif(btn.text=="W"):
                btn.bind(on_press=words_W)

            elif(btn.text=="X"):
                btn.bind(on_press=words_X)

            elif(btn.text=="Y"):
                btn.bind(on_press=words_Y)

            elif(btn.text=="Z"):
                btn.bind(on_press=words_Z)




        
        
        

        
            

            # btn.bind(on_press=callback)

        

        background.add_widget( alphabet )
        
        return(background)


if __name__ == "__main__":
    GlossaryApp().run()