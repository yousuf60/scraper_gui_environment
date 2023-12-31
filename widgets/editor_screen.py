from simplekivy import SimpleKivy
from threading import Thread
s = SimpleKivy(make_app=False)

s.build("""
#: import Window kivy.core.window.Window
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
<EditorScr>:
    BoxLayout:
        orientation: "vertical"
        ScrollView:
            effect_cls: ScrollEffect
            CodeInput:
                id: code_input
                size_hint: None, None
                width: Window.width + (dp(len(self.text))*8)
                height: Window.height - dp(55)
                text: root.input_text
                hint_text: " Type a function code ..you should yield a list with two strings"
                background_color: .95, .95, .95, .9
                
            
            
        BoxLayout:
            size_hint: 1, None
            height: dp(55)
            Button:
                text:"exec"
                background_color: .95, .95, .95, 1
                on_press:
                    root.parent.transition.direction="left"
                    root.parent.current="data" 
                    root.code_in(root.parent.get_screen("data").add_btn)
                    
            Button:
                text:"back"
                background_color: .95, .95, .95, 1
                on_press:
                    root.parent.transition.direction="left"
                    root.parent.current="data"
""")

class EditorScr(s.Screen):
    with open("code.txt") as f:
        input_text = f.read()

    def edit_str_code(self, code):
        return code.replace("\n", "\n   ")

    def execute(self, add_btn, code):
        
        exec("def x():" + self.edit_str_code(code))
        for i in locals()["x"]():
            if type(i) is list:
                add_btn(i)

    
    def code_in(self, add_btn):
        if self.ids.code_input.text:
            code_input_text = self.ids.code_input.text
            with open("code.txt", "w") as f:
                f.write(code_input_text)
            Thread(target=lambda:self.execute(add_btn, "\n" + code_input_text)).start()
            


        
