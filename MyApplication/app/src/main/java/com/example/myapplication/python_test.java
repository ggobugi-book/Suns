package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.


public class python_test extends AppCompatActivity {

    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.cnCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

            if (! Python.isStrated())
                python.start(new AndroidPlatform(this));

            Python py = Python.getInsta

    }


}
