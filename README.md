[![Python_Temp_Demo](https://github.com/nogibjj/oo46_Python_Temp/actions/workflows/actions.yml/badge.svg)][def]

# Template for Python projects

##The current implementation of the Mini-project can be executed as follows:

1. All dependencies needed for execution can be found in the requirement.txt file
2. These dependencies will be installed  by github actions(please see yml file for further details)for now.
3. Please refer the requirements.txt for manual intallations: use Make file. 

##Mini-project deliverables:
1. The myapp/main.py file can be thought of as the main app entry in the current implementation
2. It imports several libraries to read a csv file (automobiles.csv) from the dsets folder and performs the following:
    * Creates and saves both a descriptive analysis and a distribution pie chart from the input file
        * the output is then saved in the reports folder as a pdf file (Automobiles_Descriptive_Stats.pdf)
    * It applys mpg_cat() function on mpg column of the input file and creates an excell sheet with the results
        * the output of this process is also saved in the reports folder under the name: automobiles_updated.xlsx
   
    * It then alerts the user with a success message

##Testing...
1. A simple unit test implementation is provided in myapp/test_main.py as follows:
    * test_col_exist function --> test if a new column exist after calling mpg_cat function on a dataframe
    * test_my_stats --> uses pandas's assert_frame_equal testing feature to confirm the quality of two dataframes
2. This test wll also be executed by github actions. However, manual testing can also be done either with the Make file or by running python myapp/test_main.py


[def]: https://github.com/nogibjj/oo46_Python_Temp/actions/workflows/actions.yml
