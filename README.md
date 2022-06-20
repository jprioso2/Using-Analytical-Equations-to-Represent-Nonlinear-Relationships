# Using-Analytical-Equations-to-Represent-Nonlinear-Relationships

# Vensim Macros

The folder Vensim Macros includes the Macros to add in the Vensim Models. Each Macro includes the conventional nonlinear equations and the version of the nonlinear equations with reference points.

# Python script to replace existing table function

This supplementary appendix explains how to replace an existing table function using one of the six analytical equations discussed in the main manuscript using a Python 3 script we wrote specifically for this task. The code for conducting this analysis is attached in the supplementary materials as: ShapeNonlinearFunction.py. Using information about the existing table function, the script helps identify the analytical equation with an internal reference point (r_x, r_y) that best represents the nonlinear relationship.

The script estimates the best-fitting values for each of the six analytical equations based on the Sum of Square Error (SSE) statistics and Root-mean-square error (RMSE). If an analytical function is undefined for any of the existing table function values (i.e., x values, minimum and maximum y-axis values, or interior reference value), that analytical equation is not included in the estimations. After the estimations, the script reports the SSE and RMSE for each analytical equation and identifies the equation with the lowest RMSE. The script also draws a graph showing all of the estimated curves along with the original table function. Follow the instructions below to run the code and take the World Dynamics model as an example to use the Python Script.

# Text file to add the inputs:
1. Create a txt file per each Table function you want to represent using analytical equations. Save the txt file as "Input". If you want to evaluate more than one Table function at the same time, use sequential numbers after the "Input" without space as Input1, Input2, Input3 and so on. Each txt file must include the following header names in row 1.
	Column1 : x
	Column2 : y
	Column3 : reference_point_x_value
	Column4 : reference_point_y_value
	Column5 (optional) : graphs_to_display between 1 and 6 (put zero to display all feasible analytical equations)
See the recreation of the Table Functions of World Dynamics model in text format as an example.

2. Save the Txt file in the same location as the Python Script. Include the file path in the line 89 adding r before the path. For instance, "dir_path = r"C:\Users\". 

3. In the text file add the x-values and y-values in the corresponding columns (x and y). Additionally, enter the reference point X-value and Y value in the correspoding columns (reference_point_x_value and reference_point_y_value).Finally, add the number of graphs you want to display. The maximun number of  graphs to display is 6 if all analytical equations are feasible. You can leave this value empty or add 0 to display all feasible analytical equations. Ensure you do not have any extra empty rows after the last number of the table function in the text file, i.e., check that the previous rows only contain the final number of your table function. Save each change made in the text file. 

# Run the code and then respond to prompts for information when running the code:
4. Run the code to generate the results. By default the code estimates and reports results for all of the feasible analytical equations. However, if you want to display the results of only the best fitting analytical funtions, you can indicate the number of analytical fuctions to display in column5. In addition, to display the results of only the best fitting analytical functions, you can activate lines 458-464 of the code by eliminating the # at the beginning of each of these lines (but be sure to maintain the indentations).

  The next prompt asks you to: “Graph and results to display from the smallest RMSE to the largest RMSE. Select one number between 1 and 6:” This prompt asks you to select how many graphs and results to display based on the set of analytical equations that meet the constraints determined from the information entered in the previous steps. The range of values displayed in this prompt is determined by how many of the six analytical equations meet the constraints. If you enter 1, then only the graph and estimation results for the best fitting analytical equation – determined by the lowest RMSE – will be displayed. If you enter the maximum value included in the prompt, in this case 6, then the graph and estimation results for all of the analytical equations that meet the constraints will be displayed. In general, we recommend displaying the results for all of the analytical equations that meet the constraints. Enter a number within the range provided in the prompt and then press Return.

4.1. If none of the six analytical equations meet the constraints determined from the information entered in the previous steps, the prompt will instead indicate:
“There is no analytical equation available. Insert 0 to see the results:”.
In this case, the script cannot be used to replace the table function using one of the six analytical equations discussed in the main manuscript. You will need to explore alternative analytical equations. Enter 0 and press Return to exit.

5. The estimation results for the number of analytical equations you entered in  step 4 are reported on the screen and sorted from lowest to highest RMSE value. For each analytical equation, the results reported include: RMSE, SSE, and the estimated parameter value(s). Also, the script identifies the best fitting analytical equation as determined by the lowest RMSE. You can copy and paste the results directly from the Console to word. 
In addition, a graph is displayed showing the estimated analytical curve(s) along with the original table function. The code creates a folder called "Plots" where the Python script is saved and save the plots of all feasible analytical equations. 
The graph results can be helpful in selecting the most appropriate analytical equation to use when replacing the table function. In some cases, the analytical equation with the lowest RMSE may not be the most appropriate equation to use as the replacement. Therefore, it is important to carefully examine the shape of the curves displayed on the graph and to use all of the results combined with judgment to select the most appropriate analytical equation.
