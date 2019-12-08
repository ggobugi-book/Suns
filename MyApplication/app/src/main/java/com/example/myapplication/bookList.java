package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class bookList extends AppCompatActivity {

    TextView et;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book_list);


        et = (TextView)findViewById(R.id.textView1);
        String title[];
        String filename[];

        try{
            RegisterActivity task = new RegisterActivity();//서버관련해여 객체 생성
            String result = task.execute("getBookList","0","0").get();//flag:getBookList를 사용하여

            //DB에서 bookList를 넘겨옴 책이름1,책이름2,책이름3|파일이름1,파일이름2,파일이름3 으로 넘어옴

            et.setText(result);

        }
        catch(Exception e){

        }





    }
}
