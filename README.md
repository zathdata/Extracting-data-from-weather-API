# Extracting Data from a Weather API 

## Overview

This repository contains a python script that connects to a third-party weather API, fetch real-time weather data for a specified location, and then process and store the extracted information into csv file.

Its a simple script used to practice API data extraction. The API used is from `https://openweathermap.org/api`

---

## Features

* **API Integration:** Handles HTTP requests to a weather API.
* **Data Extraction:** Retrieves key weather parameters.
* **Data Persistence:** Saves the fetched data into a `weather.csv` file for easy analysis and subsequent use.

---

## Prerequisites

Before running the script, ensure you have the following:

1.  **Python 3 installed on your system.
2.  Register on `https://openweathermap.org/` and get your API key.

---

## Setup

Follow these steps to get your local copy up and running.

### 1. Clone the repository

### 2. Install dependencies

```
pip install -r requirements.txt
```
### 3. API Key

Add your API key to the API_KEY variable or create an environment file `.env` to store your API key with `API_KEY=YOUR_KEY`

## Usage

After setting up, you can run the `main.py` and fetch the data from the API. 

You can change the cities you want to look for, change the keys/columns, and choose what other different type of data by looking at the APIs documentation. 
