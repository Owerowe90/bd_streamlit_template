import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import streamlit as st

# Title and Header
st.title("Input Widgets")
st.header("Pie Chart")

# Define coin toss options
coin = ['heads', 'tails']

# Widget to select between slider and number input
slider_input = st.radio(
    "Select Slider or Number Input",
    ["Slider", "Number Input"])

# Initialize flips variable
flips = 0

# Determine flips based on user input method
if slider_input == "Slider":
    flips = st.slider("Number of tosses", 0, 100, 3)
elif slider_input == "Number Input":
    flips = st.number_input("Number of tosses")

# Button to update chart
ok = st.button("Update Chart")

# Update chart when button is clicked
if ok:
    # Simulate coin tosses
    toss = [random.choice(coin) for _ in range(int(flips))]

    # Count the number of heads and tails
    heads_count = toss.count('heads')
    tails_count = flips - heads_count

    # Create a pie chart
    labels = ['Heads', 'Tails']
    sizes = [heads_count, tails_count]
    colors = ['blue', 'orange']
    explode = (0.1, 0)  # explode the 1st slice (Heads)
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', startangle=140)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Display the pie chart using Streamlit
    st.pyplot(fig)

    # Display the counts of heads and tails
    st.write(f"Heads: {heads_count}")
    st.write(f"Tails: {tails_count}")

# Header for Line Graph
st.header("Line Graph")

# Generate random data for the DataFrame
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

# Create a select box with options "All", 'A', "B", "C"
selected_data = st.selectbox("Line Graph", ["All", 'A', "B", "C"])

# Filter data based on user selection
if selected_data == 'All':
    data_to_display = chart_data
else:
    data_to_display = chart_data[selected_data]

# Display line chart
st.line_chart(data_to_display)
