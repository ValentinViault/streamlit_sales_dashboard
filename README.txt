# Sales Dashboard

Interactive sales dashboard built with Streamlit, Pandas and Plotly.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)

---

## About

This project is an interactive sales analytics dashboard built as part of a Python data analyst portfolio. It leverages the **Superstore dataset** — a fictional retail company's sales data covering 4 years, 4 regions, 3 product categories and nearly 10,000 orders across the United States.

The goal was to turn raw CSV data into a fully interactive web app without any backend or JavaScript — just Python. Users can explore the data through dynamic filters, monitor key business metrics in real time, and identify trends through interactive visualizations.

---

## Demo

> 🔗 *Coming soon — Streamlit Cloud deployment*

---

## Features

- **Dynamic filters** — filter by year, region and category from the sidebar
- **Real-time KPIs** — total revenue, orders, average order value and profit
- **Interactive charts** — bar chart, pie chart and revenue over time (Plotly)
- **Detailed data table** — sortable and filterable

---

## Project Structure

```
sales-dashboard/
├── data/                  # Dataset (not included, see below)
├── src/
│   └── app.py             # Main Streamlit app
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/ValentinViault/streamlit_sales_dashboard.git
cd sales-dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**

Download the [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) from Kaggle and place the file in the `data/` folder:
```
data/Sample - Superstore.csv
```

**4. Run the app**
```bash
streamlit run src/app.py
```

---

## Tech Stack

| Tool | Usage |
|------|-------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Pandas](https://pandas.pydata.org) | Data manipulation |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive charts |

---

## License

MIT License — feel free to use and adapt this project.
