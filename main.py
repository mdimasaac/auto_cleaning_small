
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from visualization import visualization
st.set_page_config(layout='wide')

def main():
    auto = False
    store = False
    netflix = False
    st.markdown('<div style="text-align: center;"><h2><em>Clean My Data!</em></h2></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    options = ["Main","Visualization"]
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    if choice == "Main":
        data = pd.read_csv("auto_mpg_small.csv")
        if 'df' not in st.session_state:
            st.session_state.df = data.copy()

        cols = st.session_state.df.columns.tolist()  # Get column names
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            col = st.radio("Select Column:", cols)
            st.write("Selected Column:")
            st.subheader(col.upper())
            st.write("_____")

        with c2:
            st.markdown('<div style="text-align: left;"><h5><em>Choose Your Actions:</em></h5></div>', unsafe_allow_html=True)
            if st.button("Count Null Values (NaN)"):
                nan = st.session_state.df[col].isna().sum()
                st.write("Total NaN:", nan)
            if st.button("Check Data Type"):
                if np.issubdtype(st.session_state.df[col].dtype, np.number):
                    st.write("Data Type: Number")
                elif st.session_state.df[col].dtype == "object":
                    st.write("Data Type: Text")
                elif st.session_state.df[col].dtype == "bool":
                    st.write("Data Type: Bool")
                else:
                    st.write("Data Type: ", st.session_state.df[col].dtype)
            if st.button("Convert to Text"):
                st.session_state.df[col] = st.session_state.df[col].astype(object)
            if st.button("Convert to Number"):
                st.session_state.df[col] = st.session_state.df[col].astype(np.number)
            if st.button("Convert to Datetime"):
                st.session_state.df[col] = pd.to_datetime(st.session_state.df[col])
            if st.button("Check Mean"):
                try:
                    mean = st.session_state.df[col].mean()
                    st.write("Mean:", mean)
                except:
                    st.error("Cannot calculate mean: Not a Number")
            if st.button("Check Mode"):
                try:
                    mode = st.session_state.df[col].mode().values.tolist()[0]
                    st.write("Mode:", mode)
                except:
                    st.error("Cannot calculate Mode.")

            if st.button("Check Median"):
                try:
                    values = st.session_state.df[col].sort_values().tolist()
                    median = values[int(len(values)/2)]
                    st.write("Median:", median)
                except:
                    st.error("Cannot calculate Median.")

            if st.button("Check Min"):
                try:
                    min_val = st.session_state.df[col].min()
                    st.write("Min:", min_val)
                except:
                    st.error("Cannot Calculate Min Value")

            if st.button("Check Max"):
                try:
                    max_val = st.session_state.df[col].max()
                    st.write("Max:", max_val)
                except:
                    st.error("Cannot Calculate Max Value")
            if st.button("Remove Column"):
                try:
                    st.session_state.df = st.session_state.df.drop(columns = [col])
                except:
                    pass
            st.write("_____")
            if st.button("Restore Data"):
                st.session_state.df = data.copy()  # Restore the DataFrame to original state
                st.success("Restored the DataFrame to its original state.")

        with c3:
            st.markdown('<div style="text-align: left;"><h5><em>Replace Null/None Values With:</em></h5></div>', unsafe_allow_html=True)
            if st.button("MEAN"):
                mean = st.session_state.df[col].mean()
                st.session_state.df[col] = st.session_state.df[col].fillna(mean)
                st.success("Replaced Null with MEAN Value")
            if st.button("MODE"):
                mode = st.session_state.df[col].mode().values.tolist()[0]
                st.session_state.df[col] = st.session_state.df[col].fillna(mode)
                st.success("Replaced Null with MODE Value")
            if st.button("MEDIAN"):
                values = st.session_state.df[col].sort_values().tolist()
                median = values[int(len(values)/2)]
                st.session_state.df[col] = st.session_state.df[col].fillna(median)
                st.success("Replaced Null with MEDIAN Value")
            if st.button("INTERPOLATE"):
                st.session_state.df[col] = st.session_state.df[col].interpolate()
                st.success("Replaced Null with Interpolated Values")

            text = st.text_input("Or Fill Nulls With Text:")
            if st.button("Replace with This Text"):
                st.session_state.df[col] = st.session_state.df[col].apply(lambda x: text if pd.isnull(x) else x)
                st.write("Replaced Null With Your Text")
            st.write("_____")
        with c4:
            st.markdown('<div style="text-align: left;"><h5><em>Replace Character(s) in Text</em></h5></div>', unsafe_allow_html=True)
            value_to_replace = st.text_input("Replace This Value")
            new_value = st.text_input("With This Value")
            if st.button("Replace Character(s)"):
                newvalues = []
                if new_value == " ":
                    new_value = ""
                for i in st.session_state.df[col]:
                    i = i.replace(value_to_replace, new_value)
                    newvalues.append(i)
                st.session_state.df[col] = newvalues
                st.success("Done!")
            st.write("_____")

        st.write("_____")
        sorting_order = st.radio("Select Sorting Order:", ["Ascending", "Descending"])
        if st.button("Sort Values By Column"):
            if sorting_order == "Ascending":
                st.session_state.df = st.session_state.df.sort_values(by=col)
                st.write("Successfully sorted your data by " + col + " (ascending).")
            elif sorting_order == "Descending":
                st.session_state.df = st.session_state.df.sort_values(by=col, ascending=False)
                st.write("Successfully sorted your data by " + col + " (descending).")

        st.write(st.session_state.df)
        st.write("_____")

    
    elif choice == "Visualization":
        visualization()
main()
