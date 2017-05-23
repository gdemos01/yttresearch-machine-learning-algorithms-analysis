package records;

/**
 * Created by gdemos01 on 3/15/2017.
 */
public class DayRecord {

    private int views;
    private int likes;
    private int dislikes;
    private int comments;
    private long channel_views;
    private long channel_comments;
    private long channel_subscribers;
    private int channel_videos;

    private int tw_tweets;
    private int tw_orig_tweets;
    private int tw_retweets;
    private int tw_user_favorites;
    private int tw_hashtags;
    private int tw_eng;
    private int tw_sp;
    private int tw_user_eng;
    private int tw_user_sp;
    private int tw_user_verified;
    private int users_days_created_before_video;
    private float tw_user_followers;
    private float tw_user_friends;
    private int tw_user_statuses;

    public DayRecord() {
    }

    public DayRecord(int views, int likes, int dislikes, int comments, long channel_views, long channel_comments,
                     long channel_subscribers, int channel_videos, int tw_tweets, int tw_orig_tweets, int tw_retweets,
                     int tw_user_favorites, int tw_hashtags, int tw_eng, int tw_sp, int tw_user_eng, int tw_user_sp,
                     int tw_user_verified, int users_days_created_before_video, float tw_user_followers,
                     float tw_user_friends, int tw_user_statuses) {
        this.views = views;
        this.likes = likes;
        this.dislikes = dislikes;
        this.comments = comments;
        this.channel_views = channel_views;
        this.channel_comments = channel_comments;
        this.channel_subscribers = channel_subscribers;
        this.channel_videos = channel_videos;
        this.tw_tweets = tw_tweets;
        this.tw_orig_tweets = tw_orig_tweets;
        this.tw_retweets = tw_retweets;
        this.tw_user_favorites = tw_user_favorites;
        this.tw_hashtags = tw_hashtags;
        this.tw_eng = tw_eng;
        this.tw_sp = tw_sp;
        this.tw_user_eng = tw_user_eng;
        this.tw_user_sp = tw_user_sp;
        this.tw_user_verified = tw_user_verified;
        this.users_days_created_before_video = users_days_created_before_video;
        this.tw_user_followers = tw_user_followers;
        this.tw_user_friends = tw_user_friends;
        this.tw_user_statuses = tw_user_statuses;
    }

    public int getViews() {
        return views;
    }

    public int getLikes() {
        return likes;
    }

    public int getDislikes() {
        return dislikes;
    }

    public int getComments() {
        return comments;
    }

    public long getChannel_views() {
        return channel_views;
    }

    public long getChannel_comments() {
        return channel_comments;
    }

    public long getChannel_subscribers() {
        return channel_subscribers;
    }

    public int getChannel_videos() {
        return channel_videos;
    }

    public int getTw_tweets() {
        return tw_tweets;
    }

    public int getTw_orig_tweets() {
        return tw_orig_tweets;
    }

    public int getTw_retweets() {
        return tw_retweets;
    }

    public int getTw_user_favorites() {
        return tw_user_favorites;
    }

    public int getTw_hashtags() {
        return tw_hashtags;
    }

    public int getTw_eng() {
        return tw_eng;
    }

    public int getTw_sp() {
        return tw_sp;
    }

    public int getTw_user_eng() {
        return tw_user_eng;
    }

    public int getTw_user_sp() {
        return tw_user_sp;
    }

    public int getTw_user_verified() {
        return tw_user_verified;
    }

    public int getUsers_days_created_before_video() {
        return users_days_created_before_video;
    }

    public float getTw_user_followers() {
        return tw_user_followers;
    }

    public float getTw_user_friends() {
        return tw_user_friends;
    }

    public int getTw_user_statuses() {
        return tw_user_statuses;
    }

    public void setViews(int views) {
        this.views = views;
    }

    public void setLikes(int likes) {
        this.likes = likes;
    }

    public void setDislikes(int dislikes) {
        this.dislikes = dislikes;
    }

    public void setComments(int comments) {
        this.comments = comments;
    }

    public void setChannel_views(long channel_views) {
        this.channel_views = channel_views;
    }

    public void setChannel_comments(long channel_comments) {
        this.channel_comments = channel_comments;
    }

    public void setChannel_subscribers(long channel_subscribers) {
        this.channel_subscribers = channel_subscribers;
    }

    public void setChannel_videos(int channel_videos) {
        this.channel_videos = channel_videos;
    }

    public void setTw_tweets(int tw_tweets) {
        this.tw_tweets = tw_tweets;
    }

    public void setTw_orig_tweets(int tw_orig_tweets) {
        this.tw_orig_tweets = tw_orig_tweets;
    }

    public void setTw_retweets(int tw_retweets) {
        this.tw_retweets = tw_retweets;
    }

    public void setTw_user_favorites(int tw_user_favorites) {
        this.tw_user_favorites = tw_user_favorites;
    }

    public void setTw_hashtags(int tw_hashtags) {
        this.tw_hashtags = tw_hashtags;
    }

    public void setTw_eng(int tw_eng) {
        this.tw_eng = tw_eng;
    }

    public void setTw_sp(int tw_sp) {
        this.tw_sp = tw_sp;
    }

    public void setTw_user_eng(int tw_user_eng) {
        this.tw_user_eng = tw_user_eng;
    }

    public void setTw_user_sp(int tw_user_sp) {
        this.tw_user_sp = tw_user_sp;
    }

    public void setTw_user_verified(int tw_user_verified) {
        this.tw_user_verified = tw_user_verified;
    }

    public void setUsers_days_created_before_video(int users_days_created_before_video) {
        this.users_days_created_before_video = users_days_created_before_video;
    }

    public void setTw_user_followers(float tw_user_followers) {
        this.tw_user_followers = tw_user_followers;
    }

    public void setTw_user_friends(float tw_user_friends) {
        this.tw_user_friends = tw_user_friends;
    }

    public void setTw_user_statuses(int tw_user_statuses) {
        this.tw_user_statuses = tw_user_statuses;
    }
}
