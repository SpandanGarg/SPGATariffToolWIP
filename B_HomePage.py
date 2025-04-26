import streamlit as st

def home_page():
    st.image("Pictures/SK_logo.png", width=200)

    st.title('Welcome to the Simon-Kucher Tariff Impact Assessment Tool')
    st.markdown(
        "<h3 style='font-size:22px;'>This will help you assess the impact of tariffs on your value chain and your competitive market position</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("<h3 style='font-size:18px;'>Please provide the following information prior to getting started</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('')
        st.write('')

        st.write("Name (first and last)")
        st.write('')
        st.write('')
        st.write('')
        st.write("Company")

    with col2:
        respondent_name = st.text_input('', key='input_respondent_name_key')
        respondent_company = st.text_input('', key='input_respondent_company_key')

    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('')
        st.write('')
        st.write("Current role")
        st.write('')
        st.write('')
        st.write('')
        st.write("Email address")

    with col2:
        respondent_role = st.text_input('', key='input_respondent_role_key')
        respondent_email = st.text_input('', key='input_respondent_email_key')

    st.write("")
    col1, col2 = st.columns([2, 2])
    with col2:
        if st.button('Submit'):
            fields = [respondent_name, respondent_company, respondent_role, respondent_email]
            if all(val.strip() for val in fields):
                st.session_state.show_navigational_sidebar = True
                st.session_state.page_navigator = 'assessment'
                st.rerun()
                return
            else:
                st.session_state.home_page_proceed_flag = False

        if st.session_state.get('home_page_proceed_flag') is False:
            st.write('Please make sure to fill out all the fields before proceeding')
