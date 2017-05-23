package models;
import records.DayRecord;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Giorgos on 06-Nov-16.
 */
public class VideoData {

    private long published_at;
    private long collected_at;
    private YoutubeFeatures youtubeFeatures;
    private TwitterFeatures twitterFeatures;
    private Map<Integer,TwitterDay> twitterDayMap;
    private String video_id;
    private int totalViews;
    private int totalTweets;
    private int channel_uploads;
    private long channel_subscribers;
    private long channel_views;
    private long channel_comments;
    private int popular;
    private int viral;

    public VideoData(long pub,long col, String video_id, YoutubeFeatures youtubeFeatures, TwitterFeatures twitterFeatures){
        this.published_at = pub;
        this.collected_at = col;
        this.video_id = video_id;
        this.youtubeFeatures = youtubeFeatures;
        this.twitterFeatures = twitterFeatures;
        this.twitterDayMap = (twitterFeatures!=null)?twitterFeatures.getAllDays():new HashMap<>();
    }

    public YoutubeFeatures getYoutubeFeatures(){
        return youtubeFeatures;
    }

    public TwitterFeatures getTwitterFeatures(){
        return twitterFeatures;
    }


    /***
     * totalViews and totalTweets are going to be used later
     * in Labeling
     *
     * */
    public void calculateTotals(int t_win,int offset,int l_win){

        for(int i=0;i<=t_win;i++) {
            totalViews += youtubeFeatures.getFeaturesForDay(i).getYt_views();
            totalTweets+= twitterDayMap.get(i).getTw_tweets();
            channel_uploads+= youtubeFeatures.getFeaturesForDay(i).getYt_channel_videos();
            channel_subscribers+= youtubeFeatures.getFeaturesForDay(i).getYt_channel_subscribers();
            channel_comments+= youtubeFeatures.getFeaturesForDay(i).getYt_channel_comments();
            channel_views+= youtubeFeatures.getFeaturesForDay(i).getYt_channel_views();
        }

        for(int i=t_win+offset+1;i<=t_win+offset+l_win;i++) {
            totalViews += youtubeFeatures.getFeaturesForDay(i).getYt_views();
            totalTweets += twitterDayMap.get(i).getTw_tweets();
        }

    }

    public void setPopular(int popular) {
        this.popular = popular;
    }

    public int getPopular() {
        return popular;
    }

    public int getViral() {
        return viral;
    }

    public void setViral(int viral) {
        this.viral = viral;
    }

    public int getTotalViews() {
        return totalViews;
    }

    public int getTotalTweets() {
        return totalTweets;
    }

    public int getChannel_uploads() {
        return channel_uploads;
    }

    public long getChannel_subscribers() {
        return channel_subscribers;
    }

    public long getChannel_views() {
        return channel_views;
    }

    public long getChannel_comments() {
        return channel_comments;
    }

    /*
    @Override
    public String toString() {
        ArrayList<YoutubeDay> youtubeDays = youtubeFeatures.getAllDays();
        String ytdayStr ="";
        for(int i=0;i<youtubeDays.size();i++){
            YoutubeDay d = youtubeDays.get(i);
            TwitterDay t=null;
            TwitterDay lt=null;
            if(twitterDayMap!=null)
                t = twitterDayMap.get(i);
            int day = d.getDay();
            int views = d.getYt_views();
            int likes = d.getYt_likes();
            int dislikes = d.getYt_dislikes();
            int comments = d.getYt_comments();
            //Twitter features
            int total_tweets ;
            int original_tweets;
            int quotes;
            int retweets;
            int user_followers;
            int user_favorites;
            int tw_en_lang;
            int tw_user_en_lang;
            int tw_user_statuses;
            int tw_user_friends;
            int tw_user_verified;
            int hashtags;

            total_tweets = (t != null) ? t.getTw_tweets() : 0;
            original_tweets = (t != null) ? t.getTw_orig_tweets() : 0;
            retweets = (t != null) ? t.getTw_retweets() : 0;
            quotes = (t != null) ? t.getTw_quotes() : 0;
            user_followers = (t != null) ? t.getTw_user_followers() : 0;
            user_favorites = (t != null) ? t.getTw_user_favorites() : 0;
            tw_en_lang = (t != null) ? t.getTw_eng() : 0;
            tw_user_en_lang = (t != null) ? t.getTw_user_eng() : 0;
            tw_user_statuses = (t != null) ? t.getTw_user_statuses() : 0;
            tw_user_friends = (t != null) ? t.getTw_user_friends() : 0;
            tw_user_verified = (t != null) ? t.getTw_user_verified() : 0;
            hashtags = (t != null) ? t.getTw_hashtags() : 0;


            String str = day+"\t"+views+"\t"+likes+"\t"+dislikes+"\t"+comments+"\t"
                    +total_tweets+"\t" + original_tweets+"\t" +quotes+"\t"
                    +retweets+"\t" +user_followers+"\t" + user_favorites+"\t"
                    +tw_en_lang+"\t"+tw_user_en_lang+"\t"+tw_user_statuses+"\t"+
                    tw_user_friends+"\t"+tw_user_verified+"\t"+hashtags+"\t";
            ytdayStr = ytdayStr.concat(str);
        }
        return  video_id+"\t"+ collected_at +"\t"+
                youtubeFeatures.getYt_uploaded()+"\t"+
                youtubeFeatures.getYt_category()+"\t"+
                youtubeFeatures.getYt_uploader_uploads()+"\t"+
                youtubeFeatures.getYt_uploader_subscribers()+"\t"+
                ((twitterFeatures==null)?-1:twitterFeatures.getTw_user_followers())+"\t"+
                youtubeFeatures.getAllDays().size()+"\t"+
                ytdayStr+"\t";
    }*/

    public long getPublished_at() {
        return published_at;
    }

    public long getCollected_at() {
        return collected_at;
    }
}
