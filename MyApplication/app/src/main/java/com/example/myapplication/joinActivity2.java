package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class joinActivity2 extends AppCompatActivity {

    Button check;
    EditText userpwd;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_join2);

        check = (Button)findViewById(R.id.check);
        userpwd = (EditText) findViewById(R.id.userpwd);




        check.setOnClickListener(new View.OnClickListener() {

            Intent intent = getIntent();

            @Override
            public void onClick(View v) {

                try{
                    String pwd = userpwd.getText().toString();

                    RegisterActivity task = new RegisterActivity();
                    task.execute("join",intent.getExtras().getString("userid"),pwd).get();//회원가입 보내고

                    intent = new Intent(getApplicationContext(),myBook.class);//mybook로 이동
                    startActivity(intent);
                }
                catch(Exception e){
                }
            }
        });


    }
}
