# Analyzing and Tracking Sentiment and Topics on Social Media  

## Overview  
This project explores consumer opinions on the recently launched video game **Baldur's Gate 3** using **social media text mining** and **natural language processing (NLP)** techniques. By analyzing discussions on Reddit, this study provides insights into how sentiment has evolved from development to launch and identifies key topics of discussion.

## Problem Definition  
The project focuses on answering two key questions:  
- How has sentiment towards **Baldur’s Gate 3** changed over time on **Reddit**?  
- What features and aspects of the game are discussed the most?  

## Data Collection  
- **Platform:** Reddit (via PRAW, the Python Reddit API Wrapper)  
- **Subreddits:** r/all, r/popular, r/gaming, r/pcgaming, r/gamingleaksandrumours, r/pcmasterrace, r/truegaming  
- **Timeframe:** June 11, 2011 – August 17, 2023  
- **Dataset:** 229,981 rows (~95MB, 133MB post-processing)  
- **Data Includes:** Post titles, URLs, upvotes, submission dates, and full comment threads  

## Data Processing  
- Tokenization, lowercasing, whitespace removal  
- Lemmatization & stemming to standardize text  
- Stopword removal (custom dictionary for slang and misspellings)  

## Methodology  
### Sentiment Analysis (VADER)  
- **VADER (Valence Aware Dictionary for Sentiment Reasoning)** was chosen due to its effectiveness in analyzing social media sentiment.  
- Results show **consistently positive sentiment** since early access, with a surge of positivity on launch day (August 3, 2023).  

### Topic Modeling (LDA)  
- **Latent Dirichlet Allocation (LDA)** was used to identify discussion topics.  
- Key topics included:  
  - Game launch success compared to industry norms  
  - Gameplay mechanics and character creation  
  - In-game features such as weapons and skills  
  - Positive player experiences  

## Key Findings  
- **Baldur's Gate 3** was widely praised from **early access (2020)** to **full release (2023)**.  
- **Launch discussions** highlighted game design choices, including the **lack of microtransactions**.  
- The model effectively **correlates player sentiment with industry trends** and **captures real-time discussions**.  

## Conclusion  
By combining **sentiment analysis (VADER)** and **topic modeling (LDA)**, this project successfully tracks and interprets player sentiment on social media. The approach can be extended to other video game launches or general sentiment analysis tasks in the entertainment industry.

## Technologies Used  
- **Python** (Pandas, NumPy, PRAW, NLTK, Scikit-learn, Gensim)  
- **Data Visualization** (Matplotlib, Seaborn)  
- **Machine Learning Models:** VADER for sentiment analysis, LDA for topic modeling  

## References  
- [Metacritic](https://www.metacritic.com/game/pc)  
- [OpenCritic](https://opencritic.com/browse/pc)  
- [DataCamp - Stemming and Lemmatization](https://www.datacamp.com/tutorial/stemming-lemmatization-python)  
- [VADER Sentiment Analysis Explained](https://medium.com/@piocalderon/vader-sentiment-analysis-explained-f1c4f9101cd9)  
