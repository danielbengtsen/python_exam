import sklearn
import sklearn.linear_model
import numpy as np 

# consider making it a class with an object, to retrieve variables better, etc. (like with the ~~ week3/week4 project)

# todo: consider making yearToExclude to a List, to only call this function once in shouldExcludeYears()
def excludeYear(data_for_prediction, yearToExclude):
    return (data_for_prediction['Year'] != yearToExclude)

def shouldExcludeYears(yes, data_for_prediction):
    if (yes):
        data_crisis_years_excluded = data_for_prediction[(data_for_prediction["Education.Major"] == 'Computer Science and Math') & excludeYear(data_for_prediction, 2001) & excludeYear(data_for_prediction, 2003) & excludeYear(data_for_prediction, 2006) & excludeYear(data_for_prediction, 2008)]
        return data_crisis_years_excluded
    else:
        data_crisis_years_included = data_for_prediction[(data_for_prediction["Education.Major"] == 'Computer Science and Math')]
        return data_crisis_years_included

def get_xs_reshape(dataset_for_prediction):
    xs = dataset_for_prediction['Demographics.Total']
    return np.array(xs).reshape(-1, 1)

def get_ys(dataset_for_prediction):
    return dataset_for_prediction['Salaries.Mean']

def createLinearReg(dataset_for_prediction, xs_reshape, ys):
    data_set_new = dataset_for_prediction[["Salaries.Mean", "Year", "Demographics.Total"]]
    data_set_new = dataset_for_prediction.set_index(dataset_for_prediction["Year"])[["Salaries.Mean", "Demographics.Total"]]
    data_set_new.plot()
    #print("dataset-new",data_set_new)
    
    # Reshape data for X
    model = createModel(xs_reshape, ys)
    model.coef_
    data_set_new.plot(x=0,y=1) # x= first column and y=second column in dataframe
    #data.plot.scatter(x = 1, y = 3)
    
def createModel(xs_reshape, ys):
    model = sklearn.linear_model.LinearRegression()
    model.fit(xs_reshape, ys)
    return model

def predictByModel(model, xs_reshape):
    predicted = model.predict(xs_reshape)
    demographics_total = model.predict([[2600000]])
    print('Increasing Demographics Total by 110379 results in a total salary of {}'.format(demographics_total[0]))