import streamlit as st
import datetime

st.set_page_config(page_title="Ma Mission ✨", page_icon="🎀")

st.markdown("""
    <style>
    .main { background-color: #FFF0F5; }
    h1 { color: #FF69B4; text-align: center; margin-bottom: 20px; }
    .tableau {
        background-color: #1E3F35; 
        color: white;
        padding: 25px;
        border: 8px solid #8B4513; 
        border-radius: 15px;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 1.3rem;
        box-shadow: 5px 5px 10px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }
    .stCheckbox { font-size: 20px; padding: 10px; background: white; border-radius: 10px; margin-bottom: 10px; border: 1px solid #FFB6C1; }
    </style>
    """, unsafe_allow_html=True)

messages = [
    "Une nouvelle semaine pleine de joie ! 🌸",
    "Tu es ma plus belle réussite. ✨",
    "Petit à petit, tu deviens incroyable. 🎀",
    "Ton sourire illumine ma vie. ☀️",
    "Presque le week-end ! Courage ! 💪",
    "Profite bien de ta journée, l'artiste ! 🎨",
    "Je suis tellement fière de toi. 💕"
]

today_idx = datetime.datetime.now().weekday()

st.markdown("<h1>Bonjour, ma princesse ! ✨</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='message'>{messages[today_idx]}</p>", unsafe_allow_html=True)

st.divider()

st.subheader("🌸 Mes missions d'aujourd'hui")

col1, col2 = st.columns(2)
with col1:
    q1 = st.checkbox("📚 10 min de Coréen")
    q2 = st.checkbox("🐹 S'occuper des chons")
    q3 = st.checkbox("🎨 Ranger 5 objets")
with col2:
    q4 = st.checkbox("🛏️ Faire mon lit")
    q5 = st.checkbox("🎀 Préparer mes habits")
    q6 = st.checkbox("🎁 Bonus-Aider Maman")

points = (q1*10) + (q2*2) + (q3*2) + (q4*2) + (q5*2) + (q6*2)

st.divider()
st.write(f"### 💖 Score total : {points} / 30")

if points >= 24:
    st.balloons()
    st.success(f"Bravo ! Tu as gagné {points} minutes d'écran ! 🎀")
elif points > 0:
    st.info("Encore un petit effort ! 💕")

mon_tel = "33749472959" 
msg = f"Maman ! J'ai fini mes missions et j'ai gagne {points} minutes d'ecran !"
whatsapp_url = f"https://wa.me/{mon_tel}?text={msg.replace(' ', '%20')}"

if st.button("📤 Envoyer mon rapport à Maman"):
    st.markdown(f"### [👉 CLIQUE ICI POUR ENVOYER 💌]({whatsapp_url})")
