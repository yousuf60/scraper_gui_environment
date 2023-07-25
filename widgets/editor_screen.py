from simplekivy import SimpleKivy
s = SimpleKivy(make_app=False)

s.build("""
<Editor_Scr>:
    Button:
        text:"editor"
        on_press:
            root.parent.transition.direction="left"
            root.parent.current="data"
""")

class Editor_Scr(s.Screen):pass
