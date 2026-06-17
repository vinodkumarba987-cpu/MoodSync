from transformers import pipeline
import logging
from config import TEXT_CONFIDENCE_THRESHOLD

logger = logging.getLogger(__name__)

class TextEmotionAnalyzer:
    """Text emotion analysis using HuggingFace transformers"""
    
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        self.emotion_map = {
            'POSITIVE': 'Happy',
            'NEGATIVE': 'Sad'
        }
    
    def analyze(self, text):
        """Analyze emotion from text"""
        try:
            if not text or len(text.strip()) == 0:
                return None
            
            result = self.classifier(text[:512])[0]
            label = result['label']
            score = result['score']
            
            emotion = self.emotion_map.get(label, 'Neutral')
            
            return {
                'emotion': emotion,
                'confidence': score,
                'raw_label': label,
                'raw_score': score
            }
        except Exception as e:
            logger.error(f"Error analyzing text: {str(e)}")
            return None
    
    def analyze_batch(self, texts):
        """Analyze multiple texts"""
        try:
            results = self.classifier(texts[:512])
            analyses = []
            
            for result in results:
                label = result['label']
                score = result['score']
                emotion = self.emotion_map.get(label, 'Neutral')
                
                analyses.append({
                    'emotion': emotion,
                    'confidence': score
                })
            
            return analyses
        except Exception as e:
            logger.error(f"Error analyzing batch: {str(e)}")
            return []
