from shiny import reactive, render
from datetime import datetime
import random
from faicons import icon_svg
# From shiny.express, import just ui
from shiny.express import ui

# Constants
UPDATE_INTERVAL_SECS: int = 1

# Define the UI

ui.page_opts(title="Kersha: Live Data (Basic)", fillable=True),

with ui.sidebar(open="open"):

    ui.h2("Antarctic Explorer", class_="text-center")

    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

    ui.hr()

    ui.h6("Links:")

    ui.a(
        "GitHub Source",
        href="https://github.com/kersha0530/cintel-05-cintel",
        target="_blank",
    )

    ui.a(
        "GitHub App",
        href="https://github.com/kersha0530/cintel-05-cintel",
        target="_blank",
    )

    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")

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


with ui.layout_columns():
    with ui.card():
        ui.card_header("Current Data (placeholder only)")

with ui.layout_columns():
    with ui.card():
        ui.card_header("Current Chart (placeholder only)")


# Reactive calculation for live data
@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now" and use string format strftime() method to format it
    # 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return everything we need
    return latest_dictionary_entry

# Server logic
def app_server(input, output, session):
    @output
    @render.text
    def display_temp():
        latest_entry = reactive_calc_combined()
        return f"{latest_entry['temp']} C"

    @output
    @render.text
    def display_time():
        latest_entry = reactive_calc_combined()
        return f"{latest_entry['timestamp']}"



