import math;
import sys

def info(yesNum, noNum):
    float_yes = float(yesNum);
    float_no = float(noNum);
    float_tot = float(float_yes + float_no);
    firstVal = 0; 
    secondVal = 0;
    if float_yes != 0:
        firstVal = -(float_yes/float_tot) * math.log((float_yes/float_tot),2) 
    if float_no != 0:
        secondVal = -(float_no/float_tot) * math.log((float_no/float_tot),2)
    return firstVal + secondVal;

def infoAverage(infoValues, total_instances):
    average = 0;
    for i in range(len(infoValues)):
        infoValue_i = info(infoValues[i][0], infoValues[i][1]);
        print "info[%d,%d] = %f" % (infoValues[i][0],infoValues[i][1],infoValue_i);
        average += (float(infoValues[i][0] + infoValues[i][1])/float(total_instances)) * infoValue_i;
    print "The information value average is %f" % (average);
    return average;

def informationGain(average, yes_instances, no_instances, total_instances):
    gain = info(yes_instances, no_instances) - average;    
    print "The total information gain is %f" % (gain);
    return gain;

def startInfoGain():
    infoValues = [];
    total_instances = 0;
    yes_instances = 0;
    no_instances = 0;
    print "To begin, start entering x and y values for each information value (i.e. info[x,y]). Each value must be an integer. "
    try:
        while True:
            
            numYes = int(raw_input("Enter the number of yes instances for the attribute-value (i.e. x values):"));
            numNo = int(raw_input("Enter the number of no instances for the attribute-value (i.e. y values):"));
            infoValues.append([numYes, numNo]);
            print "info([%d,%d]) has been added as an information value to the list of information values" % (numYes,numNo);
            print "Enter any letter to exit input for new information values.";
            total_instances += numYes + numNo;
            yes_instances += numYes;
            no_instances += numNo;
    except ValueError:
       return informationGain(infoAverage(infoValues, total_instances), yes_instances, no_instances, total_instances);

if __name__ == "__main__":
    startInfoGain();
