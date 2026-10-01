#!/usr/bin/env python


import pandas as pd
import matplotlib.pyplot as plt


# read data
data = pd.read_csv("weather_data.csv")

# combine 'date' and 'time' into a single column 'recorded_at' as type datetime
data["recorded_at"] = pd.to_datetime(data["date"] + " " + data["time"])

# set 'recorded_at' as index for convenience
data = data.set_index("recorded_at")

def process_month(month_data,name_prefix):
    plot_timeseries(month_data, name_prefix,
                    column="air_temperature_celsius",
                    color="red",
                    title="air temperatur (c) at Helsinki airport",
                    plot_type="temperature",
                    show_mean=True)

    plot_timeseries(month_data, name_prefix,
                    column="precipitation_mm",
                    color="blue",
                    title="precipitation (mm) at Helsinki airport",
                    plot_type="precipitation")


def plot_timeseries(month_data,
                    name_prefix,
                    column,
                    color,
                    title,
                    plot_type,
                    show_mean=False):

    fig, ax = plt.subplots()
    
    # precipitation time series
    ax.plot(
        month_data.index,
        month_data[column],
        label=column,
        color=color,
    )
    
    ax.set_title(title)
    ax.set_xlabel("date and time")
    ax.set_ylabel(column)
    ax.legend()
    ax.grid(True)
   
    # optional logic to show the mean
    if show_mean:
        values = month_data[column].values
        mean_value = sum(values) / len(values)
        
        ax.axhline(
            y=mean_value,
            label=f"mean {column} (C): {mean_value:.1f}",
            color=color,
            linestyle="--",
        )
 
    # format x-axis for better date display
    fig.autofmt_xdate()
    
    fig.savefig(f"{name_prefix}-{plot_type}.png")

# keep only january data using datetime period indexing
january = data.loc["2024-01"]
process_month(january,"2024-01")

february = data.loc["2024-02"]
process_month(february,"2024-02")

march = data.loc["2024-03"]
process_month(march,"2024-03")
