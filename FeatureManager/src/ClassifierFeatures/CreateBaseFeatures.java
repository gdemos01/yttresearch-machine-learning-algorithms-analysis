package ClassifierFeatures;

import models.VideoData;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Map;

/**
 * Created by Giorgos on 04/01/2017
 * Baseline features for comparison
 * yt_views cumulative
 * tw_orig_tweets cumulative
 */
public class CreateBaseFeatures {

    private Map<String, VideoData> videosMap;
    private ArrayList<String> uniqueVideos;
    private int t_window;
    private int offset;
    private int l_window;
    private PrintWriter pw;
    private PrintWriter pw_twitter;
    private boolean recent;

    public CreateBaseFeatures(boolean recent,int t,int o,int l){
        this.recent=recent;
        try {
            if(!recent){
                pw = new PrintWriter((new FileWriter("yt_train_base_"+t+""+o+""+l+".txt")));
                pw_twitter = new PrintWriter(new FileWriter("tw_train_base_"+t+""+o+""+l+".txt"));
            }else{
                pw = new PrintWriter((new FileWriter("yt_train_base_recent_"+t+""+o+""+l+".txt")));
                pw_twitter = new PrintWriter(new FileWriter("tw_train_base_recent_"+t+""+o+""+l+".txt"));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void create(){
        /**
         * Getting Training data of 90%
         */
        for(int i=0;i<uniqueVideos.size();i++){
            String video = uniqueVideos.get(i);
            TrainingBaseFeatures training = new TrainingBaseFeatures(videosMap.get(video),t_window);
            pw.println(training.getBaseYoutubeFeatures());
            pw.flush();
            pw_twitter.println(training.getBaseTwitterFeatures());
            pw_twitter.flush();
        }

        pw.close();
        pw_twitter.close();
    }

    public void setVideosMap(Map<String, VideoData> videosMap) {
        this.videosMap = videosMap;
    }

    public void setUniqueVideos(ArrayList<String> uniqueVideos) {
        this.uniqueVideos = uniqueVideos;
    }

    public void setT_window(int t_window) {
        this.t_window = t_window;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public void setL_window(int l_window) {
        this.l_window = l_window;
    }
}
