import streamlit as st
import carbon_calculator as cc

# Set up page configurations (SEO & Metadata)
st.set_page_config(
    page_title="Carbon Footprint Estimator | EcoTravel",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for rich aesthetics and modern user experience (glassmorphism theme)
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

/* Apply modern font and background gradient */
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(135deg, #0c1c16 0%, #0d2218 50%, #153823 100%) !important;
    color: #f0f2f6 !important;
}

/* Title text styling with green gradient */
.main-title {
    background: linear-gradient(90deg, #56ab2f 0%, #a8e063 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    font-size: 2.8rem;
    text-align: center;
    margin-bottom: 0.2rem;
    padding-top: 1rem;
}

.sub-title {
    color: #a0aec0;
    text-align: center;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Custom card container styling with glassmorphism */
.custom-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 1.8rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.custom-card:hover {
    transform: translateY(-3px);
    border-color: rgba(168, 224, 99, 0.3);
}

.metric-title {
    font-size: 1.1rem;
    color: #a0aec0;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    font-size: 3.5rem;
    font-weight: 700;
    color: #a8e063;
    margin: 0.5rem 0;
}

.metric-unit {
    font-size: 1.2rem;
    color: #a0aec0;
    font-weight: 400;
}

/* Equivalents section grid */
.eq-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-top: 1rem;
}

.eq-card {
    background: rgba(255, 255, 255, 0.015);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: background 0.3s;
}

.eq-card:hover {
    background: rgba(255, 255, 255, 0.04);
}

.eq-val {
    font-size: 1.8rem;
    font-weight: 700;
    color: #a8e063;
}

.eq-label {
    font-size: 0.85rem;
    color: #a0aec0;
    margin-top: 5px;
}

/* Reduction tip row styling */
.tip-row {
    background: rgba(168, 224, 99, 0.05);
    border-left: 4px solid #a8e063;
    padding: 12px 16px;
    border-radius: 6px;
    margin-bottom: 12px;
    font-size: 0.95rem;
}

.formula-card {
    background: rgba(255, 255, 255, 0.01);
    border-radius: 8px;
    padding: 10px 15px;
    border: 1px dashed rgba(255, 255, 255, 0.1);
    font-family: monospace;
    color: #e2e8f0;
}
</style>
"""

# Inject custom styling
st.markdown(custom_css, unsafe_allow_html=True)

# Main Title and Subtitle
st.markdown('<div class="main-title">🌱 Carbon Footprint Estimator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Estimate, understand, and reduce your travel carbon emissions.</div>', unsafe_allow_html=True)

# Main Application Layout: Input Card
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.subheader("🎒 Travel Details")

# Input 1: Transport Mode selection
transport_options = list(cc.EMISSION_FACTORS.keys())
selected_transport = st.selectbox(
    "Choose your mode of transport:",
    options=transport_options,
    help="Select the vehicle or transit system you used for the journey."
)

# Input 2: Distance input
distance_input = st.number_input(
    "Enter the travel distance (in kilometers):",
    min_value=-500.0,  # Negative allowed here so we can demonstrate validation
    max_value=20000.0,
    value=10.0,
    step=1.0,
    help="Type in the distance you traveled."
)

st.markdown('</div>', unsafe_allow_html=True)

# Logic execution & validation handling
validation_passed = True
emissions = 0.0

# 1. Validation Check:
if distance_input < 0:
    st.error("⚠️ Validation Error: Distance cannot be negative. Please enter a positive number of kilometers.")
    validation_passed = False
elif distance_input == 0:
    st.warning("ℹ️ Validation Tip: Distance is zero. Enter a distance to calculate emissions.")
    validation_passed = False

if validation_passed:
    try:
        # 2. Calculation (Calling logic function)
        emissions = cc.calculate_emissions(selected_transport, distance_input)
    except ValueError as e:
        st.error(f"Error: {e}")
        validation_passed = False

if validation_passed:
    # 3. Calculation & Display Results Card
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">Estimated Carbon Footprint</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{emissions} <span class="metric-unit">kg CO₂</span></div>', unsafe_allow_html=True)
    
    # 4. Show the math/calculation explanation
    factor = cc.EMISSION_FACTORS[selected_transport]
    st.markdown(
        f'<div class="formula-card">Calculation: {distance_input} km × {factor} kg CO₂/km = {emissions} kg CO₂</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 5. Equivalents Section (Real-world comparison)
    # Reforestation: 1 tree absorbs ~22kg of CO2 per year.
    # Phone charging: 1 smartphone charge generates ~0.005 kg CO2.
    # Plastic bags: Production of 1 plastic bag generates ~0.033 kg CO2.
    trees_needed = round(emissions / 22.0, 2)
    phone_charges = round(emissions / 0.005)
    plastic_bags = round(emissions / 0.033)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("⚖️ Real-World Impact")
    st.write("To put this emission amount into perspective, it is equivalent to:")
    
    st.markdown(f"""
    <div class="eq-grid">
        <div class="eq-card">
            <div class="eq-val">🌲 {trees_needed}</div>
            <div class="eq-label">Trees' annual CO₂ absorption needed</div>
        </div>
        <div class="eq-card">
            <div class="eq-val">🔌 {phone_charges:,}</div>
            <div class="eq-label">Smartphone charges</div>
        </div>
        <div class="eq-card">
            <div class="eq-val">🛍️ {plastic_bags:,}</div>
            <div class="eq-label">Plastic bags manufactured</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 6. Suggest Reduction Tips Card
    tips = cc.get_reduction_tips(selected_transport)
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("💡 Dynamic Eco-Tips")
    st.write(f"Here are ways you can lower your carbon footprint for **{selected_transport}** travel:")
    
    for tip in tips:
        st.markdown(f'<div class="tip-row">🌿 {tip}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with general info & references
with st.sidebar:
    st.title("🌱 About the App")
    st.write("""
    This app is a simple, end-to-end Python tool built using Streamlit.
    It teaches how **Functions, Dictionaries, Calculations, and Validation** 
    work together in a clean, professional web application.
    """)
    st.write("---")
    st.subheader("📊 Carbon Emission Factors Used:")
    for mode, value in cc.EMISSION_FACTORS.items():
        st.markdown(f"- **{mode}**: `{value}` kg CO₂/km")
    
    st.write("---")
    st.markdown("Developed with ❤️ for green commuting.")
