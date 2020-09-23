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
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if(checktype(first_list)==False):
        return 0
    variance_value = variance(first_list)
    standard_deviation_value=math.sqrt(variance_value)
    standard_deviation_value = round(standard_deviation_value,3)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if(checktype(first_list)==False):
        return 0
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
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic

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

def sorted_list(first_list):
    if(checktype(first_list)==False):
        return 0
    length = len(first_list)
    for i in range(length):

        for j in range(0,length-i-1):
            if(first_list[j]>first_list[j+1]):
                first_list[j],first_list[j+1]=first_list[j+1],first_list[j]

    return first_list