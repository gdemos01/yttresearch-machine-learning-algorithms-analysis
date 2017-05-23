package models.ratioModels;

import models.YoutubeFeatures;

/**
 * Created by Giorgos on 02/01/2017.
 */
public class ratioYouTube {
    private int day;
    private YoutubeFeatures youtubeFeatures;
    private float ratioViews;
    private float ratioLikes;
    private float ratioDislikes;
    private float ratioComments;
    private String ytBinary;

    public ratioYouTube(int day, YoutubeFeatures yt) {
        this.day = day;
        this.youtubeFeatures = yt;
        createRatioViews();
        createRatioLikes();
        createRatioDislikes();
        createRatioComments();
    }

    public void createRatioViews(){
        int total_views =0;
        long views_n = youtubeFeatures.getFeaturesForDay(day).getYt_views();
        for(int i=0;i<day-1;i++){
            total_views+= youtubeFeatures.getFeaturesForDay(i).getYt_views();
        }
        if(total_views!=0){
            ratioViews= views_n/(float)total_views;
        }else{
            ratioViews=0;
        }
    }

    public void createRatioLikes(){
        int total_likes =0;
        int likes_n = youtubeFeatures.getFeaturesForDay(day).getYt_likes();
        for(int i=0;i<day-1;i++){
            total_likes+= youtubeFeatures.getFeaturesForDay(i).getYt_likes();
        }
        if(total_likes!=0){
            ratioLikes= likes_n/(float)total_likes;
        }else{
            ratioLikes=0;
        }
    }

    public void createRatioDislikes(){
        int total_dislikes =0;
        int dislikes_n = youtubeFeatures.getFeaturesForDay(day).getYt_dislikes();
        for(int i=0;i<day-1;i++){
            total_dislikes+= youtubeFeatures.getFeaturesForDay(i).getYt_dislikes();
        }
        if(total_dislikes!=0){
            ratioDislikes= dislikes_n/(float)total_dislikes;
        }else{
            ratioDislikes=0;
        }
    }

    public void createRatioComments(){
        int total_comments =0;
        int comments_n = youtubeFeatures.getFeaturesForDay(day).getYt_comments();
        for(int i=0;i<day-1;i++){
            total_comments+= youtubeFeatures.getFeaturesForDay(i).getYt_comments();
        }
        if(total_comments!=0){
            ratioComments= comments_n/(float)total_comments;
        }else{
            ratioComments=0;
        }
    }

    public float getRatioViews(){
        return ratioViews;
    }

    public float getRatioLikes(){
        return ratioLikes;
    }

    public float getRatioDislikes(){
        return ratioDislikes;
    }

    public float getRatioComments(){
        return ratioComments;
    }

    public void setYtBinary(String ytBinary) {
        this.ytBinary = ytBinary;
    }

    @Override
    public String toString() {
        String features = "";

        if(ytBinary.charAt(27)=='1'){features = features.concat(ratioViews + "," );}
        if(ytBinary.charAt(28)=='1'){features = features.concat(ratioLikes + "," );}
        if(ytBinary.charAt(29)=='1'){features = features.concat(ratioDislikes + "," );}
        if(ytBinary.charAt(30)=='1'){features = features.concat(ratioComments + "," ); }

        return features;
    }
}
