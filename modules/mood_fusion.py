import numpy as np
import logging
from config import FACE_WEIGHT, TEXT_WEIGHT, VOICE_WEIGHT, EMOTIONS

logger = logging.getLogger(__name__)

class MoodFusionEngine:
    """Intelligent multi-modal emotion fusion"""
    
    def __init__(self):
        self.face_weight = FACE_WEIGHT
        self.text_weight = TEXT_WEIGHT
        self.voice_weight = VOICE_WEIGHT
        self.emotions = EMOTIONS
    
    def fuse_emotions(self, face_emotion=None, text_emotion=None, voice_emotion=None):
        """Fuse multiple emotion detections into final mood"""
        try:
            emotion_scores = {emotion: 0.0 for emotion in self.emotions}
            total_weight = 0.0
            
            # Process face emotion
            if face_emotion and 'emotion' in face_emotion:
                emotion = face_emotion['emotion']
                confidence = face_emotion.get('confidence', 0.5)
                score = confidence * self.face_weight
                emotion_scores[emotion] += score
                total_weight += self.face_weight
            
            # Process text emotion
            if text_emotion and 'emotion' in text_emotion:
                emotion = text_emotion['emotion']
                confidence = text_emotion.get('confidence', 0.5)
                score = confidence * self.text_weight
                emotion_scores[emotion] += score
                total_weight += self.text_weight
            
            # Process voice emotion
            if voice_emotion and 'emotion' in voice_emotion:
                emotion = voice_emotion['emotion']
                confidence = voice_emotion.get('confidence', 0.5)
                score = confidence * self.voice_weight
                emotion_scores[emotion] += score
                total_weight += self.voice_weight
            
            # Normalize scores
            if total_weight > 0:
                for emotion in emotion_scores:
                    emotion_scores[emotion] /= total_weight
            
            # Find dominant emotion
            final_emotion = max(emotion_scores, key=emotion_scores.get)
            final_confidence = emotion_scores[final_emotion]
            
            return {
                'emotion': final_emotion,
                'confidence': final_confidence,
                'scores': emotion_scores,
                'components': {
                    'face': face_emotion,
                    'text': text_emotion,
                    'voice': voice_emotion
                }
            }
        except Exception as e:
            logger.error(f"Error fusing emotions: {str(e)}")
            return None
    
    def get_fusion_weights(self):
        """Get current fusion weights"""
        return {
            'face': self.face_weight,
            'text': self.text_weight,
            'voice': self.voice_weight
        }
