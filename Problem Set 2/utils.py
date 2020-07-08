import matplotlib.pyplot as plt

def plot_roc(fpr, tpr, filename):
    """
    Note: A different path to save figure
    """
    plt.figure()
    plt.plot(fpr, tpr, color='red', label='ROC Graph')
    plt.plot([0, 1], [0, 1], color='blue')
    plt.xlabel('fpr (False Positive Rate)')
    plt.ylabel('tpr (True Positive Rate)')
    plt.title('ROC Graph')
    plt.savefig(filename)
    #reference line; ROC curve
    
def risk_factors(feature_names, coeff):
    """
    For 4(a): Look at the top 5 risk factors of mortality and the lowest 5.
    So: use absolute value!
    For 4(b): Report the top 5 words associated with a high risk of mortality and the lowest 5.
    So: DO NOT use absolute value!
    """
   
    
    coeff_of_feature = []
#   print("All feature coefficients with signs: ")
    for index in range(len(feature_names)):
        coeff_of_feature.append([coeff[0][index], feature_names[index]])
 
    print("------------------------------")
    
    print("Sort the value itself: ")
    coeff_of_feature = []
    for index in range(len(feature_names)):
        coeff_of_feature.append([coeff[0][index], feature_names[index]])

    coeff_of_feature = sorted(coeff_of_feature)
    print("Top 5 risk factors: ")
    for coefficient, factor in coeff_of_feature[-5:]:
        print(coefficient, factor)
    
#     f = open("output.txt", "a")
#     f.write(item for item in coeff_of_feature)
#     f.close()

    print("Lowest 5 risk factors: ")
    for coefficient, factor in coeff_of_feature[0:5]:
        print(coefficient, factor)
    
    print("------------------------------")
    print("Sort using absolute value: ")
    coeff_of_feature = []
    for index in range(len(feature_names)):
        coeff_of_feature.append([abs(coeff[0][index]), feature_names[index]])

    coeff_of_feature = sorted(coeff_of_feature)
    print("Top 5 risk factors: ")
    for coefficient, factor in coeff_of_feature[-5:]:
        print(coefficient, factor)

    print("Lowest 5 risk factors: ")
    for coefficient, factor in coeff_of_feature[0:5]:
        print(coefficient, factor)
        
   
    