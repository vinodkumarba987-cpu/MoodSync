"""
Streamlit Page: Predictions
Mood predictions and forecasts
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_mood_history
from modules.prediction_engine import MoodPredictionEngine

def show():
    st.title("🔮 Mood Predictions")
    
    moods = get_mood_history(st.session_state.user_id, limit=50)
    
    if len(moods) < 5:
        st.warning("⚠️ Need at least 5 mood entries to make predictions.")
        st.info(f"Current entries: {len(moods)}/5")
        return
    
    st.markdown("### AI-Powered Mood Forecast")
    
    # Convert to dict format
    mood_dicts = [dict(m) for m in moods]
    
    # Train prediction engine
    engine = MoodPredictionEngine()
    engine.train(mood_dicts)
    
    # Get predictions
    predictions = engine.predict_trend(mood_dicts, days=7)
    
    if predictions:
        st.markdown("#### 7-Day Mood Forecast")
        
        # Create prediction dataframe
        pred_df = pd.DataFrame([
            {
                'Date': p['predicted_date'],
                'Predicted Mood': p['emotion'],
                'Confidence': f"{p['confidence']:.1%}"
            }
            for p in predictions
        ])
        
        st.dataframe(pred_df, use_container_width=True)
        
        # Visualization
        pred_visual = pd.DataFrame([
            {
                'date': p['predicted_date'],
                'confidence': p['confidence'],
                'emotion': p['emotion']
            }
            for p in predictions
        ])
        
        fig = px.line(
            pred_visual,
            x='date',
            y='confidence',
            title="Predicted Confidence Score Trend",
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Most Likely Mood (Next 7 Days):**")
            emotions_pred = [p['emotion'] for p in predictions]
            most_likely = max(set(emotions_pred), key=emotions_pred.count)
            st.metric("Prediction", most_likely)
        
        with col2:
            st.markdown("**Average Confidence:**")
            avg_conf = sum(p['confidence'] for p in predictions) / len(predictions)
            st.metric("Average", f"{avg_conf:.1%}")
    else:
        st.error("Could not generate predictions. Please try again.")

if __name__ == "__main__":
    show()
