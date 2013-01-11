'''
Created on 27.11.2012

@author: mla-mma
'''
import random
class MarkovChain : 
    #  "Class documentation goes here"
    def Create_List_Pairs (self, file):
        "This function create a list of probabilities which are extracted from the file that the user give. It creates a vector for each time step which contains P(t) and P(t+1)"
        data = open(file,"r")
        list_data = data.readlines()
        list_new_data = []

        for i in list_data:
            str1ng=(i.strip('\n')).split(' ')
            list_new_data.append(str1ng[1])
        #print list_new_data
        list_pairs=[]
        for j in range (1,len(list_new_data)):
            pair=[list_new_data[j-1], list_new_data[j]]
            list_pairs.append(pair)
        return list_pairs

    def Parameter_Mobility (self, mobility):
        "This function assign the value of the mobility."
        if mobility == "High": 
            u = 5.667
        elif mobility == "Medium":
            u = 1.1
        else:
            u = 0.2    
        return u

    def Markov (self, list_pairs, u, place=False):
        u_new=u
        for i in range (0,len(list_pairs)):
            #print i
            Pt=float(list_pairs[i][0])
            Pt1=float(list_pairs[i][1])
            #print Pt
            #print Pt1
            if (Pt==0):
                T01=(((u-1)/(u+1))*Pt)+Pt1
                T11=0 
            elif (Pt1==0):
                T01=0
                T11=0
            else:
                T01=(((u-1)/(u+1))*Pt)+Pt1
                T11=((Pt-1)/Pt)*((((u-1)/(u+1))*Pt)+Pt1)+(Pt1/Pt)
            #print T11
            # print T01
            if u==0.2: 
                #while T01<0 or T01>1 or T11<0 or T11>1:
                    while T01<0: 
                        u_new=u_new+0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                        #  print "First while T11 =", T11, "T01 =", T01
                    while T11>1:
                        u_new=u_new+0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                        #  print "Second while T11 =", T11, "T01 =", T01
                    while T11<0:
                        u_new=u_new-0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                        #  print "3rd while T11 =", T11, "T01 =", T01
            if u==1.1:
                #while T01<0 or T01>1 or T11<0 or T11>1: 
                    while T01<0: 
                        u_new=u_new+0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                      #  print "First while T11 =", T11, "T01 =", T01
                    while T01>1: 
                        u_new=u_new-0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                      #  print "2nd while T11 =", T11, "T01 =", T01
                    while T11>1:
                        u_new=u_new+0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                     #   print "3rd while T11 =", T11, "T01 =", T01
                    while T11<0:
                        u_new=u_new-0.1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                      #  print "4rd while T11 =", T11, "T01 =", T01
                    
            if u==5.667: 
                #while T01<0 or T01>1 or T11<0 or T11>1:
                    while T01>1: 
                        u_new=u_new-1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                      #  print "1st while T11 =", T11, "T01 =", T01
                    while T01<0:
                        u_new=u_new+1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                       # print "2nd while T11 =", T11, "T01 =", T01
                    while T11<0:
                        u_new=u_new-1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                       # print "3rd while T11 =", T11, "T01 =", T01
                    while T11>1:
                        u_new=u_new+1
                        T01=(((u_new-1)/(u_new+1))*Pt)+Pt1
                        T11=((Pt-1)/Pt)*((((u_new-1)/(u_new+1))*Pt)+Pt1)+(Pt1/Pt)
                       # print "4rd while T11 =", T11, "T01 =", T01
                    
            #if u_new<>u: 
               # print "Parameter of mobility was adapted"
               # print "u=", u
                #print "u_new=", u_new
            if T11<0 or T01<0: 
                print ("Warning! Transition probability is negative!")
            if T01>1 or T11>1: 
                print ("Warning! Transition probability is bigger than 1!")
    
            #print "T01 =", T01
            #print "T11 =", T11        
            pb_ran=random.uniform(0.0,1.0)
            if not place and pb_ran<=T01:
                place=True
            elif place and pb_ran<=T11:
                place=True
            else:
                place=False 
            #print "Random=", pb_ran
            print (place)
            #print " "
            u_new=u

    
    
