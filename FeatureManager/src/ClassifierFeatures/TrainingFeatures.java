package ClassifierFeatures;

import models.VideoData;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class TrainingFeatures {

    private VideoData videoData;
    private int window;
    private AllYoutubeFeatures allYoutubeFeatures;
    private AllTwitterFeatures allTwitterFeatures;
    private String ytBinary;
    private String twBinary;

    public TrainingFeatures(VideoData videoData, int window,String yt, String tw) {
        this.videoData = videoData;
        this.window = window;
        this.ytBinary = yt;
        this.twBinary = tw;
        createTrainingYoutube();
        createTrainingTwitter();
    }

    public void createTrainingYoutube(){
        allYoutubeFeatures = new AllYoutubeFeatures(window,videoData,ytBinary);
    }

    public void createTrainingTwitter(){
        allTwitterFeatures = new AllTwitterFeatures(window,videoData,twBinary);
    }

    public AllTwitterFeatures getAllTwitterFeatures() {
        return allTwitterFeatures;
    }

    public AllYoutubeFeatures getAllYoutubeFeatures() {
        return allYoutubeFeatures;
    }

}
