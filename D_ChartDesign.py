import pandas as pd
import streamlit as st
import plotly.express as px


  
def design_chart1(User_TI, Comp1_TI, Comp2_TI):
    base_values = [User_TI, Comp1_TI, Comp2_TI]
    
    chart_image = 'Base_image'

    row_choice_user = 1
    row_choice_comp1 = 1
    row_choice_comp2 = 1

    if User_TI <= 2:
        row_choice_user = 1
    
    elif User_TI >2 and User_TI <=7:
        row_choice_user = 2

    else:
        row_choice_user = 3

    
    if Comp1_TI <= 2:
        row_choice_comp1 = 3
    
    elif Comp1_TI >2 and Comp1_TI <=7:
        row_choice_comp1 = 2

    else:
        row_choice_comp1 = 1

    
    if Comp2_TI <= 2:
        row_choice_comp2 = 3
    
    elif Comp2_TI > 2 and Comp2_TI <=7:
        row_choice_comp2 = 2

    else:
        row_choice_comp2 = 1


    if max(base_values) == 0:
        chart_image = 'Pictures/Base_image.png'
    
    elif row_choice_comp1 == row_choice_comp2:
        chart_image = 'Pictures/Chart_image_' + str(row_choice_comp1)  + '.'  + str(row_choice_user) + '.png'

    else:
        multiple_image_rows = [row_choice_comp1, row_choice_comp2]
        chart_image = 'Pictures/Chart_image_' + str(sorted(multiple_image_rows)[0]) + '.' + str(sorted(multiple_image_rows)[1]) + '.' + str(row_choice_user) + '.png' 

    
    st.image(chart_image, use_container_width=False)

    if row_choice_comp1 != row_choice_comp2 and row_choice_comp1 in [1, 3] and row_choice_comp2 in [1, 3]:
        st.write('')
        st.write("##### **In this eventuality a more detailed assessment is required to understand available actions. The Simon-Kucher team is happy to setup a complimentary food-for-thought session to discuss such items in more depth.**")

def design_chart2(data):
    
    df = pd.DataFrame(data)
    # Plotly bubble chart
    fig = px.scatter(
        df,
        x="COGS",
        y="Tariff Impact",
        size="Market Share",
        color="Manufacturer",  # Optional
        hover_name="Manufacturer",
        size_max=60,
    )

    fig.update_layout(
        width=800,  # Fixed width
        height=600,  # Optional: adjust height too
        xaxis=dict(tickformat=".0%", title="COGS (%)"),
        yaxis=dict(tickformat=".0%", title="Tariff Impact (%)")
    )

    # Streamlit display
    st.plotly_chart(fig, use_container_width=True)

