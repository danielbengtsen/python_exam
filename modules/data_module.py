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

def plot_data(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title, suptitle, subplot_amount=0, y_range=[]):
    
    if(subplot_amount == 0): 
        mod_data = data[[label_column_name, x_column_name, y_column_name]]

        plt.figure(figsize=(20, 10))

        for label in labels:
            data = mod_data.loc[mod_data[label_column_name] == label]
            x_axis = data[x_column_name]
            y_axis = data[y_column_name]
            plt.plot(x_axis, y_axis)

        if(len(y_range) == 2):
                x1,x2,y1,y2 = plt.axis()  
                plt.axis((x1,x2,y_range[0],y_range[1]))    
        plt.title(suptitle[0] + "\n\n" + title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(labels)
        plt.show()
    else:
        for subplot in range(subplot_amount):
            tmp_data = data

            mod_data = tmp_data[[label_column_name[subplot], x_column_name[subplot], y_column_name[subplot]]].copy(deep=True)

            plt.figure(figsize=(20, (10*subplot_amount)))

            plt.subplot(subplot_amount, 1, subplot+1)
            for label in labels:
                tmp_data = mod_data.loc[mod_data[label_column_name[subplot]] == label]
                x_axis = tmp_data[x_column_name[subplot]]
                y_axis = tmp_data[y_column_name[subplot]]
                plt.plot(x_axis, y_axis)

            if(len(y_range) == 2):
                x1,x2,y1,y2 = plt.axis()  
                plt.axis((x1,x2,y_range[0],y_range[1]))
            plt.title(suptitle[subplot] + "\n\n" + title[subplot])
            plt.xlabel(xlabel[subplot])
            plt.ylabel(ylabel[subplot])
            plt.legend(labels)

        plt.show()


def bar_data(data, label_column_name, x_column_name, y_column_name, xlabel, ylabel, labels, title, suptitle, subplot_amount=0, y_range=[]):
    colour_arr = ["silver", "peru", "darkorange", "springgreen", "lightseagreen", "darkorchid", "fuchsia", "navy"]

    if(subplot_amount == 0):
        mod_data = data[[label_column_name, x_column_name, y_column_name]]

        loop_count = 0

        plt.figure(figsize=[20, 10])
        b_width = 0.1
        move_width = 0
        move_up = b_width
        center_x = b_width * (len(labels)) / 2

        sorted_labels = sort_labels_by_data(labels, mod_data, x_column_name, y_column_name, label_column_name)

        for label in labels:
            data = mod_data.loc[mod_data[label_column_name] == label]
            first_row = data.copy().iloc[0]
            pos_num = sorted_labels[first_row[x_column_name]].index(first_row[label_column_name]) + 1
            x_axis = data[x_column_name]
            y_axis = data[y_column_name]
            X = np.arange(len(x_axis))
            plt.bar(X+(b_width*pos_num), y_axis, width=b_width, align='center', color=colour_arr[loop_count], edgecolor="black")
            plt.xticks(X+center_x, x_axis, rotation=65)
            move_width += move_up
            loop_count += 1

        if(len(y_range) == 2):
            x1,x2,y1,y2 = plt.axis()  
            plt.axis((x1,x2,y_range[0],y_range[1]))    
        plt.title(suptitle[0] + "\n\n" + title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(labels)
        plt.show()
    else:
        for subplot in range(subplot_amount):
            tmp_data = data
            
            mod_data = data[[label_column_name[subplot], x_column_name[subplot], y_column_name[subplot]]].copy(deep=True)

            plt.figure(figsize=[20, (10*subplot_amount)])
            b_width = 0.1
            move_width = 0
            move_up = b_width
            center_x = b_width * (len(labels)) / 2

            sorted_labels = sort_labels_by_data(labels, mod_data, x_column_name[subplot], y_column_name[subplot], label_column_name[subplot])

            plt.subplot(subplot_amount, 1, subplot+1)

            loop_count = 0

            for label in labels:
                tmp_data = mod_data.loc[mod_data[label_column_name[subplot]] == label]
                first_row = tmp_data.copy().iloc[0]
                pos_num = sorted_labels[first_row[x_column_name[subplot]]].index(first_row[label_column_name[subplot]]) + 1
                x_axis = tmp_data[x_column_name[subplot]]
                y_axis = tmp_data[y_column_name[subplot]]
                X = np.arange(len(x_axis))
                plt.bar(X+(b_width*pos_num), y_axis, width=b_width, align='center', color=colour_arr[loop_count], edgecolor="black")
                plt.xticks(X+center_x, x_axis, rotation=65)
                move_width += move_up
                loop_count += 1

            if(len(y_range) == 2):
                x1,x2,y1,y2 = plt.axis()  
                plt.axis((x1,x2,y_range[0],y_range[1]))    
            plt.title(suptitle[subplot] + "\n\n" + title[subplot])
            plt.xlabel(xlabel[subplot])
            plt.ylabel(ylabel[subplot])
            plt.legend(labels)

        plt.show()

def sort_labels_by_data(labels, data, sort_x, sort_y, sort_label):
    # Remove all rows where sort_label is not in labels
    data = data[data[sort_label].isin(labels)]
    data = data.sort_values(by=[sort_y, sort_label], ascending=True)
    data_unique_x = set(data[sort_x])
    data_unique_x = list(data_unique_x)

    for index in range(len(data_unique_x)):
        data_unique_x[index] = int(data_unique_x[index])
    
    data_unique_x.sort()
    
    label_array = {}

    for x in data_unique_x:
        label_array[str(x)] = list(data[data[sort_x] == str(x)].sort_values(by=sort_y, ascending=True)[sort_label])

    return label_array

        
def create_percentage_column(data, p_of_column, p_total_column):
    new_data = (data[p_of_column] / data[p_total_column])*100
    return new_data