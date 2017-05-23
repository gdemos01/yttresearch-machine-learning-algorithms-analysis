############################################################
# Gradient Boosting Classifer for vapity Prediction    #
# @author Giorgos Demosthenous                             #
############################################################

import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
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

        # Calculating Window
        global window
        window = int((yt_train_all.shape[1] - 12)/12)

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

def exportImportance(dir,kind,name):

        fp = open(os.path.join(dir,name+'.imp' ),'w')

        features_twitter = ["tw_user_followers",
                        "tw_user_verified",
                        "tw_user_friends",
                        "tw_tweets_dif",
                        "tw_orig_tweets_dif",
                        "tw_retweets_dif",
                        "tw_quotes_dif",
                        "tw_user_favorites_dif",
                        "tw_eng_dif",
                        "tw_user_eng_dif",
                        "tw_user_statuses_dif",
                        "tw_hashtags_dif",
                        "tw_tweets_acc",
                        "tw_orig_tweets_acc",
                        "tw_retweets_acc",
                        "tw_quotes_acc",
                        "tw_user_favorites_acc",
                        "tw_eng_acc",
                        "tw_user_eng_acc",
                        "tw_user_statuses_acc",
                        "tw_hashtags_acc"]

        # Twitter days
        for i in range(0,window):
                tw_tweets = "tw_tweets_"+str((i+1))
                tw_orig_tweets = "tw_orig_tweets_"+str((i+1))
                tw_retweets = "tw_retweets_"+str((i+1))
                tw_quotes = "tw_quotes_"+str((i+1))
                tw_user_favorites = "tw_user_favorites_"+str((i+1))
                tw_eng = "tw_eng_"+str((i+1))
                tw_user_eng = "tw_user_eng_"+str((i+1))
                tw_user_statuses = "tw_user_statuses_"+str((i+1))
                tw_hashtags = "tw_hashtags_"+str((i+1))
                
                features_twitter.append(tw_tweets)
                features_twitter.append(tw_orig_tweets)
                features_twitter.append(tw_retweets)
                features_twitter.append(tw_quotes)
                features_twitter.append(tw_user_favorites)
                features_twitter.append(tw_eng)
                features_twitter.append(tw_user_eng)
                features_twitter.append(tw_user_statuses)
                features_twitter.append(tw_hashtags)

        # Twitter ratios
        for i in range(0,window):
                ratioTweets = "ratioTweets_"+str((i+1))
                ratioOrigTweets = "ratioOrigTweets_"+str((i+1))
                ratioRetweets = "ratioRetweets_"+str((i+1))
                ratioQuotes = "ratioQuotes_"+str((i+1))
                ratioUserFavorites = "ratioUserFavorites_"+str((i+1))
                ratioTwEnd = "ratioTwEnd_"+str((i+1))
                ratioUserEng = "ratioUserEng_"+str((i+1))
                ratioUserStatuses = "ratioUserStatuses_"+str((i+1))
                ratioHashtags = "ratioHashtags_"+str((i+1))

                features_twitter.append(ratioTweets)
                features_twitter.append(ratioOrigTweets)
                features_twitter.append(ratioRetweets)
                features_twitter.append(ratioQuotes)
                features_twitter.append(ratioUserFavorites)
                features_twitter.append(ratioTwEnd)
                features_twitter.append(ratioUserEng)
                features_twitter.append(ratioUserStatuses)
                features_twitter.append(ratioHashtags)

        features_youtube = ["category",
                        "uploader_uploads",
                        "uploader_subscribers",
                        "views_dif",
                        "likes_dif",
                        "dislikes_dif",
                        "comments_dif",
                        "views_acc",
                        "likes_acc",
                        "dislikes_acc",
                        "comments_acc"]

        for i in range(0,window):
                views_n = "views_"+str((i+1))
                likes_n = "likes_"+str((i+1))
                dislikes_n = "dislikes_"+str((i+1))
                comments_n = "comments_"+str((i+1))
                features_youtube.append(views_n)
                features_youtube.append(likes_n)
                features_youtube.append(dislikes_n)
                features_youtube.append(comments_n)
                
        for i in range(0,window):     
                ageRatioViews_n = "ageRatioViews_"+str((i+1))
                ageRatioLikes_n = "ageRatioLikes_"+str((i+1))
                ageRatioDislikes_n = "ageRatioDislikes_"+str((i+1))
                ageRatioComments_n = "ageRatioComments_"+str((i+1))
                features_youtube.append(ageRatioViews_n)
                features_youtube.append(ageRatioLikes_n)
                features_youtube.append(ageRatioDislikes_n)
                features_youtube.append(ageRatioComments_n)
                
        for i in range(0,window):
                ratioViews_n = "ratioViews_"+str((i+1))
                ratioLikes_n = "ratioLikes_"+str((i+1))
                ratioDislikes_n = "ratioDislikes_"+str((i+1))
                ratioComments_n = "ratioComments_"+str((i+1))
                features_youtube.append(ratioViews_n)
                features_youtube.append(ratioLikes_n)
                features_youtube.append(ratioDislikes_n)
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
        while i < len(vap_importance):
                list_importance.append([features[i],vap_importance[i]])
                i = i + 1
        list_importance.sort(key=lambda x: x[1])

        i = len(list_importance)-1
        count =1;
        while i >= 0:
                per = list_importance[i][1] * 100
                print(str(count)+'\t'+list_importance[i][0]+'\t{0:0.6f}'.format(per))
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
        
def youtubeViralAndPopular(dir,clf,imp):

        global vap_importance
        vap_importance = []

        fp = open(os.path.join(dir,'youtube_viral_and_popular.eva' ),'w')

        # All features - other(>)
        X = yt_train_all
        Y = vap_train      
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]

        if imp == 1:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using youtube Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,0,"youtube_viral_and_popular_all_old")
        elif imp == 0:
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('youtube_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Baseline features - other(>)        
                X = yt_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('youtube_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
        elif imp == 2:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using youtube Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,0,"youtube_viral_and_popular_all_old")
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('youtube_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Baseline features - other(>)        
                X = yt_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('youtube_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                

        # All features - recent(<)
        X = yt_train_all_recent
        Y = vap_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]

        if imp == 1:
                # Calculating importance than >days(other)
                print('Calculating importance for <= days (other) using youtube Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,0,"youtube_viral_and_popular_all_recent")
        elif imp == 0:
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('youtube_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Baseline features - recent(>) 
                X = yt_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('youtube_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))


                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('youtube_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))
                
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
                plt.title('Youtube Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_youtube_features.png'))
                plt.close(fig)
        elif imp == 2:
                # Calculating importance than >days(other)
                print('Calculating importance for <= days (other) using youtube Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,0,"youtube_viral_and_popular_all_recent")
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('youtube_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Baseline features - recent(>) 
                X = yt_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('youtube_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))


                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('youtube_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))
                
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
                plt.title('Youtube Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_youtube_features.png'))
                plt.close(fig)
                
        fp.close()

def twitterViralAndPopular(dir,clf,imp):

        global vap_importance
        vap_importance = []

        fp = open(os.path.join(dir,'twitter_viral_and_popular.eva' ),'w')
        
        # All features - other(>)
        X = tw_train_all
        Y = vap_train
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]

        if imp == 1:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using twitter Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,1,"twitter_viral_and_popular_all_old")
        elif imp == 0:
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('twitter_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Baseline features - other(>)
                X = tw_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('twitter_viral_and_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))
        elif imp == 2:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using twitter Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,1,"twitter_viral_and_popular_all_old")
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('twitter_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Baseline features - other(>)
                X = tw_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('twitter_viral_and_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))
        
        # All features - recent(<)
        X = tw_train_all_recent
        Y = vap_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]

        if imp == 1:
                # Calculating importance than >days(other)
                print('Calculating importance for <= days (other) using twitter Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,1,"twitter_viral_and_popular_all_recent")
        elif imp == 0:
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('twitter_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Baseline features - recent(<)
                X = tw_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('twitter_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('twitter_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

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
                plt.title('Twitter Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_twitter_features.png'))
                plt.close(fig)
        elif imp == 2:
                # Calculating importance than >days(other)
                print('Calculating importance for <= days (other) using twitter Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,1,"twitter_viral_and_popular_all_recent")
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('twitter_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Baseline features - recent(<)
                X = tw_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('twitter_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('twitter_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

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
                plt.title('Twitter Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_twitter_features.png'))
                plt.close(fig)
        
                
        fp.close()

def bothViralAndPopular(dir,clf,imp):

        # Store feature Importances
        global vap_importance
        vap_importance = []

        fp = open(os.path.join(dir,'both_viral_and_popular.eva' ),'w')

        # Combining features
        x_train_all = np.hstack((tw_train_all,yt_train_all))
        x_train_base = np.hstack((tw_train_base,yt_train_base))
        x_train_all_recent = np.hstack((tw_train_all_recent,yt_train_all_recent))
        x_train_base_recent = np.hstack((tw_train_base_recent,yt_train_base_recent))
        
        X = x_train_all
        Y = vap_train
        metrics = classify(clf,X,Y)
        precision = metrics[0]
        recall = metrics[1]
        auc = metrics[2]
        f1_all_other = metrics[3]

        if imp ==1:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using all Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,2,"both_viral_and_popular_all_old")
        elif imp ==0:
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('both_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Predict other using baseline youtube features
                X = x_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('both_viral_and_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))
        elif imp == 2:
                # Calculating importance than >days(other)
                print('Calculating importance for > days (other) using all Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,2,"both_viral_and_popular_all_old")
                print('\tAll(>14 days) AUC={0:0.2f}'.format(auc))
                fp.write('both_viral_and_popular_all_old\t{0:0.4f}\n'.format(auc))
                # Predict other using baseline youtube features
                X = x_train_base
                Y = vap_train
                metrics = classify(clf,X,Y)
                precision_base = metrics[0]
                recall_base = metrics[1]
                auc_base = metrics[2]
                f1_base_other = metrics[3]
                print('\tBaseline(>14 days) AUC={0:0.2f}'.format(auc_base))
                fp.write('both_viral_and_popular_baseline_old\t{0:0.4f}\n'.format(auc_base))
        
                
                
        # Predict recent using all youtube features
        X = x_train_all_recent
        Y = vap_train_recent
        metrics = classify(clf,X,Y)
        precision_recent = metrics[0]
        recall_recent = metrics[1]
        auc_recent = metrics[2]
        f1_all_recent = metrics[3]
  
        if imp ==1:
                #Calculating importance than <days(recent)
                print('\nCalculating importance for < days (recent) using all Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,2,"both_viral_and_popular_all_recent")
        elif imp == 0:
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('both_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Predict recent using baseline youtube features
                X = x_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('both_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('both_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

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
                plt.title('Both Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_all_features.png'))
                plt.close(fig)
        elif imp == 2:
                #Calculating importance than <days(recent)
                print('\nCalculating importance for < days (recent) using all Features ')
                importance = clf.feature_importances_
                vap_importance = importance
                exportImportance(dir,2,"both_viral_and_popular_all_recent")
                print('\tAll(<=14 days) AUC={0:0.2f}'.format(auc_recent))
                fp.write('both_viral_and_popular_all_recent\t{0:0.4f}\n'.format(auc_recent))
                # Predict recent using baseline youtube features
                X = x_train_base_recent
                Y = vap_train_recent
                metrics = classify(clf,X,Y)
                precision_base_recent = metrics[0]
                recall_base_recent = metrics[1]
                auc_base_recent = metrics[2]
                f1_base_recent = metrics[3]
                print('\tBaseline(<=14 days) AUC={0:0.2f}'.format(auc_base_recent))
                fp.write('both_viral_and_popular_baseline_recent\t{0:0.4f}\n'.format(auc_base_recent))

                # Calculating overall F1 score
                f1_average = (f1_all_other+f1_base_other+f1_all_recent+f1_base_recent)/4
                print('\t\tF1 score: {0:0.6f}'.format(f1_average))
                fp.write('both_viral_and_popular_f1_score\t{0:0.4f}\n'.format(f1_average))

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
                plt.title('Both Popular And Viral')
                plt.legend(loc='best', fancybox='True', framealpha=0.5, fontsize=8);
                fig.savefig(os.path.join(dir,'popular-viral_all_features.png'))
                plt.close(fig)
                
        fp.close()
        

