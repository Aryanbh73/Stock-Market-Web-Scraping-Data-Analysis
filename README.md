# Stock-Market-Web-Scraping-Data-Analysis

## Project Overview

The Stock Market Web Scraping & Data Analysis Project is designed to showcase how raw financial data from the web can be transformed into a structured dataset and then used for meaningful insights.

In today’s world, stock market data drives critical decisions for investors, analysts, and businesses. However, much of this data is scattered across financial websites in unstructured form. This project uses Python-based web scraping techniques to collect live market data (such as company names, stock prices, daily price changes, and trading volumes) from Groww
, one of the leading investment platforms.

Once collected, the data is cleaned and exported into a structured Excel file (stocks.xlsx), making it accessible for further processing in tools like Excel, Python (pandas, matplotlib). The project not only demonstrates technical proficiency in web scraping and automation but also emphasizes data analysis skills, transforming raw scraped data into actionable business insights.

This project also demonstrates a complete data pipeline:

- Data Acquisition (Scraping)

- Data Wrangling (Cleaning & Structuring)

- Data Storage (Excel/CSV)

- Data Analysis & Insights

## Sample Dataset

<img width="544" height="382" alt="st2" src="https://github.com/user-attachments/assets/6725727b-9379-4298-9b24-8bf44d65f292" />
<img width="544" height="382" alt="st1" src="https://github.com/user-attachments/assets/1ba1d27e-5543-4da8-8443-104706fb4be5" />

## Insights from the Data

The scraped dataset opens the door for a wide range of financial insights that can help investors, analysts, and decision-makers. By analyzing the price movements, daily changes, and trading volumes, we can uncover both short-term trading signals and long-term investment perspectives.

### 1. Market Gainers & Losers

Based on the scraped dataset:

Top Gainers:

Nike Inc (NKE) → +5.96%

Microsoft Corporation (MSFT) → +3.35%

Coca-Cola Co (KO) → +0.82%

Top Losers: On the day of scraping, no major losers were observed — most stocks showed positive performance, suggesting it was a bullish trading session.

### 2. Trading Volume as an Indicator

Nike Inc (NKE) had a volume of 11.5M, while Microsoft (MSFT) showed 36.7M, indicating strong market participation on their bullish moves.

Coca-Cola’s relatively smaller move (+0.82%) still came with a healthy 9.7M trading volume, suggesting steady investor demand.

Higher trading volume + positive price change confirms the strength of a trend, making these stocks more reliable for short-term trading signals.

### 3. Cross-Market Comparisons

The dataset mixes US-based companies with Indian companies (e.g., 3M India), enabling cross-market insights.

US Tech stocks like Microsoft showed stronger momentum compared to Consumer staples like Coca-Cola, which moved more modestly.

This difference reflects how different sectors respond to global and regional economic triggers.

### 4. Sector-Wise Observations

Technology (Microsoft, Intel, Cisco) → Show strong price gains, suggesting investor confidence in innovation-driven growth.

Consumer Goods (Coca-Cola, McDonald’s, Walmart) → More stable with moderate changes, reflecting steady demand.

Industrials (Boeing, 3M India) → Tend to be more cyclical and influenced by global trade trends.

### 5. Opportunities for Predictive Analysis

With historical scraping, one could build models to forecast daily gainers/losers.

Volume + Price movement patterns can serve as strong features in machine learning–based trading models.

Even basic moving average tracking could highlight when companies like Microsoft or Nike shift from bullish to bearish momentum.

## Project Structure

├── stocks_ws.py       # Web scraping script

├── stocks.xlsx        # Output dataset (scraped stock details)

└── README.md          # Project documentation

## Tech Stack

- Python 3.12

- Libraries:

  - requests → Fetching HTML content

  - BeautifulSoup4 → Parsing and extracting stock details

  - pandas → DataFrame creation and Excel export

- Output: stocks.xlsx (Excel dataset of stock details)
