from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class m_to_km_converter(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 130)
        self.title = "M to Km Converter"
        self.root = Builder.load_file('m_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            miles = int(self.root.ids.input_m.text) + increment
        except ValueError:
            miles = 0
        self.root.ids.input_m.text = str(miles)

    def handle_convert(self, input_m):
        kilometres = input_m / 0.621
        self.root.ids.output_label.text = str(kilometres)

m_to_km_converter().run()