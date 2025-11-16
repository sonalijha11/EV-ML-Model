import streamlit as st
import time

st.set_page_config(page_title="EV Chatbot", layout="wide")

st.markdown("""
<style>

body {
    background-color: #071e3d !important;
}

.chat-container {
    width: 80%;
    margin: auto;
    margin-top: 30px;
    padding: 20px;
    background: #0c2f5c;
    border-radius: 12px;
    height: 520px;
    overflow-y: auto;
}

.msg {
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 10px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
}

/* User message */
.user {
    background: #144272;
    color: white;
}

/* Bot message */
.bot {
    background: #205295;
    color: white;
}

.icon-box {
    background: #ffcc00;
    padding: 10px;
    border-radius: 50%;
    font-size: 18px;
}

.icon-bot {
    background: #00d4ff;
}

h2 {
    color: white;
    text-align: center;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = []

def bot_reply(q):
    q = q.lower()

    if "battery" in q:
        return "EV batteries usually last 6–8 years. Range depends on temperature, speed, and load."
    if "range" in q:
        return "Most EVs offer 250–450 km range depending on battery size and driving style."
    if "charge" in q:
        return "Fast charging takes 30–40 minutes for 80%. Slow AC charging takes 6–8 hours."
    if "motor" in q:
        return "EVs mainly use PMSM and induction motors for efficiency."
    if "hello" in q or "hi" in q:
        return "Hello! 👋 How can I assist you with EV knowledge?"
    
    return "Great question! I'm your EV assistant, always learning more! 😊"


st.markdown("<h2>ChatGPT-like Clone</h2>", unsafe_allow_html=True)

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for sender, message in st.session_state.chat:
    if sender == "user":
        st.markdown(
            f"""
            <div class='msg user'>
                <div class='icon-box'>🙋</div>
                <div>{message}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class='msg bot'>
                <div class='icon-box icon-bot'>🤖</div>
                <div>{message}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)


user_input = st.text_input("Message the EV Bot:", "")


if user_input:
  
    st.session_state.chat.append(("user", user_input))

   
    with st.spinner("Bot is typing..."):
        time.sleep(1)

    # Add bot response
    st.session_state.chat.append(("bot", bot_reply(user_input)))

    st.rerun()
