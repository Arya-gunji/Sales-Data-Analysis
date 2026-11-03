# Sales Data Analysis Project

A portfolio-ready retail sales analysis project with:
- Jupyter Notebook for data cleaning, exploratory analysis, visualizations, and insights
- Streamlit dashboard with KPI cards and interactive filters
- Monthly sales trend, regional and state sales, segment/category analysis, profit analysis, and discount vs profit plot
- CSV download for filtered records

## Important dataset note
`data/sales_data.csv` contains **synthetic sample data generated for demonstration**. It is not a real company's sales data. Use an authorized real dataset if you need to report real business findings.

## Project structure
```text
Sales-Data-Analysis/
├── app.py
├── data/
│   └── sales_data.csv
├── notebooks/
│   └── sales_analysis.ipynb
├── images/
├── requirements.txt
└── README.md
```

## Run locally
Recommended: Python 3.10 or newer.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install packages:
```bash
pip install -r requirements.txt
```

Launch Jupyter:
```bash
jupyter notebook
```
Open `notebooks/sales_analysis.ipynb` and run cells from top to bottom.

Launch dashboard from the project root:
```bash
streamlit run app.py
```

## Use your own CSV
The dashboard has a sidebar CSV uploader. The CSV should include these columns:
`Order ID`, `Order Date`, `Customer ID`, `Segment`, `Region`, `State`, `Category`, `Sales`, `Quantity`, `Discount`, `Profit`.

## GitHub upload
1. Create a new repository on GitHub, e.g. `sales-data-analysis`.
2. Open a terminal in this project folder.
3. Run:
   ```bash
   git init
   git add .
   git commit -m "Build sales data analysis project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/sales-data-analysis.git
   git push -u origin main
   ```
4. Replace `YOUR-USERNAME` with your GitHub username. Do not include passwords or API keys in the repository.

## Suggested resume bullet
Built a retail Sales Data Analysis project using Python, Pandas, Matplotlib, Seaborn, Plotly, and Streamlit; cleaned transactional data, analyzed sales and profit trends, and developed an interactive dashboard with KPI metrics and region/category filters.
