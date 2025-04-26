import pandas as pd
import streamlit as st
import pycountry as py
from D_ChartDesign import design_chart2, design_chart3


def product_A():

    num_rows = 5
    
    priority = [
        "Germany",
        "Japan",
        "China",
        "India",
        "Netherlands",
        "Korea, Republic of",  # South Korea
        "Ireland",
        "Canada",
        "Mexico"
        ]
                    
    # All country names from pycountry
    all_countries = [country.name for country in py.countries]

    # Remove priority countries and North Korea
    remaining_countries = sorted([
        c for c in all_countries 
        if c not in priority and c != "Korea, Democratic People's Republic of"
        ])

    # Final list with priority countries first
    countries = priority + remaining_countries

    st.image("Pictures/SK_logo.png", width=200)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Your Institution ", "Competitor 1 ", "Competitor 2 ", "Actions to consider"])

    with tab1:
        
        st.session_state.User_CatA_RM = st.session_state.get("User_CatA_RM", 33.33)
        st.session_state.User_CatA_FG1 = st.session_state.get("User_CatA_FG1", 33.33)
        st.session_state.User_CatA_FG2 = st.session_state.get("User_CatA_FG2", 33.33)
        st.session_state.User_CatA_NI = st.session_state.get("User_CatA_NI", 33.33)
        
        st.header("Your Institution")
        st.write('You can leave unused rows as blank (with 0 values)')
  
        col1, col2 = st.columns([1,1])

        st.write('')
        st.write('')

        col0, col1, col2, col3, col4 = st.columns([1,1,1,1,1])
        
        with col0:
            st.write('')

        with col1:
            User_CatA_RM = st.number_input('% of cost stemming from products manufactured in US with imported Raw Materials', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('User_CatA_RM', 33.3), 
                                           key = 'input_User_CatA_RM')
            st.session_state.User_CatA_RM = User_CatA_RM
                        
        with col2:
            User_CatA_FG1 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced by the manufacturing country',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('User_CatA_FG1', 33.3), 
                                           key = 'input_User_CatA_FG1')
            st.session_state.User_CatA_FG1 = User_CatA_FG1

        with col3:
            User_CatA_FG2 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced from other countries',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('User_CatA_FG2', 33.3), 
                                           key = 'input_User_CatA_FG2')
            st.session_state.User_CatA_FG2 = User_CatA_FG2
            
        
        with col4:
            User_CatA_NI = st.number_input('% of costs stemming from finished goods which are not expected to be impacted by tariffs', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('User_CatA_NI', 33.3), 
                                           key = 'input_User_CatA_NI')
            st.session_state.User_CatA_NI = User_CatA_NI

        st.write('')
        st.write('')

        for count in range(num_rows):
            if f'Cat_A_User_country_{count}' not in st.session_state:
                st.session_state[f'Cat_A_User_country_{count}'] = countries[count]

        for count in range(num_rows):
            if f'Cat_A_User_RM_{count}' not in st.session_state:
                st.session_state[f'Cat_A_User_RM_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_User_FG1_{count}' not in st.session_state:
                st.session_state[f'Cat_A_User_FG1_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_User_FG2_{count}' not in st.session_state:
                st.session_state[f'Cat_A_User_FG2_{count}'] = 0.0
       
        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
        
        with col1:
            for count in range(num_rows):
                key = f'Cat_A_User_country_{count}'
                User_country_input = st.selectbox(
                    f"Select a country #{count+1}",
                    options=countries,
                    index=countries.index(st.session_state.get(key, 1)), 
                    key = f'input_Cat_A_User_country_{count}'  # 🔑 unique key per widget
                )
                st.session_state[key] = User_country_input            

            st.markdown('##### **Totals:**')
        
        with col2:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_User_country_{count}')
                key = f"Cat_A_User_RM_{count}"
                FG_percent = st.number_input(
                    f"% of RM cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_User_RM_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            User_CatA_total_rm_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_User_RM_{count}"
                User_CatA_total_rm_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(User_CatA_total_rm_percent)) + '%'}**")

        with col3:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_User_country_{count}')
                key = f"Cat_A_User_FG1_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_User_FG1_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            User_CatA_total_fg1_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_User_FG1_{count}"
                User_CatA_total_fg1_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(User_CatA_total_fg1_percent)) + '%'}**")

        with col4:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_User_country_{count}')
                key = f"Cat_A_User_FG2_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_User_FG2_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            User_CatA_total_fg2_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_User_FG2_{count}"
                User_CatA_total_fg2_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(User_CatA_total_fg2_percent)) + '%'}**")
        
        st.write('')
        st.write('')
        
    with tab2:
        
        st.session_state.Comp1_CatA_RM = st.session_state.get("Comp1_CatA_RM", 33.33)
        st.session_state.Comp1_CatA_FG1 = st.session_state.get("Comp1_CatA_FG1", 33.33)
        st.session_state.Comp1_CatA_FG2 = st.session_state.get("Comp1_CatA_FG2", 33.33)
        st.session_state.Comp1_CatA_NI = st.session_state.get("Comp1_CatA_NI", 33.33)
        
        
        st.header("Competitor 1")
        st.write('You can leave unused rows as blank (with 0 values)')
  

        col1, col2 = st.columns([1,1])

       
        st.write('')
        st.write('')

        col0, col1, col2, col3, col4 = st.columns([1,1,1,1,1])
        with col0:
            st.write('')

        with col1:
            Comp1_CatA_RM = st.number_input('% of cost stemming from products manufactured in US with imported Raw Materials', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('Comp1_CatA_RM', 33.3), 
                                           key = 'input_Comp1_CatA_RM')
            st.session_state.Comp1_CatA_RM = Comp1_CatA_RM
            
            

        with col2:
            Comp1_CatA_FG1 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced by the manufacturing country',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('Comp1_CatA_FG1', 33.3), 
                                           key = 'input_Comp1_CatA_FG1')
            st.session_state.Comp1_CatA_FG1 = Comp1_CatA_FG1

        with col3:
            Comp1_CatA_FG2 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced from other countries',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('Comp1_CatA_FG2', 33.3), 
                                           key = 'input_Comp1_CatA_FG2')
            st.session_state.Comp1_CatA_FG2 = Comp1_CatA_FG2
            
        
        with col4:
            Comp1_CatA_NI = st.number_input('% of costs stemming from finished goods which are not expected to be impacted by tariffs', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('Comp1_CatA_NI', 33.3), 
                                           key = 'input_Comp1_CatA_NI')
            st.session_state.Comp1_CatA_NI = Comp1_CatA_NI

        st.write('')
        st.write('')


        for count in range(num_rows):
            if f'Cat_A_Comp1_country_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp1_country_{count}'] = countries[count]

        for count in range(num_rows):
            if f'Cat_A_Comp1_RM_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp1_RM_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_Comp1_FG1_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp1_FG1_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_Comp1_FG2_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp1_FG2_{count}'] = 0.0

                    
        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
        
        with col1:
            for count in range(num_rows):
                key = f'Cat_A_Comp1_country_{count}'
                Comp1_country_input = st.selectbox(
                    f"Select a country #{count+1}",
                    options=countries,
                    index=countries.index(st.session_state.get(key, 1)), 
                    key = f'input_Cat_A_Comp1_country_{count}'  # 🔑 unique key per widget
                )
                st.session_state[key] = Comp1_country_input            

            st.markdown('##### **Totals:**')

        
        with col2:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp1_country_{count}')
                key = f"Cat_A_Comp1_RM_{count}"
                FG_percent = st.number_input(
                    f"% of RM cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp1_RM_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp1_CatA_total_rm_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp1_RM_{count}"
                Comp1_CatA_total_rm_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp1_CatA_total_rm_percent)) + '%'}**")


        with col3:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp1_country_{count}')
                key = f"Cat_A_Comp1_FG1_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp1_FG1_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp1_CatA_total_fg1_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp1_FG1_{count}"
                Comp1_CatA_total_fg1_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp1_CatA_total_fg1_percent)) + '%'}**")


        with col4:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp1_country_{count}')
                key = f"Cat_A_Comp1_FG2_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp1_FG2_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp1_CatA_total_fg2_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp1_FG2_{count}"
                Comp1_CatA_total_fg2_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp1_CatA_total_fg2_percent)) + '%'}**")
        
        st.write('')
        st.write('')
        
        col1, col2, col3, col4 = st.columns([1,1,1,1])

    with tab3:
        
        st.session_state.Comp2_CatA_RM = st.session_state.get("Comp2_CatA_RM", 33.33)
        st.session_state.Comp2_CatA_FG1 = st.session_state.get("Comp2_CatA_FG1", 33.33)
        st.session_state.Comp2_CatA_FG2 = st.session_state.get("Comp2_CatA_FG2", 33.33)
        st.session_state.Comp2_CatA_NI = st.session_state.get("Comp2_CatA_NI", 33.33)
        
        
        st.header("Competitor 2")
        st.write('You can leave unused rows as blank (with 0 values)')
  

        col1, col2 = st.columns([1,1])

       
        st.write('')
        st.write('')

        col0, col1, col2, col3, col4 = st.columns([1,1,1,1,1])
        with col0:
            st.write('')

        with col1:
            Comp2_CatA_RM = st.number_input('% of cost stemming from products manufactured in US with imported Raw Materials', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('Comp2_CatA_RM', 33.3), 
                                           key = 'input_Comp2_CatA_RM')
            st.session_state.Comp2_CatA_RM = Comp2_CatA_RM
            
            

        with col2:
            Comp2_CatA_FG1 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced by the manufacturing country',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('Comp2_CatA_FG1', 33.3), 
                                           key = 'input_Comp2_CatA_FG1')
            st.session_state.Comp2_CatA_FG1 = Comp2_CatA_FG1

        with col3:
            Comp2_CatA_FG2 = st.number_input('% of cost stemming from imported Finished Goods whose raw materials are sourced from other countries',
                                           min_value = 0.0, max_value = 100.0, 
                                           value = st.session_state.get('Comp2_CatA_FG2', 33.3), 
                                           key = 'input_Comp2_CatA_FG2')
            st.session_state.Comp2_CatA_FG2 = Comp2_CatA_FG2
            
        
        with col4:
            Comp2_CatA_NI = st.number_input('% of costs stemming from finished goods which are not expected to be impacted by tariffs', 
                                           min_value = 0.0, 
                                           max_value = 100.0, 
                                           value = st.session_state.get('Comp2_CatA_NI', 33.3), 
                                           key = 'input_Comp2_CatA_NI')
            st.session_state.Comp2_CatA_NI = Comp2_CatA_NI

        st.write('')
        st.write('')


        for count in range(num_rows):
            if f'Cat_A_Comp2_country_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp2_country_{count}'] = countries[count]

        for count in range(num_rows):
            if f'Cat_A_Comp2_RM_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp2_RM_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_Comp2_FG1_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp2_FG1_{count}'] = 0.0

        for count in range(num_rows):
            if f'Cat_A_Comp2_FG2_{count}' not in st.session_state:
                st.session_state[f'Cat_A_Comp2_FG2_{count}'] = 0.0

                    
        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
        
        with col1:
            for count in range(num_rows):
                key = f'Cat_A_Comp2_country_{count}'
                Comp2_country_input = st.selectbox(
                    f"Select a country #{count+1}",
                    options=countries,
                    index=countries.index(st.session_state.get(key, 1)), 
                    key = f'input_Cat_A_Comp2_country_{count}'  # 🔑 unique key per widget
                )
                st.session_state[key] = Comp2_country_input            

            st.markdown('##### **Totals:**')

        
        with col2:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp2_country_{count}')
                key = f"Cat_A_Comp2_RM_{count}"
                FG_percent = st.number_input(
                    f"% of RM cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp2_RM_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp2_CatA_total_rm_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp2_RM_{count}"
                Comp2_CatA_total_rm_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp2_CatA_total_rm_percent)) + '%'}**")


        with col3:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp2_country_{count}')
                key = f"Cat_A_Comp2_FG1_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp2_FG1_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp2_CatA_total_fg1_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp2_FG1_{count}"
                Comp2_CatA_total_fg1_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp2_CatA_total_fg1_percent)) + '%'}**")


        with col4:
            for count in range(num_rows):
                respective_country = st.session_state.get(f'Cat_A_Comp2_country_{count}')
                key = f"Cat_A_Comp2_FG2_{count}"
                FG_percent = st.number_input(
                    f"% of FG cost from {respective_country}",
                    min_value = 0.0,
                    max_value = 100.0,
                    value = st.session_state.get(key, 0),
                    key = f'input_Cat_A_Comp2_FG2_{count}'  # 👈 same key for both widget and state
                )
                
                st.session_state[key] = FG_percent

            Comp2_CatA_total_fg2_percent = 0
            
            for count in range(num_rows):
                key = f"Cat_A_Comp2_FG2_{count}"
                Comp2_CatA_total_fg2_percent += st.session_state.get(key, 0)

            st.markdown(f"##### **{str(int(Comp2_CatA_total_fg2_percent)) + '%'}**")
        
        st.write('')
        st.write('')

    with tab4:
        design_chart2()
        st.write('')
        design_chart3()
        
        
