import json
import random
import numpy as np
from matplotlib import pyplot as plt

def calculate_adjusted_usage(ax, data, values, selected_days=None, label="Adjusted Usage", is_generated=False):
    avg_usg = data["algoData"]["avgUsg"]
    data_days = data["dataDays"]
    interval_length = data["intervalLength"]
    percentage_ranges = data["algoData"]["data"]

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

            y.append(adjusted_interval_usage)
            print(f"Day {day + 1}, Time Range: {time_range}, Adjusted Usage: {adjusted_interval_usage}")

        ax.plot(range(0, 24, 2), y, label=f"Day {day + 1}")

        # Ensure the values list has enough elements to accommodate the values
        while len(values) <= day:
            values.append([])

        # Store values in arrays based on the is_generated parameter
        if is_generated:
            values[day] = np.array(y)
        else:
            values[day] = np.array(y)

        daily_adjusted_usage = sum(y)
        cumulative_total += daily_adjusted_usage
        print(f"Day {day + 1}, Daily Total Adjusted Usage: {daily_adjusted_usage}")
        print('\n')

    print(f"Cumulative Total Adjusted Usage: {cumulative_total}")

    ax.set_xlabel("Time (hours)")
    ax.set_ylabel(label)
    ax.legend()

    return values

if __name__ == "__main__":
    with open("UG.json", "r") as file:
        input_data = json.load(file)
    with open("UG-2.json","r") as x:
        input1 = json.load(x)
    # with open("UG-3.json","r") as f:
    #     input_ = json.load(f)
    # with open("UG-4.json","r") as y:
    #     input2 = json.load(y)

    # fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

    # user_input = input("Enter selected days for UG.JSON (space-separated): ")
    # selected_days = user_input.split(" ")
    # consumption = calculate_adjusted_usage(axes[0, 0], input_data, [], selected_days, label="Consumption (in kW)")
    # axes[0, 0].set_title("Consumption")

    # user_input = input("Enter selected days for UG-2.JSON (space-separated): ")
    # selected_days = user_input.split(" ")
    # generated = calculate_adjusted_usage(axes[0, 1], input1, [], selected_days, label="Generation (in kW)", is_generated=True)
    # axes[0, 1].set_title("Generation")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    user_input = input("Enter selected days for UG.JSON (space-separated): ")
    selected_days = user_input.split(" ")
    consumption = calculate_adjusted_usage(axes[0], input_data, [], selected_days, label="Consumption (in kW)")
    axes[0].set_title("Consumption")

    user_input = input("Enter selected days for UG-2.JSON (space-separated): ")
    selected_days = user_input.split(" ")
    generated = calculate_adjusted_usage(axes[1], input1, [], selected_days, label="Generation (in kW)", is_generated=True)
    axes[1].set_title("Generation")



    # user_input = input("Enter selected days for UG-3.JSON (space-separated): ")
    # selected_days = user_input.split(" ")
    # calculate_adjusted_usage(axes[1, 0], input_, consumption, generated, selected_days, label="Grid (in kW)")
    # axes[1, 0].set_title("Grid")

    # user_input = input("Enter selected days for UG-4.JSON (space-separated): ")
    # selected_days = user_input.split(" ")
    # calculate_adjusted_usage(axes[1, 1], input2, consumption, generated, selected_days, label="Battery (in kW)")
    # axes[1, 1].set_title("Battery")

    plt.tight_layout(pad=5)  # Increase the padding to avoid overlap



    SOC = [0]*24  # Initialize SOC array

    gen = []
    con = []

    time = [2,4,6,8,10,12,14,16,18,20,22,24]

    gen = np.append(gen, np.concatenate(generated))
    con = np.append(con, np.concatenate(consumption))
    maxBh = 5

    bat = [0]*24
    grid = [0]*24

    BH = 0
    for i in range(12):
        BH += gen[i] - con[i]
        if BH < 0:
            grid[2*i] = -BH
            BH = 0
        elif BH > maxBh:
            grid[2*i] = maxBh - BH
            BH = maxBh
        else:
            grid[2*i] = 0
        SOC[2*i] = BH
        bat[2*i] = con[i] - gen[i] - grid[2*i]


# -----------------------------------------------------------------------------------------
    # Plot bat and grid lists
    # fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(12, 6))

    # ax1.plot(bat, label="bat")
    # ax1.set_ylabel("Battery Level")
    # # ax1.axhline(y=0, color='black', linestyle='--')  # Add reference line at y=0
    # ax1.legend()

    # ax2.plot(grid, label="grid")
    # ax2.set_ylabel("Grid Energy")
    # # ax2.axhline(y=0, color='black', linestyle='--')  # Add reference line at y=0
    # ax2.legend()

    # plt.xlabel("Time step")
    # plt.show()
# -----------------------------------------------------------------------------------------

    # Plot bat and grid lists
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

    ax[0].plot(bat, label="bat")
    ax[0].set_ylabel("Battery Level")
    ax[0].axhline(y=0, color='black', linestyle='--')  # Add reference line at y=0
    ax[0].legend()

    ax[1].plot(grid, label="grid")
    ax[1].set_ylabel("Grid Energy")
    ax[1].axhline(y=0, color='black', linestyle='--')  # Add reference line at y=0
    ax[1].legend()

    ax[0].set_xlabel("Time step")
    ax[1].set_xlabel("Time step")
    plt.show()

    print("Consumption:", consumption)
    print("Generated:", generated)
    print("Battery:", SOC)
