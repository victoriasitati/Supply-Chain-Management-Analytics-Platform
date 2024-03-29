import streamlit as st
import pandas as pd
import numpy as np

# Generate random sample data for the supply chain
np.random.seed(0)

products = ['Bananas', 'Tomatoes', 'Potatoes', 'Apples']
source_locations = np.random.choice(['Farm A', 'Farm B', 'Farm C', 'Farm D'], size=len(products))
transportation_routes = np.random.choice(['Truck', 'Train', 'Ship', 'Airplane'], size=len(products))
storage_facilities = np.random.choice(['Warehouse 1', 'Warehouse 2', 'Warehouse 3', 'Warehouse 4'], size=len(products))
quality_assurance = np.random.choice(['Passed', 'Failed'], size=len(products))

supply_chain_data = {
    'Product': products,
    'Source Location': source_locations,
    'Transportation Route': transportation_routes,
    'Storage Facility': storage_facilities,
    'Quality Assurance': quality_assurance
}

df = pd.DataFrame(supply_chain_data)

# Streamlit app
st.set_page_config(page_title="The Foods Supply Chain Transparency Dashboard", page_icon=":chart_with_upwards_trend:")

# Add title with image
st.image("chicken farm-cuate.png", width=600)
st.title('Supply Chain Transparency Dashboard')

# Sidebar for filtering options
st.sidebar.title("Filter Options")
selected_product = st.sidebar.selectbox('Select Product', df['Product'].unique())

# Filter data based on selected product
filtered_df = df[df['Product'] == selected_product]

# Display filtered data
st.subheader(f"Selected Product: {selected_product}")
st.dataframe(filtered_df)

# Add color to the dataframe
def highlight_quality(value):
    if value == 'Failed':
        color = 'red'
    else:
        color = 'green'
    return f'color: {color}'

st.markdown("---")
st.subheader("Filtered Data with Quality Highlighted")
st.dataframe(filtered_df.style.applymap(highlight_quality, subset=['Quality Assurance']))
