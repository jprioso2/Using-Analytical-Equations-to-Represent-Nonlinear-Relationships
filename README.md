# Using-Analytical-Equations-to-Represent-Nonlinear-Relationships
Juan Ríos-Ocampo (a, *) and Michael Shayne Gary (a)
a UNSW Business School, University of New South Wales, Sydney NSW 2052, Australia
*Correspondence to: Juan Ríos-Ocampo. E-mail: j.rios_ocampo@unsw.edu.au

## Vensim Macros

The folder "Vensim Macros" includes a set of Vensim DSS Macros that can be used to implement the conventional form of each analytical equation and also the version of each analytical equation with an interior reference point. 

## Python script to implement our procedure for using analytical functions to formulate nonlinear relationships 

This supplementary appendix explains how to replace an existing table function using one of the six analytical equations discussed in the main manuscript using a Python 3 script we wrote specifically for this task. The script for conducting this analysis is attached in the supplementary materials as: ShapeNonlinearFunction.py. Using information about an existing table function, the script helps identify the analytical equation with an internal reference point (r_x, r_y) that best represents the nonlinear relationship. Note that judgment is always required to interpret the results and select the most appropriate analytical equation.
	
	The script estimates the best-fitting values for each of the six analytical equations based on the Sum of Square Error (SSE) statistics and Root-mean-square error (RMSE). If an analytical function is undefined for any of the existing table function values (i.e., x values, minimum and maximum y-axis values, or interior reference value), that analytical equation is not included in the estimations. After the estimations, the script reports the SSE and RMSE for each analytical equation and identifies the equation with the lowest RMSE. The script also draws a graph showing all of the estimated curves along with the original table function. Follow the instructions below to run the code using the World Dynamics model as a demonstration of how to use the Python script.

### Text file to add the inputs:

1. Create a text file (with .txt file extension) for each table function that you want to represent using an analytical equation. Save the text file as "Input1.txt". If you want to evaluate more than one table function at the same time, use sequential numbers after "Input" without a space as: Input1, Input2, Input3 and so on. Each tab delimited text file must include the following column header names in row 1 (include only the text after the colon for each column, where the columns are separated by one tab).
• Column1: x
• Column2: y
• Column3: reference_point_x_value
• Column4: reference_point_y_value
• Column5 (optional): graphs_to_display (graphs to display between 1 and 6 put zero to display all feasible analytical equations)

See the text files for the table functions of the World Dynamics model as examples.

2. Save the text file in the same location (i.e., folder) as the Python script. Include the file path in line 132 of the code and add r before the path. For instance, "dir_path = r"C:\Users\". 

3. In the text file add the x-values and y-values in the corresponding columns (x and y). Additionally, enter the reference point X value and Y value in the corresponding columns (reference_point_x_value and reference_point_y_value). Finally, add the number of graphs you want to display. The maximun number of graphs to display is 6 if all of the analytical equations are feasible. You can leave this value empty or add 0 to display all feasible analytical equations. Ensure you do not have any extra empty rows after the last value in the text file; check that the previous rows only contain the final value of your table function. Save each change made in the text file. 


### Run the code and then respond to prompts for information when running the code:

4. Run the script to generate the results. By default the code estimates and reports results for all feasible analytical equations. However, if you want to display the results of only the best fitting analytical funtions, you can indicate the number (between 1 and 6) of analytical fuctions to display in column5 of each text input file. Alternatively, to display the results of only the best fitting analytical functions for each table funcion, you can activate lines 508-512 of the code by eliminating the # at the beginning of each of these lines (but be sure to maintain the indentations).

	If you activate lines 508-512 of the code, the code will display the following prompt for each table function: “Graph and results to display from the smallest RMSE to the largest RMSE. Select one number between 1 and 6:”. This prompt asks you to select how many graphs and results to display based on the set of analytical equations that meet the constraints determined from the information entered in the previous steps. The range of values displayed in this prompt is determined by how many of the six analytical equations meet the constraints. If you enter 1, then only the graph and estimation results for the best fitting analytical equation – determined by the lowest RMSE – will be displayed. If you enter the maximum value included in the prompt, in this case 6, then the graph and estimation results for all of the analytical equations that meet the constraints will be displayed. In general, we recommend initially displaying the results for all of the analytical equations that meet the constraints to visually inspect the resulting graphs. Enter a number within the range provided in the prompt and then press Enter.
	
	If none of the six analytical equations meet the constraints determined from the information entered in the previous steps, the prompt will instead indicate:
“There is no analytical equation available. You will need to explore alternative analytical equations”. In this case, the script cannot be used to replace the table function using one of the six analytical equations discussed in the main manuscript. You will need to explore alternative analytical equations.

5. The estimation results for the number of analytical equations you entered in Step 4 are reported on the screen and sorted from lowest to highest RMSE value. For each analytical equation, the results reported include: RMSE, SSE, and the estimated parameter value(s). Also, the script identifies the best fitting analytical equation as determined by the lowest RMSE. You can copy and paste the results directly from the Console to any work processor or text editor. 
	
	In addition, a graph is displayed showing the estimated analytical curve(s) along with the original table function. The script creates a subfolder called "Plots" within the folder where the Python script is saved and in that subfolder saves the plots of all feasible analytical equations.
	
	The graph results can be helpful in selecting the most appropriate analytical equation to use when replacing a table function. In some cases, the analytical equation with the lowest RMSE may not be the most appropriate equation to use as the replacement. Therefore, it is important to carefully examine the shape of the curves displayed on the graph and to use all of the results combined with judgment to select the most appropriate analytical equation.
	
	For example, the results from the Python script estimating analytical equations to replace the 22 table functions of the original World Dynamics model show that the best fitting analytical equation matches the analytical equation we chose for 15 of the 22 table functions. For the remaining seven analytical equations, the script results suggest that the Quadratic equation fits the original table function best using the RMSE criterion. However, these seven cases provide an excellent reminder that modellers must use judgment when selecting the most appropriate analytical equation to represent a nonlinear relationship. The Quadratic equation can generate non-monotonic shapes under several parameter conditions and also interpretation of the quadratic equation can be unclear when an upper limit value (i.e., maximum) does not exist. We ended up choosing different analytical equations for these seven cases after reflecting on all of the information and using our judgment.
