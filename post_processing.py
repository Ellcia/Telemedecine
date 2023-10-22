import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def post_processing(name,data):
    #data = pd.read_csv('datagret.csv')
    
    rsp = data["RESP_ABDOMEN"]
    
    signals, info = nk.rsp_process(rsp, sampling_rate=50, report="text")
    fig = nk.rsp_plot(signals, info) 
    plt.gcf().set_size_inches(15, 7.5)
    plt.savefig("static/"+name+".png")
    
    
#post_processing()