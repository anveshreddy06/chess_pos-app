import streamlit as st

st.title("chessboard position color")

#user input
#pos1 = st.number_input("Enter position1")
#pos2 = st.number_input("Enter position2")
pos1 = st.slider("Position1", 1, 8)
pos2 = st.slider("Position2", 1, 8)

r1 = [1, 3, 5, 7]
r2 = [2, 4, 6, 8]
c1 = [1, 3, 5, 7]
c2 = [2, 4, 6, 8]

if (pos1 in r1 and pos2 in c1) or (pos1 in r2 and pos2 in c2):
    st.write("The position is black")
else:
    st.write("The position is white")
