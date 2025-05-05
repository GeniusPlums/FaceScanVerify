import face_recognition
import numpy as np
import cv2

class FaceVerifier:
    """
    A class to handle face verification operations between selfie and ID images.
    """
    
    def __init__(self, threshold=0.6):
        """
        Initialize the FaceVerifier class.
        
        Args:
            threshold (float): The similarity threshold for considering faces a match (0-1)
        """
        self.threshold = threshold
    
    def extract_face_encodings(self, image):
        """
        Extract face encodings from an image.
        
        Args:
            image (numpy.ndarray): The image containing faces
            
        Returns:
            list: Face encodings found in the image
            
        Raises:
            ValueError: If no faces are found or multiple faces detected
        """
        # Find all face locations in the image
        face_locations = face_recognition.face_locations(image)
        
        # If no faces are found, raise an error
        if not face_locations:
            raise ValueError("No faces detected in the image. Please upload a clearer image.")
        
        # If multiple faces are found, use the most prominent one but warn about it
        if len(face_locations) > 1:
            # Sort face locations by area (larger faces are likely the main subject)
            sorted_locations = sorted(
                face_locations,
                key=lambda loc: (loc[2] - loc[0]) * (loc[1] - loc[3]),
                reverse=True
            )
            
            # Use only the largest face
            face_locations = [sorted_locations[0]]
        
        # Get face encodings
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        return face_encodings
    
    def calculate_similarity(self, encoding1, encoding2):
        """
        Calculate similarity between two face encodings.
        
        Args:
            encoding1 (numpy.ndarray): First face encoding
            encoding2 (numpy.ndarray): Second face encoding
            
        Returns:
            float: Similarity score between 0 and 1 (1 being identical)
        """
        # Calculate face distance (lower is more similar)
        face_distance = face_recognition.face_distance([encoding1], encoding2)[0]
        
        # Convert distance to similarity score (1 - distance, with adjustments)
        # This conversion makes the score more intuitive (higher = more similar)
        similarity = 1.0 - face_distance
        
        return similarity
    
    def verify(self, selfie_image, id_image):
        """
        Verify if the selfie and ID images contain the same person.
        
        Args:
            selfie_image (numpy.ndarray): Selfie image
            id_image (numpy.ndarray): ID document image
            
        Returns:
            tuple: (match_result, confidence_score)
                match_result (bool): True if same person, False otherwise
                confidence_score (float): Confidence score of the match (0-1)
        
        Raises:
            ValueError: If face extraction fails
        """
        try:
            # Extract face encodings
            selfie_encodings = self.extract_face_encodings(selfie_image)
            id_encodings = self.extract_face_encodings(id_image)
            
            # Calculate similarity between the faces
            similarity = self.calculate_similarity(selfie_encodings[0], id_encodings[0])
            
            # Determine if it's a match based on threshold
            is_match = similarity >= self.threshold
            
            return is_match, similarity
            
        except Exception as e:
            raise ValueError(f"Face verification failed: {str(e)}")
