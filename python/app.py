import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock  # Import Clock for non-blocking updates

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.text_input = TextInput(hint_text="Enter how many secs: ", font_size=20, size_hint=(1, 0.2))
        self.label = Label(text="", font_size=24)
        button = Button(text="Start", size_hint=(1, 0.2), on_press=self.start_countdown)

        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.label)

        return layout

    def start_countdown(self, instance):
        """Starts the countdown by retrieving the input and using Clock to update the label."""
        try:
            self.seconds = int(self.text_input.text)  # Convert input to integer
            self.label.text = f"{self.seconds} seconds left"
            Clock.schedule_interval(self.update_timer, 1)  # Call update_timer every second
        except ValueError:
            self.label.text = "Enter a valid number!"

    def update_timer(self, dt):
        """Updates the countdown every second."""
        if self.seconds > 0:
            self.seconds -= 1
            mins, secs = divmod(self.seconds, 60)
            self.label.text = f"{mins:02}:{secs:02} left"
        else:
            self.label.text = "Time's up!"
            Clock.unschedule(self.update_timer)  # Stop the countdown when done

if __name__ == "__main__":
    MyApp().run()
