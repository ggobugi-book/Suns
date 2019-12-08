package com.example.myapplication;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Dictionary;

public class cardView extends AppCompatActivity {
    private ArrayList<Dic> mArrayList;
    private CustomAdapter mAdapter;


    TextView et;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_card_view);



        RecyclerView mRecyclerView = (RecyclerView) findViewById(R.id.recyclerview_main_list);
        LinearLayoutManager mLinearLayoutManager = new LinearLayoutManager(this);
        mRecyclerView.setLayoutManager(mLinearLayoutManager);


        mArrayList = new ArrayList<>();

        mAdapter = new CustomAdapter( mArrayList);
        mRecyclerView.setAdapter(mAdapter);


        DividerItemDecoration dividerItemDecoration = new DividerItemDecoration(mRecyclerView.getContext(),
                mLinearLayoutManager.getOrientation());
        mRecyclerView.addItemDecoration(dividerItemDecoration);


        et = (TextView)findViewById(R.id.textView1);
        String title[];
        String filename[];

        try{
            RegisterActivity task = new RegisterActivity();//서버관련해여 객체 생성
            String result = task.execute("getBookList","0","0").get();//flag:getBookList를 사용하여

            //DB에서 bookList를 넘겨옴 책이름1,책이름2,책이름3|파일이름1,파일이름2,파일이름3 으로 넘어옴
            filename = result.split("|");

            Log.d("result: ",result);
            Log.d("filename : ",filename.toString());

        }
        catch(Exception e){

        }



        Dic data = new Dic(getDrawable(R.drawable.hojil),"hojil");

        mArrayList.add(data); // RecyclerView의 마지막 줄에 삽입

        mAdapter.notifyDataSetChanged();




    }
}
