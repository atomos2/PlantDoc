import streamlit as st
import tensorflow as tf
import numpy as np
import time

# Your original TensorFlow model prediction function (unchanged)
def model_prediction(test_image):
    model = tf.keras.models.load_model("Model.h5")  
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(224, 224))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) 
    predictions = model.predict(input_arr)
    index = np.argmax(predictions)
    confidence = np.max(predictions)
    return index, confidence

# Streamlit Interface
st.header("Plant Leaf Disease Recognition")

# Plant type selection
option = st.selectbox(
    "Select your plant:",
    ("Apple", "Potato", "Tomato", "Cherry", "Corn"),
)

# Image upload
test_image = st.file_uploader("Upload a clear image of the plant leaf:")

# Class labels (same order as your model)
class_name = [
    "Apple Scab", "Apple Black Rot", "Apple Cedar Rust", "Apple Healthy",
    "Cherry (Including Sour) Powdery Mildew", "Cherry (Including Sour) Healthy",
    "Corn (Maize) Cercospora Leaf Spot/Grey Leaf", "Corn (Maize) Common Rust",
    "Corn (Maize) Northern Leaf Blight", "Corn (Maize) Healthy",
    "Potato Early Blight", "Potato Late Blight", "Potato Healthy",
    "Tomato Bacterial Spot", "Tomato Early Blight", "Tomato Late Blight",
    "Tomato Leaf Mold", "Tomato Septoria Leaf Spot", "Tomato Spider Mites/two spotted",
    "Tomato Target Spot", "Tomato Yellow Leaf Curl Virus", "Tomato Mosaic Virus", "Tomato Healthy"
]

# Mapping class indices to allowed ranges for each plant
plant_class_indices = {
    "Apple": list(range(0, 4)),
    "Cherry": list(range(4, 6)),
    "Corn": list(range(6, 10)),
    "Potato": list(range(10, 13)),
    "Tomato": list(range(13, 23))
}

# Show Image
if test_image and st.button("Show Image"):
    st.image(test_image, caption="Uploaded Leaf Image", use_column_width=True)

# Predict button
if test_image and st.button("Predict"):
    result_index = model_prediction(test_image)
    pred_class = result_index[0]
    pred_confidence = result_index[1]

    # Check confidence
    if pred_confidence < 0.45:
        st.warning("Low prediction confidence ({:.2f}%). The image may be unclear or not a plant leaf. Please upload a clearer image.".format(pred_confidence * 100))
    # Check if prediction matches selected plant
    elif pred_class not in plant_class_indices[option]:
        st.error(f"The prediction ({class_name[pred_class]}) does not match the selected plant category: **{option}**.")
    else:
        st.success("Prediction: **{}**\n\nConfidence: **{:.2f}%**".format(class_name[pred_class], pred_confidence * 100))
