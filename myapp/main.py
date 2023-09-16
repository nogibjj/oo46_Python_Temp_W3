from scripts import my_stats, read_csv
import matplotlib.pyplot as plt
import polars as pl
from matplotlib.backends.backend_pdf import PdfPages

if __name__ == "__main__":
    # Fetch automobiles dataset and perform descriptive analysis by calling my_stats function
    new_df = my_stats(read_csv())
    # Set pdf filename and path
    rep = PdfPages("./reports/Automobiles_Report.pdf")
    # prepare and plot dataframe as Matplotlib table
    fig, ax = plt.subplots(figsize=(13, 4))
    ax.axis("tight")
    ax.axis("off")
    ax.set_title("A Descriptive Analysis of the Automobiles Dataset")
    my_table = ax.table(
        cellText=new_df.rows(),
        cellLoc="center",
        colColours=["gainsboro"] * len(new_df),
        colLabels=new_df.columns,
        loc="center",
        colWidths=[0.12] * (len(new_df.columns)),
    )

    #Save newly created table in the first page of the created pdf
    rep.savefig(fig, bbox_inches="tight")

    # Get value counts for car makes by origin
    df = read_csv()
    car_make_counts = df.group_by("origin", maintain_order=True).agg(pl.count())

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(y=car_make_counts["origin"], width=car_make_counts["count"])
    ax.set_title("Distribution of Car Models by Origin")
    ax.set_ylabel("Origin of cars")
    ax.set_xlabel("Number of cars produced")

    # add bar chart to the second page of pdf and save
    rep.savefig(fig, bbox_inches="tight")
    rep.close()

    # Save an excel version of descriptive stats
    new_df.write_excel(
        "./reports/Automobiles_Desc.xlsx", column_totals=True, autofit=True
    )
