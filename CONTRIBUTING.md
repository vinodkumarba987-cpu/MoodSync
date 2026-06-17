# Contributing to MoodSync

We love your input! We want to make contributing to MoodSync as easy and transparent as possible.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check if the issue already exists. When you create a bug report, include as many details as possible:

- **Use a clear, descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed**
- **Explain the behavior you expected**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear, descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Provide specific examples to demonstrate the idea**
- **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Clone your fork** locally
3. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
4. **Make your changes** with clear commit messages
5. **Push to your branch** (`git push origin feature/AmazingFeature`)
6. **Open a Pull Request** with a clear description

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/MoodSync.git
cd MoodSync

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows

# Install dependencies in development mode
pip install -r requirements.txt
pip install -e .

# Run the application
streamlit run app.py
```

## Code Standards

### Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Documentation

- Add docstrings to all functions and classes
- Update README.md if needed
- Add comments for non-obvious code

## Areas for Contribution

### High Priority
- [ ] Spotify API integration
- [ ] YouTube music search
- [ ] Real-time webcam face detection UI
- [ ] Voice emotion detection improvement
- [ ] Mobile app (React Native)

### Medium Priority
- [ ] Multi-language support
- [ ] Advanced analytics features
- [ ] Social sharing features
- [ ] Mood calendar view
- [ ] Email notifications

### Low Priority
- [ ] Theme customization
- [ ] Dark/Light theme toggle
- [ ] User preferences storage
- [ ] Settings page enhancements

## Getting Help

- Check existing [Issues](https://github.com/vinodkumarba987-cpu/MoodSync/issues)
- Read the [FAQ](FAQ.md)
- Review the [Documentation](README.md)

## License

By contributing to MoodSync, you agree that your contributions will be licensed under its MIT License.

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- Release notes
- GitHub contributors page

Thank you for contributing to MoodSync! 🎵
