[![Python_Temp_Demo](https://github.com/nogibjj/oo46_Python_Temp_W3/actions/workflows/actions.yml/badge.svg)][def]

# Template for Python projects (Week 3)

##The current implementation of the Mini-project (Week_3) can be executed as follows:

1. All dependencies needed for execution can be found in the [requirement.txt](https://github.com/nogibjj/oo46_Python_Temp_W3/blob/main/requirements.txt) file
2. These dependencies will be installed  by github actions using the Make file.


## Mini-project-Week_3 deliverables:
1. The [main.py](https://github.com/nogibjj/oo46_Python_Temp_W3/blob/main/myapp/main.py) file can be thought of as the main app entry point in the current implementation.
2. It imports several libraries to read a csv file [automobiles.csv](https://github.com/nogibjj/oo46_Python_Temp_W3/blob/main/dsets/automobiles.csv) in order to performs the following:
    * Creates and saves both a descriptive analysis and a distribution bar chart from the input file
        * the output is then saved in the reports folder as a pdf file [Automobiles_Report.pdf](https://github.com/nogibjj/oo46_Python_Temp_W3/blob/main/reports/Automobiles_Report.pdf)
    * It applys mpg_cat() function on mpg column of the input file and creates an excell sheet with the results
        * the output of this process is also saved the name: [Automobiles_Desc.xlsx](https://github.com/nogibjj/oo46_Python_Temp_W3/blob/main/reports/Automobiles_Desc.xlsx). 
   
    * It then alerts the user with a success message. You can find summary reports below.

## Testing...
1. A simple unit test implementation is provided in myapp/test_main.py as follows:
    * test_count function --> test if the value count of the dataset is as expected
    * test_my_stats --> uses polars's assert_frame_equal testing feature to confirm the quality of two dataframes
2. This test wll also be executed by github actions. However, manual testing can also be done either via Make file or by running python myapp/test_main.py

### Sample descriptive analysis of the automobiles dataset
![Report](reports/Automobiles_Report.pdf)

[def]: https://github.com/nogibjj/oo46_Python_Temp_W3/actions/workflows/actions.yml
