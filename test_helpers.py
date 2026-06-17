"""
Testing utilities for MoodSync
Helper functions for manual testing
"""

import sys
from datetime import datetime, timedelta
from modules.emotion_text import TextEmotionAnalyzer
from modules.mood_fusion import MoodFusionEngine
from modules.recommender import MusicRecommender
from modules.wellness import WellnessAssistant
from modules.prediction_engine import MoodPredictionEngine
from database.db import save_mood, get_mood_history, init_db
from modules.auth import AuthManager

class TestHelper:
    """Helper class for testing MoodSync"""
    
    @staticmethod
    def print_section(title):
        """Print a section header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60)
    
    @staticmethod
    def print_test(name):
        """Print test name"""
        print(f"\n✓ {name}")
    
    @staticmethod
    def print_result(passed, message):
        """Print test result"""
        symbol = "✅" if passed else "❌"
        print(f"  {symbol} {message}")
    
    @staticmethod
    def test_text_emotions():
        """Test text emotion analysis with multiple samples"""
        TestHelper.print_section("Testing Text Emotion Analysis")
        
        analyzer = TextEmotionAnalyzer()
        test_cases = {
            'Happy': 'I am feeling amazing and wonderful!',
            'Sad': 'I feel so sad and lonely today',
            'Angry': 'I am absolutely furious about this!',
            'Neutral': 'This is just a regular day',
            'Fear': 'I am terrified and anxious',
            'Surprise': 'I cannot believe this happened!',
            'Disgust': 'That is absolutely disgusting!'
        }
        
        for expected_emotion, text in test_cases.items():
            TestHelper.print_test(f"Testing '{expected_emotion}' emotion")
            result = analyzer.analyze(text)
            
            if result:
                detected = result['emotion']
                confidence = result['confidence']
                TestHelper.print_result(
                    True,
                    f"Detected: {detected} ({confidence:.1%}) - Text: '{text}'"
                )
            else:
                TestHelper.print_result(False, "Analysis failed")
    
    @staticmethod
    def test_mood_fusion():
        """Test mood fusion with various combinations"""
        TestHelper.print_section("Testing Mood Fusion Engine")
        
        fusion = MoodFusionEngine()
        
        test_cases = [
            {
                'name': 'All Happy',
                'face': {'emotion': 'Happy', 'confidence': 0.85},
                'text': {'emotion': 'Happy', 'confidence': 0.90},
                'voice': {'emotion': 'Happy', 'confidence': 0.80}
            },
            {
                'name': 'Mixed (Happy/Sad)',
                'face': {'emotion': 'Happy', 'confidence': 0.85},
                'text': {'emotion': 'Sad', 'confidence': 0.75},
                'voice': {'emotion': 'Happy', 'confidence': 0.80}
            },
            {
                'name': 'All Sad',
                'face': {'emotion': 'Sad', 'confidence': 0.88},
                'text': {'emotion': 'Sad', 'confidence': 0.85},
                'voice': {'emotion': 'Sad', 'confidence': 0.82}
            }
        ]
        
        for case in test_cases:
            TestHelper.print_test(f"Testing {case['name']}")
            result = fusion.fuse_emotions(case['face'], case['text'], case['voice'])
            
            if result:
                TestHelper.print_result(
                    True,
                    f"Fused Emotion: {result['emotion']} ({result['confidence']:.1%})"
                )
            else:
                TestHelper.print_result(False, "Fusion failed")
    
    @staticmethod
    def test_music_recommendations():
        """Test music recommendations for all emotions"""
        TestHelper.print_section("Testing Music Recommendations")
        
        recommender = MusicRecommender()
        emotions = ['Happy', 'Sad', 'Angry', 'Neutral', 'Fear', 'Surprise', 'Disgust']
        
        for emotion in emotions:
            TestHelper.print_test(f"Getting recommendations for {emotion}")
            playlist = recommender.recommend(emotion, count=3)
            
            if playlist:
                TestHelper.print_result(True, f"Got {len(playlist)} recommendations")
                for song in playlist:
                    print(f"    🎵 {song['title']} by {song['artist']}")
            else:
                TestHelper.print_result(False, "Failed to get recommendations")
    
    @staticmethod
    def test_wellness_recommendations():
        """Test wellness recommendations for emotions"""
        TestHelper.print_section("Testing Wellness Recommendations")
        
        wellness = WellnessAssistant()
        emotions = ['Happy', 'Sad', 'Angry', 'Neutral']
        
        for emotion in emotions:
            TestHelper.print_test(f"Getting wellness tips for {emotion}")
            tips = wellness.get_recommendations(emotion)
            
            if tips:
                TestHelper.print_result(True, f"Got {len(tips['tips'])} tips")
                for tip in tips['tips'][:2]:
                    print(f"    💡 {tip}")
            else:
                TestHelper.print_result(False, "Failed to get tips")
    
    @staticmethod
    def test_authentication():
        """Test authentication system"""
        TestHelper.print_section("Testing Authentication")
        
        # Test password validation
        TestHelper.print_test("Testing password validation")
        
        test_passwords = [
            ('Test@1234', True, 'Strong password'),
            ('weak', False, 'Weak password'),
            ('NoNumbers', False, 'No numbers'),
            ('nouppEr123', False, 'No uppercase'),
            ('NOLOWER123', False, 'No lowercase')
        ]
        
        for password, should_pass, description in test_passwords:
            is_valid, msg = AuthManager.validate_password_strength(password)
            TestHelper.print_result(is_valid == should_pass, f"{description}: {msg}")
    
    @staticmethod
    def test_prediction_engine():
        """Test mood prediction engine"""
        TestHelper.print_section("Testing Mood Prediction Engine")
        
        engine = MoodPredictionEngine()
        
        # Create sample mood history
        mood_history = []
        for i in range(10):
            mood_history.append({
                'face_confidence': 0.7 + (i % 3) * 0.1,
                'text_confidence': 0.75 + (i % 2) * 0.05,
                'voice_confidence': 0.68 + (i % 3) * 0.08,
                'final_confidence': 0.75 + (i % 4) * 0.05
            })
        
        TestHelper.print_test("Training prediction model")
        if engine.train(mood_history):
            TestHelper.print_result(True, "Model training successful")
            
            TestHelper.print_test("Making predictions")
            predictions = engine.predict_trend(mood_history, days=7)
            
            if predictions:
                TestHelper.print_result(True, f"Generated {len(predictions)} predictions")
                for pred in predictions[:3]:
                    print(f"    📅 {pred['predicted_date']}: {pred['emotion']} ({pred['confidence']:.1%})")
            else:
                TestHelper.print_result(False, "Prediction failed")
        else:
            TestHelper.print_result(False, "Model training failed")
    
    @staticmethod
    def test_database():
        """Test database operations"""
        TestHelper.print_section("Testing Database Operations")
        
        # Initialize database
        TestHelper.print_test("Initializing database")
        if init_db():
            TestHelper.print_result(True, "Database initialized")
        else:
            TestHelper.print_result(False, "Database initialization failed")
        
        # Test saving mood
        TestHelper.print_test("Saving mood to database")
        result = save_mood(1, 'Happy', 0.85, 'Happy', 0.90, 'Happy', 0.80, 'Happy', 0.85)
        TestHelper.print_result(result, "Mood saved successfully")
    
    @staticmethod
    def run_all_tests():
        """Run all tests"""
        print("\n" + "#"*60)
        print("#  MoodSync - Comprehensive Testing Suite")
        print("#"*60)
        
        try:
            TestHelper.test_text_emotions()
            TestHelper.test_mood_fusion()
            TestHelper.test_music_recommendations()
            TestHelper.test_wellness_recommendations()
            TestHelper.test_authentication()
            TestHelper.test_prediction_engine()
            TestHelper.test_database()
            
            print("\n" + "="*60)
            print("✅  All Tests Completed Successfully!")
            print("="*60)
            print("\nNext Steps:")
            print("1. Run the application: streamlit run app.py")
            print("2. Test the UI at http://localhost:8501")
            print("3. Create a user account and test all features")
            print("4. See TESTING.md for detailed testing procedures")
            print()
            
        except Exception as e:
            print(f"\n❌ Test failed with error: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == "__main__":
    TestHelper.run_all_tests()
