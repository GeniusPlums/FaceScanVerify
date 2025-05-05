# KYC Face Verification App

## Project Objective and Summary
This Streamlit application provides a user-friendly interface for KYC (Know Your Customer) face verification. It allows users to upload a selfie image and an ID document image, then compares the facial features to determine if they belong to the same person.

The application leverages computer vision and face recognition technologies to extract facial features and perform the comparison, providing a confidence score and verification result.

## Features and Functionality
- **Image Upload**: Users can upload both a selfie and an ID document image.
- **Face Detection**: The app detects if valid faces are present in the uploaded images.
- **Feature Extraction**: Facial features are extracted using the face_recognition library.
- **Facial Comparison**: Compares the facial features to determine if they match.
- **Results Display**: Provides a clear verification result with a confidence score.
- **Error Handling**: Handles various error scenarios such as invalid images or no faces detected.

## Instructions to Run the App Locally

### Prerequisites
- Python 3.6 or higher
- Virtual environment (recommended)

### Setup Steps
1. Clone this repository to your local machine.

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. Open your web browser and go to the URL displayed in your terminal (usually http://localhost:8501).

## Project Structure
- `app.py`: Main Streamlit application file containing the UI and interaction logic
- `face_verification.py`: Contains the FaceVerifier class for comparing facial features
- `utils.py`: Utility functions for image processing and result display
- `.streamlit/config.toml`: Streamlit configuration settings

## Technical Implementation
- **Face Detection**: Using the face_recognition library to detect faces in images
- **Feature Extraction**: Extracting facial encodings that represent unique facial features
- **Similarity Calculation**: Computing the similarity between facial encodings
- **Threshold-based Verification**: Determining match status based on a similarity threshold

## Industry Relevance
KYC (Know Your Customer) verification is critical in sectors such as:
- Banking and financial services
- Telecom user verification
- Online account creation and verification
- Secure access systems

This project demonstrates a key component of modern digital identity verification systems.
