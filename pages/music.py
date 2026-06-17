"""
Streamlit Page: Music
Music recommendations and player
"""

import streamlit as st
from modules.recommender import MusicRecommender
from modules.wellness import WellnessAssistant
from config import EMOTION_MUSIC_MAP

def show():
    st.title("🎵 Music Recommendations")
    
    # Select mood
    col1, col2 = st.columns(2)
    
    with col1:
        emotion = st.selectbox(
            "Select Your Mood:",
            ["Happy", "Sad", "Angry", "Neutral", "Fear", "Surprise", "Disgust"]
        )
    
    with col2:
        playlist_size = st.slider("Number of Songs:", 1, 20, 5)
    
    if st.button("Generate Playlist", key="playlist_btn"):
        with st.spinner("Creating your personalized playlist..."):
            recommender = MusicRecommender()
            playlist = recommender.create_playlist(emotion)
            
            if playlist:
                st.markdown(f"### 🎧 {playlist['name']}")
                st.markdown(f"**Emotion:** {emotion} | **Songs:** {playlist['length']}")
                st.markdown("---")
                
                # Display songs
                for i, song in enumerate(playlist['songs'][:playlist_size], 1):
                    col1, col2 = st.columns([0.5, 3])
                    
                    with col1:
                        st.markdown(f"### {i}")
                    
                    with col2:
                        st.markdown(f"**{song['title']}**")
                        st.markdown(f"*{song['artist']}*")
                        st.markdown(f"Genre: `{song['genre']}`")
                    
                    st.markdown("---")
    
    st.markdown("---")
    
    # Music Tags Info
    st.markdown("### 📌 Music Categories for Your Mood")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Emotion-Based Music Tags:**")
        tags = EMOTION_MUSIC_MAP.get(emotion, [])
        for tag in tags:
            st.markdown(f"🎵 `{tag}`")
    
    with col2:
        st.markdown("**Wellness Recommendations:**")
        wellness = WellnessAssistant()
        tips = wellness.get_recommendations(emotion)['tips']
        for tip in tips[:3]:
            st.markdown(f"✨ {tip}")
    
    st.markdown("---")
    
    # Features Info
    st.markdown("### 🚀 Coming Soon")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Spotify Integration**\n🎵 Play directly from Spotify")
    
    with col2:
        st.markdown("**YouTube Search**\n🎬 Find music videos")
    
    with col3:
        st.markdown("**Local Library**\n💿 Upload your own music")

if __name__ == "__main__":
    show()
