import streamlit as st
import datetime
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.express as px
import cufflinks as cf
import plotly.graph_objects as go

from plotly.offline import download_plotlyjs, init_notebook_mode,plot, iplot
init_notebook_mode(connected= True)
cf.go_offline()
import plotly.express as px

import pickle as pk

dataframe = pd.read_csv("data.csv")
st.sidebar.markdown("Ace Inc")
st.sidebar.markdown('<div style="text-align: center;">Marketing & Promo Analysis</div>', unsafe_allow_html=True)

from PIL import Image
image= Image.open('linegraph.png')
st.sidebar.image(image, caption = " ", width=300)


choice = st.sidebar.selectbox('Make a Choice', ['Select','Analysis','Prediction'])
plottype = ['Select','Distribution','Relationships','Comparison']
variables = ['Select','View Relationship','Categorise Relationships']


num = ['Marketing Spend','Visitors','Revenue','Gain']
cat =['Promo','Year','Month','Day_Name']
dat= ['Date', 'Week_ID']



def hist():
    #x_axis_val = col1.selectbox('Select the Variable for distribution plot', options= num
    plothi = px.histogram(dataframe, x=x_axis_val, marginal = 'rug')
    st.plotly_chart(plothi, use_container_width=True, width = 1500)

def boxpl():
    plotbo = px.box(dataframe,x=x_axis_val)
    st.plotly_chart(plotbo,use_container_width=True, width = 1000)

    
def piepl():
    colors={'Promotion Blue':'Blue','Promotion Red':'Red','No Promo':'grey'}
    plotpie = px.pie(dataframe,names = x_axis_val,color= x_axis_val,color_discrete_map=colors,
             title = f" Distribution of {x_axis_val}")
    st.plotly_chart(plotpie, use_container_width=True, width = 1000)
        
        
def hist_cat():
    plotbr = px.histogram(dataframe, x = x_axis_val, title =(f" A Distiribution of {x_axis_val} by no of Occurences") )
    st.plotly_chart(plotbr, use_container_width=True, width = 1000) 
    
def scat():
    plotscat =px.scatter(data_frame=dataframe,x=x_axis_val,y=y_axis_val,title =f" Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(plotscat, use_container_width=True, width = 1000)
    
def num_cat_avg():
    pltnumcatavg = px.histogram(dataframe, x=y_axis_val , y= x_axis_val,histfunc='avg',text_auto=True, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltnumcatavg, use_container_width=True, width = 1000)
    
def num_cat_sum():
    pltnumcatsum = px.histogram(dataframe, x= y_axis_val , y=x_axis_val,histfunc='sum',text_auto=True, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltnumcatsum, use_container_width=True, width = 1000)
    
def cat_num_avg():
    pltcatnumavg = px.histogram(dataframe, x=x_axis_val , y= y_axis_val,histfunc='avg',text_auto=True, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltcatnumavg, use_container_width=True, width = 1000)
    
def cat_num_sum():
    pltcatnumsum = px.histogram(dataframe, x=x_axis_val , y= y_axis_val,histfunc='sum',text_auto=True, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltcatnumsum, use_container_width=True, width = 1000)
    
def num_dat():
    pltnumdat = px.line(dataframe, x=y_axis_val,y=x_axis_val, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltnumdat, use_container_width=True, width = 1000)
    
def dat_num():
    pltdatnum = px.line(dataframe, x=x_axis_val,y=y_axis_val, title=f"Relationship between {x_axis_val} and {y_axis_val}")
    st.plotly_chart(pltdatnum, use_container_width=True, width = 1000)
    
if choice == 'Analysis':
    plotselect = st.sidebar.selectbox('Select Visualization type', plottype)
    
    if plotselect == 'Distribution':
        st.sidebar.markdown('<div style="text-align: center;"> A choice of Distribution would show the spread and distirbution of the chosen Variable in the form of Histograms or Bar Charts or Pie charts</div>', unsafe_allow_html=True)
        #viz = st.sidebar.selectbox('Choose Predictor', variables1)
        col1, col2 = st.columns(2)
        with col1:
            x_axis_val = st.selectbox('Select the Variable for distribution plot', options= dataframe.columns)
        #for x in x_axis_val:
               
        st.write= (f" Distribution of {x_axis_val}")
        if x_axis_val in num:
            with col2:
                pltype= st.radio('',['Histogram','Box Plot'])
            if pltype == 'Histogram':
                hist()
            elif pltype == 'Box Plot':
                boxpl()
        elif x_axis_val in cat:
            with col2:
                pltype = st.radio('', ['Bar Chart','Pie Chart'])
            if pltype == 'Bar Chart':
                hist_cat()
            elif pltype == 'Pie Chart':
                piepl()
            
        else:
            st.error(f" Selected value cannot be represented in a distribution graph. ")
            
    elif plotselect == 'Relationships':
        st.sidebar.markdown('<div style="text-align: center;"> A choice of Relationship can be used to see the relationship between the chosen Variables in the form of Histograms or Line charts or Pie charts</div>', unsafe_allow_html=True)
        col1, col2,col3 = st.columns(3)
        with col1:
            x_axis_val = st.selectbox('Select the Variable 1 for Relationship plot', options= dataframe.columns)
        #for x in x_axis_val:
        
        with col2:
            y_axis_val = st.selectbox('Select the Variable 2 for Relationship plot', options= dataframe.columns)
    
        st.write= (f" Distribution of {x_axis_val}")
        if x_axis_val in num:
            if y_axis_val in num:
                scat()
            elif y_axis_val in cat:
                with col3:
                    rltype= st.radio('',['By Average','By Total'])
                if rltype=='By Average':
                    num_cat_avg()
                elif rltype == 'By Total':
                    num_cat_sum()
            elif y_axis_val in dat:
                num_dat()
        elif x_axis_val in cat:
            if y_axis_val in num:
                with col3:
                    rltype= st.radio('',['By Average','By Total'])
                if rltype=='By Average':
                    cat_num_avg()
                elif rltype == 'By Total':
                    cat_num_sum()
            elif y_axis_val in num:
                scat()
        elif x_axis_val in dat:
            if y_axis_val in num:
                dat_num()
            elif y_axis_val in cat:
                st.error(f" Selected values cannot be plotted. ")   
            
        else:
            st.error(f" Selected value cannot be represented in a plot ")
            
    elif plotselect == 'Comparison':
        st.info(" COMING SOON ")
        image= Image.open('coming soon.jpg')
        st.image(image, caption = " ", width=300)
    
    
    
elif choice == 'Prediction':
    Scaler = pk.load(open('scaler.pk1','rb'))
    Model = pk.load(open('RF_model.pk1','rb'))
    
    st.info("Kindly input the needed parameters Parameters")
    
    def user_predictors():
        
        col1,col2=st.columns(2)
        with col1:
            Marketing_Spend=st.number_input('Marketing Spend')
            Visitors= st.number_input('Visitors')
            Month = st.selectbox('Month',('January','February','March','April','May','June','July','August','September','October','November','December'))
            if Month == 'January':
                Month_no = 1
            elif Month == 'February':
                Month_no = 2
            elif Month == 'March':
                Month_no =3
            elif Month == 'April':
                Month_no =4
            elif Month == 'May':
                Month_no =5
            elif Month == 'June':
                Month_no =6
            elif Month == 'July':
                Month_no =7
            elif Month == 'August':
                Month_no =8
            elif Month == 'September':
                Month_no =9
            elif Month == 'October':
                Month_no =10
            elif Month == 'November':
                Month_no =11
            elif Month == 'December':
                Month_no =12
            
            
        with col2:
            Promo_type = st.selectbox('Promo Type',('No Promo','Promotion Blue','Promotion Red'))
            if Promo_type=='No Promo':
                no_promo = 1
                promo_blue = 0
                promo_red=0
            elif Promo_type =='Promotion Blue':
                no_promo =0
                promo_blue = 1
                promo_red=0
            elif Promo_type =='Promotion Red':
                no_promo =0
                promo_blue = 0
                promo_red=1
            
            
            week_id = st.slider('Slide to Select Week', min_value =0, max_value=156)
            
            day_name = st.selectbox('Day of the week',('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'))
            if day_name=='Monday':
                day_mon = 1
                day_tues=0
                day_wed=0
                day_thur=0
                day_fri=0
                day_sat=0
                day_sun=0
            elif day_name=='Tuesday':
                day_mon = 0
                day_tues=1
                day_wed=0
                day_thur=0
                day_fri=0
                day_sat=0
                day_sun=0
            elif day_name=='Wednesday':
                day_mon = 0
                day_tues=0
                day_wed=1
                day_thur=0
                day_fri=0
                day_sat=0
                day_sun=0
            elif day_name=='Thursday':
                day_mon = 0
                day_tues=0
                day_wed=0
                day_thur=1
                day_fri=0
                day_sat=0
                day_sun=0
            elif day_name=='Friday':
                day_mon = 0
                day_tues=0
                day_wed=0
                day_thur=0
                day_fri=1
                day_sat=0
                day_sun=0
            elif day_name=='Saturday':
                day_mon = 0
                day_tues=0
                day_wed=0
                day_thur=0
                day_fri=0
                day_sat=1
                day_sun=0
            elif day_name=='Sunday':
                day_mon = 0
                day_tues=0
                day_wed=0
                day_thur=0
                day_fri=0
                day_sat=0
                day_sun=1
                
                
        data = {'Marketing Spend':Marketing_Spend,
                'Visitors': Visitors,
                'Week_ID': week_id,
                'Month Number': Month_no,
                '0': no_promo,
                '1': promo_blue,
                '2': promo_red,
                '3': day_mon,
                '4': day_tues,
                '5':day_wed,
                '6': day_thur,
                '7': day_fri,
                '8': day_sat,
                '9': day_sun}
        features = pd.DataFrame(data, index=[0]) # index- 0 just tells the code exclude index keeping only values
        return features  # the whole function was created just to generate a dataframe.
                
                
            
    input_data = user_predictors()  
    scaled_input_data = Scaler.transform(input_data)
    
    if st.button('PREDICT'):
        y_out= Model.predict(scaled_input_data)
        #st.write(f" For the given values {input_df}   ")
        st.write("\n")
        st.success(f" The estimated Revenue to be generated given above indices would be : #{y_out} ")
            
        
