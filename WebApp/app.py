import streamlit as st
import tensorflow as tf
import numpy as np

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) # return index of max element

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition", "Plant Diseases"])

# Main Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

elif app_mode == "About":
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into an 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purposes.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)
                """)

elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if st.button("Show Image"):
        st.image(test_image, use_column_width=True)
    # Predict button
    if st.button("Predict"):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        # Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))

elif app_mode == "Plant Diseases":
    st.header("Plant Diseases")
    diseases = {
        "Apple Scab": {
            "description": "A fungal disease caused by Venturia inaequalis, affecting apple trees and causing dark, scabby lesions on leaves and fruit.",
            "link": "https://en.wikipedia.org/wiki/Apple_scab"
        },
        "Black Rot": {
            "description": "Caused by the fungus Botryosphaeria obtusa, it affects apple trees, leading to blackened, rotting fruit and cankers on branches.",
            "link": "https://en.wikipedia.org/wiki/Black_rot_(fruit)"
        },
        "Cedar Apple Rust": {
            "description": "A fungal disease that requires two hosts: apple or crabapple, and eastern red cedar. It causes yellow-orange spots on leaves and fruit.",
            "link": "https://en.wikipedia.org/wiki/Gymnosporangium_juniperi-virginianae"
        },
        "Powdery Mildew": {
            "description": "A common fungal disease affecting a variety of plants, characterized by white, powdery fungal growth on leaves and stems.",
            "link": "https://en.wikipedia.org/wiki/Powdery_mildew"
        },
        "Cercospora Leaf Spot": {
            "description": "Caused by fungi in the genus Cercospora, it affects many plants, leading to round, necrotic spots on leaves.",
            "link": "https://en.wikipedia.org/wiki/Cercospora"
        },
        "Common Rust": {
            "description": "A fungal disease affecting maize, characterized by reddish-brown pustules on leaves.",
            "link": "https://en.wikipedia.org/wiki/Common_rust"
        },
        "Northern Leaf Blight": {
            "description": "A fungal disease of maize caused by Exserohilum turcicum, leading to long, grayish lesions on leaves.",
            "link": "https://en.wikipedia.org/wiki/Northern_corn_leaf_blight"
        },
        "Black Rot (Grape)": {
            "description": "Caused by the fungus Guignardia bidwellii, it affects grapevines, causing black, shriveled fruit and lesions on leaves.",
            "link": "https://en.wikipedia.org/wiki/Black_rot_(grape)"
        },
        "Esca (Black Measles)": {
            "description": "A complex disease of grapevines, involving several fungal pathogens, leading to leaf discoloration and blackened, rotting berries.",
            "link": "https://en.wikipedia.org/wiki/Esca_(grape)"
        },
        "Leaf Blight (Isariopsis Leaf Spot)": {
            "description": "Caused by the fungus Phomopsis viticola, it affects grapevines, leading to irregular, brown spots on leaves and fruit.",
            "link": "https://en.wikipedia.org/wiki/Phomopsis_viticola"
        },
        "Haunglongbing (Citrus Greening)": {
            "description": "A bacterial disease affecting citrus trees, causing yellowing of leaves, green fruit, and eventual tree death.",
            "link": "https://en.wikipedia.org/wiki/Citrus_greening_disease"
        },
        "Bacterial Spot (Peach)": {
            "description": "Caused by Xanthomonas campestris, it affects stone fruits like peaches, causing small, dark, water-soaked spots on leaves and fruit.",
            "link": "https://en.wikipedia.org/wiki/Bacterial_spot"
        },
        "Early Blight (Potato)": {
            "description": "A fungal disease caused by Alternaria solani, leading to concentric ring spots on leaves and tubers.",
            "link": "https://en.wikipedia.org/wiki/Alternaria_solani"
        },
        "Late Blight (Potato)": {
            "description": "Caused by the oomycete Phytophthora infestans, it leads to dark lesions on leaves and tubers, and was responsible for the Irish Potato Famine.",
            "link": "https://en.wikipedia.org/wiki/Phytophthora_infestans"
        },
        "Leaf Scorch (Strawberry)": {
            "description": "Caused by the fungus Diplocarpon earlianum, it leads to dark purple spots on strawberry leaves, which can coalesce and cause leaf death.",
            "link": "https://en.wikipedia.org/wiki/Leaf_scorch"
        },
        "Bacterial Spot (Tomato)": {
            "description": "Caused by Xanthomonas spp., it affects tomatoes, leading to small, water-soaked spots on leaves, stems, and fruit.",
            "link": "https://en.wikipedia.org/wiki/Bacterial_speck"
        },
        "Early Blight (Tomato)": {
            "description": "A common tomato disease caused by Alternaria solani, leading to dark, concentric spots on leaves, stems, and fruit.",
            "link": "https://en.wikipedia.org/wiki/Alternaria_solani"
        },
        "Late Blight (Tomato)": {
            "description": "Caused by Phytophthora infestans, it leads to dark, water-soaked lesions on leaves and fruit, with white mold growth under humid conditions.",
            "link": "https://en.wikipedia.org/wiki/Phytophthora_infestans"
        },
        "Leaf Mold (Tomato)": {
            "description": "Caused by the fungus Cladosporium fulvum, it results in yellow spots on upper leaf surfaces and olive-green mold on undersides.",
            "link": "https://en.wikipedia.org/wiki/Cladosporium_fulvum"
        },
        "Septoria Leaf Spot (Tomato)": {
            "description": "A fungal disease caused by Septoria lycopersici, it leads to small, water-soaked spots on leaves, eventually causing defoliation.",
            "link": "https://en.wikipedia.org/wiki/Septoria_lycopersici"
        },
        "Spider Mites (Two-Spotted Spider Mite)": {
            "description": "A tiny arachnid pest that feeds on plant sap, causing stippling, yellowing, and eventual leaf death.",
            "link": "https://en.wikipedia.org/wiki/Tetranychus_urticae"
        },
        "Target Spot (Tomato)": {
            "description": "Caused by the fungus Corynespora cassiicola, it leads to small, water-soaked spots on leaves that expand to form concentric rings.",
            "link": "https://en.wikipedia.org/wiki/Corynespora_cassiicola"
        },
        "Tomato Yellow Leaf Curl Virus": {
            "description": "A viral disease transmitted by whiteflies, causing yellowing and curling of leaves, stunted growth, and reduced fruit production.",
            "link": "https://en.wikipedia.org/wiki/Tomato_yellow_leaf_curl_virus"
        },
        "Tomato Mosaic Virus": {
            "description": "A viral disease causing mottling, yellowing, and distortion of leaves, and can reduce fruit yield and quality.",
            "link": "https://en.wikipedia.org/wiki/Tobacco_mosaic_virus"
        }
    }

    for disease, info in diseases.items():
        st.markdown(f"""
        ### {disease}
        - **Description:** {info['description']}
        - **[More Information]({info['link']})**
        """)
