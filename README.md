# 🌍 WHO Health Data Pipeline & Dashboard

This is a full-stack data project that demonstrates how to build a **professional-grade data pipeline and dashboard** using global health indicators from the **World Health Organization (WHO) API**.

The workflow includes:
- 📥 Automated data extraction (API)
- 🧹 Data cleaning and transformation
- 📊 Exploratory visualizations
- 💡 Modular, reusable code structure
- 📈 Publishing insights via Shiny dashboard (in progress)

Designed for rapid, reproducible health data analysis — and built to scale.

📊 **Live demo**: [https://giuliasepeda.shinyapps.io/maternal_mortality_who/](https://giuliasepeda.shinyapps.io/maternal_mortality_who/)

---

## 🎯 Project Objectives

- Automate the collection and processing of WHO indicators  
- Standardize and enrich the raw data for analysis  
- Visualize uncertainty and regional/global trends  
- Build a clear foundation for health dashboards using Shiny, Streamlit or Dash  
- Showcase data engineering and storytelling skills in a public portfolio

---

## 🧱 Project Structure

```
who_health_dashboard/
├── src/                 # Core Python modules
│   ├── who_api.py       # API query and download
│   ├── cleaning.py      # Cleaning and standardization
│   ├── visualization.py # Static chart creation
│   └── io_tools.py      # File and directory helpers
├── notebooks/           # Jupyter notebooks for EDA and prototyping
│   └── maternal_mortality_pipeline.ipynb
├── data/
│   ├── raw/             # Downloaded raw data
│   └── processed/       # Cleaned and enriched datasets
├── shiny_dashboard/     # R Shiny dashboard files (UI + server)
│   ├── app.R
│   └── ...
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🔗 Data Source

All indicators retrieved from the official [WHO Global Health Observatory API](https://ghoapi.azureedge.net/api/).  
Key example used: **Maternal mortality ratio (per 100,000 live births)**.

Additional indicators can be integrated with minimal adjustment.

---

## 🛠️ Technologies Used

**Backend & ETL:**
- Python 3.10+
- `pandas`, `requests`, `os`, `json`
- Modular OOP-style code for pipeline maintainability

**Visualization & EDA:**
- `matplotlib`, `seaborn`, `plotly` (optional)

**Dashboard (in progress):**
- R + Shiny
- `tidyverse`, `leaflet`, `shinydashboard`

---

## 📊 Current Insights

- Global trends in maternal mortality (1985–2023)
- Countries with high uncertainty margins (data quality warning)
- Year-over-year comparisons between countries or WHO regions
- First prototype dashboard: [View here](https://giuliasepeda.shinyapps.io/maternal_mortality_who/)

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone https://github.com/giuuusepeda/who_health_dashboard.git
cd who_health_dashboard
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

Run the ETL pipeline and EDA:

```bash
jupyter notebook notebooks/maternal_mortality_pipeline.ipynb
```

---

## 🧪 Sample Usage

```python
from src.who_api import fetch_indicator_data
from src.cleaning import clean_column_names
from src.visualization import plot_global_trend

df = fetch_indicator_data("MMR_100000_LIVEBIRTHS")
df = clean_column_names(df)
plot_global_trend(df)
```

---

## 📦 Project Status

✅ Data extraction and cleaning pipeline complete  
✅ Reusable code modules in place  
✅ Exploratory analysis done  
✅ First dashboard prototype published  
🔜 Add indicator selector and dynamic plots to dashboard  
🔜 CI/CD for live updates via GitHub Actions or Docker

---

## 📄 License

This project is for **personal portfolio demonstration only**.  
It is licensed under **CC BY-NC-ND 4.0** — you may view or share it, but not copy, modify, or use it commercially without permission.

🔗 [View full license](https://creativecommons.org/licenses/by-nc-nd/4.0/)

---

## 🙋‍♀️ About the Author

**Giulia Sepeda**  
Data analyst with a background in nursing and public health.  
Focused on building meaningful solutions at the intersection of health, data, and social impact.

🔗 [Portfolio](https://giuliasepeda.carrd.co) | [GitHub](https://github.com/giuuusepeda)
```
