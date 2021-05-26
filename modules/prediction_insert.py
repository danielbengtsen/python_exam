import sklearn
import sklearn.linear_model
import numpy as np
import matplotlib.pyplot as plt

# consider making it a class with an object, to retrieve variables better, etc. (like with the ~~ week3/week4 project)

# todo: consider making yearToExclude to a List, to only call this function once in shouldExcludeYears()
def excludeYear(data_for_prediction, yearToExclude):
    return (data_for_prediction['Year'] != yearToExclude)

def shouldExcludeYears(yes, data_for_prediction, industry):
    if (yes):
        data_crisis_years_excluded = data_for_prediction[(data_for_prediction["Education.Major"] == industry) & excludeYear(data_for_prediction, 2001) & excludeYear(data_for_prediction, 2003) & excludeYear(data_for_prediction, 2006) & excludeYear(data_for_prediction, 2008)]
        return data_crisis_years_excluded
    else:
        data_crisis_years_included = data_for_prediction[(data_for_prediction["Education.Major"] == industry)]
        return data_crisis_years_included

def get_xs_reshape(dataset_for_prediction, column_name):
    xs = dataset_for_prediction[column_name]
    return np.array(xs).reshape(-1, 1)

def get_ys(dataset_for_prediction):
    return dataset_for_prediction['Salaries.Mean']

def createLinearReg(dataset_for_prediction, xs_reshape, ys, column_name):
    data_set_new = dataset_for_prediction[["Salaries.Mean", "Year", column_name]]
    data_set_new = dataset_for_prediction.set_index(dataset_for_prediction["Year"])[["Salaries.Mean", column_name]]
    data_set_new.plot()
    #print("dataset-new",data_set_new)
    
    # Reshape data for X
    model = createModel(xs_reshape, ys)
    model.coef_
    #data_set_new.plot(x=0,y=1) # x= first column and y=second column in dataframe
    data_set_new.plot.scatter(x = 0, y = 1)
    plt.plot([data_set_new['Demographics.Total'].min(), data_set_new['Demographics.Total'].max()], [data_set_new['Salaries.Mean'].min(), data_set_new['Salaries.Mean'].max()])
    #
    
def createModel(xs_reshape, ys):
    model = sklearn.linear_model.LinearRegression()
    model.fit(xs_reshape, ys)
    return model

def predictByModel(model, xs_reshape, variable_for_predict ):
    predicted = model.predict(xs_reshape)
    predict_number = model.predict([[variable_for_predict]])
    print('Increasing variabale for prediction to '+ str(variable_for_predict)+ ' results in a total salary of {}'.format(round(predict_number[0])))