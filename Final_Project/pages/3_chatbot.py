import streamlit as st

st.set_page_config(page_title="EV Chatbot", page_icon="🤖")


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

def get_bot_response(user_input):

    user_input = user_input.lower()

    if "ev" in user_input or "electric vehicle" in user_input:
        return "An Electric Vehicle (EV) is a vehicle powered by electricity stored in batteries."

    elif "battery" in user_input:
        return "EVs use lithium-ion batteries. Higher battery capacity generally gives a longer driving range."

    elif "range" in user_input:
        return "EV range refers to how many kilometers the vehicle can travel on a full charge."

    elif "charging" in user_input:
        return "EVs support slow AC charging (home) and fast DC charging (public stations)."

    elif "motor" in user_input:
        return "The electric motor converts electrical energy into mechanical energy to drive the wheels."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I am your EV Assistant. How can I help you today? 😊"

    elif "bye" in user_input:
        return "Goodbye! Have a great day! ⚡"

    else:
        return "I'm not sure about that. Try asking about EVs, batteries, range, charging, or motors."


st.title("🤖 EV Chatbot Assistant")
st.write("### Ask anything related to Electric Vehicles!")

user_query = st.text_input("Your Question:", placeholder="Type here...")

if st.button("Ask"):
    if user_query.strip() != "":
        bot_reply = get_bot_response(user_query)

        st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='user-msg'><b>You:</b> {user_query}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-msg'><b>Bot:</b> {bot_reply}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

