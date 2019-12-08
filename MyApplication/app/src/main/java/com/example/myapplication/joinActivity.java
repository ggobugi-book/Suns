package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class joinActivity extends AppCompatActivity {

    Button check;
    EditText userid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_join);

        check = (Button)findViewById(R.id.check);
        userid = (EditText) findViewById(R.id.userid);

       check.setOnClickListener(new View.OnClickListener(){
           public void onClick(View view) {
               try {
                   String result;
                   String id = userid.getText().toString();
                   String pw = "1";

                   RegisterActivity task = new RegisterActivity();
                   result = task.execute("login",id, pw).get();

                   if(result.equals("1")){
                       Log.d("Data : ","아이디있음");
                   }
                   else{
                       Intent intent = new Intent(getApplicationContext(),joinActivity2.class);//아이디 없으면 조인 2로 이동
                       intent.putExtra("userid",id);
                       startActivity(intent);
                   }

               } catch (Exception e) {
                   Log.i("DBtest", ".....ERROR.....!");
               }
           }
       });
    }
}
