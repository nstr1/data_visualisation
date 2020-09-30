import pandas as pd
import matplotlib.pyplot as plt 
import pandas.api.types as ptypes

def graph(df, x_axis, y_axis):
    if not ptypes.is_numeric_dtype(df[y_axis]):
        df=df.groupby([x_axis,y_axis]).size()
        df=df.unstack()
        df.plot(kind='bar')
    else:
        df.plot(kind="line", x = x_axis, y = y_axis)
    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()
    