# cintel-05-cintel
# Kersha: Antarctic Temperature Tracker
# Antarctic Temperature Tracker

## Overview

The Antarctic Temperature Tracker is a web application built using PyShiny to monitor and display real-time temperature data from various locations in Antarctica. The application allows users to select a location and view current temperature readings, historical data trends, and statistical information such as average, minimum, and maximum temperatures.

## Features

- Real-time temperature tracking for selected Antarctic locations.
- Display of current temperature, timestamp, and location.
- Plotting of temperature trends over time.
- Display of statistical data: average, minimum, and maximum temperatures.
- User-friendly UI with a location selector and penguin imagery for visual appeal.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kersha0530/antarctic-temperature-tracker.git
    cd antarctic-temperature-tracker
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application with the following command:
```bash
python app.py


## Installation Requirements

### requirements.txt

```txt
shiny
shiny-express
scipy
matplotlib
faicons

You can install them using `pip`:
```sh
pip install shiny shiny-express faicons matplotlib

## Acknowledgments

This project benefited from using ChatGPT, which was instrumental in helping solve challenges related to UI design, font integration, and dynamic data handling in the app.

* Types of Imports
## Standard Library Imports:

These are built-in modules that come with Python. For example:

import random
from datetime import datetime

## Third-Party Library Imports:

These are additional libraries you install via pip. For example:


from shiny.express import ui
from faicons import icon_svg
import matplotlib.pyplot as plt

Organize Imports:

Keep standard library imports at the top, followed by third-party imports, and then your own modules.

Example:

python
import random
from datetime import datetime

from shiny.express import ui
from faicons import icon_svg
import matplotlib.pyplot as plt

Use Aliases:

For readability and convenience, use aliases for long module names.

import matplotlib.pyplot as plt

Import Only What You Need:

## Instead of importing the entire module, import only the functions or classes you need.
from shiny import reactive, render

## Avoid Circular Imports:
Be cautious of importing modules that import each other, as this can lead to errors.

## Adding penguin visuals
-Adding the Image: The ui.img() function places the image in the sidebar with src pointing to the image URL or a local file path. Adjust the width to control the size, and you can add more styling with CSS (e.g., .center-img to center the image).
-Centering the Image (Optional): You could add CSS to center-align the image within the sidebar by adding .center-img { display: block; margin: auto; } to the CSS in ui.tags.style.

## changing the background color to light blue
To add a background color to your PyShiny app without modifying the existing ui.page_opts configuration or the interface structure, you can use ui.tags.style to add CSS directly within your app
-The ui.tags.style block is used to add CSS styling directly, setting the background-color for the entire body of the app.
-This keeps the structure and layout of your UI intact while applying the style.

## To bridge the information gap and connect data effectively, add a link to the interactive web app developed in Cintel-04-local.
 "An Interactive Insight to the Penguin Species of Antarctica",
        "https://kersha0530.github.io/cintel-04-local/"

## Enhancing the heading fonts to bold.
Font Import: @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'); imports the "Roboto" font. You can replace Roboto with any other font from Google Fonts.
font-family for body: This sets the font globally for all text elements within body.
Header Font Weight: font-weight: 700; applies bold styling to headers for better emphasis.
You can customize specific elements like headers (h2), paragraphs (p), or sidebar text by targeting those tags or classes within the CSS block.
