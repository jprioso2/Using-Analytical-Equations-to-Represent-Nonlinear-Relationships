"""
Using Analytical Equations to Represent Nonlinear Relationships
Juan Ríos-Ocampo (a,*) and Michael Shayne Gary (a)
a UNSW Business School, University of New South Wales, Sydney NSW 2052, Australia
*Correspondence to: Juan Ríos-Ocampo. E-mail: j.rios_ocampo@unsw.edu.au

Text file to add the inputs:
1.  Create a text file per each Table function you want to represent using 
    analytical equations. Save the text file using the name "Input". If you want 
    to evaluate more than one Table function at the same time, use sequential 
    numbers after the "Input" without space as Input1, Input2, Input3 and so on. 
    Each text file must include the following header names in row 1.
    Column1 : x
    Column2 : y
    Column3 : reference_point_x_value
    Column4 : reference_point_y_value
    Column5 (optional): graphs_to_display. The number of grapth to display
            is between 1 and 6 (put zero to display all feasible analytical equations)
    See the recreation of the Table Functions of World Dynamics model in text format as an example.        
2.  Save the text file in the same location as the Python Script. 
    Include the file path in the line 89 adding r before the path. 
    For instance, "dir_path = r"C:\".
                                                                            
3.  In the text file add the x-values and y-values in the corresponding columns 
    (x and y). Additionally, enter the reference point X-value and Y value in 
    the correspoding columns (reference_point_x_value and reference_point_y_value). 
    Finally, add the number of graphs you want to display. The maximum number 
    of graphs to display is 6 if all analytical equations are feasible. 
    You can leave this value empty or add 0 to display all feasible analytical 
    equations. Ensure you do not have any extra empty rows after the last number 
    of the table function in the text file, i.e., check that the previous rows 
    only contain the final number of your table function. Save each change made 
    in the text file.  

Run the Python Script code and then respond to prompts for information when 
running the code:
4.  By default, the code estimates and reports results for all of the feasible 
    analytical equations. However, if you want to display the results of only 
    the best fitting analytical functions, you can indicate the number of analytical 
    functions to display in column5. In addition, to display the results of only 
    the best fitting analytical functions, you can activate lines 480-485 of 
    the code by eliminating the # and the space at the beginning of each of 
    these lines (but be sure to maintain the indentations).
    The next prompt asks you to: “Graph and results to display from the smallest
    RMSE to the largest RMSE. Select one number between 1 and 6:”
    This prompt asks you to select how many graphs and results to display based 
    on the set of analytical equations that meet the constraints determined 
    from the information entered in the previous steps. The range of values 
    displayed in this prompt is determined by how many of the six analytical 
    equations meet the constraints. If you enter 1, then only the graph and 
    estimation results for the best fitting analytical equation – determined 
    by the lowest RMSE – will be displayed. If you enter the maximum value 
    included in the prompt, in this case 6, then the graph and estimation 
    results for all of the analytical equations that meet the constraints will 
    be displayed. In general, we recommend displaying the results for all of 
    the analytical equations that meet the constraints. Enter a number within 
    the range provided in the prompt and then press Return.
4.1.If none of the six analytical equations meet the constraints determined 
    from the information entered in the previous steps, the prompt will instead 
    indicate:
    “There is no analytical equation available. Insert 0 to see the results:”.
    In this case, the script cannot be used to replace the table function using
    one of the six analytical equations discussed in the main manuscript. 
    You will need to explore alternative analytical equations. Enter 0 and 
    press Return to exit.
5.  The estimation results for the number of analytical equations you entered in
    step 4 are reported on the screen and sorted from lowest to highest RMSE 
    value. For each analytical equation, the results reported include: RMSE, 
    SSE, and the estimated parameter value(s). Also, the script identifies the 
    best fitting analytical equation as determined by the lowest RMSE. You can
    copy and paste the results directly from the Console to word. 
    
    In addition, a graph is displayed showing the estimated analytical curve(s) 
    along with the original table function. The code creates a folder called 
    "Plots" where the Python script is saved and save the plots of all 
    feasible analytical equations. 
    
    The graph results can be helpful in selecting the most appropriate 
    analytical equation to use when replacing the table function. In some cases, 
    the analytical equation with the lowest RMSE may not be the most appropriate 
    equation to use as the replacement. Therefore, it is important to carefully 
    examine the shape of the curves displayed on the graph and to use all of 
    the results combined with judgment to select the most appropriate 
    analytical equation.

    Analytical Equations to Represent Nonlinear Relationships
    # -Generalized logistic equation
    # -Exponential equation
    # -Modified exponential equation
    # -Quadratic equation
    # -Logarithmic equation
    # -Power equation
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
import os
import fnmatch

#%% Read Txt file

""" Identified number of Inputs (tables funtions) in the folder. 
Copy the path of the folder were you have the txt files. Include it between 
" " and using a r before. r"C:\..."
"""
dir_path = r"C:\"
count = len(fnmatch.filter(os.listdir(dir_path), 'Input*'))

Results = list()

for xx in range(1,count+1): #Iterate throught the Txt files saved in the folder
   line = lambda n:n * chr(95)
   
   print(line(95))  
   print("\n" + "TABLE FUNCTION" + " " + str(xx)) 
   Xtf1 = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["x"].to_numpy()
   Xtf = Xtf1.reshape(len(Xtf1),1)
   Ytf1 = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["y"].to_numpy()
   Ytf = Ytf1.reshape(len(Ytf1),1)
   rxinput = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["reference_point_x_value"].to_numpy()[0]
   ryinput = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["reference_point_y_value"].to_numpy()[0]
   
   table = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")
   if "graphs_to_display" not in table:
       Input = 0       
   else:
       Input1 = pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["graphs_to_display"].to_numpy()[0]
       if (np.isnan(Input1)).any():
          Input = int(0)
       else:
          Input = int(pd.read_csv("Input" + str(xx) + ".txt", sep = "\t")["graphs_to_display"].to_numpy()[0])
           
   if rxinput:
       rxinput = np.array(float(rxinput)).reshape(1,1)
   else:
       print("Use the traditional specification of the analytical equations")
       sys.exit()
   if rxinput<np.min(Xtf) or rxinput>np.max(Xtf):
       print("Reference point out of the x-axis range")
       sys.exit() 
   
   
   if ryinput:
       ryinput = np.array(float(ryinput)).reshape(1,1)
   else:
       print("Use the traditional specification of the analytical equations")
       sys.exit()
   if ryinput>np.max(Ytf) or ryinput<np.min(Ytf):
       print("Reference point out of the y-axis range")
       sys.exit() 
        
   ry = ryinput
   rx = rxinput
   
   import warnings
   warnings.filterwarnings("ignore", category=RuntimeWarning) 
   warnings.filterwarnings("ignore", category=FutureWarning) 
   
   del Xtf1, Ytf1
    
    #%% Quadratic equation
    
    #paramenters
   aQ = np.array([(Ytf[0,0])]).reshape(1,1) # min value in y(x)
   barange = np.arange(-np.max(Ytf), np.max(Ytf), 0.01)
   b =  np.array(barange).reshape(len(barange),1) #parameter to be estimated
                
    #Calibration b paramenter
   if (rx != 0).any():
       YmodListQ = list()
       blist = list()
       for j in range(len(b)):
           if (rx != 0).any():
               YmodListQ.append(aQ+(b[j,0]*Xtf)+((ry-aQ-b[j,0]*rx)/(rx**2)) * Xtf**2) #Quadratic equation
               blist.append(b[j,0])
               
   #Statistics measures        
       if len(YmodListQ) != 0:
           SSEList = list()
           RMSEList = list()
           for a in range(len(YmodListQ)):
               SSEList.append(np.sum(np.power((Ytf-YmodListQ[a]),2))) #Sum of squared error
               RMSEList.append(np.sqrt((np.power((Ytf-YmodListQ[a]),2)).mean())) #Root-mean-square error
   
   #Minimum values: Sum of squared error and root-mean-square error
           SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
           RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
           SSEmin4Q = np.min(SSEList1)
           RMSEmin4Q = np.min(RMSEList1)
                
    #Find optimal values: Y, b
           for index, item in enumerate(SSEList):
               if item == SSEmin4Q: 
                   YmodQ = YmodListQ[index]
                   bopt = blist[index]
   
           del a, j, barange, index, item, SSEList, RMSEList, SSEList1, RMSEList1
           del b, YmodListQ, blist
   #%% Exponential equation
   
   # parameters
   c =   np.array([np.min(Ytf)]).reshape(1,1) # min value in y(x)
   Sparange = np.arange(-np.max(Ytf), np.max(Ytf), 0.01) #parameter to be estimated
   
   #Exponential decay or growth shape
   if Ytf[0,0]-Ytf[-1,0] > 0:   #Exponential decay
       Sp = np.array([np.max(Ytf)]).reshape(1,1)
       d = Sp-c
   if Ytf[0,0]-Ytf[-1,0] < 0:    #Exponential growth
       Sp =  np.array(Sparange).reshape(len(Sparange),1)   
       d = Sp-c
   
   #Calibration d paramenter
   if (rx != 0).any():
       if ((ry-c)>0).any():
           YmodListExp = list()
           dlist = list()
           for j in range(len(d)):
               if ((d[j,0] != 0).any()):
                   if ((((ry-c)/d[j,0])>0).any() and ((rx != 0).any())):
                       YmodListExp.append(d[j,0]*(((ry-c)/d[j,0])**(Xtf/rx))+c)
                       dlist.append(d[j,0])
           
   #Statistics measures 
           if len(YmodListExp) != 0:        
               SSEList = list()
               RMSEList = list()
               for a in range(0, len(YmodListExp)):
                   SSEList.append(np.sum(np.power((Ytf-YmodListExp[a]),2))) #Sum of squared error
                   RMSEList.append(np.sqrt((np.power((Ytf-YmodListExp[a]),2)).mean())) #Root-mean-square error
       
   #Minimum values: Sum of squared error and root-mean-square error
               SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
               RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
               SSEmin2Exp = np.min(SSEList1)
               RMSEmin2Exp = np.min(RMSEList1)
                      
   #Find optimal values: Y, dopt, Spopt
               for index, item in enumerate(SSEList):
                   if item == SSEmin2Exp: 
                       YmodExp = YmodListExp[index]
                       dopt = dlist[index]
                       if Ytf[0,0]-Ytf[-1,0] > 0:   #Exponential decay
                           Spopt = np.max(Ytf)
                       else:
                           Spopt = dopt + c[0,0]
                          
               del Sparange, YmodListExp, item, index, a, SSEList, RMSEList
               del d, Sp, SSEList1, RMSEList1, dlist
           
   #%% Generalized Logistic equation
   
   #Paramenters
   C = np.array(1).reshape(1,1)      # Fitting parameter
   Q = np.array(1).reshape(1,1)       # Fitting parameter
   A = np.array([np.min(Ytf)]).reshape(1,1)     # A(lower y-axis value) taken from Ytf.
   K = np.array([np.max(Ytf)]).reshape(1,1)     # K(upper y-axis value) taken from Ytf.
   Marange = np.arange(Xtf[1,0],Xtf[-2,0], 0.01)  #M is calibrated evaluating with a stepway 0.01 in the range [X1,Xt-1]
   M = np.array(Marange).reshape(len(Marange),1)
         
    #Calibration M paramenter
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
        YmodListLE = list()
        mlist = list()
        for j in range(len(M)):
            if (rx != M[j,0]).any():
                if ((A<ry).any() and (ry<K).any()):
                    if ((Q*(ry - A)) != 0).any() and (rx != M[j,0]).any():
                        YmodListLE.append(A+((K-A)/(C+Q*(((A*(C-1)+K-ry*C)/(Q*(ry-A)))**((Xtf-M[j,0])/(rx-M[j,0]))))))
                        mlist.append(M[j,0])
    
    #Statistics measures 
        if len(YmodListLE) != 0:
            SSEList = list()
            RMSEList = list()
            for a in range(len(YmodListLE)):
                SSEList.append(np.sum(np.power((Ytf- YmodListLE[a]),2))) #Sum of squared error
                RMSEList.append(np.sqrt((np.power((Ytf- YmodListLE[a]),2)).mean())) #Root-mean-square error
                        
    #Minimum values: Sum of squared error and root-mean-square error     
            SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
            RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
            SSEmin1LE = np.min(SSEList1)
            RMSEmin1LE = np.min(RMSEList1)
                    
    #Find optimal values: Y, M
            for index, item in enumerate(SSEList):
                if item == SSEmin1LE: 
                    YmodLE = YmodListLE[index]
                    Mopt = mlist[index]                          
                    
            del a, j, Marange, index, item, SSEList, RMSEList,
            del YmodListLE, M, SSEList1, RMSEList1, mlist
    #%% Modified exponential equation
    
    # Parameters
   w = np.array([Ytf[0]]).reshape(1,1)  #Min value in y(x)
   alphaarange = np.arange(-np.max(Ytf), np.max(Ytf)*1.5, 0.01)  
   alpha = np.array(alphaarange).reshape(len(alphaarange),1) #parameter to be estimated
   
   #Calibration p paramenter
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       YmodListModExp = list()
       alphalist = list()
       for j in range(len(alpha)):
           KK = ((alpha[j,0]+w)-ry)
           if (((KK>0).any()) and ((rx>0).any() or (rx<0).any()) \
               and ((alpha[j,0]>0).any() or (alpha[j,0]<0).any())):
               YmodListModExp.append((alpha[j,0])*(1-(((alpha[j,0]+w-ry)/alpha[j,0])**(Xtf/rx)))+w)
               alphalist.append(alpha[j,0])
       
   #Statistics measures 
       if len(YmodListModExp) != 0:        
           SSEList = list()
           RMSEList = list()
           for a in range(len(YmodListModExp)):
               SSEList.append(np.sum(np.power((Ytf- YmodListModExp[a]),2))) #Sum of squared error
               RMSEList.append(np.sqrt(((np.power((Ytf- YmodListModExp[a]),2))).mean())) #Root-mean-square error
   
   #Minimum values: Sum of squared error and root-mean-square error
           SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
           SSEmin3ModExp = np.min(SSEList1)
           RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
           RMSEmin3ModExp = np.min(RMSEList1)
               
   #Find optimal values: Y, p
           for index, item in enumerate(RMSEList):
               if item == RMSEmin3ModExp: 
                   YmodModExp = YmodListModExp[index]
                   alphaopt = alphalist[index]
            
           del a,j, alphaarange, index, item, SSEList, RMSEList,SSEList1, RMSEList1
           del YmodListModExp, alphalist
   #%% logarithmic equation
   
   # identify if Xtf include X == 0, if yes, X=0 and Y(X=0) are excluded from the data.
   if (Xtf[0,0] > 0).any():
       XmodLog = Xtf
       YtfLog = Ytf
   else:
       XmodLog = Xtf[1:]
       Ytf2 = Ytf[1:]
       YtfLog = Ytf2
   
   #Paramenters
   if (rx != 0).any() and (rx != 1).any():
       aLogarange = np.arange(0, np.max(XmodLog), 0.01) #Max value in y(x)
       aLog = np.array(aLogarange).reshape(len(aLogarange),1) #Parameter to be estimated
       YmodListLog = list()
       aLoglist = list()
           
   #Calibration v paramenter
       for j in range(0, len(aLog)):
           if ((rx != 1).any()): 
                   YmodListLog.append(aLog[j,0]+((ry-aLog[j,0])/(np.log(rx)))*np.log(XmodLog))
                   aLoglist.append(aLog[j,0])
           
   #Statistics measures 
       if len(YmodListLog) != 0:        
           SSEList = list()
           RMSEList = list()
           for a in range(0, len(YmodListLog)):
               SSEList.append(np.sum(np.power((YtfLog-YmodListLog[a]),2))) #Sum of squared error
               RMSEList.append(np.sqrt((np.power((YtfLog-YmodListLog[a]),2)).mean())) #Root-mean-square error
   
   #Minimum values: Sum of squared error and root-mean-square error        
           SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
           RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
           SSEmin5Log = np.min(SSEList1)
           RMSEmin5Log = np.min(RMSEList1)
                      
   #Find optimal values: Y, v
           for index, item in enumerate(SSEList):
               if item == SSEmin5Log: 
                   YmodLog = YmodListLog[index]
                   aLogopt = aLoglist[index]
               
           del a, j, aLogarange, YmodListLog, item, index, SSEList, RMSEList
           del SSEList1, RMSEList1,  aLog, aLoglist
   #%% Power equation
   
   # Paramenters
   aPowerarange = np.arange(0, np.max(Xtf), 0.01) #Max value in X
   aPower = np.array(aPowerarange).reshape(len(aPowerarange),1) #parameter to be estimated
   cPower = np.array((Ytf[0])).reshape(1,1) #Min value in y(x)
   
   #Calibration u paramenter
   if (ry != 1).any() and (rx != 1).any() and (rx != 0).any() and (((ry-cPower)/aPower)>0).any():
       YmodListPower = list()  
       aPowerlist = list()
       for j in range(len(aPower)):
           if (aPower[j,0] != 0).any():
               if (((ry-cPower)/aPower[j,0])>0).any() and (aPower[j,0] != 0).any() and (rx >0).any() and (rx != 1).any():
                   YmodListPower.append(aPower[j,0]*(Xtf**((np.log((ry-cPower)/aPower[j,0]))/(np.log(rx))))+cPower)
                   aPowerlist.append(aPower[j,0])
   
   #Statistics measures 
       if len(YmodListPower) != 0:        
           SSEList = list()
           RMSEList = list()
           for a in range(0, len(YmodListPower)):
               SSEList.append(np.sum(np.power((Ytf-YmodListPower[a]),2))) #Sum of squared error
               RMSEList.append(np.sqrt((np.power((Ytf-YmodListPower[a]),2)).mean())) #Root-mean-square error
   
   #Minimum values: Sum of squared error and root-mean-square error         
           SSEList1 = [x for x in SSEList if (np.isnan(x) or np.isinf(x)) == False]
           RMSEList1 = [x for x in RMSEList if (np.isnan(x) or np.isinf(x)) == False]
           SSEmin6Power = np.min(SSEList1)
           RMSEmin6Power = np.min(RMSEList1)
                      
   #Find optimal values: Y, u
           for index, item in enumerate(SSEList):
               if item == SSEmin6Power: 
                   YmodPower = YmodListPower[index] 
                   aPoweropt = aPowerlist[index]              
                      
           del a, j, aPowerarange, YmodListPower, item, index, SSEList, RMSEList
           del SSEList1, RMSEList1, aPowerlist
   #%% Sum of square error and Root-mean-square error
   
   #Create a list with the minimum values of Root-mean-square error per equation
   RMSES = list()
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       RMSES.append(RMSEmin1LE)
   if (rx != 0).any() and (ry-c>0).any():
       RMSES.append(RMSEmin2Exp)   
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       RMSES.append(RMSEmin3ModExp)
   if (rx != 0).any():
       RMSES.append(RMSEmin4Q)
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any():
       RMSES.append(RMSEmin5Log)
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       RMSES.append(RMSEmin6Power)
   
   #Create a list with the minimum values of Sum of squared error per equation
   SSES = list()
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       SSES.append(SSEmin1LE)
   if (rx != 0).any() and (ry-c>0).any():   
       SSES.append(SSEmin2Exp)
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       SSES.append(SSEmin3ModExp)
   if (rx != 0).any():
       SSES.append(SSEmin4Q)
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       SSES.append(SSEmin5Log)
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       SSES.append(SSEmin6Power)
   
   for i in range(len(RMSES)):
       if (RMSES[i] < 0):
           RMSES[i] = 'nan'
           
   for i in range(len(SSES)):
       if (SSES[i] < 0):
           SSES[i] = 'nan'
   
   #SSE and RMSE sorted from lower to higher
   SSESsort = np.array((np.sort(SSES)), np.float64).reshape(len(SSES),1)
   RMSESsort = np.array((np.sort(RMSES)), np.float64).reshape(len(RMSES),1)
   
   # The best SSE and RMSE value within the equations evaluated 
   # (First value in the SSESsort and RMSESsort)
   if SSESsort.size > 0 or RMSESsort.size > 0:
       BestSSE = np.min(SSESsort)
       BestRMSE = np.min(RMSESsort)
   
   #%% Display message
      
   if Input == 0:  #reports results for all of the feasible analytical equations 
      Input = len(RMSESsort)
   
   if Input > len(RMSESsort):
      Input = len(SSESsort)
     
    #Indicate how many graphs to display considering the available options. To 
    #display the results of only the best fitting analytical functions, you can 
    #activate lines 483-488 of the code by eliminating the # and the space at 
    #the beginning of each of these lines (but be sure to maintain the indentations).
    
   # if RMSESsort.size>0:
   #     prompt = 'Graph and results to display from the lowest RMSE value to the highest RMSE value. Select one number between 1 and' + ' ' + str(len(RMSESsort)) + ": "
   #     Input = int(input(prompt))
   # else:
   #     prompt = 'There is no analytical equation available. Insert 0 to see the results: '
   #     Input = int(input(prompt))

   Rsort = list()
   Ssort = list()
   for e in range(Input):
       Rsort.append(RMSESsort[e,0])
       Ssort.append(SSESsort[e,0])
   #%% Indicate which value is the best option based on RMSE and SSE
   
   indexSSES = np.array(SSESsort) #numpy array
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       indexSSELE = list(indexSSES).index(SSEmin1LE) 
   if (rx != 0).any() and (ry-c>0).any():
       indexSSEExp = list(indexSSES).index(SSEmin2Exp)
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       indexSSEModExp = list(indexSSES).index(SSEmin3ModExp)
   if (rx != 0).any():
       indexSSEQ = list(indexSSES).index(SSEmin4Q)  
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       indexSSELog = list(indexSSES).index(SSEmin5Log)
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       indexSSEPower = list(indexSSES).index(SSEmin6Power)
   
   indexRMSES = np.array(RMSESsort) #numpy array
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and  (A<ry).any() and len(Xtf)>3:
       indexRMSELE = list(indexRMSES).index(RMSEmin1LE)
   if (rx != 0).any() and (ry-c>0).any():
       indexRMSEExp = list(indexRMSES).index(RMSEmin2Exp)
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       indexRMSEModExp = list(indexRMSES).index(RMSEmin3ModExp)
   if (rx != 0).any():
       indexRMSEQ = list(indexRMSES).index(RMSEmin4Q)
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       indexRMSELog = list(indexRMSES).index(RMSEmin5Log)
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       indexRMSEPower = list(indexRMSES).index(RMSEmin6Power)
      
   #%% Results (SSE, RMSE, and parameters) to print 
     
   print("\n" "Reference point: rx=%g and ry=%g \n" % (rx, ry) )  
   forprint = list();
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       forprint.append("* Generalized Logistic equation:  RMSE=%g,  SSE=%g,  M=%g, A=%g, K=%g and Q = C = 1" % (RMSEmin1LE, SSEmin1LE, Mopt, A, K))
   if (rx != 0).any() and (ry-c>0).any():
       forprint.append("* Exponential equation:           RMSE=%g,  SSE=%g,  d=%g, c=%g and Sp(d+c)=%g" % (RMSEmin2Exp, SSEmin2Exp, dopt, c, Spopt))
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       forprint.append("* Modified Exponential equation:  RMSE=%g, SSE=%g, alpha=%g and w=%g" % (RMSEmin3ModExp, SSEmin3ModExp, alphaopt, w))
   if (rx != 0).any():
       forprint.append("* Quadratic equation:             RMSE=%g,  SSE=%g,  b=%g and aQ=%g" % (RMSEmin4Q, SSEmin4Q, bopt, aQ)) 
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       if Xtf[0,0] != 0:
           forprint.append("* Logarithmic equation:           RMSE=%g,  SSE=%g,  aLog=%g" % (RMSEmin5Log, SSEmin5Log, aLogopt))
       else:
           forprint.append("* Logarithmic equation:           RMSE=%g,  SSE=%g,  aLog=%g" % (RMSEmin5Log, SSEmin5Log, aLogopt) + '\n-- However, Logarithmic equation does not cover all X-axis range due to the constrains');
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       forprint.append("* Power equation:                 RMSE=%g,  SSE=%g,  aPower=%g and cPower=%g" % (RMSEmin6Power, SSEmin6Power, aPoweropt, cPower))   
   
   
   results = (RMSES, np.arange(0,len(RMSESsort),1))
   resultssorted = np.array(results ).T
   
   resultsprint  = resultssorted[resultssorted[:, 0].argsort()]
   
   forprintsorted = list()
   for i in np.array(resultsprint[:,1], dtype = int):
       aa = forprint[i]
       forprintsorted.append(aa)
       print(aa)
   
   print("\n")
   if not ((ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3):
       print("* Generalized Logistic equation is not calculated when A(%g)>ry>K(%g) or len of Xtf is equal or less than 3" % (A,K))  
   if not ((rx != 0).any() and (ry-c>0).any()):
       print("* Exponential equation is not calculated when rx = 0 or because the constrain ry(%g)-c(%g)>0 is not satisfied" % (ry,c))  
   if not ((rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any()):
       print("* Modified exponential is not calculated when rx = 0 or p(%g)+w(%g)-ry(%g)) >0" %(np.max(Ytf), w[0], ry)) 
   if not ((rx != 0).any()):
       print("* Quadratic equation is not calculated when rx = 0")  
   if not ((ry != 1).any()  and (rx != 1).any() and (rx != 0).any()):
       print("* Logarithmic equation is not calculated when ry, rx = 0 or 1") 
   if not ((rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any()):
       print("* Power equation is not calculated when (ry(%g)-cp(%g)/aPower)>0" % (ry, cPower))  
   
   #%% Indicate the best analytical equation and return the SSE, RMSE and parameter values
   for index, item in enumerate(RMSES):
       if item == BestRMSE: 
           indexBest = index
           a = RMSES[index]
           print("\n" 'The analytical equation with the lowest RMSE is:\n' + forprint[indexBest] + "\n" 'Note that the lowest RMSE does not guarantee this analytical equation is the most appropriate.' ) 
  
   Results.append(forprintsorted)
   #%% Plots
   
   #create a folder to save plots in 600ppp
   newpath = dir_path + '\Plots' 
   if not os.path.exists(newpath):
      os.makedirs(newpath)
      
   #Original X- and Y-values
   plt.plot(Xtf, Ytf, 'k--', label='Table function', linewidth=3)
   
   #Plots per equation
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       if  RMSEmin1LE in Rsort and SSEmin1LE in Ssort:
           plt.plot(Xtf, YmodLE, label='Generalized logistic equation', linewidth=1, marker="1")
   if (rx != 0).any() and (ry-c>0).any():
       if  RMSEmin2Exp in Rsort and SSEmin2Exp in Ssort:
           plt.plot(Xtf, YmodExp, label='Exponential equation', linewidth=1, marker="2")
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       if  RMSEmin3ModExp in Rsort and SSEmin3ModExp in Ssort:
           plt.plot(Xtf, YmodModExp, label='Modified exponential equation', linewidth=1, marker=".")
   if (rx != 0).any():
       if  RMSEmin4Q in Rsort and SSEmin4Q in Ssort:
           plt.plot(Xtf, YmodQ, label='Quadratic equation', linewidth=1, marker="+")  
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       if  RMSEmin5Log in Rsort and SSEmin5Log in Ssort:
           plt.plot(XmodLog, YmodLog, label='Logarithmic equation', linewidth=1, marker="3")
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       if  RMSEmin6Power in Rsort and SSEmin6Power in Ssort:
           plt.plot(Xtf, YmodPower, label='Power equation', linewidth=1, marker="x")   
   plt.legend(frameon = False)
   plt.savefig(dir_path + '\Plots'+ '\TableFunction' + str(xx) + '.png', dpi=600)
   plt.show()
      
   #%% Remove remain variables
   if (ry != Ytf[0]).any() and (ry != Ytf[-1]).any() and (A<ry).any() and len(Xtf)>3:
       del indexRMSELE, indexSSELE
   if (rx != 0).any() and (ry-c>0).any():
       del indexRMSEExp, indexSSEExp
   if (rx != 0).any() and (((np.max(alpha)+w)-ry) >0).any():
       del indexRMSEModExp, indexSSEModExp
   if (rx != 0).any():
       del indexRMSEQ, indexSSEQ
   if (ry != 1).any()  and (rx != 1).any() and (rx != 0).any():
       del indexSSELog,indexRMSELog
   if (rx != 0).any() and (ry != 1).any() and (rx != 1).any() and (((ry-cPower)/aPower)>0).any():
       del indexSSEPower, indexRMSEPower
   if SSES == '':
       del indexRMSES,indexSSES, SSESsort, Input, prompt, Rsort, Ssort
       del item, indexBest, BestSSE, BestRMSE, forprint, i, index, RMSESsort      
