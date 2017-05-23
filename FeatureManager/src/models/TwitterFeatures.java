package models;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Giorgos on 06-Nov-16.
 */
public class TwitterFeatures {

    private Map<Integer,TwitterDay> days;
    private int tw_user_followers;
    private int tw_user_verified;
    private int tw_user_friends;


    public TwitterFeatures() {
        this.tw_user_followers = 0;
        this.tw_user_verified = 0;
        this.tw_user_friends = tw_user_friends;
        days = new HashMap<>();
    }

    public int getTw_user_friends() {
        return tw_user_friends;
    }

    public int getTw_user_followers() {
        return tw_user_followers;
    }

    public int getTw_user_verified() {
        return tw_user_verified;
    }

    public Map<Integer,TwitterDay> getAllDays() {
        return days;
    }

    @Override
    public String toString() {
        return "TwitterFeatures{" +
                "days=" + days +
                ", tw_user_followers=" + tw_user_followers +
                ", tw_user_verified=" + tw_user_verified +
                ", tw_user_friends=" + tw_user_friends +
                '}';
    }

    public void addDay(TwitterDay day, int dayNum){
        this.days.put(dayNum,day);
    }

}
