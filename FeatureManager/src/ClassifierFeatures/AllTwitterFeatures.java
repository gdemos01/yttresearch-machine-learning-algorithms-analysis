package ClassifierFeatures;

import models.TwitterDay;
import models.TwitterFeatures;
import models.VideoData;
import models.ratioModels.ratioTwitter;

import java.util.ArrayList;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class AllTwitterFeatures {

    private int window;
    private VideoData videoData;

    /**
     * Static Features
     */
    private int tw_user_followers;
    private int tw_user_verified;
    private int tw_user_friends;


    /**
     * Differences
     */
    private int tw_tweets_dif;
    private int tw_orig_tweets_dif;
    private int tw_retweets_dif;
    private int tw_user_favorites_dif;
    private int tw_eng_dif;
    private int tw_sp_dif;
    private int tw_user_eng_dif;
    private int tw_user_sp_dif;
    private int tw_user_statuses_dif;
    private int tw_hashtags_dif;


    /**
     * Accelerations
     */
    private float tw_tweets_acc;
    private float tw_orig_tweets_acc;
    private float tw_retweets_acc;
    private float tw_user_favorites_acc;
    private float tw_eng_acc;
    private float tw_sp_acc;
    private float tw_user_eng_acc;
    private float tw_user_sp_acc;
    private float tw_user_statuses_acc;
    private float tw_hashtags_acc;
    private String twBinary;

    /**
     * Dynamic features and ratios
     */
    private ArrayList<TwitterDay> days;
    private ArrayList<ratioTwitter> ratios;

    public AllTwitterFeatures(int window, VideoData videoData,String tw){
        this.window=window;
        this.videoData = videoData;
        this.twBinary = tw;
        days = new ArrayList<>();
        ratios = new ArrayList<>();

        createDays();
        calculateStaticFeatures();
        calculateDifferences();
        calculateAccelerations();
        createRatios();
    }

    /**
     * We get only the days that we are interested in
     * depending on the window
     */
    public void createDays(){
        for(int i=0;i<=window;i++){
            days.add(videoData.getTwitterFeatures().getAllDays().get(i));
        }
    }

    /**
     * Creating the ratios of all the dynamic features
     */
    public void createRatios(){
        for(int i=1;i<days.size();i++){
            ratioTwitter ratio = new ratioTwitter(i,videoData.getTwitterFeatures());
            ratio.setTwBinary(twBinary);
            ratios.add(ratio);
        }
    }

    /**
     * We calculate the average value observed for
     * our static features
     */
    public void calculateStaticFeatures(){
        TwitterFeatures tw = videoData.getTwitterFeatures();
        tw_user_verified=0;
        tw_user_followers=0;
        tw_user_friends=0;
        for(int i=0;i<=window;i++){
            TwitterDay tday = tw.getAllDays().get(i);
            tw_user_followers+= tday.getTw_user_followers();
            if(tday.getTw_user_verified()==1){
                tw_user_verified=1;
            }
            tw_user_friends+= tday.getTw_user_friends();
        }
    }

    public void calculateDifferences(){
        TwitterFeatures tw = videoData.getTwitterFeatures();
        TwitterDay td0 = tw.getAllDays().get(0);
        TwitterDay td1= tw.getAllDays().get(1);

        int firstDayTweets = td0.getTw_tweets()+td1.getTw_tweets();
        int firstDayOrigTweets= td0.getTw_orig_tweets()+td1.getTw_orig_tweets();
        int firstDayRetweets = td0.getTw_retweets()+td1.getTw_retweets();
        int firstDayUserFavorites = td0.getTw_user_favorites()+td1.getTw_user_favorites();
        int firstDayEng = td0.getTw_eng()+td1.getTw_eng();
        int firstDaySp = td0.getTw_sp() + td1.getTw_sp();
        int firstDayUserEng = td0.getTw_user_eng()+td1.getTw_user_eng();
        int firstDayUserSp = td0.getTw_user_sp() + td1.getTw_user_sp();
        int firstDayUserStatuses = td0.getTw_user_statuses()+td1.getTw_user_statuses();
        int fisrtDayHashtags = td0.getTw_hashtags()+td1.getTw_hashtags();

        int lastDayTweets=0;
        int lastDayOrigTweets=0;
        int lastDayRetweets=0;
        int lastDayUserFavorites=0;
        int lastDayEng=0;
        int lastDaySp=0;
        int lastDayUserEng=0;
        int lastDayUserSp =0;
        int lastDayUserStatuses=0;
        int lastDayHashtags=0;

        for(int i=0;i<=window;i++){
            TwitterDay tday = tw.getAllDays().get(i);
            lastDayTweets+=tday.getTw_tweets();
            lastDayOrigTweets+=tday.getTw_orig_tweets();
            lastDayRetweets+=tday.getTw_retweets();
            lastDayUserFavorites+= tday.getTw_user_favorites();
            lastDayEng+= tday.getTw_eng();
            lastDaySp+= tday.getTw_sp();
            lastDayUserEng+= tday.getTw_user_eng();
            lastDayUserSp+= tday.getTw_user_sp();
            lastDayUserStatuses+= tday.getTw_user_statuses();
            lastDayHashtags+= tday.getTw_hashtags();
        }

        tw_tweets_dif= lastDayTweets-firstDayTweets;
        tw_orig_tweets_dif =lastDayOrigTweets - firstDayOrigTweets;
        tw_retweets_dif = lastDayRetweets - firstDayRetweets;
        tw_user_favorites_dif = lastDayUserFavorites - firstDayUserFavorites;
        tw_eng_dif = lastDayEng - firstDayEng;
        tw_sp_dif = lastDaySp - firstDaySp;
        tw_user_eng_dif= lastDayUserEng-firstDayUserEng;
        tw_user_sp_dif = lastDayUserSp - firstDayUserSp;
        tw_user_statuses_dif=lastDayUserStatuses-firstDayUserStatuses;
        tw_hashtags_dif=lastDayHashtags-fisrtDayHashtags;
    }

    public void calculateAccelerations(){
        TwitterFeatures tw = videoData.getTwitterFeatures();

        tw_tweets_acc=0;
        tw_orig_tweets_acc=0;
        tw_retweets_acc=0;
        tw_user_favorites_acc=0;
        tw_eng_acc=0;
        tw_sp_acc=0;
        tw_user_eng_acc=0;
        tw_user_sp_acc=0;
        tw_user_statuses_acc=0;
        tw_hashtags_acc=0;

        for(int i=1;i<=window;i++){
            TwitterDay tday = tw.getAllDays().get(i);
            tw_tweets_acc+=tday.getTw_tweets();
            tw_orig_tweets_acc+=tday.getTw_orig_tweets();
            tw_retweets_acc+=tday.getTw_retweets();
            tw_user_favorites_acc+=tday.getTw_user_favorites();
            tw_eng_acc+=tday.getTw_eng();
            tw_sp_acc+= tday.getTw_sp();
            tw_user_eng_acc+=tday.getTw_user_eng();
            tw_user_sp_acc+= tday.getTw_user_sp();
            tw_user_statuses_acc+=tday.getTw_user_statuses();
            tw_hashtags_acc+=tday.getTw_hashtags();
        }

        tw_tweets_acc= tw_tweets_acc/(float)window;
        tw_orig_tweets_acc= tw_orig_tweets_acc/(float)window;
        tw_retweets_acc=tw_retweets_acc/(float)window;
        tw_user_favorites_acc=tw_user_favorites_acc/(float)window;
        tw_eng_acc=tw_eng_acc/(float)window;
        tw_sp_acc = tw_sp_acc/(float)window;
        tw_user_eng_acc=tw_user_eng_acc/(float)window;
        tw_user_sp_acc=tw_user_sp_acc/(float)window;
        tw_user_statuses_acc=tw_user_statuses_acc/(float)window;
        tw_hashtags_acc=tw_hashtags_acc/(float)window;
    }

    /** Need to change this**/
    @Override
    public String toString() {
        if(days.size()==1){
            String featureString = "";
            String dayStats = "";

            /**
             * Static Twitter Features
             */
            if(twBinary.charAt(0)=='1'){ featureString = featureString.concat(tw_user_followers+",");}
            if(twBinary.charAt(1)=='1'){ featureString = featureString.concat(tw_user_verified+",");}
            if(twBinary.charAt(2)=='1'){ featureString = featureString.concat(tw_user_friends+",");}

            /**
             * Day stats for only day zero
             */
            if(twBinary.charAt(23)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_tweets()+",");}
            if(twBinary.charAt(24)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_orig_tweets()+",");}
            if(twBinary.charAt(25)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_retweets()+",");}
            if(twBinary.charAt(26)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_user_favorites()+",");}
            if(twBinary.charAt(27)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_eng()+",");}
            if(twBinary.charAt(28)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_sp()+",");}
            if(twBinary.charAt(29)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_user_eng()+",");}
            if(twBinary.charAt(30)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_user_sp()+",");}
            if(twBinary.charAt(31)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_user_statuses()+",");}
            if(twBinary.charAt(32)=='1'){ dayStats = dayStats.concat(days.get(0).getTw_hashtags()+",");}

            featureString = featureString.concat(dayStats);

            /**
             * Removing last comma if it exists
             */
            if(featureString.charAt(featureString.length()-1)==','){
                featureString = featureString.substring(0,featureString.length()-1);
            }

            return featureString;
        }else{
            String featureString = "";
            String daysStats="";

            /**
             * Static Twitter Features
             */
            if(twBinary.charAt(0)=='1'){ featureString = featureString.concat(tw_user_followers+",");}
            if(twBinary.charAt(1)=='1'){ featureString = featureString.concat(tw_user_verified+",");}
            if(twBinary.charAt(2)=='1'){ featureString = featureString.concat(tw_user_friends+",");}

            /**
             * Differences
             */
            if(twBinary.charAt(3)=='1'){ featureString = featureString.concat(tw_tweets_dif+",");}
            if(twBinary.charAt(4)=='1'){ featureString = featureString.concat(tw_orig_tweets_dif+",");}
            if(twBinary.charAt(5)=='1'){ featureString = featureString.concat(tw_retweets_dif+",");}
            if(twBinary.charAt(6)=='1'){ featureString = featureString.concat(tw_user_favorites_dif+",");}
            if(twBinary.charAt(7)=='1'){ featureString = featureString.concat(tw_eng_dif+",");}
            if(twBinary.charAt(8)=='1'){ featureString = featureString.concat(tw_sp_dif+",");}
            if(twBinary.charAt(9)=='1'){ featureString = featureString.concat(tw_user_eng_dif+",");}
            if(twBinary.charAt(10)=='1'){ featureString = featureString.concat(tw_user_sp_dif+",");}
            if(twBinary.charAt(11)=='1'){ featureString = featureString.concat(tw_user_statuses_dif+",");}
            if(twBinary.charAt(12)=='1'){ featureString = featureString.concat(tw_hashtags_dif+",");}

            /**
             * Accelerations
             */
            if(twBinary.charAt(13)=='1'){ featureString = featureString.concat(tw_tweets_acc+",");}
            if(twBinary.charAt(14)=='1'){ featureString = featureString.concat(tw_orig_tweets_acc+",");}
            if(twBinary.charAt(15)=='1'){ featureString = featureString.concat(tw_retweets_acc+",");}
            if(twBinary.charAt(16)=='1'){ featureString = featureString.concat(tw_user_favorites_acc+",");}
            if(twBinary.charAt(17)=='1'){ featureString = featureString.concat(tw_eng_acc+",");}
            if(twBinary.charAt(18)=='1'){ featureString = featureString.concat(tw_sp_acc+",");}
            if(twBinary.charAt(19)=='1'){ featureString = featureString.concat(tw_user_eng_acc+",");}
            if(twBinary.charAt(20)=='1'){ featureString = featureString.concat(tw_user_sp_acc+",");}
            if(twBinary.charAt(21)=='1'){ featureString = featureString.concat(tw_user_statuses_acc+",");}
            if(twBinary.charAt(22)=='1'){ featureString = featureString.concat(tw_hashtags_acc+",");}

            /**
             * Day Stats
             */
            for(int i=1;i<days.size();i++){
                String t_dayStats = "";
                if(twBinary.charAt(23)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_tweets()+",");}
                if(twBinary.charAt(24)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_orig_tweets()+",");}
                if(twBinary.charAt(25)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_retweets()+",");}
                if(twBinary.charAt(26)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_user_favorites()+",");}
                if(twBinary.charAt(27)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_eng()+",");}
                if(twBinary.charAt(28)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_sp()+",");}
                if(twBinary.charAt(29)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_user_eng()+",");}
                if(twBinary.charAt(30)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_user_sp()+",");}
                if(twBinary.charAt(31)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_user_statuses()+",");}
                if(twBinary.charAt(32)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getTw_hashtags()+",");}
                daysStats = daysStats.concat(t_dayStats);
            }

            featureString = featureString.concat(daysStats);

            /**
             * Ratios
             */
            String ratioFeatures = "";
            for(int i=0;i<ratios.size();i++){
                ratioFeatures = ratioFeatures.concat(ratios.get(i).toString());
            }
            featureString = featureString.concat(ratioFeatures);

            /**
             * Removing last comma if it exists
             */
            if(featureString.length()>0) {
                if (featureString.charAt(featureString.length() - 1) == ',') {
                    featureString = featureString.substring(0, featureString.length() - 1);
                }
            }

            return featureString;

        }

    }
}
