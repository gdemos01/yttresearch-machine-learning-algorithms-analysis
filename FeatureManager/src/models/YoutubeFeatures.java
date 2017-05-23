package models;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Date;

/**
 * Created by Giorgos on 06-Nov-16.
 */
public class YoutubeFeatures {

    private int yt_category;
    private int yt_artificial_category;
    private Timestamp yt_uploaded;
    private int duration;
    private float comments_sentiment_neg;
    private float comments_sentiment_neu;
    private float comments_sentiment_pos;
    private float comments_sentiment_compound;
    private ArrayList<YoutubeDay> days;

    public YoutubeFeatures(int yt_category, int yt_artificial_category, Timestamp yt_uploaded, int duration,
                           float comments_sentiment_neg, float comments_sentiment_neu, float comments_sentiment_pos,
                           float comments_sentiment_compound) {
        this.yt_category = yt_category;
        this.yt_artificial_category = yt_artificial_category;
        this.yt_uploaded = yt_uploaded;
        this.duration = duration;
        this.comments_sentiment_neg = comments_sentiment_neg;
        this.comments_sentiment_neu = comments_sentiment_neu;
        this.comments_sentiment_pos = comments_sentiment_pos;
        this.comments_sentiment_compound = comments_sentiment_compound;
        this.days = new ArrayList<>();
    }

    public int getYt_category() {
        return yt_category;
    }

    public int getYt_artificial_category() {
        return yt_artificial_category;
    }

    public Timestamp getYt_uploaded() {
        return yt_uploaded;
    }

    public int getDuration() {
        return duration;
    }

    public float getComments_sentiment_neg() {
        return comments_sentiment_neg;
    }

    public float getComments_sentiment_neu() {
        return comments_sentiment_neu;
    }

    public float getComments_sentiment_pos() {
        return comments_sentiment_pos;
    }

    public float getComments_sentiment_compound() {
        return comments_sentiment_compound;
    }

    /***
     * Add Youtube features for a specific day
     * @param day
     */
    public void addDay(YoutubeDay day){
        this.days.add(day);
    }

    /***
     * Get YouTube features for a specific day
     * starting from day 1
     * @param day
     * @return
     */
    public YoutubeDay getFeaturesForDay(int day){
        YoutubeDay d = days.get(day);
        if(d.getDay()== day) {
            return d;
        }else{
            for(int i=0;i<days.size();i++){
                d = days.get(i);
                if(d.getDay()==day) return d;
            }
        }
        return d;
    }

    @Override
    public String toString() {
        return "YoutubeFeatures{" +
                "yt_category=" + yt_category +
                ", yt_artificial_category=" + yt_artificial_category +
                ", yt_uploaded=" + yt_uploaded +
                ", duration=" + duration +
                ", comments_sentiment_neg=" + comments_sentiment_neg +
                ", comments_sentiment_neu=" + comments_sentiment_neu +
                ", comments_sentiment_pos=" + comments_sentiment_pos +
                ", comments_sentiment_compound=" + comments_sentiment_compound +
                ", days=" + days +
                '}';
    }

    public ArrayList<YoutubeDay> getAllDays() {
        return days;
    }
}
