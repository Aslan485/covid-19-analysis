# 🦠 COVID-19 Global Impact Analysis

A comprehensive SQL-based analysis of COVID-19 pandemic data using real-world dataset from WHO. This project provides actionable insights into country-level impact, healthcare system performance, and regional trends.

## 📊 Project Overview

This analysis examines COVID-19 data across 200+ countries to identify:
- Most affected countries and regions
- Healthcare system efficiency through mortality and recovery rates
- Regional pandemic response effectiveness
- Weekly case trends and outbreak patterns

**Dataset:** WHO COVID-19 Country-wise Latest Data (200+ countries)

## 🎯 Key Insights Discovered

### Critical Findings:
- **United Kingdom** shows the highest death rate (15.19%) among major countries
- **Qatar** leads in recovery rates (97.02%) demonstrating effective healthcare response
- **Americas region** has the highest total cases but moderate death rate (3.88%)
- **Eastern Mediterranean** shows exceptional recovery rates (80.59%)
- **India** experienced the highest weekly percent increase (28.11%) during analysis period

### Regional Performance:
- **Best Recovery Rates**: Eastern Mediterranean (80.59%), Europe (60.42%)
- **Lowest Death Rates**: Africa (1.69%), South-East Asia (2.25%)
- **Case Volume Leaders**: Americas (8.8M cases), Europe (3.3M cases)

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/Aslan485/covid-19-analysis.git
cd covid-19-analysis
pip install -r requirements.txt
## Usage
bash
python covid_analysis.py
##📈 Analysis Features
SQL-Based Analytics
Country-level impact ranking and comparison

Mortality rate analysis across healthcare systems

Recovery efficiency metrics

Regional pandemic management evaluation

Weekly trend analysis and outbreak identification

Business Intelligence
Healthcare system performance benchmarking

Pandemic response effectiveness metrics

Risk assessment and forecasting insights

Data-driven policy evaluation

🛠️ Technical Implementation
Technologies Used
Python 3.8+ - Data processing and analysis

SQLite - Database management and query execution

Pandas - Data manipulation and CSV handling

SQL Analytics Capabilities
Complex JOIN operations and aggregations

Percentage calculations and rate analysis

Conditional filtering and ranking

Multi-level grouping and summarization

📁 Project Structure
text
covid-19-analysis/
├── covid_analysis.py     # Main analysis script
├── requirements.txt      # Dependencies
├── README.md            # Documentation
└── data/                # Dataset directory
    └── country_wise_latest.csv
🔧 SQL Query Examples
The project implements sophisticated SQL queries including:

sql
-- Mortality rate analysis with conditional filtering
SELECT country, total_cases, total_deaths,
       ROUND((deaths * 100.0 / confirmed), 2) as death_rate
FROM covid_data 
WHERE confirmed > 10000 
ORDER BY death_rate DESC;

-- Regional performance comparison
SELECT region, SUM(cases) as total_cases,
       ROUND(SUM(deaths) * 100.0 / SUM(cases), 2) as death_rate
FROM covid_data
GROUP BY region;
👨‍💻 Author
Aslan Akhundov - Data Analyst

GitHub: Aslan485

Email: axundovaslan44@gmail.com

Skills: Python, SQL, Pandas, Data Analysis, Business Intelligence

🤝 Contributing
Contributions are welcome! Please feel free to submit Pull Requests for:

Additional analytical perspectives

Data visualization enhancements

New metric calculations

Performance optimizations

📄 License
This project is licensed under the MIT License.

⭐ If you find this project useful, please give it a star!
🔗 Useful Links
World Health Organization COVID-19 Data

Pandas Documentation

SQLite Documentation

📞 Support
For questions about this analysis or dataset, please open an issue on GitHub.

