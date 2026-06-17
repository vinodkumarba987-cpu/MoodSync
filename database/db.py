import sqlite3
import logging
from config import DATABASE_PATH, DATABASE_TIMEOUT
from datetime import datetime
import os

logger = logging.getLogger(__name__)

def init_db():
    """Initialize database with schema"""
    try:
        conn = sqlite3.connect(DATABASE_PATH, timeout=DATABASE_TIMEOUT)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Mood History table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                face_emotion TEXT,
                face_confidence REAL,
                text_emotion TEXT,
                text_confidence REAL,
                voice_emotion TEXT,
                voice_confidence REAL,
                final_emotion TEXT,
                final_confidence REAL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Songs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT,
                emotion_tag TEXT,
                file_path TEXT,
                duration INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Predictions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                predicted_mood TEXT,
                confidence REAL,
                time_horizon TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Reports table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                report_type TEXT,
                file_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Database initialization error: {str(e)}")
        return False

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE_PATH, timeout=DATABASE_TIMEOUT)
    conn.row_factory = sqlite3.Row
    return conn

def create_user(username, email, password_hash):
    """Create new user"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        ''', (username, email, password_hash))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        return None

def get_user_by_username(username):
    """Get user by username"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    except Exception as e:
        logger.error(f"Error getting user: {str(e)}")
        return None

def save_mood(user_id, face_emotion, face_conf, text_emotion, text_conf, voice_emotion, voice_conf, final_emotion, final_conf):
    """Save mood history"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO mood_history 
            (user_id, face_emotion, face_confidence, text_emotion, text_confidence, 
             voice_emotion, voice_confidence, final_emotion, final_confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, face_emotion, face_conf, text_emotion, text_conf, voice_emotion, voice_conf, final_emotion, final_conf))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        logger.error(f"Error saving mood: {str(e)}")
        return False

def get_mood_history(user_id, limit=100):
    """Get mood history for user"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM mood_history WHERE user_id = ?
            ORDER BY timestamp DESC LIMIT ?
        ''', (user_id, limit))
        moods = cursor.fetchall()
        conn.close()
        return moods
    except Exception as e:
        logger.error(f"Error getting mood history: {str(e)}")
        return []

def save_prediction(user_id, predicted_mood, confidence, time_horizon):
    """Save mood prediction"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO predictions (user_id, predicted_mood, confidence, time_horizon)
            VALUES (?, ?, ?, ?)
        ''', (user_id, predicted_mood, confidence, time_horizon))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        logger.error(f"Error saving prediction: {str(e)}")
        return False

def save_report(user_id, report_type, file_path):
    """Save report info"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reports (user_id, report_type, file_path)
            VALUES (?, ?, ?)
        ''', (user_id, report_type, file_path))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        logger.error(f"Error saving report: {str(e)}")
        return False
