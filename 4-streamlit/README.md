# 🔐 Streamlit Password Generator

A simple and clean **Streamlit web app** for generating secure passwords in three different styles:

- Random passwords
- Memorable word-based passwords
- Numeric PIN codes

Built for practice, clarity, and actually being usable.

---

## Features

### Random Password
- Adjustable length
- Optional symbols
- Optional numbers

### Memorable Password
- Word-based passwords
- Custom separator
- Optional capitalization

### PIN Code
- Numeric-only
- Adjustable length

---

## Demo UI

The app provides a minimal UI with:
- Generator selection via radio buttons
- Sliders, toggles, and inputs based on the selected generator
- One-click password generation

---

## Project Structure

.
├── app.py
├── password_generator/
│ ├── RandomPaswordGenerator.py
│ ├── MemorablePasswordGenerator.py
│ └── PinGenerator.py
├── images/
│ └── lock.png
└── README.md


---

## Installation

 1. Clone the repository
```bash
git clone https://github.com/Arzhang-z/1-train/4-streamlit.git
cd password-generator-streamlit
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

2. streamlit run app.py


#### code snippet 
password = generator.generate()
st.write(f"Your password is  ```{password}```")
