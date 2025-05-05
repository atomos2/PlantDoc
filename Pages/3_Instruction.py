import streamlit as st

with st.expander("ℹ️ Instructions"):
    st.markdown("""
    **How to Use the Application:**

    1. **Select the Plant Type:** Choose the plant category (e.g., Apple, Potato, Tomato, etc.) from the dropdown. This ensures the model validates predictions within the correct class range.
    
    2. **Upload an Image:** Upload a clear image of the plant **leaf only**. Blurry, distant, or background-heavy images may reduce accuracy.
    
    3. **View Image:** Click on **'Show Image'** to visually confirm that the uploaded image is correct and clearly visible.
    
    4. **Run Prediction:** Click **'Predict'** to identify the disease class.
        - If the **confidence score** is too low, the system will ask you to try with a better-quality image.
        - If the detected class **does not match** the selected plant type, the system will prompt you to verify the image or selection.

    ---
    **Recommendations:**
    - Ensure **good lighting** and **zoomed-in leaf focus**.
    - Use **JPG or PNG** images for best results.
    - The model is lightweight and optimized for mobile/web deployment. Occasional inaccuracies may occur, especially in edge cases.
    """)
