from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

Window.size = (400, 600)


class Weather(GridLayout):
    temperature = StringProperty("None")
    city = StringProperty("None")
    result = StringProperty("None")

    def weather(self, widget):
        self.city = widget.text
        print(self.city)
        owm = OWM('a99a76ecfd5f4739737d50a7f8604843')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(self.city)
        w = observation.weather
        self.temperature = str(w.temperature('celsius') ['temp'])

    def click(self):
        self.result = self.temperature

class TheWeatherApp(App):
    pass



if __name__ == '__main__':
    TheWeatherApp().run()