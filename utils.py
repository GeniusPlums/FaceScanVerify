import streamlit as st
import numpy as np
import face_recognition
from PIL import Image
import io
import cv2

def load_and_process_image(file_upload):
    """
    Load and process an uploaded image file for face verification.
    
    Args:
        file_upload: Streamlit file upload object
        
    Returns:
        numpy.ndarray: Image as a numpy array in RGB format
    """
    # Read the file as bytes
    image_bytes = file_upload.getvalue()
    
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    
    # Decode the image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert from BGR to RGB (face_recognition uses RGB)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    return rgb_img

def check_valid_image(file_upload):
    """
    Check if an uploaded image contains a valid, detectable face.
    
    Args:
        file_upload: Streamlit file upload object
        
    Returns:
        bool: True if a face is detected, False otherwise
    """
    # Process the image
    image = load_and_process_image(file_upload)
    
    # Try to detect faces
    face_locations = face_recognition.face_locations(image)
    
    # Return True if at least one face is detected
    return len(face_locations) > 0

def display_comparison_results(match_result, confidence_score):
    """
    Display the face verification results in a visually appealing way.
    
    Args:
        match_result (bool): Whether the faces match
        confidence_score (float): Confidence score of the match (0-1)
    """
    st.header("Verification Results")
    
    confidence_percentage = confidence_score * 100
    threshold_percentage = 60  # Defining a threshold for match/no match
    
    if match_result:
        st.success("✅ IDENTITY VERIFIED")
        st.markdown(f"The selfie and ID document appear to show the **same person**.")
    else:
        st.error("❌ IDENTITY VERIFICATION FAILED")
        st.markdown(f"The selfie and ID document appear to show **different people**.")
    
    # Display confidence meter
    st.subheader("Similarity Score")
    
    # Create a progress bar for confidence
    st.progress(confidence_score)
    
    # Show the exact score
    st.markdown(f"**Similarity: {confidence_percentage:.1f}%**")
    
    # Additional explanation based on confidence level
    if confidence_percentage >= 80:
        st.info("High confidence in the match.")
    elif confidence_percentage >= threshold_percentage:
        st.info("Moderate confidence in the match.")
    else:
        st.info("Low confidence in the match.")
    
    # Add disclaimer
    st.markdown("---")
    st.caption("""
    **Disclaimer**: This verification is based on computer vision algorithms and may not be 100% accurate. 
    For critical identity verification, additional measures are recommended.
    """)
