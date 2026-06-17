import random
import logging
from config import EMOTION_MUSIC_MAP, EMOTIONS

logger = logging.getLogger(__name__)

class MusicRecommender:
    """Music recommendation engine based on mood"""
    
    def __init__(self):
        self.emotion_map = EMOTION_MUSIC_MAP
        self.sample_playlist = {
            'Happy': [
                {'title': 'Good as Hell', 'artist': 'Lizzo', 'genre': 'upbeat'},
                {'title': 'Walking on Sunshine', 'artist': 'Katrina & The Waves', 'genre': 'energetic'},
                {'title': 'Don\'t Stop Me Now', 'artist': 'Queen', 'genre': 'motivational'},
            ],
            'Sad': [
                {'title': 'Someone Like You', 'artist': 'Adele', 'genre': 'calm'},
                {'title': 'Mad World', 'artist': 'Gary Jules', 'genre': 'soothing'},
                {'title': 'The Night We Met', 'artist': 'Lord Huron', 'genre': 'healing'},
            ],
            'Angry': [
                {'title': 'Meditation Ambient', 'artist': 'Various', 'genre': 'relaxation'},
                {'title': 'Peaceful Piano', 'artist': 'Yann Tiersen', 'genre': 'instrumental'},
                {'title': 'Ambient Soundscape', 'artist': 'Various', 'genre': 'ambient'},
            ],
            'Neutral': [
                {'title': 'Lo-Fi Hip Hop', 'artist': 'Various', 'genre': 'lo-fi'},
                {'title': 'Study Focus', 'artist': 'Various', 'genre': 'focus'},
                {'title': 'Jazz Instrumental', 'artist': 'Various', 'genre': 'jazz'},
            ],
            'Fear': [
                {'title': 'Rise Up', 'artist': 'Andra Day', 'genre': 'motivational'},
                {'title': 'Stronger', 'artist': 'Kelly Clarkson', 'genre': 'uplifting'},
                {'title': 'Eye of the Tiger', 'artist': 'Survivor', 'genre': 'motivational'},
            ],
            'Surprise': [
                {'title': 'Levitating', 'artist': 'Dua Lipa', 'genre': 'trending'},
                {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'genre': 'energetic'},
                {'title': 'As It Was', 'artist': 'Harry Styles', 'genre': 'trending'},
            ],
            'Disgust': [
                {'title': 'Calm Waters', 'artist': 'Various', 'genre': 'calming'},
                {'title': 'Peaceful Mind', 'artist': 'Various', 'genre': 'peaceful'},
                {'title': 'Meditation', 'artist': 'Various', 'genre': 'meditative'},
            ]
        }
    
    def recommend(self, emotion, count=5):
        """Get music recommendations for emotion"""
        try:
            if emotion not in self.emotion_map:
                emotion = 'Neutral'
            
            playlist = self.sample_playlist.get(emotion, self.sample_playlist['Neutral'])
            
            # Return random selection or all
            if len(playlist) <= count:
                return playlist
            else:
                return random.sample(playlist, count)
        except Exception as e:
            logger.error(f"Error recommending music: {str(e)}")
            return []
    
    def get_emotion_tags(self, emotion):
        """Get music tags for emotion"""
        return self.emotion_map.get(emotion, self.emotion_map['Neutral'])
    
    def create_playlist(self, emotion, name=None):
        """Create a complete playlist"""
        try:
            songs = self.recommend(emotion, count=20)
            
            playlist = {
                'name': name or f"{emotion} Vibes",
                'emotion': emotion,
                'songs': songs,
                'length': len(songs)
            }
            
            return playlist
        except Exception as e:
            logger.error(f"Error creating playlist: {str(e)}")
            return None
