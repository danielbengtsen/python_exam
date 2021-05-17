import pandas as pd

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