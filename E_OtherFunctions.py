import streamlit as st
import pandas as pd


@st.cache_data
def load_tariff_rates():

    TR = pd.read_excel('Reference/Tariff_Rates.xlsx')

    return TR

def cost_impact(cost_breakdown, country_splits):

    cost = pd.DataFrame(country_splits)
    cost['RM_share'] = cost_breakdown['raw_materials']
    cost['FG1_share'] = cost_breakdown['finished_goods_1']
    cost['FG2_share'] = cost_breakdown['finished_goods_2']

    tariffs = load_tariff_rates()

    cost2 = pd.merge(cost, tariffs, left_on = 'countries', right_on = 'Country', how = 'left').drop('Country', axis = 1)

    cost2['RM_CI'] = cost2['raw_materials'] * cost2['RM_share'] * cost2['Tariff_Rate']
    cost2['FG1_CI'] = cost2['finished_goods_1'] * cost2['FG1_share'] * cost2['Tariff_Rate'] 
    cost2['FG2_CI'] = cost2['finished_goods_2'] * cost2['FG2_share'] * cost2['Tariff_Rate']
    cost2['Total_Impact'] = cost2['RM_CI'] + cost2['FG1_CI'] + cost2['FG2_CI']

    return (cost2['Total_Impact'].sum())*100




