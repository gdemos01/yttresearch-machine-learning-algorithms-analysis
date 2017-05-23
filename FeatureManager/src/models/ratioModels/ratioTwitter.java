package models.ratioModels;

import models.TwitterFeatures;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class ratioTwitter {

    private int day;
    private TwitterFeatures twitterFeatures;
    private float ratioTweets;
    private float ratioOrigTweets;
    private float ratioRetweets;

    private float ratioUserFavorites;
    private float ratioTwEng;
    private float ratioUserEng;
    private float ratioUserStatuses;
    private float ratioHashtags;
    private float ratioUserSp;
    private float ratioTwSp;
    private String twBinary;

    public ratioTwitter(int day, TwitterFeatures twitterFeatures) {
        this.day = day;
        this.twitterFeatures = twitterFeatures;
        createRatioTweets();
        createRatioOrigTweets();
        createRatioRetweets();
        createRatioUserFavorites();
        createRatioTwEng();
        createRatioUserEng();
        createRatioUserStatuses();
        createRatioHashtags();
        createRatioTwSp();
        createRatioUserSp();
    }

    public void createRatioTweets(){
        int total_tweets =0;
        int tweets_n = twitterFeatures.getAllDays().get(day).getTw_tweets();
        for(int i=0;i<day-1;i++){
            total_tweets+= twitterFeatures.getAllDays().get(i).getTw_tweets();
        }
        if(total_tweets!=0){
            ratioTweets = tweets_n/(float)total_tweets;
        }else{
            ratioTweets = 0;
        }
    }

    public void createRatioOrigTweets(){
        int total_orig_tweets =0;
        int tweets_orig_n = twitterFeatures.getAllDays().get(day).getTw_orig_tweets();
        for(int i=0;i<day-1;i++){
            total_orig_tweets+= twitterFeatures.getAllDays().get(i).getTw_orig_tweets();
        }
        if(total_orig_tweets!=0){
            ratioOrigTweets=tweets_orig_n/(float)total_orig_tweets;
        }else{
            ratioOrigTweets=0;
        }
    }

    public void createRatioRetweets(){
        int total_retweets =0;
        int retweet_n = twitterFeatures.getAllDays().get(day).getTw_retweets();
        for(int i=0;i<day-1;i++){
            total_retweets+= twitterFeatures.getAllDays().get(i).getTw_retweets();
        }

        if(total_retweets!=0){
            ratioRetweets=retweet_n/(float)total_retweets;
        }else{
            ratioRetweets=0;
        }
    }

    public void createRatioUserFavorites(){
        int total_favorites =0;
        int favorites_n = twitterFeatures.getAllDays().get(day).getTw_user_favorites();
        for(int i=0;i<day-1;i++){
            total_favorites+= twitterFeatures.getAllDays().get(i).getTw_user_favorites();
        }

        if(total_favorites!=0){
            ratioUserFavorites=favorites_n/(float)total_favorites;
        }else{
            ratioUserFavorites=0;
        }
    }

    public void createRatioTwEng(){
        int total_tw_eng =0;
        int tw_eng_n = twitterFeatures.getAllDays().get(day).getTw_eng();
        for(int i=0;i<day-1;i++){
            total_tw_eng+= twitterFeatures.getAllDays().get(i).getTw_eng();
        }

        if(total_tw_eng!=0){
            ratioTwEng=tw_eng_n/(float)total_tw_eng;
        }else{
            ratioTwEng=0;
        }
    }

    public void createRatioTwSp(){
        int total_tw_sp =0;
        int tw_sp_n = twitterFeatures.getAllDays().get(day).getTw_sp();
        for(int i=0;i<day-1;i++){
            total_tw_sp+= twitterFeatures.getAllDays().get(i).getTw_sp();
        }

        if(total_tw_sp!=0){
            ratioTwSp=tw_sp_n/(float)total_tw_sp;
        }else{
            ratioTwSp=0;
        }
    }

    public void createRatioUserEng(){
        int total_user_eng =0;
        int user_eng_n = twitterFeatures.getAllDays().get(day).getTw_user_eng();
        for(int i=0;i<day-1;i++){
            total_user_eng+= twitterFeatures.getAllDays().get(i).getTw_user_eng();
        }

        if(total_user_eng!=0){
            ratioUserEng=user_eng_n/(float)total_user_eng;
        }else{
            ratioUserEng=0;
        }
    }

    public void createRatioUserSp(){
        int total_user_sp =0;
        int user_sp_n = twitterFeatures.getAllDays().get(day).getTw_user_sp();
        for(int i=0;i<day-1;i++){
            total_user_sp+= twitterFeatures.getAllDays().get(i).getTw_user_sp();
        }

        if(total_user_sp!=0){
            ratioUserSp=user_sp_n/(float)total_user_sp;
        }else{
            ratioUserSp=0;
        }
    }

    public void createRatioUserStatuses(){
        int total_user_statuses =0;
        int user_statuses_n = twitterFeatures.getAllDays().get(day).getTw_user_statuses();
        for(int i=0;i<day-1;i++){
            total_user_statuses+= twitterFeatures.getAllDays().get(i).getTw_user_statuses();
        }

        if(total_user_statuses!=0){
            ratioUserStatuses=user_statuses_n/(float)total_user_statuses;
        }else{
            ratioUserStatuses=0;
        }
    }

    public void createRatioHashtags(){
        int total_hashtags =0;
        int hastags_n = twitterFeatures.getAllDays().get(day).getTw_hashtags();
        for(int i=0;i<day-1;i++){
            total_hashtags+= twitterFeatures.getAllDays().get(i).getTw_hashtags();
        }

        if(total_hashtags!=0){
            ratioHashtags=hastags_n/(float)total_hashtags;
        }else{
            ratioHashtags=0;
        }
    }

    public float getRatioTweets(){
        return ratioTweets;
    }

    public float getRatioOriginalTweets(){
        return ratioOrigTweets;
    }

    public float getRatiowRetweets(){
        return ratioRetweets;
    }

    public void setTwBinary(String twBinary) {
        this.twBinary = twBinary;
    }

    @Override
    public String toString() {
        String features = "";

        if(twBinary.charAt(33)=='1'){features = features.concat(ratioTweets + "," );}
        if(twBinary.charAt(34)=='1'){features = features.concat(ratioOrigTweets + "," );}
        if(twBinary.charAt(35)=='1'){features = features.concat(ratioRetweets + "," );}
        if(twBinary.charAt(36)=='1'){features = features.concat(ratioUserFavorites + "," ); }
        if(twBinary.charAt(37)=='1'){features = features.concat(ratioTwEng + "," );}
        if(twBinary.charAt(38)=='1'){features = features.concat(ratioTwSp + "," );}
        if(twBinary.charAt(39)=='1'){features = features.concat(ratioUserEng + "," );}
        if(twBinary.charAt(40)=='1'){features = features.concat(ratioUserSp + "," ); }
        if(twBinary.charAt(41)=='1'){features = features.concat(ratioUserStatuses + "," );}
        if(twBinary.charAt(42)=='1'){features = features.concat(ratioHashtags + "," ); }

        return features;

    }
}
