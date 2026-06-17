"""
Streamlit Page: Login
User authentication and login page
"""

import streamlit as st
from modules.auth import AuthManager

def show():
    st.title("🎵 MoodSync - Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Welcome Back!")
        st.markdown("Login to your MoodSync account")
        st.markdown("---")
        
        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )
        
        col_login, col_register = st.columns(2)
        
        with col_login:
            if st.button("🔓 Login", use_container_width=True):
                if username and password:
                    user_id, message = AuthManager.login_user(username, password)
                    
                    if user_id:
                        st.session_state.user_id = user_id
                        st.session_state.username = username
                        st.session_state.authenticated = True
                        st.success("✅ Login successful!")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
                else:
                    st.error("Please enter username and password")
        
        with col_register:
            if st.button("📝 Register", use_container_width=True):
                st.session_state.page = "register"
                st.rerun()
        
        st.markdown("---")
        st.markdown("**Demo Credentials:**")
        st.info("Username: `demo`  \nPassword: `Demo@1234`")

if __name__ == "__main__":
    show()
