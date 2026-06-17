"""
Streamlit Page: Reports
Generate and download reports
"""

import streamlit as st
from database.db import get_mood_history
from modules.report_generator import ReportGenerator
from modules.wellness import WellnessAssistant

def show():
    st.title("📄 Reports & Exports")
    
    moods = get_mood_history(st.session_state.user_id, limit=100)
    
    if not moods:
        st.info("No mood data available to generate reports.")
        return
    
    mood_dicts = [dict(m) for m in moods]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Generate PDF Report")
        if st.button("Generate PDF", key="pdf_btn"):
            with st.spinner("Generating PDF report..."):
                generator = ReportGenerator()
                filename = generator.generate_mood_report(
                    st.session_state.username,
                    mood_dicts
                )
                
                if filename:
                    st.success(f"✅ Report generated: {filename}")
                    st.markdown(f"**File:** `{filename}`")
                else:
                    st.error("Failed to generate report")
    
    with col2:
        st.markdown("### 📥 Export CSV")
        if st.button("Export CSV", key="csv_btn"):
            with st.spinner("Exporting CSV..."):
                generator = ReportGenerator()
                filename = generator.export_csv(
                    st.session_state.username,
                    mood_dicts
                )
                
                if filename:
                    st.success(f"✅ CSV exported: {filename}")
                    st.markdown(f"**File:** `{filename}`")
                else:
                    st.error("Failed to export CSV")
    
    st.markdown("---")
    
    # Wellness Summary
    st.markdown("### 💡 Wellness Summary")
    
    if mood_dicts:
        latest_mood = mood_dicts[0]
        emotion = latest_mood.get('final_emotion', 'Neutral')
        
        wellness = WellnessAssistant()
        recommendations = wellness.get_recommendations(emotion)
        routine = wellness.get_daily_routine(emotion)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Current Mood: {emotion}**")
            st.markdown("**Wellness Recommendations:**")
            for tip in recommendations['tips']:
                st.markdown(f"- {tip}")
        
        with col2:
            st.markdown("**Suggested Daily Routine:**")
            st.markdown(f"🌅 **Morning:** {routine['morning']}")
            st.markdown(f"☀️ **Midday:** {routine['midday']}")
            st.markdown(f"🌙 **Evening:** {routine['evening']}")

if __name__ == "__main__":
    show()
