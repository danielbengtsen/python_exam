import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pdb

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

def plot_data(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title, subplot_amount=0):
    
    if(subplot_amount == 0): 
        mod_data = data[[label_column_name, x_column_name, y_column_name]]

        plt.figure(figsize=(16, 10))

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
    else:
        for subplot in range(subplot_amount):
            tmp_data = data

            mod_data = tmp_data[[label_column_name[subplot], x_column_name[subplot], y_column_name[subplot]]].copy(deep=True)

            plt.figure(figsize=(16, (10*subplot_amount)))

            plt.subplot(subplot_amount, 1, subplot+1)
            for label in labels:
                tmp_data = mod_data.loc[mod_data[label_column_name[subplot]] == label]
                x_axis = tmp_data[x_column_name[subplot]]
                y_axis = tmp_data[y_column_name[subplot]]
                plt.plot(x_axis, y_axis)

            plt.title(title[subplot])
            plt.xlabel(xlabel[subplot])
            plt.ylabel(ylabel[subplot])
            plt.legend(labels)

        plt.show()


def bar_data(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title, subplot_amount=0):
    if(subplot_amount == 0):
        mod_data = data[[label_column_name, x_column_name, y_column_name]]

        plt.figure(figsize=[16, 10])
        b_width = 0.1
        move_width = 0
        move_up = b_width
        center_x = b_width * (len(labels)) / 2

        for label in labels:
            data = mod_data.loc[mod_data[label_column_name] == label]
            x_axis = data[x_column_name]
            y_axis = data[y_column_name]
            X = np.arange(len(x_axis))
            plt.bar(X+move_width, y_axis, width=b_width, align='center')
            plt.xticks(X+center_x, x_axis, rotation=65)
            move_width += move_up
            
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(labels)
        plt.show()
    else:
        for subplot in range(subplot_amount):
            tmp_data = data
            
            mod_data = data[[label_column_name[subplot], x_column_name[subplot], y_column_name[subplot]]].copy(deep=True)

            plt.figure(figsize=[16, (10*subplot_amount)])
            b_width = 0.1
            move_width = 0
            move_up = b_width
            center_x = b_width * (len(labels)) / 2

            plt.subplot(subplot_amount, 1, subplot+1)
            for label in labels:
                tmp_data = mod_data.loc[mod_data[label_column_name[subplot]] == label]
                x_axis = tmp_data[x_column_name[subplot]]
                y_axis = tmp_data[y_column_name[subplot]]
                X = np.arange(len(x_axis))
                plt.bar(X+move_width, y_axis, width=b_width, align='center')
                plt.xticks(X+center_x, x_axis, rotation=65)
                move_width += move_up
                
            plt.title(title[subplot])
            plt.xlabel(xlabel[subplot])
            plt.ylabel(ylabel[subplot])
            plt.legend(labels)

        plt.show()