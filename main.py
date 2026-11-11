from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
import subprocess

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')


class MyApp(App):
    title = "Shutdown Timer"

    def build(self):
        return Builder.load_file("main.kv")

    def start_timer(self):
        time = self.root.ids.time_input.text
    
        subprocess.Popen([
            "dotnet", "run",
            "--project", "ShutdownTimer/ShutdownTimer.csproj",
            "--", "start", time
        ])

    def stop_timer(self):
        subprocess.Popen([
            "dotnet", "run",
            "--project", "ShutdownTimer/ShutdownTimer.csproj",
            "--", "stop"
        ])


MyApp().run()