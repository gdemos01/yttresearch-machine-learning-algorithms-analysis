package models;

/**
 * Created by Giorgos on 06-Nov-16.
 */
public class TwitterDay {

    private int day;
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


    public TwitterDay(int day){
        this.day = day;
    }

    public int getTw_tweets() {
        return tw_tweets;
    }

    public void setTw_tweets(int tw_tweets) {
        this.tw_tweets = tw_tweets;
    }

    public int getTw_orig_tweets() {
        return tw_orig_tweets;
    }

    public void setTw_orig_tweets(int tw_orig_tweets) {
        this.tw_orig_tweets = tw_orig_tweets;
    }

    public int getTw_retweets() {
        return tw_retweets;
    }

    public void setTw_retweets(int tw_retweets) {
        this.tw_retweets = tw_retweets;
    }

    public int getTw_user_favorites() {
        return tw_user_favorites;
    }

    public void setTw_user_favorites(int tw_user_favorites) {
        this.tw_user_favorites = tw_user_favorites;
    }

    public int getTw_hashtags() {
        return tw_hashtags;
    }

    public void setTw_hashtags(int tw_hashtags) {
        this.tw_hashtags = tw_hashtags;
    }

    public int getTw_eng() {
        return tw_eng;
    }

    public void setTw_eng(int tw_eng) {
        this.tw_eng = tw_eng;
    }

    public int getTw_sp() {
        return tw_sp;
    }

    public void setTw_sp(int tw_sp) {
        this.tw_sp = tw_sp;
    }

    public int getTw_user_eng() {
        return tw_user_eng;
    }

    public void setTw_user_eng(int tw_user_eng) {
        this.tw_user_eng = tw_user_eng;
    }

    public int getTw_user_sp() {
        return tw_user_sp;
    }

    public void setTw_user_sp(int tw_user_sp) {
        this.tw_user_sp = tw_user_sp;
    }

    public int getTw_user_verified() {
        return tw_user_verified;
    }

    public void setTw_user_verified(int tw_user_verified) {
        this.tw_user_verified = tw_user_verified;
    }

    public int getUsers_days_created_before_video() {
        return users_days_created_before_video;
    }

    public void setUsers_days_created_before_video(int users_days_created_before_video) {
        this.users_days_created_before_video = users_days_created_before_video;
    }

    public float getTw_user_followers() {
        return tw_user_followers;
    }

    public void setTw_user_followers(float tw_user_followers) {
        this.tw_user_followers = tw_user_followers;
    }

    public float getTw_user_friends() {
        return tw_user_friends;
    }

    public void setTw_user_friends(float tw_user_friends) {
        this.tw_user_friends = tw_user_friends;
    }

    public int getTw_user_statuses() {
        return tw_user_statuses;
    }

    public void setTw_user_statuses(int tw_user_statuses) {
        this.tw_user_statuses = tw_user_statuses;
    }

    @Override
    public String toString() {
        return "TwitterDay{" +
                "day=" + day +
                ", tw_tweets=" + tw_tweets +
                ", tw_orig_tweets=" + tw_orig_tweets +
                ", tw_retweets=" + tw_retweets +
                ", tw_user_favorites=" + tw_user_favorites +
                ", tw_hashtags=" + tw_hashtags +
                ", tw_eng=" + tw_eng +
                ", tw_sp=" + tw_sp +
                ", tw_user_eng=" + tw_user_eng +
                ", tw_user_sp=" + tw_user_sp +
                ", tw_user_verified=" + tw_user_verified +
                ", users_days_created_before_video=" + users_days_created_before_video +
                ", tw_user_followers=" + tw_user_followers +
                ", tw_user_friends=" + tw_user_friends +
                ", tw_user_statuses=" + tw_user_statuses +
                '}';
    }
}
