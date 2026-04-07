Sales Dashboard
Interactive sales dashboard built with Streamlit, Pandas, and Plotly.
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
---
About
This project is an interactive sales analytics dashboard built as part of a Python data analyst portfolio.
It uses the Superstore dataset, a fictional retail dataset containing:
4 years of sales data
4 regions
3 product categories
~10,000 orders across the United States
Objective:  
Transform raw CSV data into a fully interactive web application using only Python — no backend or JavaScript required.
Users can:
Explore data with dynamic filters
Monitor key business metrics in real time
Identify trends with interactive visualizations
---
Demo
> Coming soon — Streamlit Cloud deployment
---
Features
Dynamic filters — filter by year, region, and category
Real-time KPIs — revenue, orders, average order value, profit
Interactive charts — bar chart, pie chart, and time series (Plotly)
Data table — sortable and filterable dataset view
---
Project Structure
```bash
sales-dashboard/
├── data/                  # Dataset (not included, see below)
├── src/
│   └── app.py             # Main Streamlit application
├── .gitignore
├── requirements.txt
└── README.md
```
---
Installation
1. Clone the repository
```bash
git clone https://github.com/ValentinViault/streamlit_sales_dashboard.git
cd sales-dashboard
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Download the dataset
Download the dataset from Kaggle:  
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
Then place it in the `data/` folder:
```bash
data/Sample - Superstore.csv
```
4. Run the application
```bash
streamlit run src/app.py
```
---
Tech Stack
Tool	Usage
Streamlit	Web application framework
Pandas	Data manipulation and analysis
Plotly Express	Interactive data visualization
---
License
This project is licensed under the MIT License.  
Feel free to use, modify, and share it.
