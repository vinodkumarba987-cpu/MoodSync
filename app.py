import streamlit as st
import logging
from modules.utils import setup_logging
from database.db import init_db
from config import APP_TITLE, APP_ICON

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

# Session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: #0e1117;
    }
    .stButton > button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #FF5252;
        box-shadow: 0 4px 8px rgba(255, 107, 107, 0.3);
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 2rem;
    }
    h2 {
        color: #4ECDC4;
        margin-top: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

def login_page():
    """Login page"""
    st.title(f"{APP_ICON} {APP_TITLE}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Login")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", key="login_btn"):
            if username and password:
                from modules.auth import AuthManager
                user_id, message = AuthManager.login_user(username, password)
                
                if user_id:
                    st.session_state.user_id = user_id
                    st.session_state.username = username
                    st.session_state.page = 'dashboard'
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please enter username and password")
        
        st.markdown("---")
        if st.button("Create Account"):
            st.session_state.page = 'register'
            st.rerun()

def register_page():
    """Registration page"""
    st.title(f"{APP_ICON} {APP_TITLE}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### Create Account")
        
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.button("Register", key="register_btn"):
            if not username or not email or not password:
                st.error("Please fill all fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            else:
                from modules.auth import AuthManager
                user_id, message = AuthManager.register_user(username, email, password)
                
                if user_id:
                    st.success(message)
                    st.info("Account created! Please login.")
                    if st.button("Go to Login"):
                        st.session_state.page = 'login'
                        st.rerun()
                else:
                    st.error(message)
        
        st.markdown("---")
        if st.button("Back to Login"):
            st.session_state.page = 'login'
            st.rerun()

def dashboard_page():
    """Main dashboard page"""
    st.title(f"🎵 Welcome, {st.session_state.username}!")
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown(f"### Logged in as: {st.session_state.username}")
        st.markdown("---")
        
        page_selection = st.radio(
            "Navigation",
            ["Dashboard", "Face Detection", "Text Analysis", "Voice Analysis", 
             "Music", "Analytics", "Predictions", "Reports", "Settings"]
        )
        
        st.markdown("---")
        if st.button("Logout"):
            st.session_state.user_id = None
            st.session_state.username = None
            st.session_state.page = 'login'
            st.rerun()
    
    # Main content
    if page_selection == "Dashboard":
        show_dashboard()
    elif page_selection == "Face Detection":
        show_face_detection()
    elif page_selection == "Text Analysis":
        show_text_analysis()
    elif page_selection == "Voice Analysis":
        show_voice_analysis()
    elif page_selection == "Music":
        show_music()
    elif page_selection == "Analytics":
        show_analytics()
    elif page_selection == "Predictions":
        show_predictions()
    elif page_selection == "Reports":
        show_reports()
    elif page_selection == "Settings":
        show_settings()

def show_dashboard():
    """Dashboard overview"""
    st.markdown("### Dashboard Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Analyses", "24")
    
    with col2:
        st.metric("Current Mood", "Happy", "89%")
    
    with col3:
        st.metric("Mood Streak", "7 days")
    
    st.markdown("---")
    st.markdown("### Quick Start")
    st.info("Select a detection method from the sidebar to start analyzing your mood!")

def show_face_detection():
    """Face emotion detection page"""
    st.markdown("### Real-Time Face Emotion Detection")
    
    st.info("Powered by DeepFace - Webcam access required")
    
    if st.button("Start Webcam Detection"):
        st.warning("Webcam detection requires additional setup. Use text or voice analysis for now.")

def show_text_analysis():
    """Text emotion analysis page"""
    st.markdown("### Text Emotion Analysis")
    
    text_input = st.text_area("Enter your text:", height=100)
    
    if st.button("Analyze Emotion"):
        if text_input:
            from modules.emotion_text import TextEmotionAnalyzer
            analyzer = TextEmotionAnalyzer()
            result = analyzer.analyze(text_input)
            
            if result:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Detected Emotion", result['emotion'])
                
                with col2:
                    st.metric("Confidence", f"{result['confidence']:.2%}")
                
                # Save to database
                from database.db import save_mood
                save_mood(
                    st.session_state.user_id,
                    None, None,
                    result['emotion'], result['confidence'],
                    None, None,
                    result['emotion'], result['confidence']
                )
                
                st.success("Mood saved successfully!")
        else:
            st.error("Please enter some text")

def show_voice_analysis():
    """Voice emotion detection page"""
    st.markdown("### Voice Emotion Analysis")
    st.info("Coming soon - Voice analysis feature")

def show_music():
    """Music recommendation page"""
    st.markdown("### Music Recommendations")
    
    emotion = st.selectbox("Select your mood:", 
                          ["Happy", "Sad", "Angry", "Neutral", "Fear", "Surprise", "Disgust"])
    
    if st.button("Get Recommendations"):
        from modules.recommender import MusicRecommender
        recommender = MusicRecommender()
        playlist = recommender.recommend(emotion, count=5)
        
        if playlist:
            st.markdown(f"### 🎵 {emotion} Vibes")
            for i, song in enumerate(playlist, 1):
                st.markdown(f"{i}. **{song['title']}** by {song['artist']}")

def show_analytics():
    """Analytics dashboard"""
    st.markdown("### Mood Analytics")
    
    from database.db import get_mood_history
    moods = get_mood_history(st.session_state.user_id, limit=30)
    
    if moods:
        st.markdown("### Recent Mood History")
        
        import pandas as pd
        df = pd.DataFrame([
            {
                'Timestamp': m['timestamp'],
                'Emotion': m['final_emotion'],
                'Confidence': m['final_confidence']
            }
            for m in moods
        ])
        
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No mood history yet. Start by analyzing your emotion!")

def show_predictions():
    """Mood predictions page"""
    st.markdown("### Mood Predictions")
    st.info("Based on your mood history, here are predictions for upcoming days.")
    
    from database.db import get_mood_history
    moods = get_mood_history(st.session_state.user_id, limit=50)
    
    if len(moods) >= 5:
        from modules.prediction_engine import MoodPredictionEngine
        engine = MoodPredictionEngine()
        
        # Convert to dict format for engine
        mood_dicts = [dict(m) for m in moods]
        
        if engine.train(mood_dicts):
            predictions = engine.predict_trend(mood_dicts, days=7)
            
            if predictions:
                st.markdown("### 7-Day Mood Forecast")
                
                import pandas as pd
                df = pd.DataFrame([
                    {
                        'Date': p['predicted_date'],
                        'Mood': p['emotion'],
                        'Confidence': f"{p['confidence']:.2%}"
                    }
                    for p in predictions
                ])
                
                st.dataframe(df, use_container_width=True)
    else:
        st.info("Need at least 5 mood entries to make predictions.")

def show_reports():
    """Reports generation page"""
    st.markdown("### Generate Reports")
    
    if st.button("Generate PDF Report"):
        from database.db import get_mood_history
        from modules.report_generator import ReportGenerator
        
        moods = get_mood_history(st.session_state.user_id, limit=100)
        generator = ReportGenerator()
        
        filename = generator.generate_mood_report(
            st.session_state.username,
            [dict(m) for m in moods]
        )
        
        if filename:
            st.success(f"Report generated: {filename}")
    
    if st.button("Export as CSV"):
        from database.db import get_mood_history
        from modules.report_generator import ReportGenerator
        
        moods = get_mood_history(st.session_state.user_id, limit=100)
        generator = ReportGenerator()
        
        filename = generator.export_csv(
            st.session_state.username,
            [dict(m) for m in moods]
        )
        
        if filename:
            st.success(f"CSV exported: {filename}")

def show_settings():
    """Settings page"""
    st.markdown("### Settings")
    
    st.markdown("#### Theme")
    theme = st.selectbox("Select theme:", ["Dark", "Light"])
    
    st.markdown("#### Notifications")
    notifications = st.checkbox("Enable notifications", value=True)
    
    st.markdown("#### Data")
    if st.button("Download All Data"):
        st.info("Data download feature coming soon")
    
    if st.button("Clear History"):
        if st.checkbox("I'm sure I want to delete all mood history"):
            st.warning("This action cannot be undone")

# Main app logic
if __name__ == "__main__":
    if st.session_state.user_id is None:
        if st.session_state.page == 'register':
            register_page()
        else:
            login_page()
    else:
        dashboard_page()
