# All decimal 3 places
import math
# Function to compute mean
def mean(first_list):
    # mean Logic 
    if(checktype(first_list)==False):
        return 0
    addition_of_rows= summation(first_list)
    mean_value = addition_of_rows/len(first_list)
    mean_value=round(mean_value,3)

    return round(mean_value,3)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    if(checktype(first_list)==False):
        return 0
    list_returned=list(first_list)
    list_returned= sorting(list_returned)
    #print(first_list)
    length= len(first_list)
    median_value=0
    if(length%2==0):
        median_1 =int(length/2) 
        median_2 = int((length/2)-1)
        median_value= (list_returned[median_1]+list_returned[median_2])/2
    else:
        median_value = list_returned[int((length-1)/2)]
    
    return round(median_value,3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if(checktype(first_list)==False):
        return 0
    standard_deviation_value=0
    # Computed the Variance Value as its square root will give SD
    variance_value = variance(first_list)
    standard_deviation_value=math.sqrt(variance_value)
    standard_deviation_value = round(standard_deviation_value,3)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if(checktype(first_list)==False):
        return 0
    #Taken Mean using earlier defined Mean Function
    mean_value= mean(first_list)
    variance_value=0
    sum_of_deviation_square=0
    for i in first_list:
        deviation_abs= abs(i-mean_value)
        sum_of_deviation_square+=deviation_abs*deviation_abs
    
    variance_value = round(sum_of_deviation_square/len(first_list),3)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    #Guard Code for checking the length and type of elements in list
    if(checktype(first_list)==False):
        return 0
    if(checktype(second_list)==False):
        return 0
    if(check_length(first_list,second_list)==False):
        return 0

    mse_value= mse(first_list,second_list)
    rmse_value_full=math.sqrt(mse_value)
    rmse_value=round(rmse_value_full,3)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic

    #Guard Code for checking the length and type of elements in list
    if(checktype(first_list)==False):
        return 0
    if(checktype(second_list)==False):
        return 0
    if(check_length(first_list,second_list)==False):
        return 0
    
    square_deviation_sum= 0
    first_list_sorted=first_list
    #print(first_list)
    second_list_sorted = second_list
    for i in range(0,len(first_list)):
        square_deviation_sum+=(first_list_sorted[i]-second_list_sorted[i])*(first_list_sorted[i]-second_list_sorted[i])
    
    mse_value = square_deviation_sum/len(first_list)
    mse_value= round(mse_value,3)

    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if(checktype(first_list)==False):
        return 0
    if(checktype(second_list)==False):
        return 0
    if(check_length(first_list,second_list)==False):
        return 0
    absolute_deviation_sum= 0
    first_list_sorted=list(first_list)
    #print(first_list)
    second_list_sorted = list(second_list)
    for i in range(0,len(first_list)):
        absolute_deviation_sum+=abs(first_list_sorted[i]-second_list_sorted[i])
    
    mae_value = absolute_deviation_sum/len(first_list)
    mae_value= round(mae_value,3)
    
    return mae_value



# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if(checktype(first_list)==False):
        return 0
    if(checktype(second_list)==False):
        return 0
    if(check_length(first_list,second_list)==False):
        return 0
    
    square_deviation_sum= 0
    first_list_sorted=first_list
    #print(first_list)
    second_list_sorted = second_list
    for i in range(0,len(first_list)):
        square_deviation_sum+=(first_list_sorted[i]-second_list_sorted[i])*(first_list_sorted[i]-second_list_sorted[i])

    mean_value=mean(first_list)
    deviation= 0
    for i in range(0,len(first_list)):
        deviation+= (first_list[i]-mean_value)*(first_list[i]-mean_value)

    intermediate= square_deviation_sum/deviation
    nse_value= 1-intermediate
    nse_value=round(nse_value,3)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if(checktype(first_list)==False):
        return 0
    if(checktype(second_list)==False):
        return 0
    if(check_length(first_list,second_list)==False):
        return 0

    mean_x= mean(first_list)
    mean_y=mean(second_list)

    sigma=0
    for i in range(len(first_list)):
        sigma+= (first_list[i]-mean_x)*(second_list[i]-mean_y)
    
    denominator= len(first_list)*standard_deviation(first_list)*standard_deviation(second_list)
    pcc_value= sigma/denominator
    pcc_value = round(pcc_value,3)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    if(checktype(first_list)==False):
        return 0
    mean_x= mean(first_list)
    sigma=0
    for i in range(len(first_list)):
        sigma+= (first_list[i]-mean_x)*(first_list[i]-mean_x)*(first_list[i]-mean_x)
    sd= standard_deviation(first_list)
    skewness_value=(sigma)/(sd*sd*sd*len(first_list))
    skewness_value= round(skewness_value,3)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    if(checktype(first_list)==False):
        return 0
    length = len(first_list)
    sorted_list=first_list
    #print(first_list,"Here is Bug")
    for i in range(length):

        for j in range(0,length-i-1):
            if(sorted_list[j]>sorted_list[j+1]):
                sorted_list[j],sorted_list[j+1]=sorted_list[j+1],sorted_list[j]

     
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    if(checktype(first_list)==False):
        return 0
    
    kurtosis_value=0
    mean_x= mean(first_list)
    sigma=0
    for i in range(len(first_list)):
        sigma+= (first_list[i]-mean_x)*(first_list[i]-mean_x)*(first_list[i]-mean_x)*(first_list[i]-mean_x)
    sd= standard_deviation(first_list)
    kurtosis_value=(sigma)/(sd*sd*sd*sd*len(first_list))
    kurtosis_value= round(kurtosis_value,3)

    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    if(checktype(first_list)==False):
        return 0
    summation_value=0
    for i in (first_list):
        summation_value+=i
    summation_value = round(summation_value,3)
    return summation_value


def checktype(first_list):
    status=True
    for i in first_list:
        if(isinstance(i,(int,float))==False):
            status=False
            break
    return status


def check_length(first_list,second_list):
    if(len(first_list)==len(second_list)):
        return True
    else:
        return False