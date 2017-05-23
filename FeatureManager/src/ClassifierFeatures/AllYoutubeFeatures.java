package ClassifierFeatures;

import models.VideoData;
import models.YoutubeDay;
import models.YoutubeFeatures;
import models.ratioModels.age_ratioYouTube;
import models.ratioModels.ratioYouTube;

import java.util.ArrayList;
import java.util.Date;
import java.util.StringJoiner;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class AllYoutubeFeatures {

    private int window;
    private VideoData videoData;
    private Date yt_uploaded;
    private int yt_category;
    private int yt_artificial_category;
    private int duration;
    private float comments_sentiment_neg;
    private float comments_sentiment_neu;
    private float comments_sentiment_pos;
    private float comments_sentiment_compound;
    private int channel_uploads;
    private long channel_subscribers;
    private long channel_views;
    private long channel_comments;
    private long views_dif;
    private int likes_dif;
    private int dislikes_dif;
    private int comments_dif;
    private float views_acc;
    private float likes_acc;
    private float dislikes_acc;
    private float comments_acc;
    private ArrayList<YoutubeDay> days;
    private ArrayList<age_ratioYouTube> ageRatios;
    private ArrayList<ratioYouTube> ratios;
    private String ytBinary;

    public AllYoutubeFeatures(int window, VideoData videoData,String yt){
        this.window=window;
        this.videoData = videoData;
        this.ytBinary = yt;
        days = new ArrayList<>();
        ageRatios = new ArrayList<>();
        ratios = new ArrayList<>();

        this.yt_category = videoData.getYoutubeFeatures().getYt_category();
        this.yt_artificial_category = videoData.getYoutubeFeatures().getYt_artificial_category();
        this.duration = videoData.getYoutubeFeatures().getDuration();
        this.yt_uploaded = videoData.getYoutubeFeatures().getYt_uploaded();
        this.channel_subscribers = videoData.getChannel_subscribers();
        this.channel_uploads = videoData.getChannel_uploads();
        this.channel_comments = videoData.getChannel_comments();
        this.channel_views = videoData.getChannel_views();
        this.comments_sentiment_compound = videoData.getYoutubeFeatures().getComments_sentiment_compound();
        this.comments_sentiment_neg = videoData.getYoutubeFeatures().getComments_sentiment_neg();
        this.comments_sentiment_pos = videoData.getYoutubeFeatures().getComments_sentiment_pos();
        this.comments_sentiment_neu = videoData.getYoutubeFeatures().getComments_sentiment_neu();

        createDays();
        createAgeRatios();
        createRatios();
        calculateAcceleration();
        calculateDifference();
    }

    public void calculateDifference(){
        YoutubeFeatures yt = videoData.getYoutubeFeatures();
        long firstDayViews= yt.getFeaturesForDay(0).getYt_views()+yt.getFeaturesForDay(1).getYt_views();
        int firstDayLikes = yt.getFeaturesForDay(0).getYt_likes()+yt.getFeaturesForDay(1).getYt_likes();
        int firstDayDislikes = yt.getFeaturesForDay(0).getYt_dislikes()+yt.getFeaturesForDay(1).getYt_dislikes();
        int firstDayComments = yt.getFeaturesForDay(0).getYt_comments()+yt.getFeaturesForDay(1).getYt_comments();
        int lastDayViews=0;
        int lastDayLikes=0;
        int lastDayDislikes=0;
        int lastDayComments=0;
        for(int i=0;i<=window;i++){
            lastDayViews+= yt.getFeaturesForDay(i).getYt_views();
            lastDayLikes+=yt.getFeaturesForDay(i).getYt_likes();
            lastDayDislikes+=yt.getFeaturesForDay(i).getYt_dislikes();
            lastDayComments+=yt.getFeaturesForDay(i).getYt_comments();
        }
        views_dif = lastDayViews-firstDayViews;
        likes_dif = lastDayLikes-firstDayLikes;
        dislikes_dif = lastDayDislikes-firstDayDislikes;
        comments_dif = lastDayComments-firstDayComments;
    }

    public void calculateAcceleration(){
        YoutubeFeatures yt = videoData.getYoutubeFeatures();
        views_acc=0;
        likes_acc=0;
        dislikes_acc=0;
        comments_acc=0;
        for(int i=1;i<=window;i++){
            views_acc+=yt.getFeaturesForDay(i).getYt_views();
            likes_acc+=yt.getFeaturesForDay(i).getYt_likes();
            dislikes_acc+=yt.getFeaturesForDay(i).getYt_dislikes();
            comments_acc+=yt.getFeaturesForDay(i).getYt_comments();
        }
        views_acc = views_acc/(float)window;
        likes_acc = likes_acc/(float)window;
        dislikes_acc = dislikes_acc/(float)window;
        comments_acc = comments_acc/(float)window;
    }

    public void createDays(){
        for(int i=0;i<=window;i++){
            days.add(videoData.getYoutubeFeatures().getFeaturesForDay(i));
        }
    }

    public void createAgeRatios(){
        for(int i=1;i<days.size();i++){
            age_ratioYouTube age = new age_ratioYouTube(i,videoData.getYoutubeFeatures());
            age.setYtBinary(ytBinary);
            ageRatios.add(age);
        }
    }

    public void createRatios(){
        for(int i=1;i<days.size();i++){
            ratioYouTube ratio = new ratioYouTube(i,videoData.getYoutubeFeatures());
            ratio.setYtBinary(ytBinary);
            ratios.add(ratio);
        }
    }



    public Date getYt_uploaded() {
        return yt_uploaded;
    }

    public void setYt_uploaded(Date yt_uploaded) {
        this.yt_uploaded = yt_uploaded;
    }

    public int getYt_category() {
        return yt_category;
    }

    public void setYt_category(int yt_category) {
        this.yt_category = yt_category;
    }




    @Override
    public String toString() {

        if(days.size()==1) {
            String featureString = "";
            String dayStats = "";

            /**
             * Static YouTube features
             */
            if(ytBinary.charAt(0)=='1'){ featureString = featureString.concat(yt_category+",");}
            if(ytBinary.charAt(1)=='1'){ featureString = featureString.concat(yt_artificial_category+",");}
            if(ytBinary.charAt(2)=='1'){ featureString = featureString.concat(duration+",");}
            if(ytBinary.charAt(3)=='1'){ featureString = featureString.concat(comments_sentiment_neg+",");}
            if(ytBinary.charAt(4)=='1'){ featureString = featureString.concat(comments_sentiment_neu+",");}
            if(ytBinary.charAt(5)=='1'){ featureString = featureString.concat(comments_sentiment_pos+",");}
            if(ytBinary.charAt(6)=='1'){ featureString = featureString.concat(comments_sentiment_compound+",");}
            if(ytBinary.charAt(7)=='1'){ featureString = featureString.concat(channel_uploads+",");}
            if(ytBinary.charAt(8)=='1'){ featureString = featureString.concat(channel_subscribers+",");}
            if(ytBinary.charAt(9)=='1'){ featureString = featureString.concat(channel_views+",");}
            if(ytBinary.charAt(10)=='1'){ featureString = featureString.concat(channel_comments+",");}

            /**
             * Day stats for only day zero
             */
            if(ytBinary.charAt(19)=='1'){ dayStats = dayStats.concat(days.get(0).getYt_views()+",");}
            if(ytBinary.charAt(20)=='1'){ dayStats = dayStats.concat(days.get(0).getYt_likes()+",");}
            if(ytBinary.charAt(21)=='1'){ dayStats = dayStats.concat(days.get(0).getYt_dislikes()+",");}
            if(ytBinary.charAt(22)=='1'){ dayStats = dayStats.concat(days.get(0).getYt_comments()+",");}

            /**
             * Removing last comma if it exists
             */
            if(featureString.charAt(featureString.length()-1)==','){
                featureString = featureString.substring(0,featureString.length()-1);
            }

            featureString = featureString.concat(dayStats);

            return featureString;
        }else{
            String daysStats="";
            String featureString="";

            /**
             * Static YouTube features
             */
            if(ytBinary.charAt(0)=='1'){ featureString = featureString.concat(yt_category+",");}
            if(ytBinary.charAt(1)=='1'){ featureString = featureString.concat(yt_artificial_category+",");}
            if(ytBinary.charAt(2)=='1'){ featureString = featureString.concat(duration+",");}
            if(ytBinary.charAt(3)=='1'){ featureString = featureString.concat(comments_sentiment_neg+",");}
            if(ytBinary.charAt(4)=='1'){ featureString = featureString.concat(comments_sentiment_neu+",");}
            if(ytBinary.charAt(5)=='1'){ featureString = featureString.concat(comments_sentiment_pos+",");}
            if(ytBinary.charAt(6)=='1'){ featureString = featureString.concat(comments_sentiment_compound+",");}
            if(ytBinary.charAt(7)=='1'){ featureString = featureString.concat(channel_uploads+",");}
            if(ytBinary.charAt(8)=='1'){ featureString = featureString.concat(channel_subscribers+",");}
            if(ytBinary.charAt(9)=='1'){ featureString = featureString.concat(channel_views+",");}
            if(ytBinary.charAt(10)=='1'){ featureString = featureString.concat(channel_comments+",");}

            /**
             * Differences
             */
            if(ytBinary.charAt(11)=='1'){ featureString = featureString.concat(views_dif+",");}
            if(ytBinary.charAt(12)=='1'){ featureString = featureString.concat(likes_dif+",");}
            if(ytBinary.charAt(13)=='1'){ featureString = featureString.concat(dislikes_dif+",");}
            if(ytBinary.charAt(14)=='1'){ featureString = featureString.concat(comments_dif+",");}

            /**
             * Acceleration
             */
            if(ytBinary.charAt(15)=='1'){ featureString = featureString.concat(views_acc+",");}
            if(ytBinary.charAt(16)=='1'){ featureString = featureString.concat(likes_acc+",");}
            if(ytBinary.charAt(17)=='1'){ featureString = featureString.concat(dislikes_acc+",");}
            if(ytBinary.charAt(18)=='1'){ featureString = featureString.concat(comments_acc+",");}

            /**
             * Day stats
             */
            for(int i=1;i<days.size();i++){
                String t_dayStats = "";
                if(ytBinary.charAt(19)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getYt_views()+",");}
                if(ytBinary.charAt(20)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getYt_likes()+",");}
                if(ytBinary.charAt(21)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getYt_dislikes()+",");}
                if(ytBinary.charAt(22)=='1'){ t_dayStats = t_dayStats.concat(days.get(i).getYt_comments()+",");}
                daysStats = daysStats.concat(t_dayStats);
            }

            featureString = featureString.concat(daysStats);

            /**
             * Age Ratios
             */
            String ageFeatures = "";
            for(int i=0;i<ageRatios.size();i++){
                ageFeatures = ageFeatures.concat(ageRatios.get(i).toString());
            }

            featureString = featureString.concat(ageFeatures);

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
