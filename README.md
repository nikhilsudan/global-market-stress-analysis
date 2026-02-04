# 🌍 Global Market Stress Analysis (2020–2026)

![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg) ![pandas](https://img.shields.io/badge/pandas-data%20analysis-blue) ![numpy](https://img.shields.io/badge/numpy-numerical%20computing-purple) ![matplotlib](https://img.shields.io/badge/matplotlib-visualization-orange) ![Jupyter](https://img.shields.io/badge/jupyter-notebook-red) ![MIT License](https://img.shields.io/badge/license-MIT-lightgrey)


---

## 📘 Overview

This project presents a structured empirical investigation of **global equity market stress** between **2020 and 2026**, a period marked by:

- The COVID-19 financial crisis  
- Unprecedented monetary tightening  
- Global inflation shocks  
- Geopolitical instability  
- Energy market disruptions  

Rather than developing trading strategies or black-box predictive models, the study adopts a **transparent, interpretable, and academically grounded framework** rooted in empirical finance and quantitative risk analysis.

The central objective is to document how **risk, volatility, and market fragility evolve across major equity markets during systemic stress**, and to assess whether these dynamics are synchronized or market-specific.

This project is designed to be:

- Reproducible  
- Statistically rigorous  
- Visually interpretable  
- Appropriate for academic and professional portfolios  

---

## 🎯 Research Questions

The analysis is organized around three core research questions:

1. **How did risk and performance evolve across major equity markets during a crisis-heavy period?**  
   - Were returns systematically penalized by volatility?  
   - Did some markets demonstrate greater resilience?

2. **Do global equity markets exhibit volatility clustering and synchronized turbulence?**  
   - Are stress episodes localized or systemic?  
   - Do volatility regimes persist over time?

3. **How did a unit of invested wealth evolve under repeated macro shocks?**  
   - Were recovery paths smooth or highly path-dependent?  
   - Did markets reconverge after crises?

These questions frame the empirical investigation that follows.

---

## 📊 Data

Three benchmark equity indices are analyzed:

- **NIFTY 50 (India)**  
- **S&P 500 (United States)**  
- **FTSE 100 (United Kingdom)**  

The dataset consists of **daily historical prices from January 2020 to early 2026**, sourced from publicly available market data.

All computations are implemented in Python using:

- `pandas` for data processing  
- `numpy` for numerical computation  
- `matplotlib` for professional visualization  
- `jupyter` for reproducible analysis  

---

## 🧮 Methodology

The analysis proceeds in four structured stages:

### **1. Data Cleaning and Alignment**
- Daily prices were cleaned and aligned to a common trading calendar.  
- Missing values were handled systematically to ensure comparability across markets.

### **2. Risk and Performance Measurement**
From the aligned price series, the following were computed:

- **Daily returns**  
- **30-day rolling annualized volatility**  
- **Maximum drawdowns**  
- **Sharpe ratios** (risk-adjusted returns)  

These metrics provide a comprehensive view of market risk and efficiency.

### **3. Turbulence Detection**
A data-driven turbulence indicator was constructed based on extreme volatility episodes. This allows identification of:

- Crisis regimes  
- Periods of systemic stress  
- Cross-market synchronization of shocks  

### **4. Comparative Market Analysis**
Markets were compared along three dimensions:

- **Risk (volatility and drawdowns)**  
- **Performance (cumulative wealth paths)**  
- **Stress alignment (turbulence timing and clustering)**  

This multi-layered approach ensures that conclusions are not driven by a single metric.

---

# 📊 Evidence & Findings (with Figures)

Each conclusion below is directly supported by one of your core visualizations.

---

## **1) Risk–Return Inefficiency in a Crisis Regime**

![Market Performance Snapshot](outputs/summary_dashboard_clean.png)

This figure summarizes key risk and performance metrics across markets.

### Empirical Findings

- All three markets exhibit **negative average returns over 2020–2026**, confirming that this period is dominated by crisis dynamics rather than steady growth.  
- **S&P 500 shows the highest volatility**, yet delivers poor risk-adjusted performance.  
- **NIFTY 50 appears most fragile in risk-adjusted terms**, indicating that investors were not compensated for the risk taken.  
- **FTSE 100 performs relatively better**, suggesting greater resilience during systemic turmoil.

### Interpretation

This figure reframes the entire study:  
> 2020–2026 should be interpreted as a *stress regime*, not a normal market cycle.

Traditional performance metrics such as the Sharpe ratio break down under such conditions.

---

## **2) Volatility Clustering and Turbulent Regimes**

![30-Day Volatility Regimes](outputs/volatility_regimes_30d_high_contrast.png)

This visualization overlays rolling volatility with shaded turbulent periods.

### Empirical Findings

- **Volatility clusters over time** — once markets enter high-volatility states, they tend to remain elevated for extended periods.  
- Major turbulence episodes align across all three markets, particularly during:
  - Early 2020 (COVID-19 crash)  
  - 2022 (inflation and rate hikes)  
  - Late 2024 (renewed global drawdowns)

### Interpretation

Markets behave as a **connected global system under stress**, supporting a core stylized fact of financial economics:

> *Volatility is persistent and contagious across markets.*

---

## **3) Comparative Risk Dynamics Across Markets**

![Rolling Volatility](outputs/rolling_volatility.png)

This chart compares rolling volatility across all three indices.

### Empirical Findings

- **S&P 500 consistently exhibits the highest volatility**, reflecting sensitivity to macroeconomic shocks.  
- **FTSE 100 is structurally more stable**, with fewer extreme volatility spikes.  
- **NIFTY 50 lies in between**, showing moderate risk but sharper jumps during crises.

### Risk Interpretation

From a portfolio perspective:

- Lower risk exposure → **FTSE 100**  
- Higher risk sensitivity → **S&P 500**  
- Emerging market exposure → **NIFTY 50**

This aligns with standard empirical characterizations of developed versus emerging markets.

---

## **4) Path-Dependent Wealth Under Repeated Shocks**

![Cumulative Performance](outputs/cumulative_performance.png)

This figure tracks how ₹1 / $1 / £1 evolves over time in each market.

### Empirical Findings

- All markets experienced deep drawdowns in 2020.  
- Recovery paths are **highly uneven and non-linear**, rather than smooth exponential growth.  
- Wealth trajectories diverge sharply during crises and only slowly reconverge.

### Core Conclusion

Market performance is **shock-driven rather than trend-driven**.

This reinforces the project’s central thesis:

> Financial markets are structurally fragile under stress and do not behave like equilibrium systems.

---

## 🎯 Contribution of the Project

This study demonstrates:

- Rigorous data handling  
- Sound financial reasoning  
- Clear statistical interpretation  
- Professional visualization  
- Transparent methodology  

It is suitable for:

- GitHub portfolios  
- MSc Data Science applications  
- Quantitative Finance track records  
- Financial Mathematics programs  

---

## 🚀 Future Extensions

Possible next steps include:

- Cross-market volatility spillovers  
- Lead–lag relationships between indices  
- Regime-switching models  
- Tail-risk analysis (CVaR)  
- Contagion modeling  

---

## 📌 Reproducibility

All results are fully reproducible using the provided notebook and source code. Running the analysis from scratch will regenerate all figures in the `outputs/` directory.

---

## 👤 Author

Independent quantitative research project combining finance, statistics, and data science to study global market stress.

