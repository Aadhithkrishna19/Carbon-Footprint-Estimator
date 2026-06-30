"""
Carbon Footprint Estimator - Logic Module

This module contains:
1. Dictionaries of emission factors and suggestions.
2. Functions to validate inputs and calculate carbon emissions.
3. Functions to suggest carbon reduction tips.
"""

# Dictionary mapping transport types to their carbon emission factors (in kg of CO2 per kilometer)
# Data source: Average estimates for transport emissions (e.g., Defra / greenhouse gas reporting conversion factors)
EMISSION_FACTORS = {
    "Petrol Car": 0.18,      # Average petrol car: 180g CO2/km
    "Diesel Car": 0.17,      # Average diesel car: 170g CO2/km
    "Electric Car": 0.05,    # Average EV (considering power grid mix): 50g CO2/km
    "Motorcycle": 0.10,      # Average motorcycle: 100g CO2/km
    "Bus": 0.03,             # Average bus passenger: 30g CO2/km
    "Train": 0.015,          # Average train passenger: 15g CO2/km
    "Flight (Short-haul)": 0.15, # Flight (< 3 hours) passenger: 150g CO2/km
    "Flight (Long-haul)": 0.11   # Flight (> 3 hours) passenger: 110g CO2/km
}

# Dictionary mapping transport types to dynamic reduction tips
REDUCTION_TIPS = {
    "Petrol Car": [
        "Consider carpooling with friends or colleagues to share emissions.",
        "Maintain proper tire pressure to improve fuel efficiency by up to 3%.",
        "Switch to public transport (like trains or buses) for longer commutes.",
        "Consider upgrading to a hybrid or electric vehicle for your next car."
    ],
    "Diesel Car": [
        "Avoid unnecessary idling; turn off the engine when parked or waiting.",
        "Drive smoothly – rapid acceleration and braking waste fuel.",
        "Look into park-and-ride options using public transit to enter city centers.",
        "Consider carpooling or using electric car rentals when available."
    ],
    "Electric Car": [
        "Charge your electric car during off-peak hours or when renewable energy generation is high.",
        "Utilize regenerative braking to feed power back into your battery.",
        "Use eco-mode if your vehicle supports it to maximize range and efficiency.",
        "Walk or cycle for very short trips (under 2 km) for a zero-carbon journey."
    ],
    "Motorcycle": [
        "Keep your motorcycle well-tuned and perform regular oil changes.",
        "Ride at moderate speeds; high-speed riding significantly increases fuel usage.",
        "Wear aerodynamic gear to reduce drag and improve fuel efficiency.",
        "For very short trips, consider walking or riding a bicycle."
    ],
    "Bus": [
        "Using public transport is already a great choice! It emits roughly 80% less than a petrol car per person.",
        "Try combining multiple errands into a single bus trip.",
        "Walk or cycle to the bus stop to add zero-carbon physical activity to your commute.",
        "Encourage local authorities to transition the city fleet to electric or hybrid buses."
    ],
    "Train": [
        "Trains are one of the most eco-friendly transport modes, emitting ~90% less than driving alone!",
        "Support electrified train networks and booking electronic tickets to save paper.",
        "Use public transport or walk to get to/from the train station.",
        "Keep up the great work! Share your green travel habits with others."
    ],
    "Flight (Short-haul)": [
        "Short flights are very carbon-intensive. Consider taking a high-speed train instead for distances under 800 km.",
        "Pack light! Every kilogram of luggage increases the plane's fuel consumption.",
        "Fly economy class – first and business class seats take up more space and carry a higher carbon share.",
        "Consider choosing direct flights to avoid extra takeoffs and landings, which consume the most fuel."
    ],
    "Flight (Long-haul)": [
        "Consider choosing direct routes to minimize fuel consumption from multiple takeoffs and landings.",
        "Pack only what you need – lighter aircraft burn less fuel.",
        "Fly economy class to distribute the flight's emissions among more passengers.",
        "Carbon-offset your flight through verified, gold-standard reforestation or green energy projects."
    ]
}

def calculate_emissions(transport_type: str, distance: float) -> float:
    """
    Calculates carbon emissions in kilograms of CO2.
    
    Parameters:
    - transport_type (str): The mode of transportation (must match a key in EMISSION_FACTORS).
    - distance (float): The distance traveled in kilometers.
    
    Returns:
    - float: Total CO2 emissions in kg.
    """
    # 1. Validation checks
    if transport_type not in EMISSION_FACTORS:
        raise ValueError(f"Unknown transport type: '{transport_type}'. Please choose a valid transport mode.")
        
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a numeric value (int or float).")
        
    if distance < 0:
        raise ValueError("Distance cannot be negative. Please enter a positive value.")
        
    # 2. Calculation
    factor = EMISSION_FACTORS[transport_type]
    emissions = distance * factor
    
    # 3. Round to 2 decimal places for clean display
    return round(emissions, 2)

def get_reduction_tips(transport_type: str) -> list:
    """
    Retrieves tailored reduction tips for a given transport mode.
    
    Parameters:
    - transport_type (str): The mode of transportation.
    
    Returns:
    - list: A list of string tips.
    """
    # Validation check
    if transport_type not in REDUCTION_TIPS:
        return ["Walk or cycle whenever possible.", "Switch to shared or public transport."]
        
    return REDUCTION_TIPS[transport_type]
