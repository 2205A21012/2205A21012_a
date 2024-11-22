import streamlit as st

def Gen_Efficiency(V,CL,K,IL,Rsh,Ra):
    Ish=V/Rsh
    Ia=K*IL-Ish
    CUL = Ish*2*Rsh+Ia*2*Ra
    Eff = (K*V*IL-CL-CUL)/(K*V*IL)*100
    return CUL,Eff


st.title("2205A21012-PS12")
st.write("Calculate the Efficency of DC shunt motor at Various Load")




col1, col2 = st.columns(2)
with col1:
 with st.container(border=True):
    V = st.number_input("V:in Volts)", value=230)
    IL =st.number_input("IL:in Amps", value=10.00)
    Rse=st.number_input("Rsh:Ohms", value=200.00)
    Ra= st.number_input("Ra:Ohms", value=0.10)
    CL= st.number_input("CL:kW", value=100)
    K=  st.number_input("K:Load constant",value=1)
    st.button("Compute")
           
            


with col2:
 with st.container(border=True):
    CUL,Eff = Gen_Efficiency(V,CL,IL,K,Rse,Ra)
    st.write(f"Copper losses = {CUL} W")
    st.write(f"Efficiency = {Eff} %")