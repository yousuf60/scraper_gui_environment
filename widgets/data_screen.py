from simplekivy import SimpleKivy
import webbrowser
s = SimpleKivy(make_app=False)

mainthread = s.clock.mainthread
s.build("""
<Btn>:
    size_hint: 1, None
    halign:"center"
    text_size: self.width - dp(20), None

    height:self.texture_size[1] + dp(60)
    

<DataScr>:
    BoxLayout:
        orientation: "vertical"
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
        BoxLayout:
            size_hint: 1, None
            height: dp(55)
            Button:
                text:"clear"
                on_release:
                    root.ids.btn_list.clear_widgets()
            Button:
                text:"editor"
                on_press:
                    root.parent.transition.direction="right"
                    root.parent.current="editor"

        
                
""")
class Btn(s.Button):
    link = s.StringProperty("")
    text = s.StringProperty("")
    background_color = [.9, .9, .9, .9]
    def on_press(self):
        webbrowser.open(self.link)

class DataScr(s.Screen):
    @mainthread
    def add_btn(self, text_link: list):
        if len(text_link) == 2:
            btn = Btn(text = str(text_link[0]))
            btn.link = str(text_link[1])
            self.add_to_list(btn)

    @mainthread
    def add_to_list(self, widget):
        self.ids.btn_list.add_widget(widget)
