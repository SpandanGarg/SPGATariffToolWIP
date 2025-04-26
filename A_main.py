import pandas as pd
import streamlit as st
from B_HomePage import home_page
from C_Assessment import assessment
from Z_ProductA import product_A
from Z_ProductB import product_B
from Z_ProductC import product_C

st.set_page_config(
    page_title = 'Simon-Kucher Tariff Assessment',
    layout = 'wide'
)

if 'page_navigator' not in st.session_state:
    st.session_state.page_navigator = 'home_page'

if 'show_navigational_sidebar' not in st.session_state:
    st.session_state.show_navigational_sidebar = False



for a in range(4):
    page_keys = ['Assessment_Landing_Page', 'Page_Product_Category_A', 'Page_Product_Category_B', 'Page_Product_Category_C']
    interim_page_names = ['Product Inputs', 'Product Category A', 'Product Category B', 'Product Category C'] 
    if page_keys[a] not in st.session_state:
        st.session_state[page_keys[a]] = interim_page_names[a] 

def main():
    current_page = st.session_state.page_navigator

    if st.session_state.show_navigational_sidebar and current_page != 'home_page':
        st.sidebar.title("Assessment Navigator")
        sidebar_options = [
            st.session_state.Assessment_Landing_Page,
            st.session_state.Page_Product_Category_A,
            st.session_state.Page_Product_Category_B,
            st.session_state.Page_Product_Category_C
        ]
        page_ref = sidebar_options.index(st.sidebar.radio("Select a page:", sidebar_options))
        current_page = ['assessment', 'Product A', 'Product B', 'Product C'][page_ref]

        

    if current_page == 'home_page':
        home_page()
    elif current_page == 'assessment':
        assessment()
    elif current_page == 'Product A':
        product_A()
    elif current_page == 'Product B':
        product_B()
    elif current_page == 'Product C':
        product_C()

    # Only show sidebar after assessment starts
    
    
         

    

if __name__ == "__main__":
    main()
    


