# 🔮 Prediction Market Intelligence

A modern, high-performance data dashboard designed for analyzing prediction market datasets. Built with a premium "Beautiful" glassmorphism UI, this application provides deep insights into market distributions and event analytics.

## ✨ Key Features

- **Modern Aesthetic**: Deep gradient backgrounds with glassmorphism effects and glowy UI elements.
- **Interactive Controls**: Sidebar configuration with a real-time **Color Picker** to customize chart themes.
- **Tabbed Layout**: Organized views for better data management:
  - **📊 Analytics**: Interactive distribution and categorical breakdown charts.
  - **🔍 Data Explorer**: High-performance data snapshot and summary statistics.
  - **ℹ️ Metadata**: Detailed column information and data quality metrics.
- **Optimized Performance**: Leverages Parquet file formats and Streamlit's caching for lightning-fast data loading.

## 🛠 Tech Stack

- **Frontend / App:** Streamlit  
- **Data Processing:** Pandas  
- **Visualization:** Plotly Express  
- **Storage Format:** Apache Parquet  
- **Parquet Engine:** PyArrow  
- **Language:** Python 3

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation

1. Clone the repository (or navigate to the project folder):
   ```bash
   cd Prediction_market_app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

To launch the dashboard, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`.

## 📁 Project Files

- **app.py** – Main Streamlit application
- **requirements.txt** – Python dependencies
- **README.md** – Project documentation
- **data/** – Parquet datasets (`train-00000-of-000002.parquet`, `train-00001-of-000002.parquet`)
- **utils/** – Utility modules
  - `__init__.py` – Marks folder as a Python package
  - `data_loader.py` – Loads and merges datasets
  - `analytics.py` – Analytics & visualization functions

## 🌐 Live Demo

👉 Live app here:

## 📂 Download Dataset From here 

- 🗂️ train-00000-of-000002.parquet  
  👉 Download here: (<https://drive.google.com/file/d/1QgCIF4i-968qN-1WuVeCmLWKNSotxrqe/view?usp=sharing>)

- 🗂️ train-00001-of-000002.parquet  

  👉 Download here: (<https://drive.google.com/file/d/1LRo0iqVpgeS55Q3pu3glRNS4pmxrQ-9B/view?usp=sharing>)









