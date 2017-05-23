package records;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by gdemos01 on 3/15/2017.
 */
public class VideoRecord {

    private int yt_category;
    private int yt_artificial_category;
    private Timestamp yt_uploaded ;
    private int duration;
    private float comments_sentiment_neg;
    private float comments_sentiment_neu;
    private float comments_sentiment_pos;
    private float comments_sentiment_compound;
    private List<DayRecord> days;

    public VideoRecord() {
    }

    public VideoRecord(int yt_category, int yt_artificial_category, Timestamp yt_uploaded, int duration,
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

    public void addDay(DayRecord dayRecord){
        days.add(dayRecord);
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

    public List<DayRecord> getDays() {
        return days;
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

    public void setYt_category(int yt_category) {
        this.yt_category = yt_category;
    }

    public void setYt_artificial_category(int yt_artificial_category) {
        this.yt_artificial_category = yt_artificial_category;
    }

    public void setYt_uploaded(Timestamp yt_uploaded) {
        this.yt_uploaded = yt_uploaded;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public void setComments_sentiment_neg(float comments_sentiment_neg) {
        this.comments_sentiment_neg = comments_sentiment_neg;
    }

    public void setComments_sentiment_neu(float comments_sentiment_neu) {
        this.comments_sentiment_neu = comments_sentiment_neu;
    }

    public void setComments_sentiment_pos(float comments_sentiment_pos) {
        this.comments_sentiment_pos = comments_sentiment_pos;
    }

    public void setComments_sentiment_compound(float comments_sentiment_compound) {
        this.comments_sentiment_compound = comments_sentiment_compound;
    }
}
