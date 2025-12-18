# QUOTES_EXTRACTION_ANALYSIS

A complete, end-to-end data pipeline for extracting, analyzing and visualizing quotes from the web.
This project demonstrates **web scraping**, **sentiment analysis** and **interactive data visualization**, culminating in a **fully navigable Plotly dashboard**.

The repository includes **pre-generated data and visualizations**, allowing immediate exploration without running any code.

---

## 📌 Project Overview

**QUOTES_EXTRACTION_ANALYSIS** follows a structured workflow:

1. **Data Extraction** – Scrapes quotes, authors and tags from a public website using Scrapy
2. **Sentiment Analysis** – Applies NLP techniques to classify quote sentiment
3. **Visualization** – Generates interactive Plotly charts
4. **Dashboard** – Combines all charts into a clean, browser-based interface

This mirrors a real-world analytics pipeline, from raw data to insights.

---

## 📂 Project Structure

```
QUOTES_EXTRACTION_ANALYSIS/
│
├── data_extraction/
│   ├── quotes.py              # Scrapy spider
│   └── quotes.json            # Extracted raw quotes
│
├── sentiment_analysis/
│   ├── process_sentiment.py   # Sentiment processing
│   ├── bar_chart_author.py
│   ├── bar_chart_tag.py
│   ├── pie_chart_author.py
│   ├── pie_chart_tag.py
│   ├── sankey_disgram.py
│   ├── scatter_plot.py
│   ├── sunburst_chart.py
│   ├── treemap.py
│   └── word_cloud_viz.py
│
├── visualizations/            # Generated Plotly HTML files
│   ├── bar_charts/
│   ├── pie_chart_authors/
|   ├── pie_chart_tags/
│   ├── exploratory_charts/
│   └── word_clouds/
│
├── index.html                 # Central dashboard
├── styles.css                 # Dashboard styling
└── requirements.txt           # Python dependencies
```

---

## 🔹 Data Source

* **Website:** quotes.toscrape.com
* **Content:** Quotes, authors, and thematic tags
* **Purpose:** Educational scraping target commonly used for demonstrations

**Example raw record:**

```json
{
  "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"]
}
```

---

## 🔹 Sentiment Analysis

* **Method:** NLTK VADER (rule-based sentiment analysis)
* **Output file:** `processed_quotes.json`
* **Generated fields:**

  * Compound sentiment score
  * Sentiment label: *Positive / Neutral / Negative*
  * Detailed polarity scores

**Example processed record:**

```json
{
  "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"],
  "compound": 0.25,
  "sentiment": "Positive",
  "scores": {
    "neg": 0.0,
    "neu": 0.905,
    "pos": 0.095,
    "compound": 0.25
  }
}
```

---

## 📊 Visualizations & Dashboard Architecture

All visualizations are created using **Plotly** and exported as standalone HTML files.

### Visualization Layers

* **Low-level charts**
  Individual Plotly HTML files (e.g., bar charts, pie charts, Sankey diagrams)

* **Section overview pages**
  Dedicated HTML files (e.g., `sentiment_overview.html`) aggregate and embed multiple related charts

* **Central dashboard**
  `index.html` serves as the main entry point and links to section overview pages

### Visualization Types

* Bar charts (author & tag sentiment distribution)
* Pie charts (sentiment proportions)
* Sankey diagram (relationships between authors, tags, and sentiment)
* Scatter plot (sentiment score vs. quote characteristics)
* Sunburst chart (hierarchical sentiment breakdown)
* Treemap (relative sentiment distribution)
* Word cloud (dominant themes)

This layered structure keeps the dashboard modular, scalable and easy to extend.

---

## ⚡ Quick Start (Recommended)

This repository already contains:

* Extracted data
* Processed sentiment results
* Generated visualizations
* A complete dashboard

To explore the project:

1. **Clone the repository**

```bash
git clone https://github.com/SHAIMOOM251283/QUOTES_EXTRACTION_ANALYSIS.git
cd QUOTES_EXTRACTION_ANALYSIS
```

2. **Open the dashboard**

Open the dashboard locally after cloning the repository:

```bash
# Open index.html in your browser
```

🌐 **Live Dashboard (GitHub Pages)**

You can also view the live deployed dashboard here:
👉 [https://shaimoom251283.github.io/QUOTES_EXTRACTION_ANALYSIS/](https://shaimoom251283.github.io/QUOTES_EXTRACTION_ANALYSIS/)

---

No additional setup is required.

---

## 🔄 Optional: Reproduce the Pipeline

If you want to regenerate the data and visualizations from scratch:

1. **Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the scraper**

```bash
cd data_extraction
scrapy crawl quotes -O quotes.json --set FEED_EXPORT_INDENT=4
```

4. **Run sentiment analysis and generate visualizations**

```bash
cd ../sentiment_analysis

# Generate processed sentiment data
python process_sentiment.py

# Generate visualizations (run the scripts you are interested in)
python bar_chart_author.py
python bar_chart_tag.py
python pie_chart_author.py
python pie_chart_tag.py
python sankey_disgram.py
python scatter_plot.py
python sunburst_chart.py
python treemap.py
python word_cloud_viz.py
```

5. **View the results in the dashboard**

After the visualizations are generated, open the central dashboard:

```bash
# From the project root
open index.html
```

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Scrapy** — web scraping
* **NLTK (VADER)** — sentiment analysis
* **Plotly** — interactive visualizations
* **WordCloud, Pillow, NumPy** — word cloud generation
* **HTML & CSS** — dashboard interface

---

## 🎯 Why This Project Matters

This project demonstrates how raw web data can be transformed into **actionable insights** using a structured analytics pipeline.
It highlights skills relevant to **data analysis, web scraping, visualization and dashboard design** — all within a real, reproducible project.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---
