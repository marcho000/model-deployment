import streamlit as st # type: ignore
import streamlit.components.v1 as stc # type: ignore

# Import modul ml_app.py
from ml_app import run_ml_app

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Employee Promotion Prediction App </h1>
		    <h4 style="color:white;text-align:center;">HR Team </h4>
		    </div>
            """

desc_temp = """
            ### Employee Promotion Prediction App
            This app will be used by the HR team to predict whether the employee get a promotion or not
            #### Data Source
            - https://raw.githubusercontent.com/densaiko/data_science_learning/main/dataset/Human%20Capital.csv
            #### App Content
            - Exploratory Data Analysis
            - Machine Learning Section
            """

def main():
    stc.html(html_temp)

    menu = ['Home', 'Machine Learning']
    #Mengambil pilihan tampilan
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home' :
        st.subheader('Welcome to Homepage')
    elif choice == 'Machine Learning' :
        #st.subheader('Welcome to Mechine Learning Prediction')
        run_ml_app()

if __name__=='__main__':
        main()