############################################################
# Decision Tree Classifer                                  #
# @author Giorgos Demosthenous                             #
############################################################

from sklearn.tree import DecisionTreeClassifier
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

def exportImportance(dir,kind,name,window,yt_binary,tw_binary,global_importance):

        fp = open(os.path.join(dir,name+'.imp' ),'w')

        features_twitter = []
        features_youtube = []

        # Adding appropriate features according to the binary given
        if tw_binary[0] == '1' :
                features_twitter.append("tw_user_followers")
        if tw_binary[1] == '1' :
                features_twitter.append("tw_user_verified")
        if tw_binary[2] == '1' :
                features_twitter.append("tw_user_friends")
        if tw_binary[3] == '1' :
                features_twitter.append("tw_tweets_dif")
        if tw_binary[4] == '1' :
                features_twitter.append("tw_orig_tweets_dif")
        if tw_binary[5] == '1' :
                features_twitter.append("tw_retweets_dif")
        if tw_binary[6] == '1' :
                features_twitter.append("tw_user_favorites_dif")
        if tw_binary[7] == '1' :
                features_twitter.append("tw_eng_dif")
        if tw_binary[8] == '1' :
                features_twitter.append("tw_sp_dif")
        if tw_binary[9] == '1' :
                features_twitter.append("tw_user_eng_dif")
        if tw_binary[10] == '1' :
                features_twitter.append("tw_user_sp_dif")
        if tw_binary[11] == '1' :
                features_twitter.append("tw_user_statuses_dif")
        if tw_binary[12] == '1' :
                features_twitter.append("tw_hashtags_dif")
        if tw_binary[13] == '1' :
                features_twitter.append("tw_tweets_acc")
        if tw_binary[14] == '1' :
                features_twitter.append("tw_orig_tweets_acc")
        if tw_binary[15] == '1' :
                features_twitter.append("tw_retweets_acc")
        if tw_binary[16] == '1' :
                features_twitter.append("tw_user_favorites_acc")
        if tw_binary[17] == '1' :
                features_twitter.append("tw_eng_acc")
        if tw_binary[18] == '1' :
                features_twitter.append("tw_sp_acc")
        if tw_binary[19] == '1' :
                features_twitter.append("tw_user_eng_acc")
        if tw_binary[20] == '1' :
                features_twitter.append("tw_user_sp_acc")
        if tw_binary[21] == '1' :
                features_twitter.append("tw_user_statuses_acc")
        if tw_binary[22] == '1' :
                features_twitter.append("tw_hashtags_acc")

        # Twitter days
        for i in range(0,window):
                if tw_binary[23] == '1' :
                        tw_tweets = "tw_tweets_"+str((i+1))
                        features_twitter.append(tw_tweets)
                if tw_binary[24] == '1' :
                        tw_orig_tweets = "tw_orig_tweets_"+str((i+1))
                        features_twitter.append(tw_orig_tweets)
                if tw_binary[25] == '1' :
                        tw_retweets = "tw_retweets_"+str((i+1))
                        features_twitter.append(tw_retweets)
                if tw_binary[26] == '1' :
                        tw_user_favorites = "tw_user_favorites_"+str((i+1))
                        features_twitter.append(tw_user_favorites)
                if tw_binary[27] == '1' :
                        tw_eng = "tw_eng_"+str((i+1))
                        features_twitter.append(tw_eng)
                if tw_binary[28] == '1' :
                        tw_sp = "tw_sp_"+str((i+1))
                        features_twitter.append(tw_sp)
                if tw_binary[29] == '1' :
                        tw_user_eng = "tw_user_eng_"+str((i+1))
                        features_twitter.append(tw_user_eng)
                if tw_binary[30] == '1' :
                        tw_user_sp = "tw_user_sp_"+str((i+1))
                        features_twitter.append(tw_user_sp)
                if tw_binary[31] == '1' :
                        tw_user_statuses = "tw_user_statuses_"+str((i+1))
                        features_twitter.append(tw_user_statuses)
                if tw_binary[32] == '1' :
                        tw_hashtags = "tw_hashtags_"+str((i+1))
                        features_twitter.append(tw_hashtags)
                
        # Twitter ratios
        for i in range(0,window):
                if tw_binary[33] == '1' :
                        ratioTweets = "ratioTweets_"+str((i+1))
                        features_twitter.append(ratioTweets)
                if tw_binary[34] == '1' :
                        ratioOrigTweets = "ratioOrigTweets_"+str((i+1))
                        features_twitter.append(ratioOrigTweets)
                if tw_binary[35] == '1' :
                        ratioRetweets = "ratioRetweets_"+str((i+1))
                        features_twitter.append(ratioRetweets)
                if tw_binary[36] == '1' :
                        ratioUserFavorites = "ratioUserFavorites_"+str((i+1))
                        features_twitter.append(ratioUserFavorites)
                if tw_binary[37] == '1' :
                        ratioTwEn = "ratioTwEn_"+str((i+1))
                        features_twitter.append(ratioTwEn)
                if tw_binary[38] == '1' :
                        ratioTwSp = "ratioTwSp_"+str((i+1))
                        features_twitter.append(ratioTwSp)
                if tw_binary[39] == '1' :
                        ratioUserEng = "ratioUserEng_"+str((i+1))
                        features_twitter.append(ratioUserEng)
                if tw_binary[40] == '1' :
                        ratioUserSp = "ratioUserSp_"+str((i+1))
                        features_twitter.append(ratioUserSp)
                if tw_binary[41] == '1' :
                        ratioUserStatuses = "ratioUserStatuses_"+str((i+1))
                        features_twitter.append(ratioUserStatuses)
                if tw_binary[42] == '1' :
                        ratioHashtags = "ratioHashtags_"+str((i+1))
                        features_twitter.append(ratioHashtags)
                

        if yt_binary[0] == '1' :
                features_youtube.append("category")
        if yt_binary[1] == '1' :
                features_youtube.append("artificial_category")
        if yt_binary[2] == '1' :
                features_youtube.append("video_duration")
        if yt_binary[3] == '1' :
                features_youtube.append("comments_sentiment_neg")
        if yt_binary[4] == '1' :
                features_youtube.append("comments_sentiment_neu")
        if yt_binary[5] == '1' :
                features_youtube.append("comments_sentiment_pos")
        if yt_binary[6] == '1' :
                features_youtube.append("comments_sentiment_compound")
        if yt_binary[7] == '1' :
                features_youtube.append("channel_uploads")
        if yt_binary[8] == '1' :
                features_youtube.append("channel_subscribers")
        if yt_binary[9] == '1' :
                features_youtube.append("channel_views")
        if yt_binary[10] == '1' :
                features_youtube.append("channel_comments")
        if yt_binary[11] == '1' :
                features_youtube.append("views_dif")
        if yt_binary[12] == '1' :
                features_youtube.append("likes_dif")
        if yt_binary[13] == '1' :
                features_youtube.append("dislikes_dif")
        if yt_binary[14] == '1' :
                features_youtube.append("comments_dif")
        if yt_binary[15] == '1' :
                features_youtube.append("views_acc")
        if yt_binary[16] == '1' :
                features_youtube.append("likes_acc")
        if yt_binary[17] == '1' :
                features_youtube.append("dislikes_acc")
        if yt_binary[18] == '1' :
                features_youtube.append("comments_acc")
        

        for i in range(0,window):
                if yt_binary[19] == '1' :
                        views_n = "views_"+str((i+1))
                        features_youtube.append(views_n)
                if yt_binary[20] == '1' :
                        likes_n = "likes_"+str((i+1))
                        features_youtube.append(likes_n)
                if yt_binary[21] == '1' :
                        dislikes_n = "dislikes_"+str((i+1))
                        features_youtube.append(dislikes_n)
                if yt_binary[22] == '1' :
                        comments_n = "comments_"+str((i+1))
                        features_youtube.append(comments_n)             
                
        for i in range(0,window):
                if yt_binary[23] == '1' :
                        ageRatioViews_n = "ageRatioViews_"+str((i+1))
                        features_youtube.append(ageRatioViews_n)
                if yt_binary[24] == '1' :
                        ageRatioLikes_n = "ageRatioLikes_"+str((i+1))
                        features_youtube.append(ageRatioLikes_n)
                if yt_binary[25] == '1' :
                        ageRatioDislikes_n = "ageRatioDislikes_"+str((i+1))
                        features_youtube.append(ageRatioDislikes_n)
                if yt_binary[26] == '1' :
                        ageRatioComments_n = "ageRatioComments_"+str((i+1))
                        features_youtube.append(ageRatioComments_n)

        for i in range(0,window):
                if yt_binary[27] == '1' :
                        ratioViews_n = "ratioViews_"+str((i+1))
                        features_youtube.append(ratioViews_n)
                if yt_binary[28] == '1' :
                        ratioLikes_n = "ratioLikes_"+str((i+1))
                        features_youtube.append(ratioLikes_n)
                if yt_binary[29] == '1' :
                        ratioDislikes_n = "ratioDislikes_"+str((i+1))
                        features_youtube.append(ratioDislikes_n)
                if yt_binary[30] == '1' :
                        ratioComments_n = "ratioComments_"+str((i+1))
                        features_youtube.append(ratioComments_n)
                        
        features = []
        if kind == 0:
                features = features_youtube

        if kind == 1:
                features = features_twitter

        if kind == 2:
                features = np.hstack((features_twitter,features_youtube))

        list_importance=[]
        i=0;
        while i < len(global_importance):
                list_importance.append([features[i],global_importance[i]])
                i = i + 1
        list_importance.sort(key=lambda x: x[1])

        i = len(list_importance)-1
        count =1;
        while i >= 0:
                per = list_importance[i][1] *100
                fp.write(str(count)+'\t'+list_importance[i][0]+'\t{0:0.6f}\n'.format(per))
                count = count +1
                i = i-1
        fp.close()

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
        clf = DecisionTreeClassifier()

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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m + '_popular_all_old_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
        
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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m+ '_popular_all_recent_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
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
        clf = DecisionTreeClassifier()

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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m + '_viral_all_old_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
        
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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m+ '_viral_all_recent_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
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
        clf = DecisionTreeClassifier()

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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m + '_viral_and_popular_all_old_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
        
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

        
        # Calculating importance than >days(other)
        importance = clf.feature_importances_
        global_importance = importance
        text = m+ '_viral_and_popular_all_recent_'+str(t)+str(o)+str(l)
        exportImportance(dir,k,text,t,ytBin,twBin,global_importance)
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
