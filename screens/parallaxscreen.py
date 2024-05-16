from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior

class PlayButton(CircularRippleBehavior, ButtonBehavior, Image):
    pass

class ScrollingBackground(MDBoxLayout):
    ground_texture = ObjectProperty(None)
    mountain_texture = ObjectProperty(None)
    clouds_texture = ObjectProperty(None)
    cake_texture = ObjectProperty(None)
    trees_texture = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mountain_texture = Image(source = 'assets/layers/2_mountain.png').texture
        self.mountain_texture.wrap = 'repeat'
        
        self.clouds_texture = Image(source = 'assets/layers/3_clouds.png').texture
        self.clouds_texture.wrap = 'repeat'
        
        self.cake_texture = Image(source = 'assets/layers/4_cake.png').texture
        self.cake_texture.wrap = 'repeat'
        
        self.trees_texture = Image(source = 'assets/layers/5_trees.png').texture
        self.trees_texture.wrap = 'repeat'
        
        self.ground_texture = Image(source = 'assets/layers/6_ground.png').texture
        self.ground_texture.wrap = 'repeat'
        
    def scroll_textures(self, time):
        
        self.mountain_texture.uvpos = (
            (self.mountain_texture.uvpos[0] + time/100)%Window.width, self.mountain_texture.uvpos[1]
            )
        texture = self.property('mountain_texture')
        texture.dispatch(self)
        
        self.clouds_texture.uvpos = (
            (self.clouds_texture.uvpos[0] + time/80)%Window.width, self.clouds_texture.uvpos[1]
            )
        texture = self.property('clouds_texture')
        texture.dispatch(self)
        
        self.cake_texture.uvpos = (
            (self.cake_texture.uvpos[0] + time/40)%Window.width, self.cake_texture.uvpos[1]
            )
        texture = self.property('cake_texture')
        texture.dispatch(self)
        
        self.trees_texture.uvpos = (
            (self.trees_texture.uvpos[0] + time/20)%Window.width, self.trees_texture.uvpos[1]
            )
        texture = self.property('trees_texture')
        texture.dispatch(self)
        
        self.ground_texture.uvpos = (
            (self.ground_texture.uvpos[0] + time/10)%Window.width, self.ground_texture.uvpos[1]
            )
        texture = self.property('ground_texture')
        texture.dispatch(self)
    

class ParallaxScreen(Screen):
    
    def update_frames(self):
        self.remove_widget(self.ids.play)
        Clock.schedule_interval(self.ids.scrolling_background.scroll_textures, 1/60)   