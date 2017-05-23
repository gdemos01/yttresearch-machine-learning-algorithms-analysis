package ClassifierFeatures;

import models.VideoData;

/**
 * Created by Giorgos on 04/01/2017.
 */
public class TrainingBaseFeatures {
    private VideoData videoData;
    private int window;
    private BaseTwitterFeatures baseTwitterFeatures;
    private BaseYoutubeFeatures baseYoutubeFeatures;

    public TrainingBaseFeatures(VideoData videoData, int window) {
        this.videoData = videoData;
        this.window = window;
        baseYoutubeFeatures = new BaseYoutubeFeatures(window,videoData);
        baseTwitterFeatures = new BaseTwitterFeatures(window,videoData);
    }

    public BaseTwitterFeatures getBaseTwitterFeatures() {
        return baseTwitterFeatures;
    }

    public BaseYoutubeFeatures getBaseYoutubeFeatures() {
        return baseYoutubeFeatures;
    }
}
