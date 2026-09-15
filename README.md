# MUSAR-GRIP - A Streamlit Demo for the Random Forest Model from the Research Paper "Prediction model for growth hormone resistance in a subgroup of sarcopenic patients with IGF-I deficiency"

## Overview
This Streamlit demo provides an interactive interface for understanding and evaluating the model introduced in our research paper. It allows non-technical users to run inference, visualize the model's explainability, and experiment with different patient characteristics without writing code.
The goal is to make the model’s behavior transparent, reproducible, and easy to demonstrate the real world use of a developed model.


## Installation
Clone the repository and install dependencies:
```
pip install -r requirements.txt
cd path-to-project-venv
source Scripts/activate -- venv should be activated now
cd path-to-project
streamlit run app/main.py --server.port=8502 -- make sure you are calling the main app page
```

## Details
For more technical or methodical background, please refer to the research paper. The model was trained using Python 3.9. The publicily available streamlit framework required a higher Python version, see .runtime.txt.

## Live Demo
The app is publicily [available](https://geri-demo-app-bkav5jhksyxuvh55bknalj.streamlit.app/). Please use the buttons in the app to navigate between the pages and features of the application, rather than using the web browser functions such as ‘Back’ (Alt + Left Arrow). If the app happens to be down, you simply need to ‘wake it up’.

## Contact
For any concern regarding the application or code please get in touch with Desiree Nübler via [mail](mailto:Desiree.Nuebler@med.uni-muenchen.de). 
For any concern regarding the medical background and approach please get in touch with Dr. Linda Deißler via [mail](mailto:Linda.Deissler@med.uni-muenchen.de).
