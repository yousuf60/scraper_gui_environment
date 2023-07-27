from simplekivy import SimpleKivy
s = SimpleKivy(make_app=False)

s.build("""
<EditorScr>:
    CodeInput:
        id: code_input
        text: root.input_text
        hint_text: "type a function code"
        background_color: .9, .9, .9, .9
    BoxLayout:
        Button:
            text:"exec"
            size_hint: 1, .1
            on_press:
                root.parent.transition.direction="left"
                root.parent.current="data" 
                root.code_in()

                print(root.parent.get_screen("data").ids.btn_list)
        Button:
            text:"back"
            size_hint: 1, .1
            on_press:
                root.parent.transition.direction="left"
                root.parent.current="data"
""")

class EditorScr(s.Screen):
    with open("code.txt") as f:
        input_text = f.read()

    def edit_str_code(self, code):
        return code.replace("\n", "\n\t")

    def execute(self, code):
        exec("def x():" + self.edit_str_code(code))
        for i in locals()["x"]():
            yield i

    
    def code_in(self):
    
        if self.ids.code_input.text:
            code_input_text = self.ids.code_input.text
            with open("code.txt", "w") as f:
                f.write(code_input_text)
                self.use_yields(self.execute("\n" + code_input_text))
    def use_yields(self, generator):
        for i in generator:
            print(i)

        
