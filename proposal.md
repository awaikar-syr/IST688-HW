# Proposal for Basketball Game Analytics Project

## Title

**Analyzing Performance Trends in NBA Basketball**
## Team

- Collin Kneiss (GitHub ID: cjkneiss ) - Point of Contact (POC)
- Ankit Waikar (GitHub ID: awaikar-syr)
- Odbileg Erdenebileg (GitHub ID: 156724018 (not sure))

# Introduction
Our project aims to analyze and visualize performance trends in NBA basketball using historical player and team statistics. This analysis will help uncover patterns that can predict future performance and inform strategic decisions in coaching and player development. The objective is to provide actionable insights that are easily interpretable by coaches, analysts, and fans alike.

Currently, the analysis of NBA team performance often relies on basic statistics. Our approach utilizes advanced statistical modeling combined with machine learning techniques to derive insights from a comprehensive dataset of NBA statistics, which has not been extensively explored in existing literature. If successful, our project will not only enhance decision-making processes within teams but also enrich the viewing experience for fans.

# Literature Review
Current practices in basketball analytics often depend on traditional metrics like points, assists, and rebounds. However, these methods are limited in their ability to account for contextual factors such as game location, opponent strength, and player fatigue. Recent studies have highlighted the use of advanced metrics like Player Efficiency Rating (PER) and Win Shares, but there remains a gap in applying machine learning techniques to predict team performance based on a broader range of features  .

Stakeholders for this project include:
- **Coaches:** Who need data-driven insights to enhance game strategies and player performance.
- **Sports Analysts:** Seeking comprehensive performance data for in-depth analysis.
- **Fans:** Interested in understanding player performance trends and team dynamics.
- **Teams/Organizations:** Looking to leverage data for informed recruitment and investment decisions.

# Data and Methods

## Data
We will utilize datasets from [Basketball Reference](https://www.basketball-reference.com/) and the NBA API. The primary dataset contains the following columns related to NBA team statistics:

| Column | Explanation |
|--------|-------------|
| Rk | Rank of the team in the league based on overall performance. |
| Team | The name of the basketball team. An asterisk (*) may indicate a playoff team. |
| G | Total number of games played by the team during the season. |
| MP | Minutes Played per game by the team as a whole. |
| FG | Field Goals made per game. |
| FGA | Field Goals Attempted per game. |
| FG% | Field Goal Percentage, calculated as FG divided by FGA. |
| 3P | 3-Point Field Goals made per game. |
| 3PA | 3-Point Field Goals Attempted per game. |
| 3P% | 3-Point Percentage, calculated as 3P divided by 3PA. |
| 2P | 2-Point Field Goals made per game. |
| 2PA | 2-Point Field Goals Attempted per game. |
| 2P% | 2-Point Percentage, calculated as 2P divided by 2PA. |
| eFG% | Effective Field Goal Percentage. |
| FT | Free Throws made per game. |
| FTA | Free Throws Attempted per game. |
| FT% | Free Throw Percentage. |
| ORB | Offensive Rebounds per game. |
| DRB | Defensive Rebounds per game. |
| TRB | Total Rebounds per game. |
| AST | Assists per game. |
| STL | Steals per game. |
| BLK | Blocks per game. |
| TOV | Turnovers per game. |
| PF | Personal Fouls per game. |
| PTS | Points per game scored by the team. |
| Year | Year of the season these statistics represent. |

The dataset consists of over [number] rows and [number] columns, ensuring a comprehensive view of team performance across multiple seasons. The data has been verified for reliability through cross-referencing with official league statistics.

## Methods
Our modeling approach will involve preprocessing the data to handle missing values and normalize features. We will explore various statistical techniques and machine learning algorithms, including regression analysis and ensemble methods like Random Forest and Gradient Boosting, to predict team performance metrics. Model evaluation will be aligned with stakeholders' needs, focusing on metrics like R-squared values and Mean Squared Error (MSE).

# Project Plan
| Period       | Activity                                                       | Milestone                                               |
|--------------|---------------------------------------------------------------|--------------------------------------------------------|
| [Start Date] - [End Date] | Stakeholder analysis, EDA, and initial modeling with regression techniques | Completed stakeholder analysis and data exploration.   |
| [Start Date] - [End Date] | Data preprocessing and applying machine learning algorithms | Initial pass with cleaned data and model predictions. |
| [Start Date] - [End Date] | Model evaluation and final report preparation | Completed evaluation and submitted final report.      |

# Risks
Potential risks include:
- **Data Quality Issues:** If the data is found to be unreliable, we will identify alternative datasets and re-evaluate our modeling approach.
- **Model Overfitting:** To mitigate this, we will implement cross-validation techniques to ensure our model generalizes well to unseen data.
- **Time Constraints:** If we fall behind schedule, we will prioritize key milestones to ensure project completion.

### References
1. COLLIN's Reference 1
2. COLLIN's Reference 2

## Timeline
By [Oct 9]: Proposal

By [Oct ]: Data Description & Data Analysis

By [Sep ]: Classification 

By [Sep ]: Result Interpretation

By [Nov ]: Report & Slides

By [Nov ]: Polish 
