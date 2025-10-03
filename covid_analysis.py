import sqlite3
import pandas as pd

def create_database():
    """Create database from COVID dataset"""
    # Mevcut datasetini kullan
    df = pd.read_csv(r"C:\Users\axund\Downloads\country_wise_latest.csv")  # Senin datasetin
    
    conn = sqlite3.connect('covid_analysis.db')
    df.to_sql('covid_data', conn, if_exists='replace', index=False)
    return conn

def run_covid_analysis(conn):
    """Meaningful COVID-19 impact analysis"""
    
    queries = {
        'Top 10 Most Affected Countries': """
            SELECT `Country/Region` as country,
                   `Confirmed` as total_cases,
                   `Deaths` as total_deaths,
                   `Recovered` as total_recovered,
                   ROUND((`Deaths` * 100.0 / `Confirmed`), 2) as death_rate,
                   ROUND((`Recovered` * 100.0 / `Confirmed`), 2) as recovery_rate
            FROM covid_data 
            WHERE `Confirmed` > 0
            ORDER BY `Confirmed` DESC 
            LIMIT 10;
        """,
        
        'Highest Death Rates (Countries with 10K+ Cases)': """
            SELECT `Country/Region` as country,
                   `Confirmed` as total_cases,
                   `Deaths` as total_deaths,
                   ROUND((`Deaths` * 100.0 / `Confirmed`), 2) as death_rate
            FROM covid_data
            WHERE `Confirmed` > 10000 AND `Deaths` > 0
            ORDER BY death_rate DESC
            LIMIT 10;
        """,
        
        'Best Recovery Rates (Countries with 10K+ Cases)': """
            SELECT `Country/Region` as country,
                   `Confirmed` as total_cases,
                   `Recovered` as total_recovered,
                   ROUND((`Recovered` * 100.0 / `Confirmed`), 2) as recovery_rate
            FROM covid_data
            WHERE `Confirmed` > 10000 AND `Recovered` > 0
            ORDER BY recovery_rate DESC
            LIMIT 10;
        """,
        
        'Regional Analysis by WHO Regions': """
            SELECT `WHO Region` as region,
                   SUM(`Confirmed`) as total_cases,
                   SUM(`Deaths`) as total_deaths,
                   SUM(`Recovered`) as total_recovered,
                   ROUND(SUM(`Deaths`) * 100.0 / SUM(`Confirmed`), 2) as region_death_rate,
                   ROUND(SUM(`Recovered`) * 100.0 / SUM(`Confirmed`), 2) as region_recovery_rate
            FROM covid_data
            WHERE `WHO Region` IS NOT NULL
            GROUP BY `WHO Region`
            ORDER BY total_cases DESC;
        """,
        
        'Weekly Change Analysis': """
            SELECT `Country/Region` as country,
                   `Confirmed` as total_cases,
                   `Confirmed last week` as cases_last_week,
                   `1 week change` as weekly_change,
                   `1 week % increase` as weekly_percent_increase
            FROM covid_data
            WHERE `Confirmed` > 100000
            ORDER BY ABS(`1 week change`) DESC
            LIMIT 10;
        """
    }
    
    print("🦠 COVID-19 GLOBAL IMPACT ANALYSIS")
    print("=" * 50)
    print("Real-world pandemic analysis with actionable insights\n")
    
    for name, query in queries.items():
        result = pd.read_sql_query(query, conn)
        print(f"📊 {name}:")
        print(result.to_string(index=False))
        print("\n" + "─" * 60 + "\n")
        
    conn.close()

def main():
    conn = create_database()
    run_covid_analysis(conn)

if __name__ == "__main__":
    main()