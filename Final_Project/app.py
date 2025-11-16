import streamlit as st

st.set_page_config(page_title="EV App", layout="wide")

# ---------- CUSTOM CSS (Premium Animated UI) ----------
st.markdown("""
<style>

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes glow {
    0% { text-shadow: 0 0 10px #00eaff; }
    50% { text-shadow: 0 0 20px #00eaff; }
    100% { text-shadow: 0 0 10px #00eaff; }
}

.center-box {
    background: rgba(0, 102, 255, 0.1);
    padding: 40px;
    border-radius: 20px;
    width: 70%;
    margin: 80px auto;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
    border: 1px solid #0ff;
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
}

.glow-text {
    font-size: 46px;
    color: #2DE2E6;
    font-weight: 800;
    animation: fadeIn 2s ease-out, glow 2s infinite alternate;
}

.sub-text {
    font-size: 22px;
    color: #bbb;
    margin-top: 10px;
    animation: fadeIn 2.5s ease-out;
}

/* Sidebar CSS */
.sidebar-title {
    font-size: 26px;
    font-weight: 800;
    color: #2DE2E6;
    text-align: center;
    margin-bottom: 10px;
}

.logo-box {
    text-align: center;
    margin-bottom: 25px;
}

.menu-btn {
    background: #142136;
    padding: 12px;
    width: 100%;
    border-radius: 10px;
    color: #E5E5E5;
    border: 1px solid #2DE2E6;
    margin-bottom: 12px;
    transition: 0.25s;
    font-size: 17px;
}

.menu-btn:hover {
    background: #2DE2E6;
    color: black;
    transform: translateX(5px);
}

.footer {
    text-align:center;
    margin-top: 40px;
    font-size: 14px;
    color: #aaa;
}

</style>
""", unsafe_allow_html=True)


# ----------- SIDEBAR CONTENT -----------
with st.sidebar:

    st.markdown("<div class='sidebar-title'>⚡ EV Range Predictor</div>", unsafe_allow_html=True)

    st.markdown("<div class='logo-box'>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚗  Prediction Page", key="p1", help="Open EV Prediction", use_container_width=True):
      st.switch_page("final_project/pages/1_prediction.py")


    if st.button("ℹ️  About Project", key="p2", help="Learn about EV", use_container_width=True):
      st.switch_page("final_project/pages/2_about.py")


    st.markdown("<div class='footer'>Created by Sonali Jha 💙</div>", unsafe_allow_html=True)


# -------- PAGE BODY (ANIMATED BOX) --------
st.markdown("""
<div class='center-box'>
    <div class='glow-text'>Welcome!, To the EV Range App</div>
    <div class='sub-text'>Choose an option from the left panel</div>
</div>
""", unsafe_allow_html=True)





