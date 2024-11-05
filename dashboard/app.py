from shiny import reactive, render
from shiny.express import input
from datetime import datetime
import random
from faicons import icon_svg
# From shiny.express, import just ui
from shiny.express import ui
from scipy import stats
import matplotlib.pyplot as plt

ui.tags.link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css")

# Define temperature data for different locations with sufficient readings
temperature_data = {
    "Dome A": [round(random.uniform(-18, -16), 1) for _ in range(10)],
    "McMurdo": [round(random.uniform(-10, 0), 1) for _ in range(10)],
    "Vostok": [round(random.uniform(-20, -15), 1) for _ in range(10)],
    "Amundsen-Scott": [round(random.uniform(-15, -5), 1) for _ in range(10)],
}


# Constants
UPDATE_INTERVAL_SECS: int = 1

# Define the UI

ui.page_opts(title="Kersha: Antarctic Temperature Tracker", fillable=True),

# Add CSS for background color
ui.tags.style("""
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'); /* Import a Google Font */

    body {
        background-color: #f0f8ff; /* Light blue background */
        font-family: 'Roboto', sans-serif; /* Apply the font globally */
    }

    h2 {
        font-weight: 700; /* Bold font for headers */
    }

    .center-img {
        display: block;
        margin: auto;
        width: 150px; /* Adjust width as needed */
    }
""")

with ui.sidebar(open="open"):

    ui.h2("Antarctic Explorer", class_="text-center")

    ui.div(ui.tags.i(class_="fas fa-sun", style="font-size: 2em; color: orange;"), class_="text-center")
# Location selector dropdown
    ui.input_select("location", "Select Location", choices=["Dome A", "McMurdo", "Vostok", "Amundsen-Scott"], selected="McMurdo")


  # Display the penguin image from the provided URL
    ui.img(
        src="https://media.istockphoto.com/id/147290529/photo/emperors.jpg?s=612x612&w=0&k=20&c=ZApZFJtKoXGKYYJsgNcNPTMHqqSbbAx9CBg2AF2qyJk=",
        alt="Emperor Penguins",
        class_="center-img"
    )

    ui.p(
    ui.tags.i(class_="fas fa-thermometer-half", style="font-size: 1.5em; color: red;"),
    " Real-time temperature trend with linear regression analysis."
    )

    ui.hr()

    ui.h6("Links:")

    ui.a(
        ui.tags.i(class_="fab fa-github", style="font-size: 1.5em; color: black;"),
        " An Interactive Insight to the Penguin Species of Antarctica",
        href="https://github.com/kersha0530/cintel-04-local",
        target="_blank",
    )

    ui.a(
        ui.tags.i(class_="fab fa-github", style="font-size: 1.5em; color: black;"),
        " GitHub App",
        href="https://github.com/kersha0530/cintel-05-cintel",
        target="_blank",
    )

    ui.a(
        ui.tags.i(class_="fa-brands fa-github" , style="font-size: 1.5em; color: black;"),
        "GitHub Source",
        href="https://github.com/kersha0530/cintel-05-cintel",
        target="_blank",
    )

    ui.a(
        ui.tags.i(class_="fas fa-shield-alt", style="font-size: 1.5em; color: darkblue;"),
        " PyShiny",
        href="https://shiny.posit.co/py/",
        target="_blank"
    )

#---------------------------------------------------------------------
# In Shiny Express, everything not in the sidebar is in the main panel
#---------------------------------------------------------------------
    
ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")
icon_svg("sun")

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"

@render.text
def display_location():
    latest_dictionary_entry = reactive_calc_combined()
    return latest_dictionary_entry['location']

@render.text
def display_avg_temp():
    latest_dictionary_entry = reactive_calc_combined()
    location = latest_dictionary_entry['location']
    temps = temperature_data[location]
    avg_temp = sum(temps) / len(temps) if temps else None
    return f"Average Temperature: {avg_temp} °C" if avg_temp is not None else "No data available"

@render.text
def display_min_temp():
    latest_dictionary_entry = reactive_calc_combined()
    location = latest_dictionary_entry['location']
    min_temp = min(temperature_data[location]) if temperature_data[location] else None
    return f"Minimum Temperature: {min_temp} °C" if min_temp is not None else "No data available"

@render.text
def display_max_temp():
    latest_dictionary_entry = reactive_calc_combined()
    location = latest_dictionary_entry['location']
    max_temp = max(temperature_data[location]) if temperature_data[location] else None
    return f"Maximum Temperature: {max_temp} °C" if max_temp is not None else "No data available"


 # Display the current data (location, average temp, min temp, max temp) 
with ui.layout_columns(): 
    with ui.card(): 
        ui.card_header("Current Data") 
        ui.p("Location:") 
       
   
# Display the plot 
with ui.layout_columns(): 
    with ui.card(): 
        ui.card_header("Current Chart") 
        
@render.image
def temperature_plot():
    location = input.location()
    plot_temperature_data(location)
    
    # Ensure the path is correct
    img_path = "C:\\Users\\kbrou\\OneDrive\\Documents\\temperature_plot.png"
    
    return {
        "src": img_path,
        "alt": f"Temperature Trends at {location}",
        "height": "400px"
    }

def plot_temperature_data(location):
    plt.figure(figsize=(10, 5))

    if location in temperature_data and temperature_data[location]:
        plt.plot(temperature_data[location], marker='o')
        plt.title(f'Temperature Trends at {location}')
        plt.xlabel('Time (last 10 readings)')
        plt.ylabel('Temperature (°C)')
        plt.xticks(range(len(temperature_data[location])), [f'Reading {i+1}' for i in range(len(temperature_data[location]))])
        plt.grid()
    else:
        plt.title(f'No data available for {location}')
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center', fontsize=15)

    plt.tight_layout()
    plt.savefig('C:\\Users\\kbrou\\OneDrive\\Documents\\temperature_plot.png')  # Save the plot with the full path
    plt.close()



# Server logic
def app_server(input, output, session):
    @output
    @render.text
    def display_temp():
        latest_entry = reactive_calc_combined()
        return f"{latest_entry['temp']} °C"

    @output
    @render.text
    def display_time():
        latest_entry = reactive_calc_combined()
        return f"{latest_entry['timestamp']}"


        
@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Get the selected location from the input
    selected_location = input.location()

    # Ensure we are handling a valid selected location
    if selected_location in temperature_data and temperature_data[selected_location]:
        temp = temperature_data[selected_location][-1]  # Get the latest temperature
    else:
        temp = None  # Handle unexpected location or empty data

    # Get a timestamp for "now"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp, "location": selected_location}

    # Return everything we need
    return latest_dictionary_entry
