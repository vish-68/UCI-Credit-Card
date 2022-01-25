# -*- coding: utf-8 -*-
"""
Created on Thr Sep 23 15:14:04 2021

@author: VISHAL UPARE
"""
# %%

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

# %%

app = Flask(__name__)

# %%

model = pickle.load(open("UCI_EXT_model.pkl", "rb"))

# %%
sex = {1: "MALE", 2: "FEMALE"}

edu = {1: "Graduate School", 2: "University", 3: "High School",
       4: "Others", 0: "Other", 5: "Unknown", 6: "Unknown"}

marr = {1: "Married", 2: "Single", 3: "Other", 4: "Others"}

pay0 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}

pay2 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}

pay3 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}

pay4 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}

pay5 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}

pay6 = {-2: "No Consumption", -1: "Pay duly", 1: "Payment delay for one month",
        2: "Payment delay for two month", 3: "Payment delay for three month", 4: "Payment delay for four month",
        5: "Payment delay for five month", 6: "Payment delay for six month", 7: "Payment delay for seven month",
        8: "Payment delay for eight month", 0: "Others"}


# %%


@app.route("/")
def home():
    return render_template("uci.html")
# %%



@app.route("/UCI", methods=['POST'])
def UCI():
    # int_features = [float(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    data = request.form["names"]
    data1 = request.form["LIMIT_BAL"]
    data2 = request.form["SEX"]
    data3 = request.form["EDUCATION"]
    data4 = request.form["MARRIAGE"]
    data5 = request.form["AGE"]
    data6 = request.form["PAY_0"]
    data7 = request.form["PAY_2"]
    data8 = request.form["PAY_3"]
    data9 = request.form["PAY_4"]
    data10 = request.form["PAY_5"]
    data11 = request.form["PAY_6"]
    data12 = request.form["BILL_AMT1"]
    data13 = request.form["BILL_AMT2"]
    data14 = request.form["BILL_AMT3"]
    data15 = request.form["BILL_AMT4"]
    data16 = request.form["BILL_AMT5"]
    data17 = request.form["BILL_AMT6"]
    data18 = request.form["PAY_AMT1"]
    data19 = request.form["PAY_AMT2"]
    data20 = request.form["PAY_AMT3"]
    data21 = request.form["PAY_AMT4"]
    data22 = request.form["PAY_AMT5"]
    data23 = request.form["PAY_AMT6"]

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11,
                   data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23]])
    prediction = model.predict(arr)

    # create original output dict
    output_dict1 = dict()
    output_dict1['NAME'] = data
    output_dict1['AGE'] = data5
    output_dict1['SEX'] = sex[int(data2)]
    output_dict1['EDUCATION'] = edu[int(data3)]
    output_dict1['MARRIAGE'] = marr[int(data4)]
    output_dict1['LIMIT_BAL'] = data1

    output_dict2 = dict()
    output_dict2['In September'] = pay0[int(data6)]
    output_dict2['In August'] = pay2[int(data7)]
    output_dict2['In July'] = pay3[int(data8)]
    output_dict2['In June'] = pay4[int(data9)]
    output_dict2['In May'] = pay5[int(data10)]
    output_dict2['In April'] = pay6[int(data11)]

    output_dict3 = dict()
    output_dict3['In September'] = data12
    output_dict3['In August'] = data13
    output_dict3['In July'] = data14
    output_dict3['In June'] = data15
    output_dict3['In May'] = data16
    output_dict3['In April'] = data17

    output_dict4 = dict()
    output_dict4['In September'] = data18
    output_dict4['In August'] = data19
    output_dict4['In July'] = data20
    output_dict4['In June'] = data21
    output_dict4['In May'] = data22
    output_dict4['In April'] = data23

    return render_template("uci_result.html", original_input1=output_dict1, original_input2=output_dict2, original_input3=output_dict3, original_input4=output_dict4, data=prediction)
# %%


if __name__ == '__main__':
    app.run(debug=True)

# %%
