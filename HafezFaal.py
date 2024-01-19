import requests
import streamlit as st
import json


url = "https://hafez.p.rapidapi.com/fal"

headers = {
	"X-RapidAPI-Key": "74c8056312mshc695ab0f25ef756p1700a7jsnf47882bbfcab",
	"X-RapidAPI-Host": "hafez.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

x = response.text
j = json.loads(x)

if st.button('نیت کنید و فال بگیرید'):
    st.write(j['poem'])
    st.write('-------------------')
    st.write(j['text'])
    
