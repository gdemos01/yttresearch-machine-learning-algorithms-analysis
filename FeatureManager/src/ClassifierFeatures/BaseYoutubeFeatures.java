package ClassifierFeatures;

import models.VideoData;
import models.YoutubeDay;

import java.util.ArrayList;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class BaseYoutubeFeatures {
    private int window;
    private VideoData videoData;
    private int total_views;
    private ArrayList<YoutubeDay> days;

    public BaseYoutubeFeatures(int window, VideoData videoData) {
        this.window = window;
        this.videoData = videoData;
        days = new ArrayList<>();
        createDays();
    }

    public void createDays(){
        for(int i=0;i<=window;i++){
            days.add(videoData.getYoutubeFeatures().getFeaturesForDay(i));
        }
    }


    @Override
    public String toString() {
        String daysStats="";
        for(int i=1;i<days.size();i++){
            if(i==days.size()-1){
                String dayStats = days.get(i).getYt_views()+"";
                daysStats = daysStats.concat(dayStats);
            }else {
                String dayStats = days.get(i).getYt_views() + ",";
                daysStats = daysStats.concat(dayStats);
            }

        }
        return  daysStats;
    }
}
