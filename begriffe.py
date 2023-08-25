import pandas as pd
import streamlit as st

def begriffe():
    st.markdown('<div style="text-align: center;"><h1><em>--- Lernt die Begriffe kennen ---</em></h1></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    keyword = [
    "Analyse von Markttrends","Kundenfeedback","Datengetriebene Entscheidung",
    "Datenbereinigung","Statistische Analyse","Predictive Analyse",
    "Explorative Datenanalyse","Data Mining","Machine Learning",
    "Datenmodellierung","Interaktive Dashboards","Algorithmen",
    "Data Storytelling","Database","Datensatz","Feature Engineering",
    "Zeitreihenanalyse"
    ]

    definition = [
    '''Untersuchen von Mustern und Entwicklungen auf dem Markt, 
    um Einblicke in das Verhalten von Verbrauchern und Wettbewerbern zu gewinnen.''',

    '''Sammeln und Auswerten von Rückmeldungen und Meinungen von Kunden, 
    um Einblicke in ihre Präferenzen und Bedürfnisse zu erhalten.''',

    '''Treffen von Entscheidungen basierend auf objektiver Analyse 
    und Interpretation von Daten, um bessere Geschäftsentscheidungen zu treffen.''',

    '''Prozess der Identifizierung und Korrektur von Fehlern, 
    Ungenauigkeiten und fehlenden Werten in einem Datensatz, um die Datenqualität zu verbessern.''',

    '''Anwenden von statistischen Methoden, um Muster, 
    Beziehungen und Trends in Daten zu erkennen und zu interpretieren.''',

    '''Nutzung von historischen Daten und statistischen Algorithmen, 
    um zukünftige Ereignisse oder Trends vorherzusagen.''',

    '''Untersuchen von Daten, um Muster, 
    Zusammenhänge und Abweichungen zu entdecken, 
    die zur Formulierung neuer Hypothesen führen können.''',

    '''Entdecken von verborgenen Mustern, 
    Zusammenhängen und Informationen in großen Datenmengen, 
    um wertvolle Erkenntnisse zu gewinnen.''',

    '''Anwendung von Algorithmen und Modellen, 
    die es einem Computer ermöglichen, aus Daten 
    zu lernen und Vorhersagen oder Entscheidungen zu treffen.''',

    '''Erstellen von abstrakten Darstellungen 
    von Datenstrukturen und Beziehungen, um die Datenverarbeitung 
    und -analyse zu optimieren.''',

    '''Erstellen von visuellen Berichtsoberflächen, 
    die es Benutzern ermöglichen, Daten interaktiv zu 
    erkunden und zu analysieren.''',

    '''Mathematische Anweisungen, die verwendet werden, 
    um Daten zu verarbeiten, analysieren und Muster zu erkennen.''',

    '''Kommunikation von Datenanalysen und -erkenntnissen 
    in Form einer erzählerischen Präsentation, 
    um die Botschaft verständlich und überzeugend zu vermitteln.''',

    '''Eine strukturierte Sammlung von Daten, die organisiert, 
    gespeichert und verwaltet wird. Die besteht meistens aus mehreren Tabellen''',

    '''Eine Sammlung von Daten, die Informationen zu einem 
    bestimmten Thema oder einer bestimmten Entität enthält.''',

    '''Der Prozess der Schaffung neuer Merkmale oder der 
    Transformation vorhandener Merkmale in einem Datensatz, 
    um die Leistung von Modellen in der Datenanalyse 
    oder im Maschinenlernen zu verbessern.''',

    '''Datenpunkte werden in chronologischer 
    Reihenfolge erfasst, um Muster und Trends im Laufe 
    der Zeit zu erkennen und Vorhersagen über 
    zukünftige Werte zu treffen.'''
    ]
    c1,c2,c3 = st.columns([3,1,1])
    password = " "
    passw = ""
    with c1:
        st.write("1. Erinnert an die Begriffe aus der Vormittagsrunde.")
        st.write("2. Ordnet diese Definitionen zu den passenden Begriffen.")
        st.write("3. Erst wenn ihr fertig seid, könnt ihr die Antworten kontrollieren.")
        st.write("4. Ihr könnt auch die Musterlösungen natürlich anschauen ;)")
        st.write("_______")
    with c2:
        st.write("Fertig?")
        check = st.checkbox("Antwort kontrollieren")
    with c3:
        st.write("Kontrolliert eure Antworten hier:")
        if st.checkbox("Siehe Lösungen"):
            passw = "2408"
            password = st.text_input("Insert Password (mein Geburtstag in DDMM):",type = "password")
        st.write("_____")
    a1,a2 = st.columns([2,1])
    with a1:
        b1,b2,b001 = st.columns(3)
        with b1:
            st.write(definition[10])
        with b2:
            de0 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de0")
        with b001:
            if check:
                if de0 == keyword[10]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b3,b4,b002 = st.columns(3)
        with b3:
            st.write(definition[2])
        with b4:
            de1 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de1")
        with b002:
            if check:
                if de1 == keyword[2]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b5,b6,b003 = st.columns(3)
        with b5:
            st.write(definition[14])
        with b6:
            de2 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de2")
        with b003:
            if check:
                if de2 == keyword[14]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b7,b8,b004 = st.columns(3)
        with b7:
            st.write(definition[6])
        with b8:
            de3 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de3")
        with b004:
            if check:
                if de3 == keyword[6]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b9,b10,b005 = st.columns(3)
        with b9:
            st.write(definition[8])
        with b10:
            de4 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de4")
        with b005:
            if check:
                if de4 == keyword[8]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b11,b12,b006 = st.columns(3)
        with b11:
            st.write(definition[0])
        with b12:
            de5 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de5")
        with b006:
            if check:
                if de5 == keyword[0]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b13,b14,b007 = st.columns(3)
        with b13:
            st.write(definition[12])
        with b14:
            de6 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de6")
        with b007:
            if check:
                if de6 == keyword[12]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b15,b16,b008 = st.columns(3)
        with b15:
            st.write(definition[4])
        with b16:
            de7 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de7")
        with b008:
            if check:
                if de7 == keyword[4]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b17,b18,b009 = st.columns(3)
        with b17:
            st.write(definition[16])
        with b18:
            de8 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de8")
        with b009:
            if check:
                if de8 == keyword[16]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b19,b20,b010 = st.columns(3)
        with b19:
            st.write(definition[11])
        with b20:
            de9 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de9")
        with b010:
            if check:
                if de9 == keyword[11]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b21,b22,b011 = st.columns(3)
        with b21:
            st.write(definition[3])
        with b22:
            de10 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de10")
        with b011:
            if check:
                if de10 == keyword[3]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b23,b24,b012 = st.columns(3)
        with b23:
            st.write(definition[15])
        with b24:
            de11 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de11")
        with b012:
            if check:
                if de11 == keyword[15]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b25,b26,b013 = st.columns(3)
        with b25:
            st.write(definition[7])
        with b26:
            de12 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de12")
        with b013:
            if check:
                if de12 == keyword[7]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b27,b28,b014 = st.columns(3)
        with b27:
            st.write(definition[9])
        with b28:
            de13 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de13")
        with b014:
            if check:
                if de13 == keyword[9]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b29,b30,b015 = st.columns(3)
        with b29:
            st.write(definition[1])
        with b30:
            de14 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de14")
        with b015:
            if check:
                if de14 == keyword[1]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b31,b32,b016 = st.columns(3)
        with b31:
            st.write(definition[13])
        with b32:
            de15 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de15")
        with b016:
            if check:
                if de15 == keyword[13]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
        st.write("_____")
        b33,b34,b017 = st.columns(3)
        with b33:
            st.write(definition[5])
        with b34:
            de16 = st.selectbox("Suche einen passenden Begriff:", keyword, key = "de16")
        with b017:
            if check:
                if de16 == keyword[5]:
                    st.success("richtig!")
                else:
                    st.error("falsch!")
    with a2:
        if password == passw:
            for i in range(len(keyword)):
                st.markdown('<div style="text-align: left;"><h5><i>'+keyword[i]+'</i></h5></div>', unsafe_allow_html=True)
                st.markdown('<div style="text-align: left;"><h5>'+definition[i]+'</h5></div>', unsafe_allow_html=True)
                st.write("_____")
                

