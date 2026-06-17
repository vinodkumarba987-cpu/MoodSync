import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class MoodPredictionEngine:
    """Mood prediction using machine learning"""
    
    def __init__(self):
        self.rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.emotion_encoder = LabelEncoder()
        self.is_trained = False
    
    def prepare_features(self, mood_history):
        """Prepare features from mood history"""
        try:
            if not mood_history or len(mood_history) < 5:
                return None
            
            features = []
            targets = []
            
            for i in range(len(mood_history) - 1):
                # Extract features from current mood
                current = mood_history[i]
                next_mood = mood_history[i + 1]
                
                feature_vector = [
                    float(current.get('face_confidence', 0.5)),
                    float(current.get('text_confidence', 0.5)),
                    float(current.get('voice_confidence', 0.5)),
                    float(current.get('final_confidence', 0.5)),
                ]
                
                features.append(feature_vector)
                targets.append(float(next_mood.get('final_confidence', 0.5)))
            
            return np.array(features), np.array(targets)
        except Exception as e:
            logger.error(f"Error preparing features: {str(e)}")
            return None
    
    def train(self, mood_history):
        """Train prediction model"""
        try:
            result = self.prepare_features(mood_history)
            if result is None:
                return False
            
            X, y = result
            self.rf_model.fit(X, y)
            self.is_trained = True
            return True
        except Exception as e:
            logger.error(f"Error training model: {str(e)}")
            return False
    
    def predict(self, mood_history, days_ahead=1):
        """Predict future mood"""
        try:
            if not self.is_trained or not mood_history:
                return None
            
            # Use latest mood as input
            latest_mood = mood_history[0]
            feature_vector = np.array([[
                float(latest_mood.get('face_confidence', 0.5)),
                float(latest_mood.get('text_confidence', 0.5)),
                float(latest_mood.get('voice_confidence', 0.5)),
                float(latest_mood.get('final_confidence', 0.5)),
            ]])
            
            # Predict confidence
            predicted_confidence = self.rf_model.predict(feature_vector)[0]
            
            # Map to emotion (simple mapping for demo)
            if predicted_confidence > 0.7:
                predicted_emotion = 'Happy'
            elif predicted_confidence > 0.4:
                predicted_emotion = 'Neutral'
            else:
                predicted_emotion = 'Sad'
            
            return {
                'emotion': predicted_emotion,
                'confidence': float(predicted_confidence),
                'days_ahead': days_ahead,
                'predicted_date': (datetime.now() + timedelta(days=days_ahead)).strftime('%Y-%m-%d')
            }
        except Exception as e:
            logger.error(f"Error predicting mood: {str(e)}")
            return None
    
    def predict_trend(self, mood_history, days=7):
        """Predict mood trend"""
        try:
            predictions = []
            for day in range(1, days + 1):
                pred = self.predict(mood_history, day)
                if pred:
                    predictions.append(pred)
            
            return predictions
        except Exception as e:
            logger.error(f"Error predicting trend: {str(e)}")
            return []
