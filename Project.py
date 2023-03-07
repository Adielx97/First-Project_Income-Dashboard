
#/ Table of Contents:

#/ 0. Import of Libraries 
#/ 1. Webpage title
#/ 2. Streamlit Backend Elements
#/  2.1 Web Scraping with Search Bar 
#/  2.2 Data Configuration
#/   2.2.1 Creating Data Frames (DFs)
#/    2.2.1.1 DFs for pie chart income-education level
#/    2.2.1.2 DFs from xlsx for Career Entrant by Degree
#/    2.2.1.3 DFs from xlsx for income development
#/    2.2.1.4 DFs from xlsx for interactive chart General
#/    2.2.1.5 DFs for Gender
#/    2.2.1.6 DFs for Education Level
#/    2.2.1.7 DFs for Responsibility
#/    2.2.1.8 DFs for Experience
#/    2.2.1.9 DFs  for Company Size

#/ 3. Streamlit Front End Elements
#/  3.1 App-Page Layout
#/   3.1.1 Webpage title  
#/   3.1.2 Centre title
#/   3.1.3 Searchbar title
#/   3.1.4 Background image

#/  3.2 Sidebars
#/   3.2.1 General Data
#/   3.2.2 Gender
#/   3.2.3 Education Level
#/   3.2.4 Responsibility
#/   3.2.5 Experience
#/   3.2.6 Company Size

#/   3.3 Charts / Images  
#/   3.3.1 Income Education Level Chart
#/   3.3.2 Income Career Entrants Chart
#/   3.3.3 Income Development Chart
#/   3.3.4 Interactive General Data Chart  
#/   3.3.5 Gender Chart
#/   3.3.6 Education Level Chart
#/   3.3.7 Responsibility Chart
#/   3.3.8 Experience Chart
#/   3.3.9 Company Size Chart


#/ Impressum


#/  ------0. Import of libraries ------

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from PIL import Image
from bs4 import BeautifulSoup

#/ -------1. Webpage title -------

st.set_page_config(page_title="Income-Profession-Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")


#/ -------2. Streamlit Back End Elements------


            
#/ 2.2 Configuration of Data

#/  2.2.1 Creating Dataframes (DFs)

#/   2.2.1.1 DFs for pie chart income-education level
data_income_education_level = {'Education': ['Doctorate', '2nd State Exam', 'Diploma University', 'Diploma University of Applied Science', 'Master', 'Magister', 'Master Vocation', 'Bachelor', 'Apprentice'],
                               'Income': [83668, 81580, 78687, 77696, 61906, 61876, 55222, 54210, 43471]}
df_income_education_level = pd.DataFrame(data_income_education_level)

#/   2.2.1.2 DFs from xlsx for Career Entrant by Degree
df_career_entrant = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Allgemein',
    skiprows=112,
    usecols='D,H',
    nrows=17
)

#/   2.2.1.3 DFs from xlsx for income development
df_income_dev = pd.read_excel(
    io='Income Development in Germany Until 2021.xlsx',
    engine='openpyxl',
    sheet_name='Tabellenblatt1',
    skiprows=2,
    usecols='A:B',
    nrows=1000
)

#/   2.2.1.4 DFs from xlsx for interactive chart General
df_interactive_general = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Allgemein',
    skiprows=20,
    usecols='B:I',
    nrows=40
)

#/   2.2.1.5 DFs for Gender
df_gender = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Zusammenfassung',
    skiprows=2,
    usecols='A:C',
    nrows=20
)

#/   2.2.1.6 DFs for Education Level
df_education_level = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Zusammenfassung',
    skiprows=2,
    usecols='E:G',
    nrows=16
)

#/   2.2.1.7 DFs for Responsibility
df_responsibility = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Zusammenfassung',
    skiprows=2,
    usecols='I:K',
    nrows=20
)

#/   2.2.1.8 DFs for Experience
df_x = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Zusammenfassung',
    skiprows=2,
    usecols='M:O',
    nrows=51
)

#/   2.2.1.9 DFs  for Company Size
df_size = pd.read_excel(
    io='Data Income Dashboard.xlsx',
    engine='openpyxl',
    sheet_name='Zusammenfassung',
    skiprows=2,
    usecols='Q:S',
    nrows=40
)



#/ ------- 3. Streamlit Front End Elements ------

#/ 3.1 Page Layout:

#/  3.1.2 Centre title
title = '<p style="font-family:Sans Serif; color:White; font-size: 200px; text-align:center">Income Dashboard</p>'
st.markdown(title, unsafe_allow_html=True)

#/  3.1.3 Searchbar title
st.markdown("<h1> Search Bar </h1>", unsafe_allow_html=True)

#/ 2.1 Web Scraping with Search Bar

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword, e.g. IT, Medizin, Finanzen")
    search = st.form_submit_button("Search")
    if search:
        col1, col2 = st.columns(2)
        page = requests.get(f"https://www.gehalt.de/einkommen/search?searchtext={keyword}")
        soup = BeautifulSoup(page.text, "html.parser")

        income_min = soup.find_all("div", class_="gehaltMin headline-large")
        for income_min1 in income_min:
            span_min = income_min1.find_next('span').find_next("span")

        income_max = soup.find_all("div", class_="gehaltMax headline-large")
        for income_max1 in income_max:
            span_max = income_max1.find_next('span').find_next("span")

        with col1:
            st.markdown("Minimum Expected Income per Year: ")
            st.markdown(span_min.string)
        with col2:
            st.markdown("Maximum Expected Income per Year: ")
            st.markdown(span_max.string)


#/  3.1.4 Background image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4kwallpapers.com/images/walls/thumbs_3t/8995.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


#/  3.2 Sidebars
#/   3.2.1 Sidebar General Data
st.sidebar.header("Customize Your Filter Categories")
st.sidebar.header("Filter for General Data")
location = st.sidebar.multiselect(
    "Select The Location:",
    options=df_interactive_general["Location"].unique(), key = "1"
    #default=df_interactive_general["Location"].unique()
)
df_interactive_selection = df_interactive_general.query(
    "Location == @location"
)

#/   3.2.2 Sidebar Gender
st.sidebar.header("Filter for Gender Data")
industry_gender = st.sidebar.multiselect(
    "Select The Industry:",
    options=df_gender["Industry_G"].unique(), key = "2"
    #default=df_gender["Industry"].unique()
)
df_gender_selection = df_gender.query("Industry_G == @industry_gender")

#/   3.2.3 Sidebar Education Level
st.sidebar.header("Filter for Education Level Data")
industry_ed = st.sidebar.multiselect(
    "Select The Industry:",
    options=df_education_level["Industry_E"].unique(), key = "3"
    #default=df_gender["Industry"].unique()
)
df_education_level_selection = df_education_level.query("Industry_E == @industry_ed")

#/   3.2.4 Sidebar Responsibility
st.sidebar.header("Filter for Responsibility Data")
industry_resp = st.sidebar.multiselect(
    "Select The Industry:",
    options=df_responsibility["Industry_R"].unique(), key = "4"
    #default=df_gender["Industry"].unique()
)
df_responsibility_selection = df_responsibility.query("Industry_R == @industry_resp") 


#/   3.2.5 Sidebar Experience
st.sidebar.header("Filter for Experience Data")
industry_x = st.sidebar.multiselect(
    "Select The Industry:",
    options=df_x["Industry_X"].unique(), key = "5"
    #default=df_gender["Industry"].unique()
)
df_x_selection = df_x.query("Industry_X == @industry_x")


#/   3.2.6 Sidebar Company Size
st.sidebar.header("Filter for Company Size Data")
industry_size = st.sidebar.multiselect(
    "Select The Industry:",
    options=df_size["Industry_S"].unique(), key = "6"
    #default=df_gender["Industry"].unique()
)
df_size_selection = df_size.query("Industry_S == @industry_size")


#/  3.3 Charts / Images

#/    3.3.1 Income Education Level Chart
fig_income_education_level = px.bar(
    df_income_education_level,
    x="Income",
    y="Education",
    orientation="h",
    color="Education",
    title="<b> Income in Relation to Education Level </b>",
    text_auto=True
).update_yaxes(categoryorder="total ascending")
fig_income_education_level.update_layout(font_size=15, width=600)

#/    3.3.2 Income Career Entrants Chart
fig_career_entrant = px.bar(
    df_career_entrant,
    x="Career Entrant",
    y="Degree",
    orientation="h",
    color="Degree",
    title="<b> Career Entrant Income in Relation to Degree </b>",
    text_auto=True
).update_yaxes(categoryorder="total ascending")
fig_career_entrant.update_layout(font_size=17, width=600)

st.markdown("<h1 style='text-align:center'><b> Your Choice Matters </b></h1>", unsafe_allow_html=True)

# --> Visualizing Income Education Level and Career Entrant Charts
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_income_education_level)
with col2:
    st.plotly_chart(fig_career_entrant)


#/    3.3.3 Income Development Chart
fig_income_dev = px.line(
    df_income_dev,
    x="Income Development in Germany Until 2021",
    y="In Percentage Points",
    category_orders={},
    title="<b> Income Development in Germany</b>",
    markers=True,
    template="plotly_white"
)
fig_income_dev.update_layout(width=1200, font_size=20)
st.plotly_chart(fig_income_dev)


#/    3.3.4 Interactive General Data Chart  
fig_interactive = px.bar(
    df_interactive_selection,
    title="General Income in Germany For Different Locations",
    x="Location",
    y=["Responsibilities", "No Responsibilities", "Academic", "Non Academic", "Academic Entrant", "Non Academic Entrant", "Mean"],
    orientation="v",
    barmode='group',
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_interactive.update_layout(bargap=0.2, font_size=20, width=1200)

st.title(":bar_chart: Interactive Charts")

st.plotly_chart(fig_interactive)


#/    3.3.5 Gender Chart
fig_gender = px.bar(
    df_gender_selection,
    title="Gender Pay Gap In Selected Industry",
    x="Industry_G",
    y="Income_G",
    labels={'Industry_G': 'Selected Industry', 'Income_G': 'Income By Gender'},
    barmode="group",
    color="Gender",
    orientation="v",
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_gender.update_layout(bargap=0.2, height=400)
fig_gender.update_layout(font_size=20)

fig_gender2 = px.line(
    df_gender_selection,
    x='Industry_G',
    y="Income_G",
    color="Gender",
    labels={'Industry_G': 'Selected Industry', 'Income_G': 'Income By Gender'},
    text='Income_G',
    markers=True,
)
fig_gender2.update_layout(
    yaxis={"dtick": 5000, "range": [30000, 70000]}, height=300,
    xaxis=(dict(showgrid=False))
)
fig_gender2.update_layout(font_size=15)

image1, gender, image2 = st.columns([0.2, 0.5, 0.1])
with image1:
    image_man = Image.open('Mann.png')
    st.image(image_man,caption=None, width=275)
with gender:
    st.plotly_chart(fig_gender)
    st.plotly_chart(fig_gender2)
with image2:
    image_woman = Image.open('Frau.png')
    st.image(image_woman, caption=None, width=245)


#/    3.3.6 Education Level Chart
fig_education_level = px.bar(
    df_education_level_selection,
    title="Income In Relation To Education Level",
    x="Industry_E",
    y="Income_E",
    labels={'Industry_E': 'Selected Industry', 'Income_E': 'Income By Education Level'},
    barmode="group",
    color="Education Level",
    orientation="v",
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_education_level.update_layout(bargap=0.2, width=600)
fig_education_level.update_layout(font_size=20)

#/    3.3.7 Responsibility Chart
fig_responsibility = px.bar(
    df_responsibility_selection,
    title="<B> Income in Relation to Responsibility",
    x="Industry_R",
    y="Income_R",
    labels={'Industry_R': 'Selected Industry', 'Income_R': 'Income By Responsibility'},
    barmode="group",
    color="Responsibility",
    orientation="v",
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_responsibility.update_layout(bargap=0.2, width=600)
fig_responsibility.update_layout(font_size=20)

 
#/    3.3.8 Experience Chart
fig_x = px.bar(
    df_x_selection,
    title="<b>Income In Relation to Experience</b>",
    x="Industry_X",
    y="Income_X",
    labels={'Industry_X': 'Selected Industry', 'Income_X': 'Income By Experience'},
    barmode="group",
    color="Experience",
    orientation="v",
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_x.update_layout(bargap=0.2, width=600)
fig_x.update_layout(font_size=20)


#/    3.3.9 Company Size Chart
fig_size = px.bar(
    df_size_selection,
    title='<b>Income In Relation to Company Size</b>',
    x="Industry_S",
    y="Income_S",
    labels={'Industry_S': 'Selected Industry', 'Income_S': 'Income By Company Size'},
    barmode="group",
    color="Size",
    orientation="v",
    text_auto=True
).update_xaxes(categoryorder="total descending")
fig_size.update_layout(bargap=0.2, width=600)
fig_size.update_layout(font_size=20)

#/ --> Visualizing Plots for education, responsibility, experience, size 
education, responsibility = st.columns(2)
with education:
    st.plotly_chart(fig_education_level)
with responsibility:
    st.plotly_chart(fig_responsibility)

experience, size = st.columns(2)
with experience:
    st.plotly_chart(fig_x)
with size:
    st.plotly_chart(fig_size)

    
    
# -------- Impressum --------
founders = '<p style="font-family:Sans Serif; color:White; font-size: 100px; text-align:center">Created by</p>'
st.markdown(founders, unsafe_allow_html=True)
image_Iqbal, image_Viet = st.columns(2)
with image_Iqbal:
    name_Iqbal = '<p style="font-family:Sans Serif; color:White; font-size: 50px; text-align:center">Iqbal Adel</p>'
    st.markdown(name_Iqbal, unsafe_allow_html=True)
with image_Viet:
    name_Viet = '<p style="font-family:Sans Serif; color:White; font-size: 50px; text-align:center">Huan Viet Ta</p>'
    st.markdown(name_Viet, unsafe_allow_html=True)



