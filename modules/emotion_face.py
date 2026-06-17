import cv2
import numpy as np
from deepface import DeepFace
import logging
from config import FACE_CONFIDENCE_THRESHOLD

logger = logging.getLogger(__name__)

class FaceEmotionDetector:
    """Real-time face emotion detection using DeepFace"""
    
    def __init__(self):
        self.emotions = ['Happy', 'Sad', 'Angry', 'Neutral', 'Fear', 'Surprise', 'Disgust']
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_emotion(self, frame):
        """Detect emotion from video frame"""
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            
            if result:
                emotion_dict = result[0]['emotion']
                dominant_emotion = result[0]['dominant_emotion']
                confidence = emotion_dict[dominant_emotion] / 100.0
                
                return {
                    'emotion': dominant_emotion,
                    'confidence': confidence,
                    'all_emotions': {k: v/100.0 for k, v in emotion_dict.items()}
                }
        except Exception as e:
            logger.error(f"Error detecting emotion: {str(e)}")
        
        return None
    
    def detect_faces_with_emotions(self, frame):
        """Detect faces and their emotions"""
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            results = []
            for (x, y, w, h) in faces:
                face_roi = frame[y:y+h, x:x+w]
                emotion_result = self.detect_emotion(face_roi)
                
                if emotion_result:
                    results.append({
                        'bbox': (x, y, w, h),
                        'emotion': emotion_result['emotion'],
                        'confidence': emotion_result['confidence']
                    })
            
            return results
        except Exception as e:
            logger.error(f"Error detecting faces: {str(e)}")
            return []
    
    def draw_boxes(self, frame, detections):
        """Draw bounding boxes on frame"""
        for det in detections:
            x, y, w, h = det['bbox']
            emotion = det['emotion']
            confidence = det['confidence']
            
            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Put text
            text = f"{emotion} ({confidence:.2f})"
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        return frame
