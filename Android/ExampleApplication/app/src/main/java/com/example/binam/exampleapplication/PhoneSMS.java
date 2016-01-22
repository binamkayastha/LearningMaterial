package com.example.binam.exampleapplication;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class PhoneSMS extends AppCompatActivity {

    EditText etPhone;
    EditText etMsg;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_phone_sms);

        etPhone = (EditText) findViewById(R.id.etphone);
        etMsg = (EditText) findViewById(R.id.etmessage);
    }

    public void call (View view) {
        String phnum = etPhone.getText().toString();
        Intent callIntent = new Intent(Intent.ACTION_CALL);
        callIntent.setData(Uri.parse("tel:" + phnum));
        startActivity(callIntent);
    }

    public void message (View view) {
        String phnum = etPhone.getText().toString();
        String msg = etMsg.getText().toString();
        SmsManager smsManager = SmsManager.getDefault();
        smsManager.sendTextMessage(phnum, null, msg, null, null);
        Toast.makeText(getApplicationContext(), "Message sent", Toast.LENGTH_LONG).show();

    }

}
