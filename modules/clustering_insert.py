from sklearn import preprocessing
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd
import numpy as np 

# Normalization
def doNormalization(meanshift_except_major):
    scaler = preprocessing.MinMaxScaler()
    names = meanshift_except_major.columns
    d = scaler.fit_transform(meanshift_except_major)
    return pd.DataFrame(d, columns=names)

#We will add a new column in dataset which shows the cluster the data of a particular row belongs to.
def addClusterGroupToDataSet(meanshift_data_scaled, labels):
    meanshift_data_scaled['cluster_group'] = np.nan
    data_length=len(meanshift_data_scaled)
    for i in range(data_length):
        meanshift_data_scaled.iloc[i,meanshift_data_scaled.columns.get_loc('cluster_group')] = labels[i]
    return meanshift_data_scaled

def makeAnalyzer(meanshift_data_scaled, calculated_bandwidth):
    #We found the bandwith using the estimate_bandiwth function mentioned in below cell.
    analyzer = MeanShift(bandwidth=calculated_bandwidth) #We will provide only bandwith in hyperparameter . The smaller values of bandwith result in tall
    #skinny kernels & larger values result in short fat kernels.
    analyzer.fit(meanshift_data_scaled)
    return analyzer
    

def makeLabelsFromAnalyzer(analyzer):
    labels = analyzer.labels_
    return labels

def calculateAmountOfClusters(analyzer):
    labels_data = analyzer.labels_
    cluster_centers = analyzer.cluster_centers_

    labels_unique = np.unique(labels_data)
    n_clusters = len(labels_unique)
    print('Number of estimated clusters : {}'.format(n_clusters))
    
def createGrouping(scaled_chosen_dataset):
    #Grouping entries by Cluster
    meanshift_data_scaled_clusters = scaled_chosen_dataset.copy()
    meanshift_data_scaled_clusters = scaled_chosen_dataset.groupby(['cluster_group']).mean()
    #Count of entries in each cluster
    meanshift_data_scaled_clusters['Counts'] = pd.Series(scaled_chosen_dataset.groupby(['cluster_group']).size())
    return meanshift_data_scaled_clusters