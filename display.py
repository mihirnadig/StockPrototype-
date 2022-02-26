import streamlit as st
from movingAverage import MovingAverage

st.title("Visualization of Data")
st.subheader("Control Data")



# print(control_data.head())
# print(control_data.head())
range_data = int(st.slider("Range", 100, 1000, 200))
average_value = int(st.slider("Average value", 1, 200, 50))

stock = MovingAverage("msft", range_data)
control_data = stock.control()
hello_data = stock.average(average_value)

control_data["average data"] = hello_data
print(control_data.head())



if st.checkbox("Show Raw Data"):
    st.subheader("Control Data")
    st.write(control_data)

st.subheader("Control Data Plotted")
st.line_chart(control_data)



