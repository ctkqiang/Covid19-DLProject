package my.kylogger.johnmelodyme.iot.embedded.machinelearning.covid19;
/**
 *                   Copyright 2020 © John Melody Me
 *
 *       Licensed under the Apache License, Version 2.0 (the "License");
 *       you may not use this file except in compliance with the License.
 *       You may obtain a copy of the License at
 *
 *                   http://www.apache.org/licenses/LICENSE-2.0
 *
 *       Unless required by applicable law or agreed to in writing, software
 *       distributed under the License is distributed on an "AS IS" BASIS,
 *       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *       See the License for the specific language governing permissions and
 *       limitations under the License.
 *       @Author : John Melody Me
 *       @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
 *       @INPIREDBYGF: Cindy Tan Sin Dee <3
 */

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.telephony.PhoneStateListener;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;

public class CovidNineteenActivity extends AppCompatActivity {
    public static final String TAG = "CovidNineteenActivity";
    public static final String DEATH_RATE = "https://github.com/johnmelodyme/Covid19-DLProject/blob/master/data/deaths.csv";
    public GraphView deathRate;
    private Button Plot;

    //TODO DeclarationInit:
    public void DeclarationInit() {
        deathRate = findViewById(R.id.death);
        Plot = findViewById(R.id.plot);
    }

    private void createLineGraph(List<String[]> result) {
        DataPoint[] dataPoints = new DataPoint[result.size()];
        for (int i = 0; i < result.size(); i++){
            String [] rows = result.get(i);
//            Log.d(TAG, "Output " + Integer.parseInt(rows[0]) + " " + Integer.parseInt(rows[1]));
            dataPoints[i] = new DataPoint(Integer.parseInt(rows[0]), Integer.parseInt(rows[1]));
        }
        LineGraphSeries<DataPoint> series = new LineGraphSeries<DataPoint>(dataPoints);
        deathRate.addSeries(series);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "onCreate: " + CovidNineteenActivity.class.getSimpleName());
        DeclarationInit();

        Plot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DownloadFilesTask downloadFilesTask = new DownloadFilesTask();
                downloadFilesTask.execute();
            }
        });
    }

    private class DownloadFilesTask extends AsyncTask<URL, Void, List<String[]>> {
        protected List<String[]> doInBackground(URL... urls) {
            return downloadRemoteTextFileContent();
        }

        protected void onPostExecute(List<String[]> result) {
            if(result != null){
                createLineGraph(result);
            }
        }
    }

    private List<String[]> downloadRemoteTextFileContent(){
        URL mUrl = null;
        List<String[]> csvLine = new ArrayList<>();
        String[] content = null;
        try {
            mUrl = new URL(DEATH_RATE);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        try {
            assert mUrl != null;
            URLConnection connection = mUrl.openConnection();
            BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String line = "";
            while((line = br.readLine()) != null){
                content = line.split(",");
                csvLine.add(content);
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return csvLine;
    }
}
