from simplekivy import SimpleKivy
from .data_screen import DataScr
from .editor_screen import EditorScr
s = SimpleKivy(title="scraper")
screenManager = s.build("""
ScreenManager:
    canvas.before:
        Color:
            rgba: .4, .4, .81, 1
        Rectangle:
            pos: self.pos
            size: self.size
    DataScr:
        name: "data"

    EditorScr
        name: "editor"
        
""")
