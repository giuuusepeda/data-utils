#  WHO API Data Pipeline

A **Data Science project** that builds an ETL pipeline to fetch, clean, transform, and visualize global health data from the World Health Organization (WHO) API. Designed with a modular structure for easy reuse and professional workflows.

##  About the project

This project demonstrates how to:  
- Automate health data collection from WHO API  
- Clean and standardize raw data for analysis  
- Visualize global health trends with confidence intervals  
- Organize code into reusable Python modules for production-ready workflows  

💡 Ideal for quick, reproducible analyses of WHO datasets.

---

##  Project structure

```

who\_api\_pipeline/
├── src/                 # Python modules for reusable functions
│   ├── cleaning.py      # Data cleaning functions
│   ├── visualization.py # Visualization functions
│   ├── who\_api.py       # Functions to interact with WHO API
│   └── io\_tools.py      # Input/output utilities
├── notebooks/           # Jupyter notebooks for analysis
│   └── pipeline\_WHO.ipynb
├── data/                # Raw and processed data
│   └── raw/
│   └── processed/
├── requirements.txt     # Project dependencies
└── README.md            # This file

````

---

## 🛠️ Technologies & libraries

-  Python 3.10+
-  Pandas
-  Matplotlib & Seaborn
-  Requests (API consumption)
-  Modular Python structure

---

##  Example insights

### - Global trend (1985–2023)

Displays total estimated cases globally, including uncertainty ranges.

![Global trend](images/global_trend.png)

### - Countries with highest uncertainty

Highlights countries where WHO estimations show larger confidence intervals, reflecting weaker data systems.

![Uncertainty chart](images/interval_uncertainty.png)

---

##  How to use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/who_api_pipeline.git
   cd who_api_pipeline
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. Run the notebook:

   ```bash
   jupyter notebook notebooks/pipeline_WHO.ipynb
   ```

---

##  Example usage in notebook

```python
from src.cleaning import clean_column_names, add_interval_width
from src.visualization import plot_global_trend

# Data cleaning
df = clean_column_names(df)
df = add_interval_width(df)

# Visualization
plot_global_trend(df)
```

---

##  References

* [WHO Global Health Observatory API](https://www.who.int/data/gho/info/gho-odata-api)
* [WHO Indicator Metadata](https://www.who.int/data/gho/indicator-metadata-registry)

---

##  Project status

📦 MVP complete: modular functions and exploratory data analysis (EDA).
🚀 Next steps: Add interactive dashboards with Streamlit or Plotly Dash.

---


⚠️ This repository is intended for personal portfolio purposes only.  
Unauthorized use, redistribution, or copying of any part of this content is strictly prohibited.


```
