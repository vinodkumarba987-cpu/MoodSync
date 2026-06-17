"""
Streamlit Page: Register
User registration page
"""

import streamlit as st
from modules.auth import AuthManager

def show():
    st.title("🎵 MoodSync - Register")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Create Your Account")
        st.markdown("Join MoodSync today")
        st.markdown("---")
        
        username = st.text_input(
            "Username",
            placeholder="Choose a username"
        )
        email = st.text_input(
            "Email",
            placeholder="your@email.com"
        )
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a strong password"
        )
        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm your password"
        )
        
        st.info("**Password Requirements:**\n- Minimum 8 characters\n- Uppercase & lowercase letters\n- At least one number")
        
        col_register, col_login = st.columns(2)
        
        with col_register:
            if st.button("✅ Register", use_container_width=True):
                if not username or not email or not password:
                    st.error("Please fill all fields")
                elif password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    user_id, message = AuthManager.register_user(username, email, password)
                    
                    if user_id:
                        st.success(f"✅ {message}")
                        st.info("Account created successfully! Redirecting to login...")
                        st.session_state.page = "login"
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
        
        with col_login:
            if st.button("🔙 Back to Login", use_container_width=True):
                st.session_state.page = "login"
                st.rerun()

if __name__ == "__main__":
    show()
