# Sales Data Analysis Project

A portfolio-ready Retail Sales Data Analysis project built using Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit.

## Project Overview

This project focuses on analyzing retail sales data to identify sales trends, profit performance, regional performance, and category-wise insights.

It includes:
- Jupyter Notebook for data cleaning, exploratory data analysis (EDA), visualizations, and insights.
- Interactive Streamlit dashboard with KPI cards and filters.
- Monthly sales trend analysis.
- Region-wise and state-wise sales analysis.
- Segment and category-wise sales analysis.
- Profit and discount analysis.
- Download option for filtered CSV data.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Structure

```text
Sales-Data-Analysis/
│
├── app.py
├── filtered_sales_data.csv
├── README.md
├── requirements.txt
├── .gitignore
│
└── notebooks/
    ├── sales_analysis.ipynb
    │
    └── outputs/
        ├── category_sales_summary.csv
        ├── monthly_sales_summary.csv
        └── region_sales_summary.csv
```

## Dataset Information

The project uses `filtered_sales_data.csv` as its default dataset.

The dataset contains retail sales information such as order details, customer information, region, category, sales, quantity, discount, and profit.

**Note:** The dataset is synthetic sample data for demonstration purposes and does not represent an actual company's sales.

## Installation and Execution

Recommended: Python 3.10 or newer.

### 1. Clone the Repository

```bash
git clone https://github.com/Arya-gunji/Sales-Data-Analysis.git
cd Sales-Data-Analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/sales_analysis.ipynb` and execute the cells from top to bottom.

### 6. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## Dashboard Features

- Total Orders
- Total Customers
- Total Net Profit
- Total Sales Income
- Estimated Discount Value
- Total Quantity
- Monthly Sales Trend
- Sales by Region and State
- Sales by Segment and Category
- Profit by Category
- Discount vs Profit
- Interactive Filters
- Download Filtered Data as CSV

## Use Your Own CSV

The dashboard provides a CSV upload option.

Your CSV should contain these columns:

`Order ID`, `Order Date`, `Customer ID`, `Segment`, `Region`, `State`, `Category`, `Sales`, `Quantity`, `Discount`, `Profit`.

## GitHub Repository

[Sales Data Analysis – GitHub](https://github.com/Arya-gunji/Sales-Data-Analysis)

## Resume Description

Built a Retail Sales Data Analysis project using Python, Pandas, NumPy, Plotly, and Streamlit. Performed data cleaning, exploratory data analysis, and sales and profit analysis. Developed an interactive dashboard featuring KPI metrics, regional and category-wise insights, monthly sales trends, and CSV download functionality.
