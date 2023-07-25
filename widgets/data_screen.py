from simplekivy import SimpleKivy
s = SimpleKivy(make_app=False)

s.build("""
<Data_Scr>:
    Button:
        text:"s"
        on_press:
            root.parent.transition.direction="right"
            root.parent.current="editor"
""")

class Data_Scr(s.Screen):pass
