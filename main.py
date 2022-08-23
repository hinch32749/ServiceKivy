from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "618")

from kivymd.uix.behaviors import FakeRectangularElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MyCamera(Camera):
    """class for new camera"""

class CardWithElevation(
    RectangularRippleBehavior,
    FakeRectangularElevationBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    md_bg_color=[255/255, 255/255, 255/255, 1]


class CardWithElevationForGarageCar(
    FakeRectangularElevationBehavior,
    MDBoxLayout,
):
    md_bg_color=[255/255, 255/255, 255/255, 1]


class ServiceCar(MDScreen):

    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png('./images/cam_img.png')
        # img = self.ids['image_photo']
        # img.source = './images/cam_img.png'


    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file('servicecarmain.kv')


class ServiceCarMain(MDApp):
    def build(self):
        return ServiceCar()


ServiceCarMain().run()
