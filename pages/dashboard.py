"""
Streamlit Page: Dashboard
Main dashboard with emotion detection interface
"""

import streamlit as st
import cv2
from modules.emotion_text import TextEmotionAnalyzer
from modules.mood_fusion import MoodFusionEngine
from modules.recommender import MusicRecommender
from modules.wellness import WellnessAssistant
from database.db import save_mood, get_mood_history
from config import EMOTION_COLORS

def show():
    st.title("🎵 Dashboard")
    
    # Get latest mood
    moods = get_mood_history(st.session_state.user_id, limit=1)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if moods:
            current_mood = dict(moods[0])
            emotion = current_mood.get('final_emotion', 'Unknown')
            confidence = current_mood.get('final_confidence', 0)
            st.metric("Current Mood", emotion, f"{confidence:.1%}")
        else:
            st.metric("Current Mood", "Not Analyzed")
    
    with col2:
        moods_list = get_mood_history(st.session_state.user_id, limit=100)
        st.metric("Total Analyses", len(moods_list))
    
    with col3:
        st.metric("Account Status", "Active")
    
    st.markdown("---")
    
    # Emotion Detection Tabs
    tab1, tab2, tab3 = st.tabs(["📝 Text Analysis", "🎤 Voice Analysis", "🔄 Mood Fusion"])
    
    with tab1:
        st.markdown("### Text Emotion Analysis")
        text_input = st.text_area(
            "How are you feeling? Share your thoughts:",
            height=100,
            placeholder="Type your feelings here..."
        )
        
        if st.button("Analyze Text Emotion", key="text_analyze"):
            if text_input:
                with st.spinner("Analyzing emotion..."):
                    analyzer = TextEmotionAnalyzer()
                    result = analyzer.analyze(text_input)
                    
                    if result:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.metric(
                                "Detected Emotion",
                                result['emotion'],
                                f"{result['confidence']:.1%}"
                            )
                        
                        with col2:
                            # Show all emotion scores
                            st.markdown("**All Emotions:**")
                            emotions_text = "\n".join([f"- {e}: {s:.1%}" for e, s in result.get('all_emotions', {}).items()])
                            st.text(emotions_text)
                        
                        # Save to database
                        save_mood(
                            st.session_state.user_id,
                            None, None,
                            result['emotion'], result['confidence'],
                            None, None,
                            result['emotion'], result['confidence']
                        )
                        st.success("✅ Mood saved successfully!")
            else:
                st.error("Please enter some text")
    
    with tab2:
        st.markdown("### Voice Emotion Analysis")
        st.info("🎤 Voice emotion detection coming soon!")
        st.markdown("This feature will allow you to record your voice and analyze the emotion from your tone and speech patterns.")
    
    with tab3:
        st.markdown("### Mood Fusion Engine")
        st.markdown("Combine multiple emotion detections for accurate mood analysis.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            face_emotion = st.selectbox("Face Emotion:", ["Happy", "Sad", "Angry", "Neutral", "Fear", "Surprise", "Disgust"], key="face_select")
            face_conf = st.slider("Confidence:", 0.0, 1.0, 0.8, key="face_conf")
        
        with col2:
            text_emotion = st.selectbox("Text Emotion:", ["Happy", "Sad", "Angry", "Neutral", "Fear", "Surprise", "Disgust"], key="text_select")
            text_conf = st.slider("Confidence:", 0.0, 1.0, 0.8, key="text_conf")
        
        with col3:
            voice_emotion = st.selectbox("Voice Emotion:", ["Happy", "Sad", "Angry", "Neutral", "Fear", "Surprise", "Disgust"], key="voice_select")
            voice_conf = st.slider("Confidence:", 0.0, 1.0, 0.8, key="voice_conf")
        
        if st.button("Fuse Emotions", key="fuse_btn"):
            fusion = MoodFusionEngine()
            result = fusion.fuse_emotions(
                {'emotion': face_emotion, 'confidence': face_conf},
                {'emotion': text_emotion, 'confidence': text_conf},
                {'emotion': voice_emotion, 'confidence': voice_conf}
            )
            
            if result:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(
                        "Final Mood",
                        result['emotion'],
                        f"{result['confidence']:.1%}"
                    )
                
                with col2:
                    st.markdown("**Emotion Scores:**")
                    for emotion, score in result['scores'].items():
                        st.markdown(f"- {emotion}: {score:.1%}")
                
                # Save to database
                save_mood(
                    st.session_state.user_id,
                    face_emotion, face_conf,
                    text_emotion, text_conf,
                    voice_emotion, voice_conf,
                    result['emotion'], result['confidence']
                )
                st.success("✅ Mood saved!")

if __name__ == "__main__":
    show()
