import streamlit as st
import pandas as pd
import time

# ------------------------------
# App Config
# ------------------------------
st.set_page_config(page_title="Crypto Tycoon 💰", layout="wide")
st.title("Crypto Tycoon 💎 XRP Edition")
st.subheader("Click, earn, upgrade, and grow your crypto empire!")

# ------------------------------
# Load / Initialize Data
# ------------------------------
try:
    data = pd.read_csv("crypto_tycoon.csv")
except:
    data = pd.DataFrame([{
        "Balance": 0,
        "Click Power": 1,
        "Miners": 0,
        "Traders": 0,
        "Banks": 0,
        "Income/sec": 0
    }])

# ------------------------------
# Helper Functions
# ------------------------------
def save_data():
    data.to_csv("crypto_tycoon.csv", index=False)

def update_income():
    data.at[0, "Income/sec"] = data.at[0, "Miners"]*1 + data.at[0, "Traders"]*5 + data.at[0, "Banks"]*20

def earn_click():
    data.at[0, "Balance"] += data.at[0, "Click Power"]
    save_data()

def buy_upgrade(upgrade):
    cost = 0
    if upgrade == "Miner":
        cost = 50 + data.at[0, "Miners"]*25
        if data.at[0, "Balance"] >= cost:
            data.at[0, "Balance"] -= cost
            data.at[0, "Miners"] += 1
    elif upgrade == "Trader":
        cost = 200 + data.at[0, "Traders"]*100
        if data.at[0, "Balance"] >= cost:
            data.at[0, "Balance"] -= cost
            data.at[0, "Traders"] += 1
    elif upgrade == "Bank":
        cost = 1000 + data.at[0, "Banks"]*500
        if data.at[0, "Balance"] >= cost:
            data.at[0, "Balance"] -= cost
            data.at[0, "Banks"] += 1
    update_income()
    save_data()

def earn_passive():
    data.at[0, "Balance"] += data.at[0, "Income/sec"]
    save_data()

# ------------------------------
# Main Game Loop
# ------------------------------
st.metric("Your Balance 💰", f"{data.at[0, 'Balance']} XRP")
st.metric("Income/sec ⚡", f"{data.at[0, 'Income/sec']} XRP")

if st.button("💎 Mine XRP!"):
    earn_click()
    st.experimental_rerun()

st.subheader("Upgrades 🛠️")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"Miner ({data.at[0,'Miners']}) - Cost: {50 + data.at[0,'Miners']*25}")
    if st.button("Buy Miner"):
        buy_upgrade("Miner")
        st.experimental_rerun()
with col2:
    st.write(f"Trader ({data.at[0,'Traders']}) - Cost: {200 + data.at[0,'Traders']*100}")
    if st.button("Buy Trader"):
        buy_upgrade("Trader")
        st.experimental_rerun()
with col3:
    st.write(f"Bank ({data.at[0,'Banks']}) - Cost: {1000 + data.at[0,'Banks']*500}")
    if st.button("Buy Bank"):
        buy_upgrade("Bank")
        st.experimental_rerun()

# ------------------------------
# Passive Income Timer
# ------------------------------
update_income()
st.subheader("Passive Income 💸")
st.write("Earned automatically based on your upgrades!")

if st.button("Collect Passive Income"):
    earn_passive()
    st.experimental_rerun()

# ------------------------------
# Achievements
# ------------------------------
st.subheader("Achievements 🏆")
achievements = []
if data.at[0,"Balance"] >= 100: achievements.append("100 XRP 💰")
if data.at[0,"Balance"] >= 500: achievements.append("500 XRP 💎")
if data.at[0,"Balance"] >= 1000: achievements.append("1k XRP 🏅")
if data.at[0,"Miners"] >= 5: achievements.append("5 Miners 🚀")
if data.at[0,"Traders"] >= 3: achievements.append("3 Traders 📈")
if data.at[0,"Banks"] >= 2: achievements.append("2 Banks 🏦")

if achievements:
    for a in achievements:
        st.success(a)
else:
    st.write("No achievements yet. Keep clicking!")

# ------------------------------
# Save data
# ------------------------------
save_data()