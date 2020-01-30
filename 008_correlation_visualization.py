#!/usr/bin/python3

# ===================================================================
#    IMPORT SECTION
# ===================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

import pandas as pd

style.use('ggplot')


# ===================================================================
#    FUNCTION DEFINITION
# ===================================================================
def visualize_data():
    df = pd.read_csv('data/sp500_joined_closes.csv')

    # we could graph any company
    # df['AAPL'].plot()
    # plt.show()

    #  Building a correlation table
    # The .corr() automatically will look at the entire DataFrame,
    # and determine the correlation of every column to every column.
    df_corr = df.corr()
    print(df_corr.head())

    # save correlation table for convenience
    # df_corr.to_csv('data/sp500corr.csv')

    # building heatmap
    data1 = df_corr.values
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    # which will give us red for negative correlations,
    # green for positive correlations,
    # and yellow for no-correlations
    heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
    fig1.colorbar(heatmap1)

    # setting axes ticks (will be filled with company names)
    ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)

    # setting axes flipped (x on top, y on left)
    ax1.invert_yaxis()
    ax1.xaxis.tick_top()

    #  actually going to add the company names to the currently-nameless ticks
    column_labels = df_corr.columns
    row_labels = df_corr.index
    ax1.set_xticklabels(column_labels)
    ax1.set_yticklabels(row_labels)

    plt.xticks(rotation=90)
    heatmap1.set_clim(-1, 1)
    plt.tight_layout()
    # plt.savefig("correlations.png", dpi=(300))
    plt.show()


# ===================================================================
#    CLASS DEFINITION
# ===================================================================

# ===================================================================
#    START OF PROGRAM
# ===================================================================
if __name__ == '__main__':
    # Chances are, investing in a bunch of companies with zero correlation over time
    # would be a decent way to be diverse, but we really don't know at this point.
    visualize_data()
    pass