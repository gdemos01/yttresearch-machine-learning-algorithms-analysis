import ClassifierFeatures.CreateBaseFeatures;
import ClassifierFeatures.CreateFeatures;
import models.VideoData;
import records.VideoRecord;

import java.io.*;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Created by gdemos01 on 3/15/2017.
 */
public class Exporter {


    private static BufferedReader bf;
    private static int t_window;
    private static int offset;
    private static int l_window;
    private static int split_days;
    private String twFeatures;
    private String ytFeatures;
    private static Map<String, VideoData> videosMapRecent;
    private static Map<String, VideoData> videosMap;
    private static ArrayList<String> uniqueVideos;
    private static ArrayList<String> uniqueVideosRecent;
    private static FeatureManager featureManager;

    public static void readCSV(String experimentDirectory){
        /**
         * Loading Videos from file
         */
        try {
            bf = new BufferedReader(new FileReader(new File(experimentDirectory)));

            String line=bf.readLine();
            System.out.println(line);
            while((line = bf.readLine())!=null){
                String parts[] = line.split("\t");
                String videoID = parts[0];
                if(!videosMap.containsKey(videoID)) {
                    long published_at = Long.parseLong(parts[3]);
                    long collected_at = Long.parseLong(parts[4]);
                    VideoData videoData =
                            new VideoData(published_at,collected_at,
                                    videoID, featureManager.prepareYouTubeFeatures(parts),
                                    featureManager.prepareTwitterFeatures(parts));

                    if(parts[parts.length-2].equals("1")){
                        videoData.setPopular(1);
                    }else{
                        videoData.setPopular(0);
                    }

                    if(parts[parts.length-1].equals("1")){
                        videoData.setViral(1);
                    }else{
                        videoData.setViral(0);
                    }

                    /**
                     * If there aren't any Youtube or Twitter features
                     * we should not include the video
                     */
                    if(!(videoData.getYoutubeFeatures()==null)&&!(videoData.getTwitterFeatures()==null)){
                        long uploaded = videoData.getPublished_at();
                        long today = videoData.getCollected_at();
                        long daysPassed = (today-uploaded)/(1000*60*60*24);
                        if(daysPassed>split_days){
                            uniqueVideos.add(videoID);
                            videoData.calculateTotals(t_window,offset,l_window);
                            videosMap.put(videoID,videoData);
                        }else{
                            uniqueVideosRecent.add(videoID);
                            videoData.calculateTotals(t_window,offset,l_window);
                            videosMapRecent.put(videoID,videoData);
                        }
                    }

                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }

    public static void main(String  args[]){
        videosMap = new HashMap<>();
        videosMapRecent = new HashMap<>();

        Scanner scan = new Scanner(System.in);
        String experimentDirectory = "";
        String ytFeatures ="";
        String twFeatures = "";
        int split_days = 14;

        /**
         * User Input
         */
        System.out.print("Enter directory of CSV file: ");
        experimentDirectory = scan.nextLine();
        //System.out.print("Enter YouTube features binary: ");
        //ytFeatures = scan.nextLine();
        //System.out.print("Enter Twitter features binary: ");
        //twFeatures = scan.nextLine();
        System.out.print("Enter training window: ");
        int t_window = scan.nextInt();
        System.out.print("Enter offset: ");
        int offset = scan.nextInt();
        System.out.print("Enter labeling window: ");
        int l_window = scan.nextInt();

        ytFeatures = "1111111111111111111111111111111";
        twFeatures = "1111111111111111111111111111111111111111111";
        uniqueVideos = new ArrayList<>();
        uniqueVideosRecent = new ArrayList<>();

        /**
         * To run  Feature manager:
         */
        featureManager = new FeatureManager(t_window,offset,l_window,split_days,ytFeatures,twFeatures);
        readCSV(experimentDirectory);
        featureManager.populate(videosMap,videosMapRecent,uniqueVideos,uniqueVideosRecent);
        featureManager.createFeatures();

    }
}
