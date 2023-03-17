import streamlit as st
import random as rand
import pandas as pd
# from tkinter import font, Tk, ttk

st.title('Rainbow Dice')

def reset_button():
    st.session_state['red'] = False
    st.session_state['yel'] = False
    st.session_state['gre'] = False
    st.session_state['blu'] = False
    st.session_state['pen'] = False
    return

def roll_dice():
    """
    Rolls all of the dice and returns a random integer 1-6 for each die.
    """
    white1 = rand.randint(1,6)
    white2 = rand.randint(1,6)
    red = rand.randint(1,6)
    yellow = rand.randint(1,6)
    green = rand.randint(1,6)
    blue = rand.randint(1,6)
    # st.write(f"White = {white_1} and {white_2} for a total of {white_1 + white_2}")
    # st.write(f"red = {red} for options of {red + white_1} or {red + white_2}")
    # st.write(f"Yellow = {yellow} for options of {yellow + white_1} or {yellow + white_2}")
    # st.write(f"green = {green} for options of {green + white_1} or {green + white_2}")
    # st.write(f"blue = {blue} for options of {blue + white_1} or {blue + white_2}")
    return [white1, white2, red, yellow, green, blue]

diceColor = ["⬜","⬜","🟥","🟨","🟩","🟦"]
dice = [1,1,1,1,1,1] # Default Dice values

# Sidebar lockout filters
st.sidebar.markdown("Locked Out Colors")
lockRed = st.sidebar.checkbox("🟥 Lock Out Red",key='red')
lockYellow = st.sidebar.checkbox("🟨 Lock Out Yellow",key='yel')
lockGreen = st.sidebar.checkbox("🟩 Lock Out Green",key='gre')
lockBlue = st.sidebar.checkbox("🟦 Lock Out Blue",key='blu')
lockPen = st.sidebar.checkbox("✖ Lock Out Penalties",key='pen')

# Filter DataFrame for "locked out" colors
filterValues = [0,1,2,3,4,5]
if lockRed: filterValues.remove(2)
if lockYellow: filterValues.remove(3)
if lockGreen: filterValues.remove(4)
if lockBlue: filterValues.remove(5)    
# filterValues

if len(filterValues) <= 3 or lockPen:
    st.header("GAME OVER")
    reset = st.button("RESET GAME",on_click=reset_button)
else:
    if st.button('ROLL DICE'): # When button press, dice are rolled
        dice = roll_dice()
        
    # Add white dice to colored dice for options
    opt1 = [dice[0]+x for x in dice]
    opt2 = [dice[1]+y for y in dice]

    # Make sure only white1 and white2 values are added
    opt1[0],opt2[1] = opt1[1],opt2[0] 

    # combine roll data with options added
    dice_rolls = {"Color":diceColor,"Rolled":dice,"Option 1":opt1,"Option 2":opt2} 

    # presented dataframe
    diceFrame = pd.DataFrame(data=dice_rolls)
    filterDice = diceFrame.filter(axis=0,items=filterValues)
    # diceFrame
    filterDice