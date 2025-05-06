import cv2
import numpy as np
from face_verification import FaceVerifier

def test_verification():
    print("Testing face verification functionality...")
    
    # Load the test images
    selfie_img = cv2.imread('test_images/selfie.jpg')
    id_img = cv2.imread('test_images/id_card.jpg')
    different_img = cv2.imread('test_images/different_face.jpg')
    
    # Convert to RGB (face_recognition uses RGB)
    selfie_rgb = cv2.cvtColor(selfie_img, cv2.COLOR_BGR2RGB)
    id_rgb = cv2.cvtColor(id_img, cv2.COLOR_BGR2RGB)
    different_rgb = cv2.cvtColor(different_img, cv2.COLOR_BGR2RGB)
    
    # Create a verifier instance
    verifier = FaceVerifier(threshold=0.6)
    
    print("\nTest 1: Comparing similar faces (selfie and ID)")
    try:
        result, confidence = verifier.verify(selfie_rgb, id_rgb)
        print(f"Match result: {result}")
        print(f"Confidence score: {confidence:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print("\nTest 2: Comparing different faces (should not match)")
    try:
        result, confidence = verifier.verify(selfie_rgb, different_rgb)
        print(f"Match result: {result}")
        print(f"Confidence score: {confidence:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Test with invalid images
    print("\nTest 3: Testing with empty image (should raise an error)")
    empty_img = np.zeros((100, 100, 3), dtype=np.uint8)
    try:
        result, confidence = verifier.verify(empty_img, selfie_rgb)
        print(f"Match result: {result}")
        print(f"Confidence score: {confidence:.2f}")
    except Exception as e:
        print(f"Error (expected): {str(e)}")

if __name__ == "__main__":
    test_verification()
