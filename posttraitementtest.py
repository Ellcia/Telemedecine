import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV en utilisant pandas
data = pd.read_csv('datagret.csv')


rsp = data["RESP_THORAX"]
nk.signal_plot(rsp, sampling_rate=50) # Visualize

# Clean signal
cleaned = nk.rsp_clean(rsp, sampling_rate=50)


# Extract peaks
df, peaks_dict = nk.rsp_peaks(cleaned) 
info = nk.rsp_fixpeaks(peaks_dict)
formatted = nk.signal_formatpeaks(info, desired_length=len(cleaned),peak_indices=info["RSP_Peaks"])
nk.signal_plot(pd.DataFrame({"RSP_Raw": rsp, "RSP_Clean": cleaned}), sampling_rate=50, subplots=True)

candidate_peaks = nk.events_plot(peaks_dict['RSP_Peaks'], cleaned)

fixed_peaks = nk.events_plot(info['RSP_Peaks'], cleaned)

# Extract rate
rsp_rate = nk.rsp_rate(cleaned, peaks_dict, sampling_rate=50)

# Visualize
nk.signal_plot(rsp_rate, sampling_rate=50)
plt.ylabel('Breaths Per Minute')

rrv = nk.rsp_rrv(rsp_rate, info, sampling_rate=50, show=True)
rrv