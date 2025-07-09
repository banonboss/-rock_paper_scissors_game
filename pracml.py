import streamlit as st
import random

st.title("✊ Rock, 🖐 Paper, ✌ Scissors Game")

options = ["Rock", "Paper", "Scissors"]
player_choice = st.selectbox("Choose your move:", options)

if st.button("Play"):
    computer_choice = random.choice(options)

    st.write(f"🧍 You chose: *{player_choice}*")
    st.write(f"🤖 Computer chose: *{computer_choice}*")

    if player_choice == computer_choice:
        st.info("It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        st.success("You win! 🎉")
    else:
        st.error("Computer wins! 😢")