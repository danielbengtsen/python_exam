import pandas as pd
import matplotlib.pyplot as plt

def retrieve_data(data_link_or_path, save_to_file=False, save_path=""):
    """
    Will retrieve csv data from a local path or download url.
    "data_link_or_path" is the URL to download from or the path to the local file to read from.
    "save_to_file" is set to false per default in order to read from a local file. If set to true, save_path should be set aswell.
    "save_path" is the path to save and store the downloaded csv-file.
    """
    data = pd.read_csv(data_link_or_path, delimiter=",")
    
    if(save_to_file):
        data.to_csv(save_path)
        
    return data

def plot_data(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title):
    mod_data = data[[label_column_name, x_column_name, y_column_name]]

    plt.figure(figsize=(12, 10), dpi=80)

    for label in labels:
        data = mod_data.loc[mod_data[label_column_name] == label]
        x_axis = data[x_column_name]
        y_axis = data[y_column_name]
        plt.plot(x_axis, y_axis)
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(labels)
    plt.show()


def plot_data2(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title, subplot_amount=0):
    mod_data = data[[label_column_name, x_column_name, y_column_name]]

    plt.figure(figsize=(12, 10), dpi=80)

    for label in labels:
        data = mod_data.loc[mod_data[label_column_name] == label]
        x_axis = data[x_column_name]
        y_axis = data[y_column_name]
        plt.plot(x_axis, y_axis)
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(labels)
    plt.show()