import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfFile, PdfPages
from scripts import mpg_cat, my_stats, read_csv

if __name__ == "__main__":
    #Fetch automobiles dataset and perform descriptive analysis by calling my_stats function
    df = read_csv()
    d_stats = my_stats(df)
    #prepare the new dataframe for futher processing 
    d_stats.index.name = "stats"
    d_stats.round(3)

    #Set pdf filename and path
    rep = PdfPages('./reports/Automobiles_Descriptive_Stats.pdf')
    #prepare and plot dataframe
    fig, ax = plt.subplots(figsize = (12,4))
    ax.axis('tight')
    ax.axis('off')
    ax.set_title('A Descriptive Analysis of the Automobiles Dataset')
    my_table = ax.table(cellText=d_stats.values, rowLabels=d_stats.index, cellLoc='center',
                        colColours=['gainsboro'] * len(d_stats), colLabels=d_stats.columns, loc='center',
                        colWidths= [0.12]*(len(d_stats.columns)))
    w, h = my_table[0,1].get_width(), my_table[0,1].get_height()
    my_table.add_cell(0, -1, w,h, text=d_stats.index.name)

    #Save dataframe in the first page of the created pdf
    rep.savefig(fig, bbox_inches = 'tight')

    # Get value counts for car makes
    car_make_counts = df['origin'].value_counts()

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(car_make_counts, labels=car_make_counts.index, autopct='%1.2f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Distribution of Car Models by Origin')

    #add creted pie chart to the second page of pdf and save
    rep.savefig(fig, bbox_inches = 'tight')
    rep.close()

    #apply the mpg_cat function to the automobile dataset by adding a Fuel Efficiency column
    df['Fuel Efficiency'] = df.loc[:,'mpg'].apply(mpg_cat)
    df.to_excel('./reports/automobiles_updated.xlsx')
    print("Descriptives analysis successfully done......\n")
    print("....Check reports folder for the reports.")
    # print('\n-----------------------------------------------\n')
    # print('A segment of an insightful info about the Automobile Dataset:')
    # print(df.iloc[20:41,:]) 
    #print(df.sort_values('yr', ascending = False).head(20))
   
    