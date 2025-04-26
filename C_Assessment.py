import pandas as pd
import streamlit as st



def assessment():

    st.image("Pictures/SK_logo.png", width=200)

    st.markdown(
        "<h3 style='font-size:22px;'>Here you will outline key details for up to 3 product categories</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("<h3 style='font-size:18px;'>Please provide the necessary inputs, you may leave unneeded product categories or competitors blank</h3>", unsafe_allow_html=True)


    mkt_shares = ['Cat_A_User_Mkt_Share', 'Cat_A_Comp1_Mkt_Share', 'Cat_A_Comp2_Mkt_Share',
              'Cat_B_User_Mkt_Share', 'Cat_B_Comp1_Mkt_Share', 'Cat_B_Comp2_Mkt_Share',
              'Cat_C_User_Mkt_Share', 'Cat_C_Comp1_Mkt_Share', 'Cat_C_Comp2_Mkt_Share']

    unit_prices = ['Cat_A_User_Unit_Price','Cat_A_Comp1_Unit_Price','Cat_A_Comp2_Unit_Price',
                   'Cat_B_User_Unit_Price','Cat_B_Comp1_Unit_Price','Cat_B_Comp2_Unit_Price',
                   'Cat_C_User_Unit_Price','Cat_C_Comp1_Unit_Price','Cat_C_Comp2_Unit_Price']
    
    COGS = ['Cat_A_User_COGS','Cat_A_Comp1_COGS','Cat_A_Comp2_COGS',
            'Cat_B_User_COGS','Cat_B_Comp1_COGS','Cat_B_Comp2_COGS',
            'Cat_C_User_COGS','Cat_C_Comp1_COGS','Cat_C_Comp2_COGS']


    for mktshare in mkt_shares:
        if mktshare not in st.session_state: 
            st.session_state[mktshare] = 33.3

    for unitprice in unit_prices:
        if unitprice not in st.session_state: 
            st.session_state[unitprice] = 0.0

    for COG in COGS:
        if COG not in st.session_state: 
            st.session_state[COG] = 0.0
        

    
    col1, col2, col3, col4 = st.columns([4,6,6,6])
    
    
    with col2:
        Prod_A = st.text_input('', value = st.session_state.Page_Product_Category_A, key = 'input_Product_Cat_A')
    
    with col3:
        Prod_B = st.text_input('', value = st.session_state.Page_Product_Category_B, key = 'input_Product_Cat_B')
    
    with col4:
        Prod_C = st.text_input('', value = st.session_state.Page_Product_Category_C, key = 'input_Product_Cat_C')


    updated = False

    if Prod_A != st.session_state.Page_Product_Category_A:
        st.session_state.Page_Product_Category_A = Prod_A
        updated = True

    if Prod_B != st.session_state.Page_Product_Category_B:
        st.session_state.Page_Product_Category_B = Prod_B
        updated = True

    if Prod_C != st.session_state.Page_Product_Category_C:
        st.session_state.Page_Product_Category_C = Prod_C
        updated = True

    if updated:
        st.rerun()

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([4,2,2,2,2,2,2,2,2,2])

    with col1:
        st.write('')
        st.write('')
        st.write('Your product data:')

        st.write('')
        st.write('')
        st.write('')
        st.write('Competitor 1 product data:')
        st.write('')
        st.write('')
        st.write('')
        st.write('Competitor 2 product data:')
    
    with col2:
        Cat_A_User_Mkt_Share = st.number_input('Market share (%)', 
                                               value = st.session_state.get('Cat_A_User_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_A_User_Mkt_Share')
        
        Cat_A_Comp1_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_A_Comp1_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_A_Comp1_Mkt_Share')

        Cat_A_Comp2_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_A_Comp2_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_A_Comp2_Mkt_Share')
        
        st.session_state['Cat_A_User_Mkt_Share'] = Cat_A_User_Mkt_Share
        st.session_state['Cat_A_Comp1_Mkt_Share'] = Cat_A_Comp1_Mkt_Share
        st.session_state['Cat_A_Comp2_Mkt_Share'] = Cat_A_Comp2_Mkt_Share
    
    with col3:
        Cat_A_User_Unit_Price = st.number_input('Unit price ($)', 
                                                value = st.session_state.get('Cat_A_User_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_A_User_Unit_Price')
        
        Cat_A_Comp1_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_A_Comp1_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_A_Comp1_Unit_Price')
        
        Cat_A_Comp2_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_A_Comp2_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_A_Comp2_Unit_Price')
        
        st.session_state['Cat_A_User_Unit_Price'] = Cat_A_User_Unit_Price
        st.session_state['Cat_A_Comp1_Unit_Price'] = Cat_A_Comp1_Unit_Price
        st.session_state['Cat_A_Comp2_Unit_Price'] = Cat_A_Comp2_Unit_Price

    with col4:
        Cat_A_User_COGS = st.number_input('COGS (%)', 
                                          value = st.session_state.get('Cat_A_User_COGS', 0.0),
                                          min_value=0.00,
                                          key = 'input_Cat_A_User_COGS')
        
        Cat_A_Comp1_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_A_Comp1_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_A_Comp1_COGS')
        
        Cat_A_Comp2_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_A_Comp2_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_A_Comp2_COGS')
        
        st.session_state['Cat_A_User_COGS'] = Cat_A_User_COGS
        st.session_state['Cat_A_Comp1_COGS'] = Cat_A_Comp1_COGS
        st.session_state['Cat_A_Comp2_COGS'] = Cat_A_Comp2_COGS
    
    with col5:
        Cat_B_User_Mkt_Share = st.number_input('Market share (%)', 
                                               value = st.session_state.get('Cat_B_User_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_B_User_Mkt_Share')
        
        Cat_B_Comp1_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_B_Comp1_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_B_Comp1_Mkt_Share')

        Cat_B_Comp2_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_B_Comp2_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_B_Comp2_Mkt_Share')
        
        st.session_state['Cat_B_User_Mkt_Share'] = Cat_B_User_Mkt_Share
        st.session_state['Cat_B_Comp1_Mkt_Share'] = Cat_B_Comp1_Mkt_Share
        st.session_state['Cat_B_Comp2_Mkt_Share'] = Cat_B_Comp2_Mkt_Share
    
    with col6:
        Cat_B_User_Unit_Price = st.number_input('Unit price ($)', 
                                                value = st.session_state.get('Cat_B_User_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_B_User_Unit_Price')
        
        Cat_B_Comp1_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_B_Comp1_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_B_Comp1_Unit_Price')
        
        Cat_B_Comp2_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_B_Comp2_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_B_Comp2_Unit_Price')
        
        st.session_state['Cat_B_User_Unit_Price'] = Cat_B_User_Unit_Price
        st.session_state['Cat_B_Comp1_Unit_Price'] = Cat_B_Comp1_Unit_Price
        st.session_state['Cat_B_Comp2_Unit_Price'] = Cat_B_Comp2_Unit_Price

    with col7:
        Cat_B_User_COGS = st.number_input('COGS (%)', 
                                          value = st.session_state.get('Cat_B_User_COGS', 0.0),
                                          min_value=0.00,
                                          key = 'input_Cat_B_User_COGS')
        
        Cat_B_Comp1_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_B_Comp1_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_B_Comp1_COGS')
        
        Cat_B_Comp2_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_B_Comp2_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_B_Comp2_COGS')
        
        st.session_state['Cat_B_User_COGS'] = Cat_B_User_COGS
        st.session_state['Cat_B_Comp1_COGS'] = Cat_B_Comp1_COGS
        st.session_state['Cat_B_Comp2_COGS'] = Cat_B_Comp2_COGS

    with col8:
        Cat_C_User_Mkt_Share = st.number_input('Market share (%)', 
                                               value = st.session_state.get('Cat_C_User_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_C_User_Mkt_Share')
        
        Cat_C_Comp1_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_C_Comp1_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_C_Comp1_Mkt_Share')

        Cat_C_Comp2_Mkt_Share = st.number_input('', 
                                               value = st.session_state.get('Cat_C_Comp2_Mkt_Share', 33.3), 
                                               min_value=0.00, 
                                               max_value=100.00,
                                               key = 'input_Cat_C_Comp2_Mkt_Share')
        
        st.session_state['Cat_C_User_Mkt_Share'] = Cat_C_User_Mkt_Share
        st.session_state['Cat_C_Comp1_Mkt_Share'] = Cat_C_Comp1_Mkt_Share
        st.session_state['Cat_C_Comp2_Mkt_Share'] = Cat_C_Comp2_Mkt_Share
    
    with col9:
        Cat_C_User_Unit_Price = st.number_input('Unit price ($)', 
                                                value = st.session_state.get('Cat_C_User_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_C_User_Unit_Price')
        
        Cat_C_Comp1_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_C_Comp1_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_C_Comp1_Unit_Price')
        
        Cat_C_Comp2_Unit_Price = st.number_input('', 
                                                value = st.session_state.get('Cat_C_Comp2_Unit_Price', 0.0), 
                                                min_value=0.00,
                                                key = 'input_Cat_C_Comp2_Unit_Price')
        
        st.session_state['Cat_C_User_Unit_Price'] = Cat_C_User_Unit_Price
        st.session_state['Cat_C_Comp1_Unit_Price'] = Cat_C_Comp1_Unit_Price
        st.session_state['Cat_C_Comp2_Unit_Price'] = Cat_C_Comp2_Unit_Price

    with col10:
        Cat_C_User_COGS = st.number_input('COGS (%)', 
                                          value = st.session_state.get('Cat_C_User_COGS', 0.0),
                                          min_value=0.00,
                                          key = 'input_Cat_C_User_COGS')
        
        Cat_C_Comp1_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_C_Comp1_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_C_Comp1_COGS')
        
        Cat_C_Comp2_COGS = st.number_input('', 
                                            value = st.session_state.get('Cat_C_Comp2_COGS', 0.0), 
                                            min_value=0.00,
                                            key = 'input_Cat_C_Comp2_COGS')
        
        st.session_state['Cat_C_User_COGS'] = Cat_C_User_COGS
        st.session_state['Cat_C_Comp1_COGS'] = Cat_C_Comp1_COGS
        st.session_state['Cat_C_Comp2_COGS'] = Cat_C_Comp2_COGS
    
    
    
    
