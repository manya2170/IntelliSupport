
import os
import requests
import streamlit as st

# ---------------- CONFIGURATION ----------------

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://intellisupport-182428470121.asia-south1.run.app"
).rstrip("/")

st.set_page_config(
    page_title="IntelliSupport | AI Helpdesk",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b1120;
    color: #e5eaf5;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #111a2e;
    border-right: 1px solid #25324a;
}

[data-testid="stSidebar"] * {
    color: #e5eaf5;
}

.brand {
    font-size: 27px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
}

.brand span {
    color: #60a5fa;
}

.tagline {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 5px;
}

.hero {
    padding: 65px 20px 30px 20px;
    text-align: center;
}

.hero-icon {
    font-size: 48px;
    margin-bottom: 15px;
}

.hero h1 {
    color: #ffffff;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.hero p {
    color: #94a3b8;
    font-size: 16px;
}

.feature-card {
    background: linear-gradient(145deg, #17243b, #111a2e);
    border: 1px solid #2b3b57;
    padding: 20px;
    border-radius: 15px;
    min-height: 130px;
    margin-bottom: 12px;
}

.feature-card h4 {
    color: #93c5fd;
    margin-bottom: 8px;
}

.feature-card p {
    color: #aab8ce;
    font-size: 13px;
}

.status {
    background: #102b2a;
    color: #6ee7b7;
    border: 1px solid #1d5148;
    border-radius: 20px;
    padding: 8px 12px;
    font-size: 12px;
    display: inline-block;
}

.stChatMessage {
    background: #15223a;
    border: 1px solid #263853;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    border: 1px solid #3b82f6;
    border-radius: 14px;
}

.stButton > button {
    border-radius: 10px;
    border: 1px solid #334766;
    background: #192943;
    color: #e5eaf5;
    padding: 10px 14px;
}

.stButton > button:hover {
    border-color: #60a5fa;
    color: #93c5fd;
}

hr {
    border-color: #263853;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 25px 0;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown(
        '<div class="brand">💠 Intelli<span>Support</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tagline">AI-powered customer experience</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### Workspace")
    st.markdown("💬  AI Support Assistant")
    st.markdown("📚  Knowledge Base")
    st.markdown("⚡  Powered by RAG")

    st.markdown("---")

    st.markdown("### System Status")

    try:
        health = requests.get(
            f"{BACKEND_URL}/health",
            timeout=8
        )
        if health.ok:
            st.markdown(
                '<span class="status">● Backend Online</span>',
                unsafe_allow_html=True
            )
        else:
            st.warning("Backend unavailable")
    except requests.RequestException:
        st.error("Backend connection failed")

    st.markdown("---")

    if st.button("＋ New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.selected_question = None
        st.rerun()

    st.markdown("---")
    st.caption("IntelliSupport v1.0")
    st.caption("Built with FastAPI • Groq • RAG • Supabase")

# ---------------- MAIN HEADER ----------------

left, right = st.columns([3, 1])

with left:
    st.markdown("## AI Support Assistant")
    st.caption("Your intelligent assistant, available whenever you need help.")

with right:
    st.markdown(
        '<div style="text-align:right;padding-top:15px;">'
        '<span class="status">● AI SYSTEM ACTIVE</span></div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------- WELCOME SCREEN ----------------

if not st.session_state.messages:

    st.markdown("""
    <div class="hero">
        <div class="hero-icon">💠</div>
        <h1>How can we help you?</h1>
        <p>Ask a question and let our AI assistant find the right answer.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <h4>💳 Payment Assistance</h4>
            <p>Get help with failed payments and transaction issues.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore payment help →", use_container_width=True):
            st.session_state.selected_question = "How can I resolve a failed payment?"

    with c2:
        st.markdown("""
        <div class="feature-card">
            <h4>📦 Order Tracking</h4>
            <p>Understand order tracking and delivery information.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore order help →", use_container_width=True):
            st.session_state.selected_question = "How can I track my order?"

    with c3:
        st.markdown("""
        <div class="feature-card">
            <h4>↩️ Refund Support</h4>
            <p>Learn about refund eligibility and the refund process.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore refund help →", use_container_width=True):
            st.session_state.selected_question = "What is the refund policy?"

    st.markdown("<br>", unsafe_allow_html=True)

# ---------------- CHAT HISTORY ----------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CHAT FUNCTION ----------------

def send_message(prompt):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("IntelliSupport is thinking..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/rag-chat",
                    json={"message": prompt},
                    timeout=150
                )

                response.raise_for_status()
                answer = response.json().get(
                    "assistant_response",
                    "I couldn't generate a response. Please try again."
                )

            except requests.Timeout:
                answer = "The request took too long. Please try again."

            except requests.RequestException:
                answer = "I'm unable to connect to the support service right now. Please try again later."

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# ---------------- INPUT ----------------

prompt = st.chat_input("Type your question here...")

if st.session_state.selected_question:
    selected = st.session_state.selected_question
    st.session_state.selected_question = None
    send_message(selected)

elif prompt:
    send_message(prompt)

# ---------------- FOOTER ----------------

st.markdown("---")
st.markdown("""
<div class="footer">
    IntelliSupport · Intelligent Customer Support · Powered by AI
</div>
""", unsafe_allow_html=True)
