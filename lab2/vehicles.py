import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 


"""
Create a function to get Date_Standard_Deviation, Lower and Upper.
"""
def bootstrap(statistic_func, iterations, data):
    samples = np.random.choice(data,replace = True, size = [iterations, len(data)])
    #print samples.shape
    data_std = data.std()
    vals = []
    for sample in samples:
        sta = statistic_func(sample)
        #print sta
        vals.append(sta)
    b = np.array(vals)
    #print b
    lower, upper = np.percentile(b, [2.5, 97.5])
    return data_std,lower, upper



if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    #print((df.columns))

    #get the list of Current Fleet.
    Current_Fleet_Data = df.values.T[0]
    #get the list of New Fleet.
    New_Fleet_Data = df.values.T[1]

    """
    Deleted all NAN values from the list of New_Fleet_Data and copied it into Formatted_New_Fleet_Data.
    
    """
    Formatted_New_Fleet_Data = []
    for i in range (0, len(New_Fleet_Data)):
        if (0 < New_Fleet_Data[i] < 100):
            Formatted_New_Fleet_Data.append(int(New_Fleet_Data[i]))
    #print(Formatted_New_Fleet_Data)
    #print(len(Formatted_New_Fleet_Data))


    """
    Moved some data from Current_Fleet_Data to Formatted_New_Fleet_Data().
    """
    n1 = len(Current_Fleet_Data)
    n2 = len(Formatted_New_Fleet_Data)
    n = (n1 - n2) / 2
    for i in range (0, int(n)):
        Formatted_New_Fleet_Data.append(int(Current_Fleet_Data[n1-i-1]))
    #print(len(Formatted_New_Fleet_Data))


    """
    Deleted some data copied into Formatted_New_Fleet_Data and copied it into Formatted_Current_Fleet_Data,
    keeping the data number of new fleet and current fleet equal.
    """
    Formatted_Current_Fleet_Data = []
    for i in range (0, len(Formatted_New_Fleet_Data)):
        Formatted_Current_Fleet_Data.append(int(Current_Fleet_Data[i]))
    #print(Formatted_Current_Fleet_Data)
    #print(len(Formatted_Current_Fleet_Data))


    """
    Added Day numbers to match Formatted_New_Fleet_Data and Formatted_Current_Fleet_Data.
    """
    New_Fleet_Data_Days = []
    Current_Fleet_Data_Days = []
    for i in range (0, len(Formatted_New_Fleet_Data)):
        New_Fleet_Data_Days.append(int(i))
        Current_Fleet_Data_Days.append(int(i))


    """
    Create two data frames for Formatted_New_Fleet_Data and Formatted_Current_Fleet_Data.
    """
    New_Fleet_Data_Frame_df = pd.DataFrame(np.array([New_Fleet_Data_Days, Formatted_New_Fleet_Data]).T, columns=['Day', 'New Fleet'])
    Current_Fleet_Data_Frame_df = pd.DataFrame(np.array([Current_Fleet_Data_Days,Formatted_Current_Fleet_Data]).T, columns = ['Day', 'Current Fleet'])
    #print(New_Fleet_Data_Frame_df)
    #print(Current_Fleet_Data_Frame_df)



    """
    Caculate the standard deviation of Current Fleet and New Fleet.
    """
    print("New Fleet")
    print((("std: %f") % (np.std(Formatted_New_Fleet_Data))))

    print()
    print("Current Fleet")
    print((("std: %f")%(np.std(Formatted_Current_Fleet_Data))))



    """
    drawing the graph of New_Fleet_Scaterplot with Days.
    """
    sns_plot = sns.lmplot(New_Fleet_Data_Frame_df.columns[0], New_Fleet_Data_Frame_df.columns[1], data=New_Fleet_Data_Frame_df, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("New_Fleet_scaterplot.png", bbox_inches='tight')
    sns_plot.savefig("New_Fleet_scaterplot.pdf", bbox_inches='tight')



    """
    drawing the graph of Current_Fleet_Scaterplot with Days.
    """
    sns_plot = sns.lmplot(Current_Fleet_Data_Frame_df.columns[0], Current_Fleet_Data_Frame_df.columns[1], data=Current_Fleet_Data_Frame_df, fit_reg=False)

    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)

    sns_plot.savefig("Current_Fleet_scaterplot.png",bbox_inches='tight')
    sns_plot.savefig("Current_Fleet_scaterplot.pdf",bbox_inches='tight')




    """
    Convert lists to Numpy format
    """
    Np_New_Fleet_Data = New_Fleet_Data_Frame_df.values.T[1]
    Np_Current_Fleet_Data = Current_Fleet_Data_Frame_df.values.T[1]



    """
    Draw the graphs of New_Fleet_histogram.
    """
    plt.clf()
    sns_plot2 = sns.distplot(Np_New_Fleet_Data, bins=100, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('New Fleet')
    axes.set_ylabel('Numbers')

    sns_plot2.savefig("New_Fleet_histogram.png",bbox_inches='tight')
    sns_plot2.savefig("New_Fleet_histogram.pdf",bbox_inches='tight')



    """
    Draw the graphs of Current_Fleet_histogram.
    """
    plt.clf()
    sns_plot2 = sns.distplot(Np_Current_Fleet_Data, bins=100, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('Current Fleet')
    axes.set_ylabel('Numbers')

    sns_plot2.savefig("Current_Fleet_histogram.png", bbox_inches='tight')
    sns_plot2.savefig("Current_Fleet_histogram.pdf", bbox_inches='tight')



    """
    Draw the graph of New_Fleet_Bootstrap_confidence.
    """
    current_boots = []
    for i in range(100, 300, 1):
        boot = bootstrap(np.std, i, Np_New_Fleet_Data)
        current_boots.append([i, boot[0], "Standard_Deviation"])
        current_boots.append([i, boot[1], "lower"])
        current_boots.append([i, boot[2], "upper"])

    New_Fleet_Data_Frame_df_boot = pd.DataFrame(current_boots, columns=['New_Fleet_Bootstrap Iterations', 'Standard_Deviation', "Value"])
    sns_plot = sns.lmplot(New_Fleet_Data_Frame_df_boot.columns[0], New_Fleet_Data_Frame_df_boot.columns[1], data =New_Fleet_Data_Frame_df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(5, 8)
    sns_plot.axes[0, 0].set_xlim(100, 300)

    sns_plot.savefig("New_Fleet_bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("New_Fleet_bootstrap_confidence.pdf", bbox_inches='tight')



    """
    Draw the graph of Current_Fleet_Bootstrap_confidence.
    """
    new_boots = []
    for i in range(100, 300, 1):
        boot = bootstrap(np.std, i, Np_Current_Fleet_Data)
        new_boots.append([i, boot[0], "Standard_Deviation"])
        new_boots.append([i, boot[1], "lower"])
        new_boots.append([i, boot[2], "upper"])

    Current_Fleet_Data_Frame_df_boot = pd.DataFrame(new_boots, columns=['Current_Fleet_Bootstrap Iterations', 'Standard_Deviation', "Value"])
    sns_plot = sns.lmplot(Current_Fleet_Data_Frame_df_boot.columns[0], Current_Fleet_Data_Frame_df_boot.columns[1], data =Current_Fleet_Data_Frame_df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(3, 6)
    sns_plot.axes[0, 0].set_xlim(100, 300)

    sns_plot.savefig("Current_Fleet_bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("Current_Fleet_bootstrap_confidence.pdf", bbox_inches='tight')

