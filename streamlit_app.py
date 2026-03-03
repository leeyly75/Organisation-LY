import streamlit as st
import datetime

1. 페이지 설정
st.set_page_config(page_title="Ma Mission ✨", page_icon="🎀")

2. 핑크색 스타일 적용
st.markdown("""
<style>
.main { background-color: #FFF0F5; }
h1 { color: #FF69B4; text-align: center; margin-bottom: 0; }
.message { text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 20px; font-style: italic; }
.stCheckbox { font-size: 20px; padding: 10px; background: white; border-radius: 10px; margin-bottom: 10px; border: 1px solid #FFB6C1; }
</style>
""", unsafe_allow_html=True)

3. 요일별 자동 메시지 설정
messages = [
"Une nouvelle semaine pleine de joie ! 🌸",       # 월
"Tu es ma plus belle réussite. ✨",               # 화
"Petit à petit, tu deviens incroyable. 🎀",       # 수
"Ton sourire illumine ma vie. ☀️",                # 목
"Presque le week-end ! Courage ! 💪",             # 금
"Profite bien de ta journée, l'artiste ! 🎨",     # 토
"Je suis tellement fière de toi. 💕"              # 일
]

오늘 요일 가져오기 (0=월요일, 6=일요일)
today_idx = datetime.datetime.now().weekday()

4. 메인 타이틀 & 자동 메시지 출력
st.markdown("<h1>Bonjour, ma princesse ! ✨</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='message'>{messages[today_idx]}</p>", unsafe_allow_html=True)

st.divider()

5. 미션 리스트
st.subheader("🌸 Mes missions d'aujourd'hui")

col1, col2 = st.columns(2)
with col1:
q1 = st.checkbox("📚 10 min de Coréen")
q2 = st.checkbox("🦷 Dents et appareil")
q3 = st.checkbox("🛏️ Faire mon lit")
with col2:
q4 = st.checkbox("🐹 S'occuper des chons")
q5 = st.checkbox("👗 Préparer mes habits")
q6 = st.checkbox("🎁 Bonus Aider Maman")

6. 점수 계산
points = (q110) + (q25) + (q35) + (q410) + (q55) + (q65)

st.divider()
st.write(f"### 💖 Score total : {points} / 40")

7. 성공 이벤트
if points >= 30:
st.balloons()
st.success(f"Bravo ! Tu as gagné {points} minutes d'écran ! 🎀")
elif points > 0:
st.info("Encore un petit effort ! 💕")

8. 엄마에게 보고하기
mon_tel = "33749472959"
msg = f"Maman ! J'ai fini mes missions et j'ai gagne {points} minutes d'ecran !"
whatsapp_url = f"https://wa.me/{mon_tel}?text={msg.replace(' ', '%20')}"

if st.button("📤 Envoyer mon rapport à Maman"):
st.markdown(f"### ")
