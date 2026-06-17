import speech_recognition as sr
import librosa
import numpy as np
import logging
from config import VOICE_SAMPLE_RATE, VOICE_DURATION

logger = logging.getLogger(__name__)

class VoiceEmotionDetector:
    """Voice emotion detection using speech recognition and audio features"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.emotions = ['Happy', 'Sad', 'Angry', 'Neutral', 'Fear', 'Surprise', 'Disgust']
        self.sample_rate = VOICE_SAMPLE_RATE
    
    def transcribe_audio(self, audio_file_path):
        """Convert audio to text"""
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = self.recognizer.record(source)
            
            text = self.recognizer.recognize_google(audio)
            return text
        except Exception as e:
            logger.error(f"Error transcribing audio: {str(e)}")
            return None
    
    def extract_features(self, audio_file_path):
        """Extract audio features"""
        try:
            y, sr_val = librosa.load(audio_file_path, sr=self.sample_rate)
            
            # Extract features
            mfcc = librosa.feature.mfcc(y=y, sr=sr_val, n_mfcc=13)
            mfcc_mean = np.mean(mfcc, axis=1)
            
            zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
            zcr_mean = np.mean(zero_crossing_rate)
            
            spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr_val)[0]
            sc_mean = np.mean(spectral_centroid)
            
            return {
                'mfcc': mfcc_mean,
                'zcr': zcr_mean,
                'spectral_centroid': sc_mean
            }
        except Exception as e:
            logger.error(f"Error extracting features: {str(e)}")
            return None
    
    def detect_emotion(self, audio_file_path):
        """Detect emotion from audio file"""
        try:
            # Get transcript
            transcript = self.transcribe_audio(audio_file_path)
            
            # For now, return a basic emotion detection
            # In production, use a trained deep learning model
            emotion = 'Neutral'
            confidence = 0.7
            
            return {
                'emotion': emotion,
                'confidence': confidence,
                'transcript': transcript
            }
        except Exception as e:
            logger.error(f"Error detecting voice emotion: {str(e)}")
            return None
