# FloraWise
FloraWise is an AI-powered web application for plant recognition and disease detection using deep learning. The project leverages TensorFlow, Keras, and Streamlit to classify plant species and detect diseases from leaf images. By providing real-time predictions, FloraWise aims to assist farmers, botanists, and researchers in early disease diagnosis and improving agricultural productivity.
## Features
🌿 **Plant Species Recognition**: Identifies plant species from leaf images.

🦠 **Disease Detection**: Detects plant diseases and provides actionable insights.

📷 **User-Friendly Interface**: Enables easy image uploads for real-time classification.

📊 **Deep Learning Model**: Trained on a large dataset using CNN (Convolutional Neural Networks).

🌐 **Streamlit Deployment**: Web-based interactive UI for seamless user experience.

## Repository Structure
```
FloraWise-Plant-Disease-Prediction-/
│── 📂 notebooks/               # Jupyter Notebooks for training & testing
│   ├── train_model.ipynb        # Model training process
│   ├── test_model.ipynb         # Model evaluation & testing
│
│── 📂 model/                   # Saved deep learning model
│   ├── flora_model.h5           # Trained model file
│
│── 📂 app/                     # Deployment files for Streamlit app
│   ├── app.py                   # Streamlit app main script
│   ├── requirements.txt         # Dependencies for Streamlit
│
│── 📂 docs/                    # Project documentation
│   ├── SDLC Documentation.pdf   # Software Development Life Cycle report
│
│── README.md                    # Overview and setup instructions
```
## Installation & Setup:
### Clone the repository
```
git clone https://github.com/yourusername/FloraWise-Plant-Disease-Prediction.git
cd FloraWise-Plant-Disease-Prediction-
```
### Create a virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r app/requirements.txt
```
### Run the Streamlit application
```
streamlit run app/app.py
```
