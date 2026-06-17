"""
Streamlit Page: Settings
User settings and preferences
"""

import streamlit as st
from database.db import get_user_by_username

def show():
    st.title("⚙️ Settings")
    
    # User Profile
    st.markdown("### 👤 User Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Username:** {st.session_state.username}")
        user = get_user_by_username(st.session_state.username)
        if user:
            st.markdown(f"**Email:** {user['email']}")
            st.markdown(f"**Member Since:** {user['created_at']}")
    
    with col2:
        if st.button("Edit Profile"):
            st.info("Profile editing coming soon")
    
    st.markdown("---")
    
    # Preferences
    st.markdown("### 🎨 Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        theme = st.selectbox(
            "Theme",
            ["Dark", "Light"],
            help="Choose your preferred theme"
        )
    
    with col2:
        notifications = st.checkbox(
            "Enable Notifications",
            value=True,
            help="Receive mood reminders"
        )
    
    language = st.selectbox(
        "Language",
        ["English", "Spanish", "French", "German"]
    )
    
    st.markdown("---")
    
    # Data Management
    st.markdown("### 📦 Data Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📥 Download Data"):
            st.info("Your data download will be prepared. Check your email.")
    
    with col2:
        if st.button("🔄 Reset Statistics"):
            if st.checkbox("Confirm reset (cannot be undone)"):
                st.warning("Feature coming soon")
    
    with col3:
        if st.button("🗑️ Delete Account"):
            if st.checkbox("I understand this is permanent"):
                st.error("Feature coming soon")
    
    st.markdown("---")
    
    # About
    st.markdown("### ℹ️ About MoodSync")
    st.info("""
    **MoodSync v1.0**
    
    AI-powered emotion recognition and music recommendation platform
    
    Built with:
    - TensorFlow & PyTorch
    - DeepFace & HuggingFace
    - Streamlit & SQLite
    
    © 2024 MoodSync. All rights reserved.
    """)

if __name__ == "__main__":
    show()
