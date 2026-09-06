# SCT_DS_Task04 – Traffic Accident Analysis

## 📌 Task Overview

This project is part of the **SkillCraft Technology Data Science Internship – Task 04**.

The objective is to analyze traffic accident data and identify patterns related to **road conditions, weather, time, accident severity, traffic signals, and accident hotspots**.

## 📊 Dataset

The analysis uses the **US Accidents (March 2023)** dataset.

* Records: **7,728,394**
* Features: **46**
* Location: United States
* Dataset file: `US_Accidents_March23.csv`

> The original CSV dataset is not included in this GitHub repository because of its very large file size. It is excluded using `.gitignore`.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## 🔍 Analysis Performed

The following aspects were analyzed:

1. Accidents by hour of the day
2. Accidents by weather condition
3. Accident severity distribution
4. Day vs. night accidents
5. Accidents at traffic signals
6. Top 10 states with the highest number of accidents
7. Top 10 cities with the highest number of accidents

## 📈 Key Findings

* **Severity 2** accidents were the most common.
* Accident counts were highest during the **morning and evening commuting hours**.
* The highest accident activity occurred around **7–8 AM** and **4–5 PM**.
* Most recorded accidents occurred during **daylight hours**.
* **Fair** weather was the most frequently recorded weather condition.
* Accident counts varied considerably across states and cities.
* Traffic-signal-related accidents represented a smaller portion of the total accidents than accidents without a recorded traffic signal.

> These findings describe patterns in the dataset and do not necessarily imply that a particular weather condition or traffic feature directly caused an accident.

## 📊 Visualizations

The project includes the following visualizations:

* `accidents_by_hour.png`
* `accidents_by_weather.png`
* `accidents_by_severity.png`
* `accidents_day_night.png`
* `accidents_traffic_signal.png`
* `top_10_accident_states.png`
* `top_10_accident_cities.png`

## 📁 Project Structure

```text
SCT_DS_Task04/
│
├── dataset/
│   └── US_Accidents_March23.csv
│
├── outputs/
│   ├── accidents_by_hour.png
│   ├── accidents_by_weather.png
│   ├── accidents_by_severity.png
│   ├── accidents_day_night.png
│   ├── accidents_traffic_signal.png
│   ├── top_10_accident_states.png
│   └── top_10_accident_cities.png
│
├── task4_traffic_accidents.py
├── .gitignore
└── README.md
```

## ▶️ How to Run

Install the required Python libraries:

```bash
pip install pandas matplotlib seaborn
```

Place the dataset inside:

```text
dataset/US_Accidents_March23.csv
```

Then run:

```bash
python task4_traffic_accidents.py
```

The generated charts will be saved in the `outputs` folder.

## 🎯 Learning Outcomes

Through this task, I gained practical experience in:

* Handling and analyzing a large real-world dataset
* Data preprocessing using Pandas
* Extracting time-based features
* Grouping and aggregating accident data
* Identifying patterns and hotspots
* Creating data visualizations
* Interpreting real-world data trends
* Managing a data science project using Git and GitHub

## 👩‍💻 Internship

**SkillCraft Technology – Data Science Internship**

**Task 04: Traffic Accident Analysis**
