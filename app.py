import streamlit as st


def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    
    Ish = V / Rsh
    
    
    Ia = K * IL - Ish
    
    
    CUL = Ish**2 * Rsh + Ia**2 * Ra
    
    
    Eff = ((K * V * IL - CL - CUL) / (K * V * IL)) * 100
    
    return Eff, CUL


st.title("Calculate the efficiency and Copper losses-2205A21012")


st.header("Input Parameters")
V = st.number_input("Vin Volt", min_value=1.0, step=0.1, value=220.0)
IL = st.number_input("IL:in Amps", min_value=0.1, step=0.1, value=10.0)
Rsh = st.number_input("Rsh:Ohms", min_value=0.1, step=0.1, value=220.0)
Ra = st.number_input("Ra:Ohms", min_value=0.1, step=0.1, value=0.5)
CL = st.number_input("CL:Watts", min_value=0.0, step=0.1, value=500.0)

K = st.number_input("Loading on Generator (K)", min_value=0.1, step=0.1, value=1.0)




if st.button("Calculate Efficiency and Copper Losses"):
    Eff, CUL = Gen_Eff(V, CL, IL, K, Rsh, Ra)
    
    
    with st.container():
        st.header("Results")
        st.metric(label="Efficiency (%)", value=f"{Eff:.2f}")
        st.metric(label="Copper Losses (W)", value=f"{CUL:.2f}")
        
        with st.expander("Details of Calculation"):
            st.write(f"Shunt Field Current (Ish): {V / Rsh:.2f} A")
            st.write(f"Armature Current (Ia): {K * IL - V / Rsh:.2f} A")
            st.write(f"Copper Losses (CUL): {CUL:.2f} W")
            st.write(f"Efficiency (Eff): {Eff:.2f}%")