import matplotlib.pyplot as plt


def plot_temperature_and_precipitation(
    month_data,
    month,
    output_directory,
):
    """Create temperature and precipitation plots for one month."""

    plot_timeseries(
        month_data=month_data,
        month=month,
        output_directory=output_directory,
        column="air_temperature_celsius",
        color="red",
        title="Air temperature (°C) at Helsinki Airport",
        plot_type="temperature",
        show_mean=True,
    )

    plot_timeseries(
        month_data=month_data,
        month=month,
        output_directory=output_directory,
        column="precipitation_mm",
        color="blue",
        title="Precipitation (mm) at Helsinki Airport",
        plot_type="precipitation",
    )


def plot_timeseries(
    month_data,
    month,
    output_directory,
    column,
    color,
    title,
    plot_type,
    show_mean=False,
):
    """Create and save one weather time-series plot."""

    output_directory.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots()

    axis.plot(
        month_data.index,
        month_data[column],
        color=color,
        label=column,
    )

    axis.set_title(title)
    axis.set_xlabel("Date and time")
    axis.set_ylabel(column)
    axis.legend()
    axis.grid(True)

    if show_mean:
        mean_value = month_data[column].mean()

        axis.axhline(
            y=mean_value,
            color=color,
            linestyle="--",
            label=f"Mean: {mean_value:.1f}",
        )

    figure.autofmt_xdate()

    output_file = output_directory / f"{month}-{plot_type}.png"
    figure.savefig(output_file, bbox_inches="tight")

    plt.close(figure)
