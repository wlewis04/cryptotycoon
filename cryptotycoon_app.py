mport streamlit as st

# ------------------------------
# Config
# ------------------------------
st.set_page_config(page_title="Crypto Tycoon 💰", layout="wide")
st.title("Crypto Tycoon 💎 XRP Edition")
st.subheader("Click, earn, upgrade, and grow your crypto empire!")

# ------------------------------
# Initialize Game State
# ------------------------------
if "tycoon" not in st.session_state:
    st.session_state.tycoon = {
        "Balance": 0,
        "Click Power": 1,
        "Miners": 0,
        "Traders": 0,
        "Banks": 0,
        "IncomePerSec": 0
    }

tycoon = st.session_state.tycoon

# ------------------------------
# Helper Functions
# ------------------------------
def update_income():
    tycoon["IncomePerSec"] = tycoon["Miners"]*1 + tycoon["Traders"]*5 + tycoon["Banks"]*20

def earn_click():
    tycoon["Balance"] += tycoon["Click Power"]

def buy_upgrade(upgrade):
    if upgrade == "Miner":
        cost = 50 + tycoon["Miners"]*25
        if tycoon["Balance"] >= cost:
            tycoon["Balance"] -= cost
            tycoon["Miners"] += 1
    elif upgrade == "Trader":
        cost = 200 + tycoon["Traders"]*100
        if tycoon["Balance"] >= cost:
            tycoon["Balance"] -= cost
            tycoon["Traders"] += 1
    elif upgrade == "Bank":
        cost = 1000 + tycoon["Banks"]*500
        if tycoon["Balance"] >= cost:
            tycoon["Balance"] -= cost
            tycoon["Banks"] += 1
    update_income()

def earn_passive():
    tycoon["Balance"] += tycoon["IncomePerSec"]

# ------------------------------
# Main UI
# ------------------------------
update_income()
st.metric("Your Balance 💰", f"{tycoon['Balance']} XRP")
st.metric("Income/sec ⚡", f"{tycoon['IncomePerSec']} XRP")

if st.button("💎 Mine XRP!"):
    earn_click()

st.subheader("Upgrades 🛠️")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"Miner ({tycoon['Miners']}) - Cost: {50 + tycoon['Miners']*25}")
    if st.button("Buy Miner", key="miner"):
        buy_upgrade("Miner")
with col2:
    st.write(f"Trader ({tycoon['Traders']}) - Cost: {200 + tycoon['Traders']*100}")
    if st.button("Buy Trader", key="trader"):
        buy_upgrade("Trader")
with col3:
    st.write(f"Bank ({tycoon['Banks']}) - Cost: {1000 + tycoon['Banks']*500}")
    if st.button("Buy Bank", key="bank"):
        buy_upgrade("Bank")

st.subheader("Passive Income 💸")
st.write("Click below to collect income from your upgrades!")
if st.button("Collect Passive Income"):
    earn_passive()

# ------------------------------
# Achievements
# ------------------------------
st.subheader("Achievements 🏆")
achievements = []
if tycoon["Balance"] >= 100: achievements.append("100 XRP 💰")
if tycoon["Balance"] >= 500: achievements.append("500 XRP 💎")
if tycoon["Balance"] >= 1000: achievements.append("1k XRP 🏅")
if tycoon["Miners"] >= 5: achievements.append("5 Miners 🚀")
if tycoon["Traders"] >= 3: achievements.append("3 Traders 📈")
if tycoon["Banks"] >= 2: achievements.append("2 Banks 🏦")

for a in achievements:
    st.success(a)

# ------------------------------
# Optional Premium / Stripe
# ------------------------------
st.sidebar.header("Upgrade to Premium 🚀")
st.sidebar.write("Unlock multipliers and exclusive upgrades!")
if st.sidebar.button("Upgrade via Stripe"):
    st.sidebar.markdown("[Click here to pay via Stripe](YOUR_STRIPE_CHECKOUT_LINK)")

st.sidebar.subheader("Tip 💡")
st.sidebar.info("Click often, upgrade wisely, and watch your empire grow! 🚀")