import os
import streamlit as st
import time
import requests

BACKEND_URL = os.environ.get("BACKEND_URL", "https://thinkrai.onrender.com")

st.set_page_config(
    page_title="ThinkrAI | DSA Socratic Tutor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0e1117;
        font-family: 'Inter', sans-serif;
    }
    
    /* Chat Container */
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding-bottom: 100px;
    }

    /* Message Bubbles */
    .user-message {
        background-color: #2b313e;
        color: #ffffff;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin-bottom: 15px;
        text-align: right;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #3d4451;
        max-width: 80%;
        width: fit-content;
        margin-left: auto;
    }

    .bot-message {
        background: rgba(25, 28, 36, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color: #e0e0e0;
        padding: 20px;
        border-radius: 20px 20px 20px 5px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.05);
        max-width: 85%;
        width: fit-content;
    }

    /* Input Field */
    .stTextInput > div > div > input {
        background-color: #1a1d24;
        color: #ffffff;
        border: 1px solid #3d4451;
        border-radius: 12px;
        padding: 12px 15px;
        font-size: 16px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #4facfe;
        box-shadow: 0 0 0 1px #4facfe;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #13161c;
        border-right: 1px solid #2d333b;
    }
    
    /* Typography */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0e1117; 
    }
    ::-webkit-scrollbar-thumb {
        background: #3d4451; 
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #57606f; 
    }

</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("🧠 ThinkrAI")
    st.markdown("---")
    st.markdown("### About")
    st.info(
        "ThinkrAI uses the **Socratic Method** to help you master **Data Structures & Algorithms**. "
        "Instead of giving code, it asks guiding questions to strengthen your problem-solving skills."
    )

    st.markdown("### Suggested Topics")
    st.markdown("""
    - 🌳 **Trees & Graphs**
    - 🔗 **Linked Lists**
    - ⚡ **Dynamic Programming**
    - 🔍 **Searching & Sorting**
    """)
    st.markdown("---")
    st.markdown("### Settings")
    st.caption(f"Backend: `{BACKEND_URL}`")
    
    if st.button("Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()


st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>DSA Socratic Tutor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b9bb4; margin-bottom: 20px;'>Master Data Structures & Algorithms one question at a time.</p>", unsafe_allow_html=True)

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask a question about your topic..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    status_placeholder = st.empty()
    status_placeholder.info("Thinking...")
    
    try:
        response_placeholder = st.empty()
        full_response = ""
        
        max_retries = 3
        response = None
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    status_placeholder.warning(
                        f"🔄 Server is waking up... Retry {attempt}/{max_retries - 1} "
                        f"(Render free tier spins down after inactivity)"
                    )
                response = requests.post(
                    f"{BACKEND_URL}/query",
                    json={"question": prompt},
                    timeout=120
                )
                response.raise_for_status()
                break
            except requests.exceptions.Timeout:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2)
        
        status_placeholder.empty()
        response_text = response.json()["answer"]
        
        for chunk in response_text.split():
            full_response += chunk + " "
            time.sleep(0.02)
            response_placeholder.markdown(f'<div class="bot-message">{full_response}▌</div>', unsafe_allow_html=True)
        
        response_placeholder.markdown(f'<div class="bot-message">{full_response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        
    except requests.exceptions.Timeout:
        status_placeholder.empty()
        st.error(
            "⏱️ The server is taking too long to respond. "
            "This usually happens when the Render server is cold-starting. "
            "Please wait a minute and try again."
        )
    except requests.exceptions.ConnectionError:
        status_placeholder.empty()
        st.error(
            "🔌 Could not connect to the backend. "
            "Please check that the backend is deployed and running."
        )
    except Exception as e:
        status_placeholder.empty()
        st.error(f"An error occurred: {e}")
