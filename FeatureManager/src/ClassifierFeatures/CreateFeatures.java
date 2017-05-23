package ClassifierFeatures;

import models.VideoData;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Map;

/**
 * Created by Giorgos on 04/01/2017.
 * Creating Classifier features for each video
 * For 1 day training enter window = 0
 */
public class CreateFeatures {

    private Map<String, VideoData> videosMap;
    private ArrayList<String> uniqueVideos;
    private int t_window;
    private int offset;
    private int l_window;
    private boolean recent;
    private PrintWriter pw;
    private PrintWriter lab;
    private PrintWriter pw_twitter;
    private String ytBinary;
    private String twBinary;

    public CreateFeatures(boolean recent,int t,int o,int l){
        this.recent = recent;
        try {
            if(!recent){
                pw = new PrintWriter((new FileWriter("yt_train_all_"+t+""+o+""+l+".txt")));
                lab = new PrintWriter(new FileWriter("labeling_"+t+""+o+""+l+".txt"));
                pw_twitter = new PrintWriter(new FileWriter("tw_train_all_"+t+""+o+""+l+".txt"));
            }else{
                pw = new PrintWriter((new FileWriter("yt_train_all_recent_"+t+""+o+""+l+".txt")));
                lab = new PrintWriter(new FileWriter("labeling_recent_"+t+""+o+""+l+".txt"));
                pw_twitter = new PrintWriter(new FileWriter("tw_train_all_recent_"+t+""+o+""+l+".txt"));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void create(){
        /**
         * Getting Training data
         */
        for(int i=0;i<uniqueVideos.size();i++){
            String video = uniqueVideos.get(i);
            TrainingFeatures training = new TrainingFeatures(videosMap.get(video),t_window,ytBinary,twBinary);
            pw.println(training.getAllYoutubeFeatures());
            pw.flush();
            pw_twitter.println(training.getAllTwitterFeatures());
            pw_twitter.flush();
        }


        /**
         * Getting Labeling data
         */
        LabelingFeatures label = new LabelingFeatures(videosMap);
        for(int i=0;i<uniqueVideos.size();i++){
            label.labelKnown(videosMap.get(uniqueVideos.get(i)));
        }
        lab.println(label.getLabeledPopular());
        lab.println(label.getLabeledViral());
        lab.flush();

        pw.close();
        pw_twitter.close();
        lab.close();
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

    public void setYtBinary(String ytBinary) {
        this.ytBinary = ytBinary;
    }

    public void setTwBinary(String twBinary) {
        this.twBinary = twBinary;
    }
}
