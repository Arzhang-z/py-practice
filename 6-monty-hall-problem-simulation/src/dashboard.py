import streamlit as st
from src.main import simulate_game
import time


st.title(":goat: Monty Hall Simulation")


num_games = st.number_input("Enter number of games to simulate",
    min_value = 100,
    max_value = 10000,
    value = 500,
    step = 100
)


col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")


chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)


wins_no_switch = 0
wins_switch = 0


for i in range(num_games):
    num_wins_with_swiitching, num_wins_without_switching = simulate_game(1)
    wins_switch += num_wins_with_swiitching
    wins_no_switch += num_wins_without_switching

    chart1.add_rows([wins_no_switch / (i+1) ])
    chart2.add_rows([wins_switch / (i+1) ])

    time.sleep(0.01)