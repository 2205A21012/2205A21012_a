import streamlit as st

st.title("2205A21012-PS12")
st.write("calculate the efficiecncy OF dc shunt motors at various loads.")

def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    Ish = V / Rsh
    Ia = K * IL - Ish
    CUL = Ish**2 * Rsh + Ia**2 * Ra
    Eff = (K * V * IL - CL - CUL) / (K * V * IL) * 100
    return Eff, CUL

#

# Input fields
col1,col2=st.columns(2)
with col1:
    V = st.number_input("Voltage (V)", value=230)
    CL = st.number_input("Core Losses (CL) in watts", value=100)
    IL = st.number_input("Full Load Current (IL) in Amps",value=10)
    K = st.number_input("Loading on Generator (K)", value=1)
    Rsh = st.number_input("Shunt Field Resistance (Rsh)", value=200)
    Ra = st.number_input("Armature Resistance (Ra)",value=0.10)
    a=st.button("compute")
                         

with col2:
    if a:
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rsh, Ra)
        st.write(f"Efficiency: {Eff:.2f}%")
        st.write(f"Copper Losses: {CUL:.2f} W")

