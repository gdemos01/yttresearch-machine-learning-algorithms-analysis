package ClassifierFeatures;

import models.VideoData;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class LabelingFeatures {

    private Map<String, VideoData> videosMap = new HashMap<>();
    private List<Integer> labeledPopular;
    private List<Integer> labeledViral;

    public LabelingFeatures(Map<String, VideoData> videosMap) {
        this.videosMap = videosMap;
        this.labeledPopular = new LinkedList<>();
        this.labeledViral = new LinkedList<>();
    }


    public void labelKnown(VideoData video){

        if(video.getPopular()==1){
            labeledPopular.add(1);
        }else{
            labeledPopular.add(0);
        }

        if(video.getViral()==1){
            labeledViral.add(1);
        }else{
            labeledViral.add(0);
        }
    }


    public List<Integer> getLabeledPopular() {
        return labeledPopular;
    }

    public List<Integer> getLabeledViral() {
        return labeledViral;
    }

}
