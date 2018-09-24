package com.example.eliza.benlizapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.Button;

import android.view.View;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Spinner s= (Spinner) findViewById(R.id.spin);
        final Button calc_butt = (Button) findViewById(R.id.calc_button);
        calc_butt.setVisibility(View.INVISIBLE);
        final Button choose_butt=(Button) findViewById(R.id.choose_button);
        choose_butt.setVisibility(View.INVISIBLE);
        final Button settings_butt=(Button) findViewById(R.id.settings_button);
        settings_butt.setVisibility(View.INVISIBLE);


        s.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                Toast.makeText(MainActivity.this,parent.getSelectedItem().toString(), Toast.LENGTH_SHORT).show();

                calc_butt.setVisibility(View.VISIBLE);
                choose_butt.setVisibility(View.VISIBLE);
                settings_butt.setVisibility(View.VISIBLE);

            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }
    public void onItemSelected(AdapterView<?> parent, View v, int position, long id) {


    }
}

