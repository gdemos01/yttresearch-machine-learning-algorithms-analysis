package ClassifierFeatures;

import models.TwitterDay;
import models.VideoData;

import java.util.ArrayList;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class BaseTwitterFeatures {
    private int window;
    private VideoData videoData;
    private int total_orig_tweets;
    private ArrayList<TwitterDay> days;

    public BaseTwitterFeatures(int window, VideoData videoData) {
        this.window = window;
        this.videoData = videoData;
        days = new ArrayList<>();
        createDays();
    }

    /**
     * We get only the days that we are interested in
     * depending on the window
     */
    public void createDays(){
        for(int i=0;i<=window;i++){
            days.add(videoData.getTwitterFeatures().getAllDays().get(i));
        }
    }



    @Override
    public String toString() {
        String daysStats="";
        for(int i=1;i<days.size();i++){
            if(i==days.size()-1) {
                String dayStats = days.get(i).getTw_orig_tweets() + "";
                daysStats = daysStats.concat(dayStats);
            }else{
                String dayStats = days.get(i).getTw_orig_tweets() + ",";
                daysStats = daysStats.concat(dayStats);
            }
        }
        return  daysStats;
    }
}
