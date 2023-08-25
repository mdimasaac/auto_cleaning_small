
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from visualization import visualization
from begriffe import begriffe
st.set_page_config(layout='wide')

def main():
    options = ["Main","Visualization","Definitionen (DE)"]
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    if choice == "Main":
        st.markdown('<div style="text-align: center;"><h1><em>--- Clean My Data! ---</em></h1></div>', unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        d1,d2,d3 = st.columns([1,2,1])
        with d2:
            st.markdown('''<div style="text-align: justify;">
                <h4><u>Data Cleaning</u> is a crucial aspect of data analytics that involves identifying and rectifying errors, 
                inconsistencies, and inaccuracies in raw data. 
                It is essential because clean and accurate data forms the foundation for meaningful analysis and insights.
                </h4></div>''', unsafe_allow_html=True)
        st.write("_____")
        a1,a2,a3,a4 = st.columns([1,.75,1.25,1])
        
        with a2:
            intros = [
                    "High-Quality Insights", "Effective Decision-Making",
                    "Enhanced Data Visualization","Data Consistency",
                    "Minimized Bias and Errors","Time and Resource Efficiency",
                    "Improved Model Performance","Enhanced Collaboration",
                    "Regulatory and Compliance Requirements","Long-Term Data Usability"
            ]
            intro = st.selectbox("Motivations",intros)
        with a3:
            explanations = [
                    '''Accurate data leads to accurate insights. 
                    Data cleaning ensures that the data used for analysis is reliable, 
                    reducing the risk of making incorrect conclusions or decisions based on faulty information.''',

                    '''Clean data allows analysts to make informed decisions based on accurate information. 
                    It helps in identifying trends, patterns, and correlations that drive strategic choices 
                    and business outcomes.''',

                    '''Clean data improves the quality of visualizations, 
                    making it easier to communicate findings and results to stakeholders. 
                    Clarity in visuals facilitates better understanding and interpretation of complex information.''',

                    '''Inconsistencies in data, such as different spellings of the same category, 
                    can lead to confusion and errors. Cleaning data ensures uniformity and consistency, 
                    making it easier to analyze and interpret.''',

                    '''Dirty data can introduce bias and errors in analyses. 
                    Data cleaning helps to minimize these biases by removing or correcting inaccuracies, 
                    leading to more objective and reliable insights.''',

                    '''Working with clean data reduces the time spent on troubleshooting issues 
                    that arise due to dirty data. Analysts can focus more on 
                    extracting insights and value from the data.''',

                    '''In machine learning and predictive analytics, clean data leads to 
                    more accurate model training and predictions. 
                    Models built on clean data are more likely to generalize well to new data.''',

                    '''Clean data can be easily shared and understood by colleagues, 
                    facilitating collaborative efforts across teams. 
                    It reduces confusion and misunderstandings related to data interpretation.''',

                    '''Some industries have strict regulations on data accuracy and privacy. 
                    Data cleaning helps in meeting these compliance requirements and maintaining data integrity.''',

                    '''Well-cleaned data retains its value over time. 
                    Data that has been properly cleaned and documented can be reused for future analyses, 
                    avoiding redundant efforts.'''
            ]
            if intro == intros[0]:
                expl = explanations[0]
            elif intro == intros[1]:
                expl = explanations[1]
            elif intro == intros[2]:
                expl = explanations[2]
            elif intro == intros[3]:
                expl = explanations[3]
            elif intro == intros[4]:
                expl = explanations[4]
            elif intro == intros[5]:
                expl = explanations[5]
            elif intro == intros[6]:
                expl = explanations[6]
            elif intro == intros[7]:
                expl = explanations[7]
            elif intro == intros[8]:
                expl = explanations[8]
            elif intro == intros[9]:
                expl = explanations[9]
            st.markdown('<div style="text-align: justify;"><h5><em>'+expl+'</em></h5></div>', unsafe_allow_html=True)
        st.write("_____")
        st.subheader("How To Play:")
        st.write("1. Wählt eine Spalte aus der Liste der Spaltennamen (linke Seite)")
        st.write("2. Kontrolliert den Datentyp, ob alles in Ordnung ist (eine Zahl muss als 'Number' formatiert, ,usw.)")
        st.write("3. Kontrolliert, ob in der Spalte Null-Values vorhanden sind.")
        st.write("4. Wenn ja, versucht sie mithilfe einer der gezeigten Methode (Mean, Mode, etc.) zu ersetzen.")
        st.write("5. Die Null-Values können ebenso durch einen freigegebenen Text gegeben, wenn es sinnvoller ist.")
        st.write("6. Schaut an die Tabelle unten. Findet inkonsistente Formatierung. Löscht/ersetzt die unnötige Charakters im Text.")
        st.write("7. Falls ihr einige Begriffe nicht versteht, könnt ihr die Erklärung dazu auf der rechten Seite.")
        st.write("8. Falls ihr etwas komisches getan habt und den Datensatz zum Anfangszustand bringen wollt, clickt auf 'Restore Data'")
        st.write(" ")
        st.write(" ")
        st.write("... viel Spaß! :)")
        st.write("_____")
        data = pd.read_csv("superstore_small.csv")
        data["order_date"] = pd.to_datetime(data["order_date"])
        if 'df' not in st.session_state:
            st.session_state.df = data.copy()

        cols = st.session_state.df.columns.tolist()  # Get column names
        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            col = st.radio("Select Column:", cols)
            st.write("Selected Column:")
            st.subheader(col.upper())
           

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

            convert = st.selectbox("Convert to:", ["Text","Number","Date"])
            if convert == "Text":
                try:
                    st.session_state.df[col] = st.session_state.df[col].astype(object)
                except:
                    st.error("Cannot convert.")
            elif convert == "Number":
                try:
                    st.session_state.df[col] = st.session_state.df[col].astype(np.number)
                except:
                    st.error("Cannot convert.")
            elif convert == "Date":
                try:
                    st.session_state.df[col] = pd.to_datetime(st.session_state.df[col])
                except:
                    st.error("Cannot convert.")

            measure = st.selectbox("Check Measures:", ["Mean","Mode","Median","Min","Max"])
            if measure == ("Mean"):
                try:
                    mean = st.session_state.df[col].mean()
                    st.write("Mean:", mean)
                except:
                    st.error("Cannot calculate mean: Not a Number")
            if measure == ("Mode"):
                try:
                    mode = st.session_state.df[col].mode().values.tolist()[0]
                    st.write("Mode:", mode)
                except:
                    st.error("Cannot calculate Mode.")

            if measure == ("Median"):
                try:
                    values = st.session_state.df[col].sort_values().tolist()
                    median = values[int(len(values)/2)]
                    st.write("Median:", median)
                except:
                    st.error("Cannot calculate Median.")

            if measure == ("Min"):
                try:
                    min_val = st.session_state.df[col].min()
                    st.write("Min:", min_val)
                except:
                    st.error("Cannot Calculate Min Value - Replace Null Values First")

            if measure == ("Max"):
                try:
                    max_val = st.session_state.df[col].max()
                    st.write("Max:", max_val)
                except:
                    st.error("Cannot Calculate Max Value - Replace Null Values First")
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
            st.markdown('<div style="text-align: left;"><h5><em>Replace Null/None Values</em></h5></div>', unsafe_allow_html=True)
            replace = st.selectbox("Replace with which value?",["Mean","Mode","Median","Interpolate"])
            if st.button("Replace Null"):
                if replace == ("Mean"):
                    mean = st.session_state.df[col].mean()
                    st.session_state.df[col] = st.session_state.df[col].fillna(mean)
                    
                if replace == ("Mode"):
                    mode = st.session_state.df[col].mode().values.tolist()[0]
                    st.session_state.df[col] = st.session_state.df[col].fillna(mode)
                    
                if replace == ("Median"):
                    values = st.session_state.df[col].sort_values().tolist()
                    median = values[int(len(values)/2)]
                    st.session_state.df[col] = st.session_state.df[col].fillna(median)
                    
                if replace == ("INTERPOLATE"):
                    st.session_state.df[col] = st.session_state.df[col].interpolate()
                st.success("Replaced Null. See Updated Data Below.")

            text = st.text_input("Or Fill Nulls With Text:")
            conditions = st.checkbox("On Conditions...")
            if conditions:
                where = st.selectbox("Where (Pick a Column)", cols)
                contains = st.text_input("Contains (text):")

            if st.button("Replace with This Text"):
                if conditions:
                    st.session_state.df[col] = st.session_state.df.apply(
                    lambda row: text if (pd.isnull(row[col])) and (contains in row[where]) else row[col],
                    axis=1)
                else:
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
        
        with c5:
            st.markdown('<div style="text-align: left;"><h5><em>Need Help?</em></h5></div>', unsafe_allow_html=True)
            helps = ["Null Values","Data Types","Text","Number","Datetime","Mean","Mode","Median","Interpolate"]
            plshelp = st.selectbox("I need help with...", helps)
            help_details = [
                    '''Null values, or missing values, are placeholders indicating the absence of 
                    actual data in a dataset. Handling null values during data cleaning is 
                    essential to ensure accurate analysis and meaningful insights,
                    either by filling them with values or removing them.''',

                    '''Data Types define how information is stored and processed. Texts can only be processed
                    using methods for texts, Numbers can only be processed using mathematical operations, etc.''',

                    '''The Text (str) data type represents strings of characters, 
                    which can include letters, numbers, symbols, and spaces.''',

                    '''The Number data type is used to store numerical values. 
                    These values can be whole numbers (int) or numbers with decimals (float). It can be calculated
                    using mathematical formulas.''',

                    '''The Datetime data type is used to store dates and times. 
                    It combines information about the calendar date (year, month, day) 
                    with the clock time (hours, minutes, seconds).''',

                    '''Mean is the average of a set of values, calculated by adding them up 
                    and dividing by the number of values.''',

                    '''Mode is the value that appears most frequently in a set of values.''',

                    '''Median is the middle value in a set of values when they are arranged in order.''',

                    '''Interpolate means estimating missing values based on nearby values 
                    (values before and values after).'''
            ]
            if plshelp == helps[0]:
                details = help_details[0]
            elif plshelp == helps[1]:
                details = help_details[1]
            elif plshelp == helps[2]:
                details = help_details[2]
            elif plshelp == helps[3]:
                details = help_details[3]
            elif plshelp == helps[4]:
                details = help_details[4]
            elif plshelp == helps[5]:
                details = help_details[5]
            elif plshelp == helps[6]:
                details = help_details[6]
            elif plshelp == helps[7]:
                details = help_details[7]
            elif plshelp == helps[8]:
                details = help_details[8]
            st.markdown('<div style="text-align: justify;"><h6><em>'+details+'</em></h6></div>', unsafe_allow_html=True)

        st.write("_____")
        
        sorting_order = st.selectbox("Select Sorting Order:", ["Ascending", "Descending"])
        if sorting_order == "Ascending":
            st.session_state.df = st.session_state.df.sort_values(by=col)
        elif sorting_order == "Descending":
            st.session_state.df = st.session_state.df.sort_values(by=col, ascending=False)
        category = st.session_state.df["category"].unique().tolist()
        st.data_editor(st.session_state.df)
        st.write("_____")
    elif choice == "Definitionen (DE)":
        begriffe()
    elif choice == "Visualization":
        visualization()
main()
