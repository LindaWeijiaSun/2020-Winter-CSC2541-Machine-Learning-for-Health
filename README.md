# 2020-Winter-CSC2541-Machine-Learning-for-Health
CSC2541 Topics in Machine Learning: Machine Learning for Health (ML4H); 

**Instructor**: Dr. Marzyeh Ghassemi; 

**Course page**: https://cs2541-ml4h2020.github.io/

## Two problem sets

### Problem set 1 - Clinical Time Series
- Data exploration of [MIMIC-III critical care database](https://mimic.physionet.org/) using Postgre SQL.
- **Predicting Mortality in the ICU**:  
  - Train a logistic regression model (using scikit-learn) to predict in-ICU mortality from all of the variables
  - Use the clinical notes text data to train a bag-of-words model to predict in-ICU mortality

- **Predicting Hypertension with LSTMs**:
  - As a baseline, train a logistic regression to predict hypertension
  - Train an LSTM (using **Keras**) to predict hypertension
  
### Problem set 2 - Fairness in Healthcare
- Fairness Metrics
- **TF-IDF Model for ICU Mortality**:
  - Build a logistic regression model for ICU mortality on TF-IDF note representations, then evaluate its fairness with regards to gender.
- **Sentence Completion:**
  - Use [ClinicalBERT](https://arxiv.org/abs/1904.05342) to complete clinically relevant sentences (fill missing words).
- **Multi-Group Fairness Metric**
- **Bias**:
  - Construct a classifier to predict the CCS code groups using all notes in a multi-task manner

  
