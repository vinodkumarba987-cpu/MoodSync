import bcrypt
import logging
from database.db import get_db_connection

logger = logging.getLogger(__name__)

class AuthManager:
    """User authentication management"""
    
    @staticmethod
    def hash_password(password):
        """Hash password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password, password_hash):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    
    @staticmethod
    def validate_password_strength(password):
        """Validate password strength"""
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        if not any(c.isupper() for c in password):
            return False, "Password must contain uppercase letters"
        if not any(c.islower() for c in password):
            return False, "Password must contain lowercase letters"
        if not any(c.isdigit() for c in password):
            return False, "Password must contain numbers"
        return True, "Password is strong"
    
    @staticmethod
    def register_user(username, email, password):
        """Register new user"""
        try:
            # Validate password
            is_valid, message = AuthManager.validate_password_strength(password)
            if not is_valid:
                return None, message
            
            # Hash password
            password_hash = AuthManager.hash_password(password)
            
            # Create user
            from database.db import create_user
            user_id = create_user(username, email, password_hash)
            
            if user_id:
                return user_id, "Registration successful"
            else:
                return None, "Username or email already exists"
        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
            return None, str(e)
    
    @staticmethod
    def login_user(username, password):
        """Authenticate user login"""
        try:
            from database.db import get_user_by_username
            user = get_user_by_username(username)
            
            if user and AuthManager.verify_password(password, user['password_hash']):
                return user['id'], "Login successful"
            else:
                return None, "Invalid username or password"
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return None, str(e)
