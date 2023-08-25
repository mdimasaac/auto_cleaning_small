def visualization():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objs as go
    st.markdown('<div style="text-align: center;"><h1><em>--- Explorative Datenanalyse ---</em></h1></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write("Übungsaufgaben:")
    st.write("1. Findet 3 Sub-Kategorien, die die größten Profit machen.")
    st.write("2. Findet 3 Sub-Kategorien, die die größten Sales machen.")
    st.write("3. Wann ist die Profit am niedrigsten und wie groß?")
    st.write("4. Welcher Kunde hat die Größte Profit gebracht?")
    st.write("5. Wann findet man die größten Discount? Gibt es ein Tag, wo da die meisten Discounts sich befinden?")
    st.write("_____")
    df = pd.read_csv("superstore.csv")
    df = df.iloc[:200]
    # df["Order Date"] = pd.to_datetime(df["Order Date"])

    cols = df.columns.tolist()
    style = ["Bar","Scatter","Line"]
    c1,c2,c3 = st.columns([1,4,1])
    data = []
    with c2:
        colx = st.selectbox("Select Value for x-Axis:", cols)
        x = df[colx].values.tolist()
        pivot = st.checkbox("Group by this axis")
        if pivot:
            try:
                grouped = df.groupby(colx).sum()
                st.write("aggfunc: [sum]")
            except:
                grouped = df.groupby(colx).count()
                st.write("aggfunc: [count]")
            grouped = grouped.sort_index(sort_datetime_index=True)
            x = grouped.index.tolist()
        else:
            x = df[colx].values.tolist()

    a1,a2 = st.columns(2)
    with a1:
        colya = st.selectbox("Select Value for y-Axis (graph A):", cols)
        typea = st.selectbox("Select Plot Style (graph A)", style)
        if pivot:
            ya = grouped[colya].values.tolist()
        else:
            ya = df[colya].values.tolist()
        if typea == "Bar":
            trace1 = go.Bar(
            x = x,
            y = ya,
            width = .5,
            textposition='outside',name = colya
            )
        elif typea == "Scatter":
            trace1 = go.Scatter(
            x = x,
            y = ya,
            mode = "markers",name = colya
            )
        elif typea == "Line":
            trace1 = go.Scatter(
            x = x,
            y = ya,
            mode = "lines",name = colya
            )
        if st.checkbox("Show Graph A"):
            data.append(trace1)
    with a2:
        colyb = st.selectbox("Select Value for y-Axis (graph B):", cols)
        typeb = st.selectbox("Select Plot Style (graph B)", style)
        if pivot:
            yb = grouped[colyb].values.tolist()
        else:
            yb = df[colyb].values.tolist()
        if typeb == "Bar":
            trace2 = go.Bar(
            x = x,
            y = yb,
            width = .5,
            textposition='outside',name = colyb
            )
        elif typeb == "Scatter":
            trace2 = go.Scatter(
            x = x,
            y = yb,
            mode = "markers",name = colyb
            )
        elif typeb == "Line":
            trace2 = go.Scatter(
            x = x,
            y = yb,
            mode = "lines",name = colyb
            )
        if st.checkbox("Show Graph B"):
            data.append(trace2)

    b1,b2,b3 = st.columns([.5,4,.5])
    with b2:
        fig = go.Figure(data = data)
        fig.update_layout(template="plotly_dark",
        autosize=True, height = 600
        )
        st.plotly_chart(fig, use_container_width=True)
            