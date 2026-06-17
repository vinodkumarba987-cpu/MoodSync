"""
Streamlit Page: Analytics
Mood analytics and visualizations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_mood_history
from config import EMOTION_COLORS
from datetime import datetime, timedelta

def show():
    st.title("📊 Analytics Dashboard")
    
    # Get mood history
    moods = get_mood_history(st.session_state.user_id, limit=100)
    
    if not moods:
        st.info("No mood data available yet. Start detecting emotions to see analytics!")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame([
        {
            'timestamp': m['timestamp'],
            'emotion': m['final_emotion'],
            'confidence': m['final_confidence']
        }
        for m in moods
    ])
    
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Analyses", len(df))
    
    with col2:
        mood_counts = df['emotion'].value_counts()
        st.metric("Most Frequent Mood", mood_counts.index[0])
    
    with col3:
        st.metric("Average Confidence", f"{df['confidence'].mean():.1%}")
    
    with col4:
        unique_dates = df['date'].nunique()
        st.metric("Days Tracked", unique_dates)
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Emotion Distribution")
        emotion_dist = df['emotion'].value_counts()
        fig = px.pie(
            values=emotion_dist.values,
            names=emotion_dist.index,
            color_discrete_map=EMOTION_COLORS
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Emotion Frequency")
        fig = px.bar(
            emotion_dist,
            x=emotion_dist.index,
            y=emotion_dist.values,
            color=emotion_dist.index,
            color_discrete_map=EMOTION_COLORS
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Time series
    st.markdown("### Confidence Trend")
    df_sorted = df.sort_values('timestamp')
    fig = px.line(
        df_sorted,
        x='timestamp',
        y='confidence',
        title="Confidence Score Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Recent mood history table
    st.markdown("### Recent Mood History")
    display_df = df_sorted[['timestamp', 'emotion', 'confidence']].tail(10).copy()
    display_df['confidence'] = display_df['confidence'].apply(lambda x: f"{x:.1%}")
    st.dataframe(display_df, use_container_width=True)

if __name__ == "__main__":
    show()
