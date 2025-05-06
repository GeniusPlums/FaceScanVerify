import streamlit as st
import numpy as np
from PIL import Image
import io
import cv2
import base64

def generate_test_image_with_face():
    """Generate a test image with face-like features that is more likely to be detected by face_recognition."""
    # Create a 400x400 image with color similar to skin tone
    img = np.ones((400, 400, 3), dtype=np.uint8) * 255
    img[:, :, 0] = 200  # Adjust blue
    img[:, :, 1] = 180  # Adjust green
    img[:, :, 2] = 170  # Adjust red
    
    # Face oval
    cv2.ellipse(img, (200, 200), (160, 200), 0, 0, 360, (170, 150, 140), -1)
    
    # Add more realistic eye regions for better detection
    # Left eye region
    cv2.ellipse(img, (130, 150), (30, 20), 0, 0, 360, (255, 255, 255), -1)
    cv2.circle(img, (130, 150), 10, (50, 50, 80), -1)  # Iris
    cv2.circle(img, (130, 150), 4, (10, 10, 10), -1)   # Pupil
    
    # Right eye region
    cv2.ellipse(img, (270, 150), (30, 20), 0, 0, 360, (255, 255, 255), -1)
    cv2.circle(img, (270, 150), 10, (50, 50, 80), -1)  # Iris
    cv2.circle(img, (270, 150), 4, (10, 10, 10), -1)   # Pupil
    
    # Eyebrows
    cv2.ellipse(img, (130, 130), (35, 10), 0, 0, 180, (100, 80, 70), 3)
    cv2.ellipse(img, (270, 130), (35, 10), 0, 180, 360, (100, 80, 70), 3)
    
    # Nose with more detail
    cv2.ellipse(img, (200, 220), (15, 30), 0, 0, 180, (140, 120, 110), -1)
    cv2.ellipse(img, (200, 220), (25, 10), 180, 0, 180, (150, 130, 120), -1)
    
    # Mouth with more detail for better recognition
    cv2.ellipse(img, (200, 280), (60, 25), 0, 0, 180, (130, 40, 40), -1) # Outer lip
    cv2.ellipse(img, (200, 280), (50, 15), 0, 0, 180, (180, 100, 100), -1) # Inner lip
    
    # Add shading for 3D effect
    # Left cheek highlight
    cv2.ellipse(img, (120, 220), (40, 60), 45, 0, 360, (190, 170, 160), -1)
    # Right cheek highlight
    cv2.ellipse(img, (280, 220), (40, 60), 135, 0, 360, (190, 170, 160), -1)
    
    return img

def test_face_detection():
    """Test if our face_recognition module can detect our generated face."""
    import face_recognition
    
    print("Testing face detection on our generated test image...")
    
    # Generate test images
    test_face_img = generate_test_image_with_face()
    
    # Save for inspection
    cv2.imwrite('test_face.jpg', test_face_img)
    
    # Convert BGR to RGB (what face_recognition expects)
    rgb_img = cv2.cvtColor(test_face_img, cv2.COLOR_BGR2RGB)
    
    # Attempt face detection
    face_locations = face_recognition.face_locations(rgb_img)
    
    if face_locations:
        print(f"Success! Detected {len(face_locations)} face(s) in the test image.")
        print(f"Face location: {face_locations[0]}")
        return True
    else:
        print("No faces detected in the test image.")
        return False

if __name__ == "__main__":
    test_face_detection()
