import cv2
import numpy as np

# Create a blank image with white background (representing a selfie)
def create_test_selfie():
    # Create a 400x400 white image
    img = np.ones((400, 400, 3), dtype=np.uint8) * 255
    
    # Draw a simple face outline
    # Head
    cv2.circle(img, (200, 200), 150, (0, 0, 0), 2)
    
    # Eyes
    cv2.circle(img, (150, 150), 20, (0, 0, 0), 2)  # Left eye
    cv2.circle(img, (250, 150), 20, (0, 0, 0), 2)  # Right eye
    cv2.circle(img, (150, 150), 5, (0, 0, 0), -1)  # Left pupil
    cv2.circle(img, (250, 150), 5, (0, 0, 0), -1)  # Right pupil
    
    # Nose
    cv2.line(img, (200, 170), (200, 220), (0, 0, 0), 2)
    
    # Mouth
    cv2.ellipse(img, (200, 250), (50, 20), 0, 0, 180, (0, 0, 0), 2)
    
    # Save the image
    cv2.imwrite('test_images/selfie.jpg', img)
    print("Test selfie created at test_images/selfie.jpg")

# Create a similar image with slight differences for the ID
def create_test_id():
    # Create a 400x400 light blue image (representing an ID)
    img = np.ones((400, 400, 3), dtype=np.uint8) * 255
    img[:, :, 0] = 240  # Add slight blue tint
    
    # Draw a similar face with slight differences
    # Head
    cv2.circle(img, (200, 200), 150, (0, 0, 0), 2)
    
    # Eyes
    cv2.circle(img, (150, 150), 20, (0, 0, 0), 2)  # Left eye
    cv2.circle(img, (250, 150), 20, (0, 0, 0), 2)  # Right eye
    cv2.circle(img, (150, 150), 5, (0, 0, 0), -1)  # Left pupil
    cv2.circle(img, (250, 150), 5, (0, 0, 0), -1)  # Right pupil
    
    # Nose
    cv2.line(img, (200, 170), (200, 220), (0, 0, 0), 2)
    
    # Mouth - slightly different
    cv2.ellipse(img, (200, 250), (60, 15), 0, 0, 180, (0, 0, 0), 2)
    
    # Add ID card borders
    cv2.rectangle(img, (30, 30), (370, 370), (0, 0, 0), 2)
    cv2.putText(img, "ID CARD", (150, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    # Save the image
    cv2.imwrite('test_images/id_card.jpg', img)
    print("Test ID created at test_images/id_card.jpg")

# Create a completely different face for negative testing
def create_different_face():
    # Create a 400x400 white image
    img = np.ones((400, 400, 3), dtype=np.uint8) * 255
    
    # Draw a different face
    # Head
    cv2.circle(img, (200, 200), 130, (0, 0, 0), 2)
    
    # Eyes - smaller and closer together
    cv2.circle(img, (170, 170), 15, (0, 0, 0), 2)  # Left eye
    cv2.circle(img, (230, 170), 15, (0, 0, 0), 2)  # Right eye
    cv2.circle(img, (170, 170), 4, (0, 0, 0), -1)  # Left pupil
    cv2.circle(img, (230, 170), 4, (0, 0, 0), -1)  # Right pupil
    
    # Nose
    cv2.line(img, (200, 190), (200, 230), (0, 0, 0), 2)
    
    # Mouth - different shape
    cv2.ellipse(img, (200, 260), (40, 10), 0, 0, 180, (0, 0, 0), 2)
    
    # Add glasses
    cv2.rectangle(img, (155, 160), (185, 180), (0, 0, 0), 1)
    cv2.rectangle(img, (215, 160), (245, 180), (0, 0, 0), 1)
    cv2.line(img, (185, 170), (215, 170), (0, 0, 0), 1)
    
    # Save the image
    cv2.imwrite('test_images/different_face.jpg', img)
    print("Different face created at test_images/different_face.jpg")

if __name__ == "__main__":
    create_test_selfie()
    create_test_id()
    create_different_face()
    print("All test images created successfully!")
