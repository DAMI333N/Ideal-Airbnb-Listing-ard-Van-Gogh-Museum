import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Airbnb Listings around Van Gogh Museum")
st.markdown("Here we can see the dataframe created for my project.")

# Read dataframe
dataframe = pd.read_csv(
    "Airbnb Amsterdam Listings_SGD.csv",
    names=[
        "Airbnb Listing ID",
        "Price (SGD)",
        "Latitude",
        "Longitude",
        "Meters from Van Gogh Museum",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above SGD $170 per night
dataframe = dataframe[dataframe["Price"] <= 170]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "$ " + dataframe["Price"].round(2).astype(str)
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and Van Gogh Museum with a blue dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    color_discrete_sequence=["blue", "red"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))

st.plotly_chart(fig, use_container_width=True)
