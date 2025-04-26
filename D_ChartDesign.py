import pandas as pd
import streamlit as st
import plotly.express as px


def generate_metric1(title, width="300px", bgcolor="#DFE2E7"):
    # Determine delta color based on the delta value
    return f"""
    <div style="
        background-color: {bgcolor};
        padding: 20px;
        border-radius: 8px;
        width: {width};
        height: 100px;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    ">
        <div style="font-size: 18px; color: #555;">{title}</div>
    </div>
    """

def generate_metric2(title, width="300px", bgcolor="#30AE12"):
    # Determine delta color based on the delta value
    return f"""
    <div style="
        background-color: {bgcolor};
        padding: 20px;
        border-radius: 8px;
        width: {width};
        height: 100px;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    ">
        <div style="font-size: 18px; color: #555;">{title}</div>
    </div>
    """

def design_chart1():
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.markdown(generate_metric1('Pass-through costs and capture margin'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric1('Pass-through costs and capture margin'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric1('Maintain price'), unsafe_allow_html=True)


    with col2:
        st.markdown(generate_metric1('Pass-through costs and capture margin'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric1('Full pass-through'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric1('Strategic partial pass-through'), unsafe_allow_html=True)

    with col3:
        st.markdown(generate_metric1('Full pass-through'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric2('Strategic partial pass-through'), unsafe_allow_html=True)
        st.write('')
        st.markdown(generate_metric1('Explore alternatives'), unsafe_allow_html=True)
  
def design_chart2():
    st.write('')
    st.image("Pictures/Chart_image_2.3.png", width = 1000)

def design_chart3():
    data = {
    "Product": ["XIENCE", "Resolute", "Biomatrix", "Eluvia"],
    "COGS": [.3, .15, .43, .39],
    "Tariff_Impact": [.05, .03, .13, .22],
    "Market_Share": [30, 50, 20, 40],
    "Manufacturer": ["Abbott", "Medtronic", "Biosensors", "Boston Scientific"]
    }

    df = pd.DataFrame(data)

    # Plotly bubble chart
    fig = px.scatter(
        df,
        x="COGS",
        y="Tariff_Impact",
        size="Market_Share",
        color="Manufacturer",  # Optional
        hover_name="Product",
        size_max=60,
        title="Bubble Chart: COGS vs Tariff Impact"
    )

    fig.update_layout(
        width=800,  # Fixed width
        height=600,  # Optional: adjust height too
        xaxis=dict(range=[0, 0.8], tickformat=".0%", title="COGS (%)"),
        yaxis=dict(range=[0, 0.3], tickformat=".0%", title="Tariff Impact (%)")
    )

    # Streamlit display
    st.plotly_chart(fig, use_container_width=True)

