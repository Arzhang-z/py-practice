# Monty Hall Simulation Game

## Description
this implementation solves the famous Monty Hall problem, ppresenting intractive dashboard where you can simulate numerous iterations of the game and visibly note the win percentages in both scenarios, i.e. switching and not switching the chosen door.


## Project Struture
```
.
|__ README.md
|__ requirements.txt
|__ src
    |__ main.py
    |__ main.ipynb
    |__ dashboard.py

```

`README.md:` This descriptive file
`requirements.txt:` Contains all the required modules and libraries needed to run the project
`src/main.py:` Contains the Python program to simulate the Monty hall game
`src.dashboard.py:` The Streamlit application file to display an interactive dashboard


## Requiremnets
- Python 3.7 or higher
- Streamlit

To install necessary packages, run:
```bash
pip install -r requirements.txt
```

## How to Run
you can play the Monty Hall game simulation by adding `src` directory to the PYTHONPATH by doing this:
```bash
cd 6-monty-hall-problem-simulator
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

then running:
```bash
pyton src/main.py
```

to start the streamlit dashboard, run:
```bash
streamlit run src/dashboard.py
```

## Results
On running the Streamlit application, You will see an input field where you can specify the number of games to simulate. The app will then perform a simulation for each game, both where the contestant switches doors and where they don't. Lastly, the dashboard will display the win percentages dynamically as two chart goas on.
- showing how likelihood of winning changes based on your decision to switch or not to the other door.
- You might guessed it has the same winrate, but in fact, switching to the other door, improves your chance of winning to ``` 66% ``` wile staying with your initial choice might give you the chance of ```33% ``` in the long rum