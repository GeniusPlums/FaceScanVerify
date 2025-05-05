import streamlit as st
import os
import tempfile
from PIL import Image
import numpy as np

from face_verification import FaceVerifier
from utils import load_and_process_image, check_valid_image, display_comparison_results

# Set page configuration
st.set_page_config(
    page_title="KYC Face Verification",
    page_icon="🔍",
    layout="centered"
)

# Initialize session state variables if they don't exist
if 'verification_result' not in st.session_state:
    st.session_state.verification_result = None
if 'confidence_score' not in st.session_state:
    st.session_state.confidence_score = None
if 'error_message' not in st.session_state:
    st.session_state.error_message = None

def main():
    st.title("KYC Face Verification")
    
    # App description
    st.markdown("""
    This application compares a selfie with an ID document to verify if they show the same person.
    
    ### How it works:
    1. Upload a clear selfie photo
    2. Upload an image of your ID document showing your face
    3. The app will analyze and compare the facial features
    4. Results will show whether the faces match
    """)
    
    # Create columns for uploads
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload Selfie")
        selfie_file = st.file_uploader("Upload a clear selfie", type=['jpg', 'jpeg', 'png'])
        if selfie_file:
            try:
                if check_valid_image(selfie_file):
                    st.image(selfie_file, caption="Selfie Image", use_column_width=True)
                else:
                    st.error("No face detected in selfie. Please upload a clearer image.")
                    selfie_file = None
            except Exception as e:
                st.error(f"Error processing selfie: {str(e)}")
                selfie_file = None
    
    with col2:
        st.subheader("Upload ID Document")
        id_file = st.file_uploader("Upload your ID document", type=['jpg', 'jpeg', 'png'])
        if id_file:
            try:
                if check_valid_image(id_file):
                    st.image(id_file, caption="ID Document", use_column_width=True)
                else:
                    st.error("No face detected in ID document. Please upload a clearer image.")
                    id_file = None
            except Exception as e:
                st.error(f"Error processing ID: {str(e)}")
                id_file = None
    
    # Process verification when both images are uploaded
    verify_button = st.button("Verify Identity", disabled=(not selfie_file or not id_file))
    
    if verify_button:
        with st.spinner("Analyzing faces and comparing..."):
            try:
                # Process images
                selfie_img = load_and_process_image(selfie_file)
                id_img = load_and_process_image(id_file)
                
                # Create verifier instance
                verifier = FaceVerifier()
                
                # Perform verification
                result, confidence = verifier.verify(selfie_img, id_img)
                
                # Store results in session state
                st.session_state.verification_result = result
                st.session_state.confidence_score = confidence
                st.session_state.error_message = None
                
            except Exception as e:
                st.session_state.error_message = str(e)
                st.session_state.verification_result = None
    
    # Display results if available
    if st.session_state.error_message:
        st.error(f"Error during verification: {st.session_state.error_message}")
    
    if st.session_state.verification_result is not None:
        display_comparison_results(
            st.session_state.verification_result, 
            st.session_state.confidence_score
        )

if __name__ == "__main__":
    main()
