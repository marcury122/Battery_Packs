import json
import random
from matplotlib import pyplot as plt

def calculate_adjusted_usage(ax, data, selected_days=None, selected_set="set1", selected_month=1, label="Adjusted Usage"):
    avg_usg = data["algoData"]["avgUsg"]  
    data_days = data["dataDays"]
    interval_length = data["intervalLength"]
    percentage_ranges = data["algoData"]["data"][selected_set]

    def get_random_percentage(range_tuple):
        if isinstance(range_tuple, list) and len(range_tuple) == 2:
            return random.uniform(range_tuple[0], range_tuple[1])
        else:
            return None

    if selected_days is None:
        selected_days = list(range(1, data_days + 1))
    else:
        selected_days = [int(day) for day in selected_days]

    cumulative_total = 0

    for day in range(data_days):
        if day + 1 not in selected_days:
            continue

        usage_per_day = avg_usg / data_days
        number_reads = 24 * 3600 / interval_length
        usage_per_interval = usage_per_day / number_reads

        y = []

        for time_range, percentage_range in percentage_ranges.items():
            if time_range == "months":
                continue

            random_percentage = get_random_percentage(percentage_range)
            adjusted_interval_usage = usage_per_interval * (random_percentage / 100)

            y.append(adjusted_interval_usage/2)
            print(f"Day {day + 1}, Time Range: {time_range}, Adjusted Usage: {adjusted_interval_usage}")

        ax.plot(range(0, 24, 2), y, label=f"Day {day + 1}")

        daily_adjusted_usage = sum(y)
        cumulative_total += daily_adjusted_usage
        print(f"Day {day + 1}, Daily Energy usage: {daily_adjusted_usage*2}")
        print('\n')
    print(f"Energy Used: {cumulative_total*2}")
    print('\n')

    ax.set_xlabel("Time (hours)")
    ax.set_ylabel(label)
    ax.legend()

def calculate_adjusted_usage2(ax, data, selected_days=None, selected_set="set1", selected_month=1, label="Adjusted Usage"):
    avg_usg = data["algoData"]["avgUsg"]  
    data_days = data["dataDays"]
    interval_length = data["intervalLength"]
    percentage_ranges = data["algoData"]["data"][selected_set]

    def get_random_percentage(range_tuple):
        if isinstance(range_tuple, list) and len(range_tuple) == 2:
            return random.uniform(range_tuple[0], range_tuple[1])
        else:
            return None

    if selected_days is None:
        selected_days = list(range(1, data_days + 1))
    else:
        selected_days = [int(day) for day in selected_days]

    cumulative_total = 0

    for day in range(data_days):
        if day + 1 not in selected_days:
            continue

        usage_per_day = avg_usg / data_days
        number_reads = 24 * 3600 / interval_length
        usage_per_interval = usage_per_day / number_reads

        y = []

        for time_range, percentage_range in percentage_ranges.items():
            if time_range == "months":
                continue

            random_percentage = get_random_percentage(percentage_range)
            adjusted_interval_usage = usage_per_interval * (random_percentage / 100)

            y.append(adjusted_interval_usage/2)
            print(f"Day {day + 1}, Time Range: {time_range}, Adjusted Usage: {adjusted_interval_usage}")

        ax.plot(range(0, 24, 2), y, label=f"Day {day + 1}")

        daily_adjusted_usage = sum(y)
        cumulative_total += daily_adjusted_usage
        print(f"Day {day + 1}, Daily Energy Generation: {daily_adjusted_usage*2}")
        print('\n')
    print(f"Energy Generation: {cumulative_total*2}")
    print('\n')

    ax.set_xlabel("Time (hours)")
    ax.set_ylabel(label)
    ax.legend()

if _name_ == "_main_":
    with open("UG.JSON", "r") as file:
        input_data = json.load(file)
    with open("UG-2.JSON","r") as f:
        input1 = json.load(f)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    selected_set = input("Enter the set (set1 or set2): ")
    selected_month = int(input("Enter the month (1 for January, 2 for February, etc.): "))
    user_input_days = input("Enter selected days for consumption (space-separated): ")

    calculate_adjusted_usage(axes[0], input_data, selected_days=user_input_days.split(), selected_set=selected_set, selected_month=selected_month, label="Consumption (in kW)")
    axes[0].set_title("Consumption")
    print('\n')
    calculate_adjusted_usage2(axes[1], input1, selected_days=user_input_days.split(), selected_set=selected_set, selected_month=selected_month, label="Generation (in kW)")
    axes[1].set_title("Generation")

    plt.tight_layout()
    plt.show()