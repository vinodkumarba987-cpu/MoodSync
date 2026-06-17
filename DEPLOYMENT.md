# MoodSync Installation & Deployment Guide

## 🚀 Quick Start Installation

### Windows Installation

#### Step 1: Download and Extract
```bash
git clone https://github.com/vinodkumarba987-cpu/MoodSync.git
cd MoodSync
```

#### Step 2: Run Setup Script
```bash
setup.bat
```

Or manually:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir database models datasets songs reports logs assets

# Initialize database
python -c "from database.db import init_db; init_db()"
```

#### Step 3: Configure Environment
```bash
copy .env.example .env
# Edit .env with your configuration
```

#### Step 4: Run Application
```bash
streamlit run app.py
```

### Linux/Mac Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/vinodkumarba987-cpu/MoodSync.git
cd MoodSync
```

#### Step 2: Run Setup Script
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p database models datasets songs reports logs assets

# Initialize database
python -c "from database.db import init_db; init_db()"
```

#### Step 3: Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

#### Step 4: Run Application
```bash
streamlit run app.py
```

## 🐳 Docker Deployment

### Prerequisites
- Docker
- Docker Compose

### Quick Start with Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Access the application
# Open http://localhost:8501 in your browser

# View logs
docker-compose logs -f moodsync

# Stop the application
docker-compose down
```

### Manual Docker Commands

```bash
# Build the image
docker build -t moodsync:latest .

# Run the container
docker run -d \
  --name moodsync \
  -p 8501:8501 \
  -v $(pwd)/database:/app/database \
  -v $(pwd)/reports:/app/reports \
  -v $(pwd)/logs:/app/logs \
  moodsync:latest

# Access logs
docker logs -f moodsync

# Stop the container
docker stop moodsync

# Remove the container
docker rm moodsync
```

## ☁️ Cloud Deployment

### Heroku Deployment

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create Heroku app
heroku create moodsync-app

# Add Procfile
echo "web: streamlit run app.py --server.port=\\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### AWS Deployment

```bash
# Using AWS Elastic Beanstalk
eb init
eb create moodsync-env
eb deploy
eb open
```

### Google Cloud Deployment

```bash
# Using Google Cloud Run
gcloud run deploy moodsync \
  --source . \
  --platform managed \
  --region us-central1
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file with your configuration:

```env
# Database
DATABASE_PATH=./database/moodsync.db

# Logging
LOG_LEVEL=INFO

# Spotify Integration
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret

# Debug Mode
DEBUG_MODE=False
```

## 📊 Database Initialization

The database is automatically initialized on first run. To manually initialize:

```bash
python -c "from database.db import init_db; init_db()"
```

## 🧪 Testing

```bash
# Create a test user
python -c "
from modules.auth import AuthManager
user_id, msg = AuthManager.register_user('demo', 'demo@moodsync.com', 'Demo@1234')
print(f'User created: {user_id}')
"

# Login test
python -c "
from modules.auth import AuthManager
user_id, msg = AuthManager.login_user('demo', 'Demo@1234')
print(f'Login: {msg}')
"
```

## 🚨 Troubleshooting

### Issue: Module not found errors
**Solution:**
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Database locked
**Solution:**
```bash
# Remove the database file
rm database/moodsync.db
# Reinitialize
python -c "from database.db import init_db; init_db()"
```

### Issue: TensorFlow/GPU issues
**Solution:**
```bash
# Use CPU-only TensorFlow
pip install tensorflow-cpu
```

### Issue: Port 8501 already in use
**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

## 📋 System Requirements

- **Python**: 3.8+
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB for models and data
- **Webcam**: For face detection (optional)
- **Microphone**: For voice analysis (optional)

## 🔒 Security Considerations

1. **Change default credentials**: Update demo user password
2. **Use HTTPS**: In production, always use HTTPS
3. **Environment variables**: Never commit `.env` to version control
4. **Database backups**: Regularly backup the database
5. **Update dependencies**: Keep packages updated

## 📈 Performance Optimization

```bash
# Use production server instead of Streamlit's development server
pip install gunicorn
gunicorn -b 0.0.0.0:8501 app:app

# Use caching for faster performance
# Streamlit caching is built-in with @st.cache_data
```

## 🆘 Getting Help

- Check [README.md](README.md) for detailed documentation
- Review [Issues](https://github.com/vinodkumarba987-cpu/MoodSync/issues)
- Create a new issue for bug reports
- Submit pull requests for improvements

## 📝 License

MIT License - See LICENSE file for details

---

**Happy mood tracking! 🎵**
