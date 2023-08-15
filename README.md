# Streamlit App for TTC Subway Delay Prediction

Welcome to the **Streamlit App for TTC Subway Delay Prediction** project! This interactive data application is designed to help users predict the delay time of the Toronto Transit Commission (TTC) subway with a high accuracy of 93%, utilizing the powerful XGBoost algorithm. The app allows users to explore the dataset, make predictions, and gain insights for better transit planning and operational efficiency.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Dependencies](#dependencies)
- [Acknowledgments](#acknowledgments)

## Introduction
Public transportation systems play a crucial role in urban areas, and predicting subway delays can significantly impact both commuters' experiences and transit management. This project offers a streamlined solution to predicting TTC subway delays using advanced machine learning techniques and providing users with an intuitive interface to interact with the data and predictions.

## Installation
To run the Streamlit app locally, follow these steps:
1. Clone the repository:
    `git clone https://github.com/shivanisehrawat4/Streamlit-App-for-TTC-Subway-Delay.git`
    `cd Streamlit-App-for-TTC-Subway-Delay`

2. Install the required dependencies:
    `pip install -r requirements.txt`

## Usage
1. Navigate to the project directory and run the Streamlit app using the following command:
    `streamlit run app.py`

2. The app interface will open in your default web browser, allowing you to interact with the dataset and make predictions.

3. Explore the dataset using various visualization tools provided in the app. Understand patterns and trends related to subway delays.

4. Utilize the predictive capabilities of the app by entering relevant features. The XGBoost algorithm with a 93% accuracy rate will provide you with delay time predictions.

5. Gain insights into potential factors contributing to subway delays and make informed decisions for transit planning and operations.

## Files
- `app.py`: The main Streamlit application file that integrates data visualization, prediction, and user interface components.
- `data_pre_processing.ipynb`: Jupyter Notebook containing the data preprocessing steps applied to the dataset.
- `explore.py`: Python module for generating various data visualizations and exploratory analyses.
- `predict.py`: Python module for utilizing the trained XGBoost models to make delay predictions.
- `subway_delay_dt.pkl`, `subway_delay_gb.pkl`, `subway_delay_rf.pkl`: Pretrained DecisionTree, XGBoost, and RandomForest models saved as pickle files for delay prediction.

## Dependencies
The project relies on the following libraries and tools:
- Python 3.7+
- Streamlit
- Pandas
- Numpy
- Matplotlib
- Seaborn
- XGBoost

All the dependencies can be installed using the command mentioned in the [Installation](#installation) section.

## Acknowledgments
I would like to express my gratitude to the Toronto Transit Commission (TTC) for providing the dataset necessary for this project. Additionally, I acknowledge the contributions of the open-source community and the Streamlit development team for enabling us to create interactive data applications effortlessly.

Feel free to contribute, open issues, or provide feedback to help us enhance this project and make it even more valuable for improving public transportation experiences!


