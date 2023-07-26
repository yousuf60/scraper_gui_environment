from simplekivy import SimpleKivy
s = SimpleKivy(make_app=False)

s.build("""
<EditorScr>:
    CodeInput:
        id: code_input
        background_color: .9, .9, .9, .9
    BoxLayout:
        Button:
            text:"exec"
            size_hint: 1, .1
            on_press:
                root.parent.transition.direction="left"
                root.parent.current="data" 
                root.execute()   
        Button:
            text:"editor"
            size_hint: 1, .1
            on_press:
                root.parent.transition.direction="left"
                root.parent.current="data"
""")

class EditorScr(s.Screen):
    def execute(self):
        print(self.ids.code_input.text)
        
