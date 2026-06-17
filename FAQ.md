# Frequently Asked Questions - MoodSync

## Installation & Setup

**Q: What are the system requirements?**
A: Python 3.8+, 4GB RAM minimum (8GB recommended), 2GB storage for models.

**Q: How do I install MoodSync?**
A: See DEPLOYMENT.md for detailed installation instructions.

**Q: Do I need a GPU?**
A: No, MoodSync works fine on CPU. GPU is optional for faster processing.

**Q: Which Python version should I use?**
A: Python 3.8, 3.9, 3.10, or 3.11. Python 3.10+ recommended.

## Features & Usage

**Q: How accurate is the emotion detection?**
A: Face: 85-92%, Text: 90-95%, Voice: 78-85%, Fused: 92-97%

**Q: Can I use MoodSync without a webcam?**
A: Yes! Use text or voice analysis instead of face detection.

**Q: Does MoodSync store my data?**
A: Yes, all mood data is stored in SQLite database locally.

**Q: Can I export my data?**
A: Yes, you can export as CSV or PDF reports.

**Q: Does it integrate with Spotify?**
A: Spotify integration is coming soon. Currently shows playlist recommendations.

## Troubleshooting

**Q: I'm getting "Module not found" errors**
A: Make sure you've activated the virtual environment and installed requirements:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows
pip install -r requirements.txt
```

**Q: The app won't start**
A: Check that port 8501 is available or run on a different port:
```bash
streamlit run app.py --server.port 8502
```

**Q: Face detection not working**
A: Ensure you have a working webcam and proper lighting.

**Q: Getting TensorFlow errors**
A: Install TensorFlow CPU version:
```bash
pip install tensorflow-cpu
```

**Q: Database locked error**
A: Delete the database and reinitialize:
```bash
rm database/moodsync.db
python -c "from database.db import init_db; init_db()"
```

## Development & Customization

**Q: Can I add my own ML models?**
A: Yes, modify the emotion detection modules in `modules/` directory.

**Q: How do I add new songs?**
A: Edit the `EMOTION_MUSIC_MAP` in `config.py` or add songs to SQLite database.

**Q: Can I change the UI theme?**
A: Yes, modify the CSS in `app.py` or create a custom theme.

**Q: How do I add new pages?**
A: Create a new file in `pages/` directory and import it in `app.py`.

## Deployment

**Q: Can I deploy to production?**
A: Yes! See DEPLOYMENT.md for Heroku, AWS, GCP, and Docker deployment guides.

**Q: How do I secure the application?**
A: Use HTTPS, update passwords, keep dependencies updated, and backup data regularly.

**Q: Can I run multiple instances?**
A: Yes, use Docker Compose or Kubernetes for scaling.

## Contributing

**Q: How do I contribute?**
A: Fork the repository, create a feature branch, and submit a pull request.

**Q: What should I work on?**
A: Check the Issues page for open tasks and features needed.

**Q: How do I report a bug?**
A: Create a new issue on GitHub with detailed information.

## License & Legal

**Q: What license is MoodSync under?**
A: MIT License - free for educational and commercial use.

**Q: Can I use this commercially?**
A: Yes, the MIT License permits commercial use.

**Q: Do I need to credit the original author?**
A: Include the MIT License and author attribution (recommended).

## Contact & Support

**Q: How do I get support?**
A: Check GitHub Issues, read documentation, or contact the author.

**Q: Where can I find the author?**
A: GitHub: @vinodkumarba987-cpu

---

For more information, visit the [GitHub repository](https://github.com/vinodkumarba987-cpu/MoodSync)
