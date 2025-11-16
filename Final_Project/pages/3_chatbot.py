import streamlit as st
import time

st.set_page_config(page_title="EV Chatbot", layout="wide")

# ---------------- CSS FOR BEAUTIFUL CHAT UI ----------------
st.markdown("""
<style>

body {
    background-color: #071e3d !important;
}

.chat-box {
    width: 80%;
    height: 520px;
    margin: auto;
    margin-top: 20px;
    padding: 20px;
    overflow-y: auto;
    background: #0c2f5c;
    border-radius: 12px;
}

.msg {
    padding: 15px;
    margin-top: 15px;
    border-radius: 10px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
}

.user {
    background: #144272;
    color: white;
}

.bot {
    background: #205295;
    color: white;
}

.icon {
    padding: 10px;
    border-radius: 50%;
    font-size: 18px;
}

.user-icon {
    background: #ffcc00;
}

.bot-icon {
    background: #00d4ff;
}

h2 {
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --------------- CHAT HISTORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# --------------- BOT LOGIC ----------------
def bot_reply(q):
    q = q.lower()

    if "what is ev" in q or "ev kya" in q:
        return "EV (Electric Vehicle) is a vehicle powered by an electric motor using a rechargeable battery instead of petrol/diesel. ⚡🚗"

    if "battery" in q:
        return "EV batteries last about 6–8 years. Range depends on battery size, weather, speed, and load."

    if "range" in q:
        return "Most EVs provide 250–450 km range depending on battery size and driving style."

    if "charge" in q:
        return "Fast charging: 30–40 minutes. Slow charging: 6–8 hours."

    if "motor" in q:
        return "Most EVs use PMSM or induction motors due to high efficiency and torque."

    if "hello" in q or "hi" in q:
        return "Hello! 👋 I'm your EV assistant. How can I help?"

    return "Awesome question! I'm your EV assistant — ask me anything about EVs! 😊"


# --------------- TITLE ----------------
st.markdown("<h2>ChatGPT-like Clone</h2>", unsafe_allow_html=True)

# --------------- CHAT WINDOW ----------------
chat_window = st.container()

with chat_window:
    st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

    for sender, message in st.session_state.chat:

        if sender == "user":
            st.markdown(
                f"""
                <div class='msg user'>
                    <div class='icon user-icon'>🙋</div>
                    <div>{message}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(
                f"""
                <div class='msg bot'>
                    <div class='icon bot-icon'>🤖</div>
                    <div>{message}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --------------- INPUT BOX ----------------
user_input = st.text_input("Ask something about EVs:", "")

# --------------- PROCESS INPUT ----------------
if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Typing..."):
        time.sleep(1)

    st.session_state.chat.append(("bot", bot_reply(user_input)))

    st.rerun()
