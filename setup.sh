#!/bin/bash
# MoodSync Setup Script for Linux/Mac

echo "🎵 MoodSync - Setup Script"
echo "==========================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python3 --version

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "✓ Installing dependencies..."
pip install -r requirements.txt

# Create directories
echo "✓ Creating necessary directories..."
mkdir -p database models datasets songs reports logs assets

# Initialize database
echo "✓ Initializing database..."
python -c "from database.db import init_db; init_db()"

# Create .env file
if [ ! -f .env ]; then
    echo "✓ Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please update .env with your configuration"
fi

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "To run MoodSync, use:"
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
echo "The app will be available at: http://localhost:8501"
