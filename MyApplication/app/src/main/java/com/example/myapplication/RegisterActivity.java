package com.example.myapplication;

import android.os.AsyncTask;
import android.util.Log;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class RegisterActivity extends AsyncTask<String, Void, String> {
    String sendMsg, receiveMsg;

    //여기는 웹사이트 접속하는곳
    @Override
    protected String doInBackground(String... strings) {
        try {
            String str;
            URL url = new URL("http://70.12.225.119:8080/AndroidWeb/androidDB.jsp");

            if(strings[0].equals("login")){
                Log.d("State","로그인 들어감");
                url = new URL("http://70.12.225.119:8080/AndroidWeb/androidDB.jsp");
            }
            else if(strings[0].equals("join")){
                Log.d("State","조인 들어감");
                url = new URL("http://70.12.225.119:8080/AndroidWeb/join.jsp");
            }
            else if(strings[0].equals("getBookList")){
                Log.d("State","조인 들어감");
                url = new URL("http://70.12.225.119:8080/AndroidWeb/getBookList.jsp");
            }


            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setRequestMethod("POST");
            OutputStreamWriter osw = new OutputStreamWriter(conn.getOutputStream());

            // 전송할 데이터. GET 방식으로 작성
            sendMsg = "id=" + strings[1] + "&pw=" + strings[2];

            osw.write(sendMsg);
            osw.flush();

            //jsp와 통신 성공 시 수행
            if (conn.getResponseCode() == conn.HTTP_OK) {

                InputStreamReader tmp = new InputStreamReader(conn.getInputStream(), "UTF-8");
                BufferedReader reader = new BufferedReader(tmp);
                StringBuffer buffer = new StringBuffer();


                // jsp에서 보낸 값을 받는 부분
                while ((str = reader.readLine()) != null) {
                    //Log.i("Result",str);
                    buffer.append(str);
                }

                Document doc = Jsoup.parse(buffer.toString());
                Elements title = doc.select("body");
                receiveMsg = title.text();

            } else {
                Log.d("data : ","통신실패");
            }

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //jsp로부터 받은 리턴 값
        return receiveMsg;
    }

}
