import math
import streamlit as st

st.title("Futures Pricing Calculator")

S0 = st.number_input("Spot price", value=2000.0)
r = st.number_input("Interest rate (e.g. 0.04 = 4%)", value=0.04)
T = st.number_input("Time to expiry (years)", value=1.0)
u = st.number_input("Storage cost (u)", value=0.01)
q = st.number_input("Dividend / yield (q)", value=0.0)
F_market = st.number_input("Market futures price", value=2130.0)

F_fair = S0 * math.exp((r + u - q) * T)
gap = F_market - F_fair

st.metric("Fair futures price", round(F_fair, 2))
st.metric("Mispricing gap", round(gap, 2))

if gap > 0:
    st.success("Cash-and-carry arbitrage: buy spot, short futures")
elif gap < 0:
    st.warning("Reverse cash-and-carry: short spot, long futures")
else:
    st.info("No arbitrage")
