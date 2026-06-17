import logging
from config import WELLNESS_TIPS
import random

logger = logging.getLogger(__name__)

class WellnessAssistant:
    """Generate wellness recommendations based on mood"""
    
    def __init__(self):
        self.wellness_tips = WELLNESS_TIPS
    
    def get_recommendations(self, emotion):
        """Get wellness recommendations for emotion"""
        try:
            if emotion not in self.wellness_tips:
                emotion = 'Neutral'
            
            tips = self.wellness_tips[emotion]
            return {
                'emotion': emotion,
                'tips': tips,
                'count': len(tips)
            }
        except Exception as e:
            logger.error(f"Error getting recommendations: {str(e)}")
            return None
    
    def get_random_tip(self, emotion):
        """Get a random wellness tip for emotion"""
        try:
            tips = self.get_recommendations(emotion)
            if tips:
                return random.choice(tips['tips'])
            return None
        except Exception as e:
            logger.error(f"Error getting random tip: {str(e)}")
            return None
    
    def get_daily_routine(self, emotion):
        """Get daily routine suggestions for emotion"""
        routines = {
            'Happy': {
                'morning': 'Start with gratitude meditation',
                'midday': 'Continue positive momentum with a healthy snack',
                'evening': 'Reflect on what made you happy today'
            },
            'Sad': {
                'morning': 'Gentle stretching and deep breathing',
                'midday': 'Take a walk in nature or sunlight',
                'evening': 'Talk to someone you care about'
            },
            'Angry': {
                'morning': 'Practice calming breathing exercises',
                'midday': 'Take a break and step outside',
                'evening': 'Do a relaxing activity like yoga'
            },
            'Neutral': {
                'morning': 'Set a daily goal',
                'midday': 'Work on meaningful tasks',
                'evening': 'Review your progress'
            },
            'Fear': {
                'morning': 'Affirmations and grounding techniques',
                'midday': 'Connect with supportive people',
                'evening': 'Practice self-care activities'
            },
            'Surprise': {
                'morning': 'Embrace the unexpected',
                'midday': 'Explore new opportunities',
                'evening': 'Share your experience with others'
            },
            'Disgust': {
                'morning': 'Cleanse your space and mind',
                'midday': 'Engage in something you enjoy',
                'evening': 'Practice forgiveness and letting go'
            }
        }
        
        return routines.get(emotion, routines['Neutral'])
