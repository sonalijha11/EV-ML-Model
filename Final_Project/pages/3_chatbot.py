import streamlit as st

st.set_page_config(page_title="EV Chatbot", page_icon="🤖")

# ---------- Custom CSS -------
st.markdown("""
<style>
.chat-box {
    background-color: #0F172A;
    padding: 20px;
    border-radius: 10px;
    color: white;
    margin-top: 20px;
    font-size: 17px;
}
.user-msg {
    background-color: #1E293B;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 10px;
    color: #E2E8F0;
}
.bot-msg {
    background-color: #334155;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 10px;
    color: #F8FAFC;
}
</style>
""", unsafe_allow_html=True)

# ---------- RULE-BASED RESPONSES ----------
def get_bot_response(user_input):

    user_input = user_input.lower()

    if "ev" in user_input or "electric vehicle" in user_input:
        return "EV (Electric Vehicle) ek environmentally friendly vehicle hai jo battery mein stored electricity se chalta hai!"

    elif "battery" in user_input:
        return "An EV battery lithium-ion hoti hai. Zyada battery capacity = longer driving range."

    elif "range" in user_input:
        return "EV range ka matlab hai ek full charge par kitne kilometers gaadi chal sakti hai."

    elif "charging" in user_input:
        return "EVs generally slow AC charging (home) aur fast DC charging (public stations) support karte hain."

    elif "motor" in user_input:
        return "EV motor electric energy ko mechanical energy me convert karke wheels ko drive karti hai."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! Kaise ho? I am your EV Assistant 🤖"

    elif "bye" in user_input:
        return "Bye! Drive safe and keep learning about EVs ⚡"

    else:
        return "Sorry, mujhe samajh nahi aaya. Try asking about EV, battery, range, charging or motor!"

# ---------- UI ----------
st.title("🤖 EV Chatbot Assistant")
st.write("### EV se related kuch bhi poochho!")

user_query = st.text_input("Your Question:", placeholder="Type here...")

if st.button("Ask"):
    if user_query.strip() != "":
        bot_reply = get_bot_response(user_query)

        st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='user-msg'><b>You:</b> {user_query}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-msg'><b>Bot:</b> {bot_reply}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
