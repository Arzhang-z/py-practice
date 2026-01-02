import streamlit as st
from password_generator import RandomPaswordGenerator
from password_generator import MemorablePasswordGenerator
from password_generator import PinGenerator


st.image("/home/arzhang/projects/1-train/tmp-py-practice/py-practice/4-streamlit/images/lock.png",width=400)
st.title("Password Generator")


option = st.radio(
    "Select a password genertor",
    ["Random Password", "Memorable Password", "Pin code"]
)

if option == "Pin code":
    length = st.slider("Select the length for the pin code",2,100,8)
    
    generator = PinGenerator(length)

elif option == "Random Password":
    length = st.slider("Select the length for the Password ",2,100,8)
    include_symbol = st.toggle("Include Symbols")
    include_numbers = st.toggle("Include Numbers")

    generator = RandomPaswordGenerator(length,include_numbers,include_symbol)

elif option == "Memorable Password":
    num_of_words = st.slider("select the number of words",2,100,4)
    seperator = st.text_input("Seperator","_")
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words,seperator,capitalization,None)


password = generator.generate()
st.write(f"Your password is  ```{password}```  ")