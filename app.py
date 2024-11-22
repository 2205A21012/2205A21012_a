import streamlit as st

def Gen_Efficiency(V, CL, K, IL, Rsh, Ra):
    Ish = V / Rsh
    Ia = K * IL - Ish
    CUL = Ish**2 * Rsh + Ia**2 * Ra
    Eff = ((K * V * IL - CL - CUL) * 100) / (K * V * IL)
    return CUL, Eff

st.title("2205A21012-PS12")
st.write("Calculate the Efficiency of DC Shunt Motor at Various Load")

# Create two columns for input and output
col1, col2 = st.columns(2)

# Input section in the first column
with col1:
    st.header("Input Parameters")
    V = st.number_input("V: Voltage (in Volts)", value=230.0)
    IL = st.number_input("IL: Load Current (in Amps)", value=10.0)
    Rsh = st.number_input("Rsh: Shunt Resistance (in Ohms)", value=200.0)
    Ra = st.number_input("Ra: Armature Resistance (in Ohms)", value=0.1)
    CL = st.number_input("CL: Core Loss (in kW)", value=100.0) * 1000  # Convert to watts
    K = st.number_input("K: Load Constant", value=1.0)
    compute = st.button("Compute")  # Trigger calculation

# Output section in the second column
with col2:
    st.header("Results")
    if compute:
        CUL, Eff = Gen_Efficiency(V, CL, K, IL, Rsh, Ra)
        st.write(f"Copper Losses = {CUL:.2f} W")
        st.write(f"Efficiency = {Eff:.2f} %")
    else:
        st.write("Click 'Compute' to calculate the results.")
