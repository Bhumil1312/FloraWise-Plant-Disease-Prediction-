# FloraWise
FloraWise is an AI-powered web application for plant recognition and disease detection using deep learning. The project leverages TensorFlow, Keras, and Streamlit to classify plant species and detect diseases from leaf images. By providing real-time predictions, FloraWise aims to assist farmers, botanists, and researchers in early disease diagnosis and improving agricultural productivity.
## Features
**Plant Species Recognition**: Identifies plant species from leaf images.

**Disease Detection**: Detects plant diseases and provides actionable insights.

**User-Friendly Interface**: Enables easy image uploads for real-time classification.

**Deep Learning Model**: Trained on a large dataset using CNN (Convolutional Neural Networks).

**Streamlit Deployment**: Web-based interactive UI for seamless user experience.

## Repository Structure
```
FloraWise-Plant-Disease-Prediction-/
│── 📂 Notebooks/                 # Jupyter Notebooks for training & testing
│   ├── Train_plant_disease.ipynb  # Model training process
│   ├── Test_plant_disease.ipynb   # Model evaluation & testing
│
│── 📂 Model/                   # Saved deep learning model
│   ├── trained_model.h5         # Trained model file
│
│── 📂 WebApp/                  # Deployment files for Streamlit app
│   ├── app.py                   # Streamlit app main script
│   ├── home_page.jpeg           # Dependencies for Streamlit
│
│── 📂 Documentation/                      # Project documentation
│   ├── SDLC Documentation(FloraWise).pdf   # Software Development Life Cycle report
│
│── README.md                    # Overview and setup instructions
```
## Installation & Setup:
### Clone the repository
```
git clone https://github.com/yourusername/FloraWise-Plant-Disease-Prediction-.git
cd FloraWise-Plant-Disease-Prediction-
```
### Create a virtual environment & install dependencies
```
python -m venv FloraWise
source FloraWise/bin/activate  # On Windows use `FloraWise\Scripts\activate`
pip install -r WebApp/home_page.jpeg
```
### Run the Streamlit application
```
streamlit run WebApp/app.py
```
