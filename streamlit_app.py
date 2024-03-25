import json
import streamlit as st
import folium
from streamlit_folium import folium_static


def main():
    st.title("MAP MANTEP")

    # Sidebar input for destinations
    destinations_input = st.text_area("Enter Destination Locations (Latitude, Longitude):", """[
  {
    "latitude": "-6.285289935884475",
    "longtitude": "106.79558514676206",
    "desc": "test 1 description, <br/> bebas terserah ini popup"
  },
  {
    "latitude" : "-6.263448244919199",
    "longtitude" : "106.88484554808909",
    "desc": "test 2 description, <br/> bebas terserah ini popup"
  },
  {
    "latitude" : "-6.402623005332708",
    "longtitude" : "106.79766989414128",
    "desc": "test 3 description, <br/> bebas terserah ini popup"
  }
]""")

    # Convert input to list of coordinates
    destinations = []
    try:
      for i in json.loads(destinations_input.strip()):
          lat = float(i['latitude'])
          lon = float(i['longtitude'])
          desc = i['desc']
          destinations.append({
            "lat" : lat,
            "lon" : lon,
            "desc" : desc,
          })
    except:
        st.error("Please enter valid JSON ")
        return

    # Create map object 
    my_map = folium.Map(location=[destinations[0]['lat'], destinations[0]['lon']])

    # Add numbered markers for destinations
    for i, v in enumerate(destinations):
        folium.Marker(
            location=[v['lat'], v['lon']],
            popup=folium.Popup(v['desc'],min_width=300, max_width=300),
            # icon=folium.DivIcon(html=f"<div style='font-size: 12; color: red, ;'>{i+1}</div>")
            icon=folium.DivIcon(
        icon_size=(150,36),
        icon_anchor=(7,20),
        html=f"""<div style='background-color: red; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; justify-content: center; align-items: center;'>{i+1}</div>""",
        )
        ).add_to(my_map)

    # Add route line connecting all destinations
    folium.PolyLine(
        locations=[ (i['lat'], i['lon']) for i in destinations],
        color='blue',
        weight=3,
        popup="Route"
    ).add_to(my_map)

    # Display map
    folium_static(my_map)

if __name__ == "__main__":
    main()
