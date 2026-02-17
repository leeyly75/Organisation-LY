import streamlit as st
import time

# Configuration style "Lusha" : joyeux et clair
st.set_page_config(page_title="Ma Mission Quotidienne", page_icon="🦊")

st.title("🦊 Ma Mission : En route vers la récompense !")
st.write("Complète tes quêtes pour gagner ton temps de liberté.")

# --- SECTION 1 : LA ROUTINE (Focus TDAH) ---
st.subheader("📋 Mes Quêtes du jour")
col1, col2 = st.columns(2)

with col1:
    q1 = st.checkbox("📚 10 min de Coréen")
    q2 = st.checkbox("🦷 Se brosser les dents et nettoyer l'appareil")
    q3 = st.checkbox("🧸 Ranger 5 objets")

with col2:
    q4 = st.checkbox("🐹 S'occuper des chons")
    q5 = st.checkbox("👗 Préparer ses habits")
    q6 = st.checkbox("🛏️ Faire le lit")

# --- SECTION 2 : LE CALCULATEUR DE RÉCOMPENSE ---
st.divider()
st.subheader("💎 Mon Butin")

# On définit les points (ex: 20 min par quête de coréen, 5 min pour le reste)
points_totaux = 0
if q1: points_totaux += 20
if q2: points_totaux += 5
if q3: points_totaux += 5
if q4: points_totaux += 5
if q5: points_totaux += 5
if q6: points_totaux += 5

st.metric(label="Temps d'écran gagné (minutes)", value=f"{points_totaux} min")

if points_totaux >= 45:
    st.balloons()
    st.success("C'est gagné ! Tu as été super efficace aujourd'hui ! ✨")

# --- SECTION 3 : LE CHRONO (Pour aider à se concentrer) ---
st.divider()
st.subheader("⏱️ Chrono Focus")
duree = st.number_input("Combien de minutes pour ta tâche ?", 1, 30, 10)
if st.button("Démarrer le chrono !"):
    with st.empty():
        for i in range(duree * 60, 0, -1):
            mins, secs = divmod(i, 60)
            st.header(f"⏳ {mins:02d}:{secs:02d}")
            time.sleep(1)
        st.header("✅ Temps fini ! Bravo !")

# --- SECTION 4 : RAPPORT À MAMAN ---
st.divider()
if st.button("📤 Envoyer mon rapport à Maman"):
    st.write(f"Bravo ! Rapport prêt pour Maman Yeonsil : {points_totaux} minutes méritées.")
