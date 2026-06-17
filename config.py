import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).parent
DATABASE_DIR = BASE_DIR / "database"
MODELS_DIR = BASE_DIR / "models"
DATASETS_DIR = BASE_DIR / "datasets"
SONGS_DIR = BASE_DIR / "songs"
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"

for directory in [DATABASE_DIR, MODELS_DIR, DATASETS_DIR, SONGS_DIR, REPORTS_DIR, LOGS_DIR, ASSETS_DIR]:
    directory.mkdir(exist_ok=True)

DATABASE_PATH = os.getenv('DATABASE_PATH', str(DATABASE_DIR / 'moodsync.db'))
DATABASE_TIMEOUT = 30
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = LOGS_DIR / 'moodsync.log'

FACE_EMOTION_MODELS = ['DeepFace']
FACE_CONFIDENCE_THRESHOLD = 0.5
TEXT_EMOTION_MODEL = 'distilbert-base-uncased-finetuned-sst-2-english'
TEXT_CONFIDENCE_THRESHOLD = 0.5
TEXT_MAX_LENGTH = 512
VOICE_SAMPLE_RATE = 16000
VOICE_DURATION = 10
VOICE_CONFIDENCE_THRESHOLD = 0.5

FACE_WEIGHT = 0.50
TEXT_WEIGHT = 0.30
VOICE_WEIGHT = 0.20

EMOTIONS = ['Happy', 'Sad', 'Angry', 'Neutral', 'Fear', 'Surprise', 'Disgust']

MUSIC_PLAYBACK_VOLUME = 0.7
MUSIC_QUEUE_SIZE = 50

EMOTION_MUSIC_MAP = {
    'Happy': ['upbeat', 'energetic', 'motivational'],
    'Sad': ['calm', 'soothing', 'healing', 'lo-fi'],
    'Angry': ['relaxation', 'instrumental', 'ambient'],
    'Neutral': ['lo-fi', 'focus', 'study', 'jazz'],
    'Fear': ['motivational', 'uplifting'],
    'Surprise': ['trending', 'energetic'],
    'Disgust': ['calming', 'peaceful', 'meditative']
}

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID', '')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET', '')

APP_TITLE = "🎵 MoodSync – Your Mood, Your Music"
APP_ICON = "🎵"
DASHBOARD_THEME = "dark"

COLOR_SCHEME = {'primary': '#FF6B6B', 'secondary': '#4ECDC4', 'success': '#45B7D1'}
EMOTION_COLORS = {
    'Happy': '#FFD700', 'Sad': '#4ECDC4', 'Angry': '#FF6B6B',
    'Neutral': '#95A5A6', 'Fear': '#8B4513', 'Surprise': '#9B59B6',
    'Disgust': '#27AE60'
}

PASSWORD_MIN_LENGTH = 8
SESSION_TIMEOUT_MINUTES = 60
MAX_LOGIN_ATTEMPTS = 5

WELLNESS_TIPS = {
    'Happy': ['Maintain your positive energy!', 'Try learning something new.', 'Share your happiness.'],
    'Sad': ['Take a walk.', 'Listen to relaxing music.', 'Talk to a friend.'],
    'Angry': ['Practice breathing exercises.', 'Take a break.', 'Go for a walk.'],
    'Neutral': ['Listen to focus music.', 'Try productive tasks.', 'Take a meditation break.'],
    'Fear': ['Practice grounding.', 'Remember past successes.', 'Take deep breaths.'],
    'Surprise': ['Embrace the change.', 'Stay curious.', 'Share your excitement.'],
    'Disgust': ['Practice self-care.', 'Let go of negativity.', 'Spend time in nature.']
}

DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
