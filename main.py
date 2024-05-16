from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '506')

from kivymd.app import MDApp

from screens.parallaxscreen import ParallaxScreen

class MainApp(MDApp):
    def build(self):
        self.title = 'Game Parallax'
        
    def on_start(self):
        self.root.current= 'parallax_screen'
        
if __name__ == '__main__':
    MainApp().run()