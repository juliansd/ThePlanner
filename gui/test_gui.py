from kivy.app import App
from kivy.uix.button import Button
import kivy
kivy.require('1.10.0')



class TestApp(App):
    def build(self):
        return Button(text='Welcome to your Planner! Click to continue')

TestApp().run()

if __name__ == '__main__':
    TestApp().run()
