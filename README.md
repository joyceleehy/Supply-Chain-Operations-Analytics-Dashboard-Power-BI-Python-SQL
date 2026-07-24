# Supply Chain Operations Analytics Dashboard

## Overview

This project analyzes supply chain operational data to uncover delivery performance issues and operational bottlenecks.

Using Python, SQL, and Power BI, I developed an end-to-end analytics solution that transforms raw supply chain data into interactive dashboards and actionable business insights for monitoring fulfillment performance and supporting operational decision-making.

**Dataset:** DataCo Smart Supply Chain (Kaggle)

**Tools Used**

- Python (Pandas)
- SQL
- Power BI
- DAX
- Excel

---

# Business Problem

E-commerce businesses rely on efficient supply chain operations to deliver customer orders on time while maintaining operational efficiency.

Business teams require visibility into questions such as:

- Are customer orders being delivered on time?
- Which shipping methods are underperforming?
- What factors contribute most to delivery delays?
- Are operational issues isolated to specific product categories or broader logistics processes?

This project focuses on analyzing operational data to identify delivery performance patterns, uncover operational bottlenecks, and provide practical recommendations for improving supply chain performance.

---

# Analytics Workflow

## 1. Data Exploration & Cleaning (Python)

The raw dataset was explored and prepared using Python and Pandas.

Data preparation activities included:

- Reviewing order, customer, product, shipping, and delivery-related fields
- Removing irrelevant and empty columns
- Standardizing column names
- Converting date columns into consistent formats
- Handling data quality issues during preparation
- Performing exploratory data analysis (EDA) to understand business trends and data distribution

---

## 2. SQL Analysis

After cleaning, the dataset was analyzed using SQL to calculate operational KPIs and identify performance trends.

SQL was used to:

- Calculate fulfillment rate
- Measure on-time delivery performance
- Calculate average delivery delays
- Analyze cancellation rates
- Compare shipping performance across delivery modes
- Analyze regional and product category performance
- Prepare summarized datasets for Power BI visualization

---

## 3. Power BI Dashboard Development

The cleaned dataset was imported into Power BI to build an interactive dashboard for operational monitoring.

Dashboard development included:

- Data modeling within Power BI
- KPI calculations using DAX measures
- Interactive slicers and filters
- Trend analysis across delivery performance
- Exception-focused visualizations to highlight operational issues

---

# Key KPIs

The dashboard tracks the following operational metrics:

- Total Orders
- Fulfillment Rate
- On-Time Delivery Rate
- Average Delivery Delay
- Cancellation Rate
- Orders by Shipping Mode
- Orders by Region
- Product Category Performance

---

# Dashboard Pages

| Page | Purpose |
|------|---------|
| Executive Overview | High-level operational KPIs including order volume, fulfillment rate, on-time delivery rate, and cancellation rate |
| Delivery Performance Analysis | Delivery trends, shipping mode comparison, and SLA performance |
| Product & Regional Analysis | Delivery performance across product categories and regions |
| Exception Analysis | Identification of delayed deliveries and operational issues requiring attention |

---

## Executive Overview

![Executive Overview](dashboard_screenshots/01_executive_overview.png)

High-level operational dashboard summarizing key supply chain KPIs including fulfillment rate, on-time delivery rate, average delivery delay, cancellation rate, and overall order volume.

---

## Delivery Performance Analysis

![Delivery Performance Analysis](dashboard_screenshots/02_delivery_performance.png)

Analyzes delivery performance across shipping methods, identifies delay trends, and evaluates shipping efficiency.

---

## Product & Regional Analysis

![Product & Regional Analysis](dashboard_screenshots/03_product_regional_analysis.png)

Examines delivery performance across different product categories and geographical regions to identify operational patterns.

---

## Exception Analysis

![Exception Analysis](dashboard_screenshots/04_exception_analysis.png)

Highlights operational exceptions requiring attention, including delayed deliveries and underperforming shipping methods.

---

# Key Insights

## Delivery Timeliness Is the Main Operational Challenge

Only **45.17%** of orders were delivered on time, while late deliveries averaged **1.62 days** behind schedule.

The analysis indicates that delivery execution and timeline management are the primary operational challenges rather than order cancellation.

---

## Shipping Expectations May Not Match Operational Reality

On-time delivery performance varied significantly across shipping methods:

- First Class — **4.68%**
- Second Class — **23.37%**
- Standard Class — **61.93%**

The findings suggest that faster shipping commitments may not align with actual operational capabilities.

---

## Delivery Issues Are Systemic Rather Than Product-Specific

On-time delivery performance across product categories remained within a relatively narrow range of approximately **41–45%**.

This indicates that delivery challenges are more likely related to broader logistics processes rather than individual product categories.

---

## Fulfillment Challenges Are Driven by Timeliness

Fulfillment rate was **43.82%**, while cancellations remained relatively low at **2.05%**.

This suggests that improving delivery reliability would have a greater operational impact than focusing solely on reducing cancellations.

---

# Recommendations

Based on the analysis, the following improvements are recommended:

### Review Shipping Commitments

Reassess delivery promises for expedited shipping methods to better align customer expectations with operational capability.

### Improve Delivery Performance Monitoring

Monitor shipping mode performance, regional trends, and delivery delays regularly to identify operational bottlenecks earlier.

### Strengthen Exception Tracking

Implement automated monitoring for delivery delays and operational exceptions to support faster issue identification and resolution.

---

# Skills Demonstrated

- Python (Pandas)
- SQL
- Power BI
- DAX
- Data Cleaning
- Exploratory Data Analysis (EDA)
- KPI Development
- Data Visualization
- Operational Analytics
- Business Analysis
- Dashboard Design

---

# Repository Structure

```text
supply-chain-ops-dashboard/

├── python/
│   ├── explore_data.py
│   ├── clean_data.py
│   ├── load_to_sql.py
│   └── kpi_queries.py

├── data/
│   └── cleaned_supply_chain_data.csv

├── dashboard_screenshots/
│   ├── 01_executive_overview.png
│   ├── 02_delivery_performance.png
│   ├── 03_product_regional_analysis.png
│   └── 04_exception_analysis.png

├── Supply_Chain.pbix

└── README.md
```

---

# Future Improvements

Potential enhancements include:

- Develop demand forecasting models
- Build predictive models for delivery delays
- Automate operational reporting workflows
- Implement automated data quality monitoring
- Incorporate real-time shipment tracking

---

# About This Project

This project demonstrates an end-to-end analytics workflow using Python, SQL, and Power BI to transform raw supply chain data into actionable business insights.

The workflow covers:

**Raw Data → Data Cleaning → SQL Analysis → Power BI Dashboard → Business Recommendations**

The project showcases practical skills in operational analytics, data preparation, KPI development, dashboard design, and business storytelling.

---

## Connect

- **GitHub:** https://github.com/joyceleehy
- **Tableau Public:** https://public.tableau.com/app/profile/joyce.lee.how.yee
