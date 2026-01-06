import streamlit as st
from constants import Currencies
from Currency_converter import convert_currency, get_exchange_rate


st.title(':dollar: Currency Converter')


st.markdown('''
This tool allows you to instantly convert amounts between different currencies around the world
             	
:earth_americas:. Enter the amount and choose the currencies to see th result           
''')
base_currency = st.selectbox("From Currency (Base): ", Currencies, index=1)
target_currency = st.selectbox("To Currency (Target): ", Currencies, index=0)

amount = st.number_input('Eneter Amonut: ',min_value=0.0, value=100.0)

if amount > 0 and base_currency != target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f":white_check_mark: Exchange Rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label='Base Currency', value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; color: white; margin: 0;'>&#8594;</h1>",unsafe_allow_html=True)
        col3.metric(label='Target Currency', value=f"{converted_amount:.2f} {target_currency}")
    else:
        st.error('Error fetching exchange rate')

st.markdown('---')