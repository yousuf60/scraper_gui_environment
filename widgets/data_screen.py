from simplekivy import SimpleKivy
s = SimpleKivy(make_app=False)

s.build("""
<Btn>:
    size_hint: 1, None
    height: dp(60)
    background_color: 1, 0, 0, .7
<DataScr>:
    RecycleView:
        BoxLayout:
            orientation: "vertical"
            size_hint: 1, None
            height: self.minimum_height
            BoxLayout:
                id: btn_list
                orientation: "vertical"
                pos_hint: {"center_x": .5}
                size_hint: .9, None
                height: self.minimum_height
                spacing: dp(20)
                Btn:
                    text: "Fwef"
                Btn:
                Btn:
                Btn:

    Button:
        text:"editor"
        size_hint: 1, .1
        on_press:
            root.parent.transition.direction="right"
            root.parent.current="editor"
            
""")
class Btn(s.Button):pass
class DataScr(s.Screen):pass
