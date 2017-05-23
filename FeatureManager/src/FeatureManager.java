import ClassifierFeatures.CreateBaseFeatures;
import ClassifierFeatures.CreateFeatures;
import models.*;
import records.DayRecord;
import records.VideoRecord;

import java.io.*;
import java.sql.Timestamp;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

/**
 * Created by Giorgos on 29/12/2016.
 */
public class FeatureManager {

    private int t_window;
    private int offset;
    private int l_window;
    private int split_days;
    private String twFeatures;
    private String ytFeatures;
    private Map<String, VideoData> videosMapRecent;
    private Map<String, VideoData> videosMap;
    private ArrayList<String> uniqueVideos;
    private ArrayList<String> uniqueVideosRecent;


    public FeatureManager(int t,int o,int l, int split,String yt,String tw){
        this.t_window = t;
        this.offset = o;
        this.l_window = l;
        this.split_days = split;
        this.ytFeatures = yt;
        this.twFeatures = tw;
        videosMap = new HashMap<>();
        videosMapRecent = new HashMap<>();
        uniqueVideos = new ArrayList<>();
        uniqueVideosRecent = new ArrayList<>();
    }

    public YoutubeFeatures prepareYouTubeFeatures(String parts[]) throws ParseException {

        int yt_category = Integer.parseInt(parts[1]);
        int yt_artificial_category = Integer.parseInt(parts[2]);
        Timestamp yt_uploaded = new Timestamp(Long.parseLong(parts[3]));
        int duration = Integer.parseInt(parts[5]);
        float comments_sentiment_neg =Float.parseFloat(parts[6]);
        float comments_sentiment_neu =Float.parseFloat(parts[7]);
        float comments_sentiment_pos =Float.parseFloat(parts[8]);
        float comments_sentiment_compound =Float.parseFloat(parts[9]);


        /**
         * These data could change depending on the file input
         * Our case:
         * 10 features at the beggining
         * 22 features per day
         */
        int initialFeatures = 10;
        int dayFeatures = 22;
        int numOfDays = (parts.length-initialFeatures)/dayFeatures;

        YoutubeFeatures yt =new YoutubeFeatures(yt_category, yt_artificial_category,yt_uploaded, duration,
                comments_sentiment_neg,comments_sentiment_neu, comments_sentiment_pos,comments_sentiment_compound);

        /**
         * Creating days for youtube features
         */
        int dayCount = initialFeatures;
        for(int i=0;i<numOfDays;i++){
            long views = Long.parseLong(parts[dayCount]);
            int likes = Integer.parseInt(parts[dayCount+1]);
            int dislikes = Integer.parseInt(parts[dayCount+2]);
            int comments = Integer.parseInt(parts[dayCount+3]);
            long channel_views =Long.parseLong(parts[dayCount+4]);
            long channel_comments =Long.parseLong(parts[dayCount+5]);
            long channel_subscribers =Long.parseLong(parts[dayCount+6]);
            int channel_videos =Integer.parseInt(parts[dayCount+7]);

            YoutubeDay day = new YoutubeDay(i,views,likes,dislikes,comments,channel_views,channel_comments,
                                    channel_subscribers,channel_videos);
            dayCount+= dayFeatures;
            yt.addDay(day);
        }
        return yt;
    }

    public YoutubeFeatures mapYouTubeFeatures(VideoRecord vr,int numOfDays){

        int yt_category = vr.getYt_category();
        int yt_artificial_category = vr.getYt_artificial_category();
        Timestamp yt_uploaded = vr.getYt_uploaded();
        int duration = vr.getDuration();
        float comments_sentiment_neg = vr.getComments_sentiment_neg();
        float comments_sentiment_neu = vr.getComments_sentiment_neu();
        float comments_sentiment_pos = vr.getComments_sentiment_pos();
        float comments_sentiment_compound = vr.getComments_sentiment_compound();

        YoutubeFeatures yt =new YoutubeFeatures(yt_category, yt_artificial_category,yt_uploaded, duration,
                comments_sentiment_neg,comments_sentiment_neu, comments_sentiment_pos,comments_sentiment_compound);

        /**
         * Creating days for youtube features
         */

        for(int i=0;i<numOfDays;i++){
            DayRecord dr = vr.getDays().get(i);
            int views = dr.getViews();
            int likes = dr.getLikes();
            int dislikes = dr.getDislikes();
            int comments = dr.getComments();
            long channel_views = dr.getChannel_views();
            long channel_comments = dr.getChannel_comments();
            long channel_subscribers = dr.getChannel_subscribers();
            int channel_videos = dr.getChannel_videos();

            YoutubeDay day = new YoutubeDay(i,views,likes,dislikes,comments,channel_views,channel_comments,
                    channel_subscribers,channel_videos);
            yt.addDay(day);
        }

        return yt;

    }

    public TwitterFeatures prepareTwitterFeatures(String parts[]){

        TwitterFeatures tw = new TwitterFeatures();

        /**
         * These data could change depending on the file input
         * Our case:
         * 10 features at the beggining
         * 22 features per day
         */
        int initialFeatures = 10;
        int dayFeatures = 22;
        int numOfDays = (parts.length-initialFeatures)/dayFeatures;

        /**
         * Creating days for twitter features
         */
        int dayCount = initialFeatures;
        for(int i=0;i<numOfDays;i++){
            TwitterDay day = new TwitterDay(i);
            day.setTw_tweets(Integer.parseInt(parts[dayCount+8]));
            day.setTw_orig_tweets(Integer.parseInt(parts[dayCount+9]));
            day.setTw_retweets(Integer.parseInt(parts[dayCount+10]));
            day.setTw_user_favorites(Integer.parseInt(parts[dayCount+11]));
            day.setTw_hashtags(Integer.parseInt(parts[dayCount+12]));
            day.setTw_eng(Integer.parseInt(parts[dayCount+13]));
            day.setTw_sp(Integer.parseInt(parts[dayCount+14]));
            day.setTw_user_eng(Integer.parseInt(parts[dayCount+15]));
            day.setTw_user_sp(Integer.parseInt(parts[dayCount+16]));
            day.setTw_user_verified(Integer.parseInt(parts[dayCount+17]));
            day.setUsers_days_created_before_video((int)Float.parseFloat(parts[dayCount+18]));
            day.setTw_user_followers(Float.parseFloat(parts[dayCount+19]));
            day.setTw_user_friends(Float.parseFloat(parts[dayCount+20]));
            day.setTw_user_statuses((int)Float.parseFloat(parts[dayCount+21]));
            dayCount+= dayFeatures;
            tw.addDay(day,i);
        }

        return tw;
    }

    public TwitterFeatures mapTwitterFeatures(VideoRecord vr, int numOfDays){

        TwitterFeatures tw = new TwitterFeatures();

        /**
         * Creating days for twitter features
         */
        for(int i=0;i<numOfDays;i++){
            DayRecord dr = vr.getDays().get(i);
            TwitterDay day = new TwitterDay(i);
            day.setTw_tweets(dr.getTw_tweets());
            day.setTw_orig_tweets(dr.getTw_orig_tweets());
            day.setTw_retweets(dr.getTw_retweets());
            day.setTw_user_favorites(dr.getTw_user_favorites());
            day.setTw_hashtags(dr.getTw_hashtags());
            day.setTw_eng(dr.getTw_eng());
            day.setTw_sp(dr.getTw_sp());
            day.setTw_user_eng(dr.getTw_user_eng());
            day.setTw_user_sp(dr.getTw_user_sp());
            day.setTw_user_verified(dr.getTw_user_verified());
            day.setUsers_days_created_before_video(dr.getUsers_days_created_before_video());
            day.setTw_user_followers(dr.getTw_user_followers());
            day.setTw_user_friends(dr.getTw_user_friends());
            day.setTw_user_statuses(dr.getTw_user_statuses());
            tw.addDay(day,i);
        }

        return tw;
    }

    public void createFeatures(){
        CreateFeatures features = new CreateFeatures(false,t_window,offset,l_window);
        features.setT_window(t_window);
        features.setOffset(offset);
        features.setL_window(l_window);
        features.setUniqueVideos(uniqueVideos);
        features.setVideosMap(videosMap);
        features.setTwBinary(twFeatures);
        features.setYtBinary(ytFeatures);
        features.create();

        CreateFeatures featuresRecent = new CreateFeatures(true,t_window,offset,l_window);
        featuresRecent.setT_window(t_window);
        featuresRecent.setOffset(offset);
        featuresRecent.setL_window(l_window);
        featuresRecent.setUniqueVideos(uniqueVideosRecent);
        featuresRecent.setVideosMap(videosMapRecent);
        featuresRecent.setTwBinary(twFeatures);
        featuresRecent.setYtBinary(ytFeatures);
        featuresRecent.create();

        CreateBaseFeatures baseFeatures = new CreateBaseFeatures(false,t_window,offset,l_window);
        baseFeatures.setT_window(t_window);
        baseFeatures.setOffset(offset);
        baseFeatures.setL_window(l_window);
        baseFeatures.setVideosMap(videosMap);
        baseFeatures.setUniqueVideos(uniqueVideos);
        baseFeatures.create();

        CreateBaseFeatures baseFeaturesRecent = new CreateBaseFeatures(true,t_window,offset,l_window);
        baseFeaturesRecent.setT_window(t_window);
        baseFeaturesRecent.setOffset(offset);
        baseFeaturesRecent.setL_window(l_window);
        baseFeaturesRecent.setVideosMap(videosMapRecent);
        baseFeaturesRecent.setUniqueVideos(uniqueVideosRecent);
        baseFeaturesRecent.create();

        System.out.println("Created Features");
    }


    public void populate(Map<String, VideoData> videosMap,Map<String, VideoData> videosMapRecent,
                         ArrayList<String> uniqueVideos,ArrayList<String> uniqueVideosRecent){
        this.videosMap = videosMap;
        this.videosMapRecent = videosMapRecent;
        this.uniqueVideos = uniqueVideos;
        this. uniqueVideosRecent = uniqueVideosRecent;
    }


}
