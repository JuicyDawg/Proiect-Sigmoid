import tkinter as tk
import json
import requests
import random 
class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.city = tk.StringVar()
        self.city.set("London")
        self.api_key = "48e6d36936c69efbb8539e6a7dda33dc"
        self.weather_data = {}
        self.create_widgets()
    def create_widgets(self):
            
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

            
        tk.Label(search_frame, text="City").pack(side=tk.LEFT)
        city_entry = tk.Entry(search_frame, textvariable=self.city)
        city_entry.pack(side=tk.LEFT)

            
        search_button = tk.Button(search_frame, text="Search", command=self.get_weather_data)
        search_button.pack(side=tk.LEFT)

            
        weather_frame = tk.Frame(self.root)
        weather_frame.pack(pady=10)

        
        weather_label = tk.Label(weather_frame, text="")
        weather_label.pack(pady=10)

        graph_frame = tk.Frame(self.root)
        graph_frame.pack(pady=10)

        
        self.graph_canvas = tk.Canvas(graph_frame, width=400, height=200)
        self.graph_canvas.pack(pady=10)
    def get_weather_data(self):
        city = self.city.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
                data = json.loads(response.text)
                self.weather_data[city] = data
                self.display_weather_data(city)
        else:
            print("Error getting weather data")
    def display_weather_data(self, city):
        weather_data = self.weather_data[city]
        weather_label = tk.Label(self.root, text=f"Weather in {city}: {weather_data['weather'][0]['description']}\nTemperature: {weather_data['main']['temp']} K")
        weather_label.pack(pady=10)
    def create_graph(self):
            
        random_graph = []
        for i in range(10):
            random_graph.append(random.randint(0, 100))
            self.graph_canvas.delete("all")
            x_values = list(range(len(random_graph)))
            y_values = [i for i in random_graph]
            self.graph_canvas.create_line(x_values, y_values)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    app.run()
   
def open_sigmoid_ai():
    url = "https://www.instagram.com/sigmoid.ai/"
    webbrowser.open(url)

button = "Click me to visit Sigmoid.ai's Instagram!"


print(button)
open_sigmoid_ai()