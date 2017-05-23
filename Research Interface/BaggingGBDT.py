############################################################
# Bagging Decision Tree Classifier                         #
# @author Giorgos Demosthenous                             #
############################################################

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
import threading
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import DataLoader as dl

def loadData(dir,t,o,l):
        
        # Loading Twitter training features
        global tw_train_all
        global tw_train_all_recent
        global tw_train_base
        global tw_train_base_recent

        tw_train_all = dl.load_tw_train_all(dir,t,o,l)
        tw_train_all_recent = dl.load_tw_train_all_recent(dir,t,o,l)
        tw_train_base = dl.load_tw_train_base(dir,t,o,l)
        tw_train_base_recent = dl.load_tw_train_base_recent(dir,t,o,l)


        # Loading Youtube training features
        global yt_train_all
        global yt_train_all_recent
        global yt_train_base
        global yt_train_base_recent
        
        yt_train_all = dl.load_yt_train_all(dir,t,o,l)
        yt_train_all_recent = dl.load_yt_train_all_recent(dir,t,o,l)
        yt_train_base = dl.load_yt_train_base(dir,t,o,l)
        yt_train_base_recent = dl.load_yt_train_base_recent(dir,t,o,l)

        # Loading Labeling data
        global popular_train
        global popular_train_recent
        global viral_train
        global viral_train_recent

        labeled = dl.load_labeling(dir,t,o,l)
        popular_train = np.array(labeled[0])
        viral_train = np.array(labeled[1])

        # Create viral and popular list
        global vap_train
        vap_train=[]
        for i in range(popular_train.size):
                if ((popular_train[i]==1) and (viral_train[i]==1)):
                        vap_train.append(1)
                else:
                        vap_train.append(0)

        vap_train = np.array(vap_train)

        labeled_recent = dl.load_labeling_recent(dir,t,o,l)
        popular_train_recent = np.array(labeled_recent[0])
        viral_train_recent = np.array(labeled_recent[1])

        # Create viral and popular list
        global vap_train_recent
        vap_train_recent = []
        for i in range(popular_train_recent.size):
                if ((popular_train_recent[i]==1) and (viral_train_recent[i]==1)):
                        vap_train_recent.append(1)
                else:
                        vap_train_recent.append(0)

        vap_train_recent = np.array(vap_train_recent)

def classify(clf,X,Y):
        
        kf = KFold(n_splits=10, random_state=0, shuffle=False)
        
        maxShapePre = 0
        maxShapeRec = 0
        auc = 0
        metrics = []
        f1 = 0

        # Handling Errors in sets
        errorNaN = 0

        for train_index, test_index in kf.split(X):
                #print("TRAIN:", train_index, "TEST:", test_index)
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]
                
                clf.fit(X_train,Y_train)
                scores = clf.predict_proba(X_test)[:,1]
                        
                prediction = clf.predict(X_test)
                #Calculating F1 score
                f1 = f1 + f1_score(Y_test, prediction, average='macro')
                
                t_precision, t_recall, thresholds = precision_recall_curve(Y_test, scores)

                # Known Error of Scikit Learn
                # They recomended the following solution:
                for i in range(0,len(t_recall)):
                        if(np.isnan(t_recall[i])):
                           t_recall[i]=1.0

                if t_precision.shape[0] > maxShapePre :
                        precision = t_precision
                        maxShapePre = t_precision.shape[0]

                if t_recall.shape[0] > maxShapeRec :
                        recall = t_recall
                        maxShapeRec = t_recall.shape[0]

                # Known Error of Scikit Learn
                # Discarded corapted AUCs from average
                av_pre = average_precision_score(Y_test,scores)
                if(np.isnan(av_pre)):
                        errorNaN = errorNaN + 1;
                else:
                        auc = auc + av_pre
                #print(metrics.accuracy_score(prediction,Y_test))

        #Calculate average AUC
        auc = np.divide(auc,10-errorNaN)

        #Calculating average F1 score
        f1 = np.divide(f1,10)

        # Return metrics
        metrics.append(precision)
        metrics.append(recall)
        metrics.append(auc)
        metrics.append(f1)

        return metrics

def popular(dir,t,o,l,m,train,k,ytBin,twBin):

        metrics = []
        clf = BaggingClassifier(GradientBoostingClassifier(n_estimators=100))

        name = m+'_popular_'+str(t)+str(o)+str(l)+'.eva'
        
        fp = open(os.path.join(dir,name),'w')

        # All features - other(>)
        X = train[0]
        Y = popular_train      
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]

        
        fp.write(m+'_popular_all_old\t{0:0.4f}\n'.format(auc))
        # Baseline features - other(>)        
        X = train[1]
        Y = popular_train
        metrics = classify(clf,X,Y)
        precision_base = metrics[0]
        recall_base = metrics[1]
        auc_base = metrics[2]
        f1_base_other = metrics[3]
        fp.write(m+'_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))   

        # All features - recent(<)
        X = train[2]
        Y = popular_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]

        
        fp.write(m+'_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))

        # Baseline features - recent(>) 
        X = train[3]
        Y = popular_train_recent
        metrics = classify(clf,X,Y)
        precision_base_recent = metrics[0]
        recall_base_recent = metrics[1]
        auc_base_recent = metrics[2]
        f1_base_recent = metrics[3]
        fp.write(m+'_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

        # Calculating overall F1 score
        f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
        fp.write(m+'_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

        fig = plt.figure()
        plt.plot(recall,precision,label='All(>14 days) AUC={0:0.2f}'.format(auc))
        plt.plot(recall_recent,precision_recent,label='All(<=14 days) AUC={0:0.2f}'.format(auc_recent))
        plt.plot(recall_base,precision_base,label='Baseline(>14 days) AUC={0:0.2f}'.format(auc_base))
        plt.plot(recall_base_recent,precision_base_recent,label='Baseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.plot([0.5],[0.5])
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        text = m+ ' popular'
        plt.title(text)
        plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
        text = 'popular_'+m+'_features_'+str(t)+str(o)+str(l)+'.png'
        fig.savefig(os.path.join(dir,text))
        plt.close(fig)
                
        fp.close()

def viral(dir,t,o,l,m,train,k,ytBin,twBin):
        metrics = []
        clf = BaggingClassifier(GradientBoostingClassifier(n_estimators=100))

        name = m+'_viral_'+str(t)+str(o)+str(l)+'.eva'
        
        fp = open(os.path.join(dir,name),'w')

        # All features - other(>)
        X = train[0]
        Y = viral_train      
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]

        
        fp.write(m+'_viral_all_old\t{0:0.4f}\n'.format(auc))
        # Baseline features - other(>)        
        X = train[1]
        Y = viral_train
        metrics = classify(clf,X,Y)
        precision_base = metrics[0]
        recall_base = metrics[1]
        auc_base = metrics[2]
        f1_base_other = metrics[3]
        fp.write(m+'_viral_baseline_old\t{0:0.4f}\n'.format(auc_base))   

        # All features - recent(<)
        X = train[2]
        Y = viral_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]

        fp.write(m+'_viral_all_recent\t{0:0.4f}\n'.format(auc_recent))

        # Baseline features - recent(>) 
        X = train[3]
        Y = viral_train_recent
        metrics = classify(clf,X,Y)
        precision_base_recent = metrics[0]
        recall_base_recent = metrics[1]
        auc_base_recent = metrics[2]
        f1_base_recent = metrics[3]
        fp.write(m+'_viral_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

        # Calculating overall F1 score
        f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
        fp.write(m+'_viral_f1_score\t{0:0.4f}\n'.format(f1_average))

        fig = plt.figure()
        plt.plot(recall,precision,label='All(>14 days) AUC={0:0.2f}'.format(auc))
        plt.plot(recall_recent,precision_recent,label='All(<=14 days) AUC={0:0.2f}'.format(auc_recent))
        plt.plot(recall_base,precision_base,label='Baseline(>14 days) AUC={0:0.2f}'.format(auc_base))
        plt.plot(recall_base_recent,precision_base_recent,label='Baseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.plot([0.5],[0.5])
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        text = m+ ' viral'
        plt.title(text)
        plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
        text = 'viral_'+m+'_features_'+str(t)+str(o)+str(l)+'.png'
        fig.savefig(os.path.join(dir,text))
        plt.close(fig)
                
        fp.close()

def viralAndPopular(dir,t,o,l,m,train,k,ytBin,twBin):

        metrics = []
        clf = BaggingClassifier(GradientBoostingClassifier(n_estimators=100))
        name = m+'_viral_and_popular_'+str(t)+str(o)+str(l)+'.eva'
        
        fp = open(os.path.join(dir,name),'w')

        # All features - other(>)
        X = train[0]
        Y = vap_train      
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]
        
        fp.write(m+'_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
        # Baseline features - other(>)        
        X = train[1]
        Y = vap_train
        metrics = classify(clf,X,Y)
        precision_base = metrics[0]
        recall_base = metrics[1]
        auc_base = metrics[2]
        f1_base_other = metrics[3]
        fp.write(m+'_viral_and_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))   

        # All features - recent(<)
        X = train[2]
        Y = vap_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]

        fp.write(m+'_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))

        # Baseline features - recent(>) 
        X = train[3]
        Y = vap_train_recent
        metrics = classify(clf,X,Y)
        precision_base_recent = metrics[0]
        recall_base_recent = metrics[1]
        auc_base_recent = metrics[2]
        f1_base_recent = metrics[3]
        fp.write(m+'_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

        # Calculating overall F1 score
        f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
        fp.write(m+'_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

        fig = plt.figure()
        plt.plot(recall,precision,label='All(>14 days) AUC={0:0.2f}'.format(auc))
        plt.plot(recall_recent,precision_recent,label='All(<=14 days) AUC={0:0.2f}'.format(auc_recent))
        plt.plot(recall_base,precision_base,label='Baseline(>14 days) AUC={0:0.2f}'.format(auc_base))
        plt.plot(recall_base_recent,precision_base_recent,label='Baseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.plot([0.5],[0.5])
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        text = m+ ' viral and popular'
        plt.title(text)
        plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
        text = 'popular-viral_'+m+'_features_'+str(t)+str(o)+str(l)+'.png'
        fig.savefig(os.path.join(dir,text))
        plt.close(fig)
                
        fp.close()

def export(dir,t,o,l,yt_binary,tw_binary):
        # Load Data For Classification
        loadData(dir,t,o,l)

        # Predicting Popularity Using YouTube Features
        print('Predicting Popularity Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        popular(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Popularity Using Twitter Features
        print('Predicting Popularity Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        popular(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Popularity Using All Features
        print('Predicting Popularity Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        popular(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using YouTube Features
        print('Predicting Virality Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        viral(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using Twitter Features
        print('Predicting Virality Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        viral(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using All Features
        print('Predicting Virality Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        viral(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using YouTube Features
        print('Predicting Virality and Popularity Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using Twitter Features
        print('Predicting Virality and Popularity Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using All Features
        print('Predicting Virality and Popularity Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')
        
def main():

        # Input
        if len(sys.argv) <6:
                print(len(sys.argv))
                print ("Arguments needed")
                print ("Arg1:\t Data Directory")
                print ("Arg2:\t Training Window")
                print ("Arg3:\t Offset")
                print ("Arg4:\t Labeling Window")
                print ("Arg5:\t Youtube Features Binary")
                print ("Arg6:\t Twitter Features Features Binary")
                sys.exit(1)
                
        dir =  sys.argv[1]
        t = int(sys.argv[2])
        o = int(sys.argv[3])
        l = int(sys.argv[4])
        yt_binary = sys.argv[5]
        tw_binary = sys.argv[6]

        # Load Data For Classification
        loadData(dir,t,o,l)

        # Predicting Popularity Using YouTube Features
        print('Predicting Popularity Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        popular(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Popularity Using Twitter Features
        print('Predicting Popularity Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        popular(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Popularity Using All Features
        print('Predicting Popularity Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        popular(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using YouTube Features
        print('Predicting Virality Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        viral(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using Twitter Features
        print('Predicting Virality Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        viral(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality Using All Features
        print('Predicting Virality Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        viral(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using YouTube Features
        print('Predicting Virality and Popularity Using YouTube Features')
        m  = 'youtube'
        train = []
        train.append(yt_train_all)
        train.append(yt_train_base)
        train.append(yt_train_all_recent)
        train.append(yt_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,0,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using Twitter Features
        print('Predicting Virality and Popularity Using Twitter Features')
        m  = 'twitter'
        train = []
        train.append(tw_train_all)
        train.append(tw_train_base)
        train.append(tw_train_all_recent)
        train.append(tw_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,1,yt_binary,tw_binary)
        print('Done')

        # Predicting Virality and Popularity Using All Features
        print('Predicting Virality and Popularity Using All Features')
        m  = 'both'
        train = []
        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))  
        train.append(x_train_all)
        train.append(x_train_base)
        train.append(x_train_all_recent)
        train.append(x_train_base_recent)
        viralAndPopular(dir,t,o,l,m,train,2,yt_binary,tw_binary)
        print('Done')

if __name__== '__main__':
        main()
