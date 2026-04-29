# 🌎 Global Trade & Economic Explorer

An interactive web application built with **Python** that provides real-time visualizations of global economic indicators. This project fetches live data directly from the **World Bank Open Data API** to analyze trends across 40+ key metrics for any country in the world.

## 🚀 Live Features
- **Real-time Data Fetching:** Utilizes `wbgapi` to ensure the most up-to-date economic information.
- **Dynamic Exploration:** Users can filter by Country and Category (Trade, Macroeconomics, Social, and Development).
- **Interactive Visualizations:** High-quality area charts and data tables powered by **Plotly**.
- **Key Metrics:** Instantly view Latest Value, All-time High, and Period Averages.
- **Data Export:** Built-in functionality to download filtered datasets as CSV files.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** [Streamlit](https://streamlit.io) (Web Interface)
- **Data Analysis:** [Pandas](https://pydata.org)
- **Visualizations:** [Plotly Express](https://plotly.com)
- **Data Source:** [World Bank API (wbgapi)](https://github.com)

## 📁 Project Structure
The project follows a modular architecture for better maintainability:
- `main.py`: The entry point and UI structure of the application.
- `utils/data_loader.py`: Handles API connections and data cleaning logic.
- `utils/catalog.py`: Contains the organized mapping of 40+ economic indicators.
- `assets/style.css`: Custom CSS for a professional, polished look.
- `requirements.txt`: List of dependencies for easy setup.

## ⚙️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/matifelitti/global-trade-explorer
   cd global-trade-explorer
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

## 📊 Sample Indicators Included
- **Foreign Trade:** Exports/Imports (% of GDP), FDI, Tourism receipts.
- **Macroeconomics:** GDP Growth, Inflation, Central Government Debt.
- **Social & Labor:** Unemployment rate, Life expectancy, Literacy rate.
- **Development:** CO2 Emissions, R&D Expenditure, Internet usage.

