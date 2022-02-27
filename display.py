import streamlit as st
from movingAverage import MovingAverage

st.title("Moving Average Stock Calculator")
st.subheader("Stock Selection")

stock_list = ["swppx","msft","aapl"]

input = st.selectbox(
     'Select Stock/Index Fund to be Analyzed', stock_list)
st.write('You selected:', input)


# print(control_data.head())
# print(control_data.head())
st.subheader("Input Selection")
range_data = int(st.slider("Date Range", 100, 5000, 200))
average_value_1 = int(st.slider("Moving average value One", 1, 200, 50))
average_value_2 = int(st.slider("Moving average value Two", 1, 200, 100))

stock = MovingAverage(input, range_data)
control_data = stock.control()
average_data_1 = stock.average_moving(average_value_1)
average_data_2 = stock.average_moving(average_value_2)

print(control_data.head())
print(average_value_1)
print(average_data_1.head())
print(average_value_2)
print(average_data_2.head())

# if st.checkbox("Show Raw Data"):
#     st.subheader("Control Data")
#     st.write(control_data)

control_data["average data 1"] = average_data_1
control_data["average data 2"] = average_data_2

st.subheader(f"{input.upper()} Data Plotted")
st.line_chart(control_data)

if st.checkbox("Show Raw Data"):
    st.subheader(f"Raw Data for {input} days")
    st.write(control_data)


