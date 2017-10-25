
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.10.0')


# class ScatterTextWidget(BoxLayout):
#     pass
# <ScatterTextWidget>
#     orientation: 'vertical'
#     TextInput:
#         id: my_textinput
#         font_size: 150
#         size_hint_y: None
#         height: 200
#         text: 'default'
#     FloatLayout:
#         Scatter:
#             Label:
#                 text: my_textinput.text
#                 font_size:150


class WelcomeWindowWidget(BoxLayout):
    pass


class Planner(App):

    def build(self):
        # return ScatterTextWidget()
        return WelcomeWindowWidget()

if __name__ == '__main__':
    Planner().run()
