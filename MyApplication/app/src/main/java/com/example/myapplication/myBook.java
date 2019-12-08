package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.graphics.Point;
import android.os.Bundle;
import android.util.Log;
import android.view.Display;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;
import android.widget.EditText;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;

public class myBook extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_book);



        try{

            final EditText book = (EditText)findViewById(R.id.book);
            final String allText = readFromAssets("bookText/hojil.txt");




            Display display = getWindowManager().getDefaultDisplay();
            Point size = new Point();
            display.getSize(size);
            int width = size.x;
            int height = size.y;

            final int standard = width/2;
            final int pageStantard = 350;

            book.setText(allText.substring(0,pageStantard));//처음 페이지

            book.setOnTouchListener(new View.OnTouchListener() {//페이지 이동하는 코드 수정해야함
                int count = 1;

                String preText = "";
                String currentText =allText.substring(0,pageStantard);
                String proText = allText.substring(pageStantard,allText.length());



                @Override
                public boolean onTouch(View v, MotionEvent event) {
                    if(event.getAction() == MotionEvent.ACTION_DOWN){
                        if(event.getX()<standard && count >1 ){

                            count--;

                            proText = currentText.concat(proText);

                            currentText = preText.substring(preText.length()-pageStantard);
                            preText = preText.substring(0,preText.length()-pageStantard);

                            book.setText(currentText);
                        }
                        else if(event.getX()>standard){
                            try{
                                preText = preText.concat(currentText);
                                currentText = proText.substring(0,pageStantard);
                                proText = proText.substring(pageStantard);

                                book.setText(currentText);
                                count++;
                            }
                            catch(Exception e){
                                e.printStackTrace();
                            }
                        }
                    }
                    return true;
                }
            });

        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
    private String readFromAssets(String filename) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(getAssets().open(filename)));

        StringBuilder sb = new StringBuilder();
        String line = reader.readLine();
        while(line != null) {
            sb.append("\n");
            sb.append(line);
            line = reader.readLine();
        }
        reader.close();
        return sb.toString();
    }
}
