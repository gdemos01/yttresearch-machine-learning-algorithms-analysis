package models;

/**
 * Created by Giorgos on 06-Nov-16.
 */
public class YoutubeDay {

    private int day;
    private long yt_views;
    private int yt_likes;
    private int yt_dislikes;
    private int yt_comments;
    private long yt_channel_views;
    private long yt_channel_comments;
    private long yt_channel_subscribers;
    private int yt_channel_videos;


    public YoutubeDay(int day, long yt_views, int yt_likes, int yt_dislikes, int yt_comments, long yt_channel_views,
                      long yt_channel_comments, long yt_channel_subscribers, int yt_channel_videos) {
        this.day = day;
        this.yt_views = yt_views;
        this.yt_likes = yt_likes;
        this.yt_dislikes = yt_dislikes;
        this.yt_comments = yt_comments;
        this.yt_channel_views = yt_channel_views;
        this.yt_channel_comments = yt_channel_comments;
        this.yt_channel_subscribers = yt_channel_subscribers;
        this.yt_channel_videos = yt_channel_videos;
    }

    public int getDay() {
        return day;
    }

    public long getYt_views() {
        return yt_views;
    }

    public int getYt_likes() {
        return yt_likes;
    }

    public int getYt_dislikes() {
        return yt_dislikes;
    }

    public int getYt_comments() {
        return yt_comments;
    }

    public long getYt_channel_views() {
        return yt_channel_views;
    }

    public long getYt_channel_comments() {
        return yt_channel_comments;
    }

    public long getYt_channel_subscribers() {
        return yt_channel_subscribers;
    }

    public int getYt_channel_videos() {
        return yt_channel_videos;
    }

    @Override
    public String toString() {
        return "YoutubeDay{" +
                "day=" + day +
                ", yt_views=" + yt_views +
                ", yt_likes=" + yt_likes +
                ", yt_dislikes=" + yt_dislikes +
                ", yt_comments=" + yt_comments +
                '}';
    }
}