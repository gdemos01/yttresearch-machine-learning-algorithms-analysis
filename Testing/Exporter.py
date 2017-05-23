############################################################
# User Interface for Machine Learning experiments          #
# @author Giorgos Demosthenous                             #
############################################################

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import VotingClassifier

from sklearn import svm

import os
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
import DataLoader as dl
import PopularityClassifier
import ViralityClassifier
import ViralityAndPopularityClassifier
import PopularityClassifier_type2
import ViralityClassifier_type2
import ViralityAndPopularityClassifier_type2

def renamePopular(dir,t,o,l):
        name = 'youtube_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'youtube_popular.eva'),os.path.join(dir,name))
        name = 'twitter_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'twitter_popular.eva'),os.path.join(dir,name))
        name = 'both_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'both_popular.eva'),os.path.join(dir,name))
        name = 'popular_youtube_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular_youtube_features.png'),os.path.join(dir,name))
        name = 'popular_twitter_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular_twitter_features.png'),os.path.join(dir,name))
        name = 'popular_all_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular_all_features.png'),os.path.join(dir,name))
        
def renameViral(dir,t,o,l):        
        name = 'youtube_viral_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'youtube_viral.eva'),os.path.join(dir,name))        
        name = 'twitter_viral_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'twitter_viral.eva'),os.path.join(dir,name))
        name = 'both_viral_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'both_viral.eva'),os.path.join(dir,name))
        name = 'viral_youtube_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'viral_youtube_features.png'),os.path.join(dir,name))
        name = 'viral_twitter_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'viral_twitter_features.png'),os.path.join(dir,name))
        name = 'viral_all_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'viral_all_features.png'),os.path.join(dir,name))
 

def renameVAP(dir,t,o,l):
        name = 'youtube_viral_and_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'youtube_viral_and_popular.eva'),os.path.join(dir,name))
        name = 'twitter_viral_and_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'twitter_viral_and_popular.eva'),os.path.join(dir,name))
        name = 'both_viral_and_popular_'+str(t)+str(o)+str(l)+'.eva'
        os.rename(os.path.join(dir,'both_viral_and_popular.eva'),os.path.join(dir,name))
        name = 'popular-viral_youtube_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular-viral_youtube_features.png'),os.path.join(dir,name))
        name = 'popular-viral_twitter_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular-viral_twitter_features.png'),os.path.join(dir,name))
        name = 'popular-viral_all_features_'+str(t)+str(o)+str(l)+'.png'
        os.rename(os.path.join(dir,'popular-viral_all_features.png'),os.path.join(dir,name))

def isExported(dir,t,o,l):
        
        name = 'youtube_popular_'+str(t)+str(o)+str(l)+'.eva'
        exists = os.path.isfile(os.path.join(dir,name))
        name = 'youtube_viral_'+str(t)+str(o)+str(l)+'.eva'
        exists =  os.path.isfile(os.path.join(dir,name))
        name = 'youtube_viral_and_popular_'+str(t)+str(o)+str(l)+'.eva'
        exists =  os.path.isfile(os.path.join(dir,name))

        return exists
                
def classify(dir,clf,action):

        for t in range(1,8):
                for o in range(0,8):
                        for l in range(1,8):
                                if t==1 or t==2 or t==3 or t==7:
                                        if o==0 or o==1 or o==3 or o==7:
                                                if l==1 or l==2 or l==3 or l==7:
                                                        sum = t+o+l
                                                        if(not isExported(dir,t,o,l) and sum<=14):
                                                                if int(action) == 1:
                                                                        PopularityClassifier.loadData(dir,t,o,l)
                                                                        PopularityClassifier.twitterPopular(dir,clf,0)
                                                                        PopularityClassifier.youtubePopular(dir,clf,0)
                                                                        PopularityClassifier.bothPopular(dir,clf,0)
                                                                        renamePopular(dir,t,o,l)
                                                                elif int(action) == 2:
                                                                        ViralityClassifier.loadData(dir,t,o,l)
                                                                        ViralityClassifier.twitterViral(dir,clf,0)
                                                                        ViralityClassifier.youtubeViral(dir,clf,0)
                                                                        ViralityClassifier.bothViral(dir,clf,0)
                                                                        renameViral(dir,t,o,l)
                                                                elif int(action) == 3:
                                                                        ViralityAndPopularityClassifier.loadData(dir,t,o,l)
                                                                        ViralityAndPopularityClassifier.youtubeViralAndPopular(dir,clf,0)
                                                                        ViralityAndPopularityClassifier.twitterViralAndPopular(dir,clf,0)
                                                                        ViralityAndPopularityClassifier.bothViralAndPopular(dir,clf,0)
                                                                        renameVAP(dir,t,o,l)

def classify_type2(dir,clf,action):

        for t in range(1,8):
                for o in range(0,8):
                        for l in range(1,8):
                                if t==1 or t==2 or t==3 or t==7:
                                        if o==0 or o==1 or o==3 or o==7:
                                                if l==1 or l==2 or l==3 or l==7:
                                                        sum = t+o+l
                                                        if(not isExported(dir,t,o,l) and sum<=14):
                                                                if int(action) == 1:
                                                                        PopularityClassifier_type2.loadData(dir,t,o,l)
                                                                        PopularityClassifier_type2.twitterPopular(dir,clf,0)
                                                                        PopularityClassifier_type2.youtubePopular(dir,clf,0)
                                                                        PopularityClassifier_type2.bothPopular(dir,clf,0)
                                                                        renamePopular(dir,t,o,l)
                                                                elif int(action) == 2:
                                                                        ViralityClassifier_type2.loadData(dir,t,o,l)
                                                                        ViralityClassifier_type2.twitterViral(dir,clf,0)
                                                                        ViralityClassifier_type2.youtubeViral(dir,clf,0)
                                                                        ViralityClassifier_type2.bothViral(dir,clf,0)
                                                                        renameViral(dir,t,o,l)
                                                                elif int(action) == 3:
                                                                        ViralityAndPopularityClassifier_type2.loadData(dir,t,o,l)
                                                                        ViralityAndPopularityClassifier_type2.youtubeViralAndPopular(dir,clf,0)
                                                                        ViralityAndPopularityClassifier_type2.twitterViralAndPopular(dir,clf,0)
                                                                        ViralityAndPopularityClassifier_type2.bothViralAndPopular(dir,clf,0)
                                                                        renameVAP(dir,t,o,l)
         
                                                                                                                       
        
def exportPresentationData(classifier,action,dir):
        
        if int(classifier)==1:
                clf = GradientBoostingClassifier()
                classify(dir,clf,action)
        elif int(classifier) == 2:
                clf = LogisticRegression()
                classify(dir,clf,action)
        elif int(classifier) == 3:
                clf = KNeighborsClassifier(n_neighbors=5)
                classify(dir,clf,action)
        elif int(classifier) == 4:
                clf = DecisionTreeClassifier()
                classify(dir,clf,action)
        elif int(classifier) == 5:
                clf = svm.LinearSVC()
                classify_type2(dir,clf,action)
        elif int(classifier) == 6:
                clf = RandomForestClassifier()
                classify(dir,clf,action)
        elif int(classifier) == 7:
                clf = ExtraTreesClassifier()
                classify(dir,clf,action)
        elif int(classifier) == 8:
                clf = IsolationForest()
                classify_type2(dir,clf,action)
        elif int(classifier) == 9:
                clf = AdaBoostClassifier(n_estimators=100)
                classify(dir,clf,action)
        elif int(classifier) == 10:
                clf = BaggingClassifier(DecisionTreeClassifier())
                classify(dir,clf,action)
        elif int(classifier) == 11:
                clf1 = GradientBoostingClassifier()
                clf2 = AdaBoostClassifier()
                clf = VotingClassifier(estimators=[('abdt', clf1), ('gbdt', clf2)], voting='soft')
                classify(dir,clf,action)

        
        

def userInput():
        print('Welcome')
        print('Choose Algorithm to export data')
        print('\t1. Gradient Boosting Decision Tree')
        print('\t2. Logistic Regression')
        print('\t3. K Nearest Neighbours')
        print('\t4. Decision Tree')
        print('\t5. SVM - LinearSVC')
        print('\t6. Random Forest')
        print('\t7. Extra Trees')
        print('\t8. Isolation Forest')
        print('\t9. AdaBoost Decision Tree')
        print('\t10. Bagging Decision Tree')
        print('\t11. Voting - AdaBoost/GradientBoosting Decision Tree')

        dir = input('Give Data Directory: ')
        
        # Exporting Popularity
        print('Exporting Popularity')
        exportPresentationData(classifier,1,dir)

        # Exporting Virality
        print('Exporting Virality')
        exportPresentationData(classifier,2,dir)
        
        # Exporting Virality and Popularity
        print('Exporting Popularity and Virality')
        exportPresentationData(classifier,3,dir)
                

def main():
        userInput()
if __name__=='__main__':
        main()
