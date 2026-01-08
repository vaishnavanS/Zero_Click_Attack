package com.mock.banking;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

public class ZeroClickReceiver extends BroadcastReceiver {
    private static final String TAG = "ZeroClickSim";

    @Override
    public void onReceive(Context context, Intent intent) {
        if ("com.mock.bank.TRIGGER_TRANSFER".equals(intent.getAction())) {
            // This code runs automatically in the background when the intent is received.
            // NO user interaction (click/tap) is required.
            
            String amount = intent.getStringExtra("amount");
            String targetAccount = intent.getStringExtra("to_account");

            if (amount == null) amount = "$1,000";
            if (targetAccount == null) targetAccount = "ATTACKER-ACCOUNT-999";

            Log.d(TAG, "[SECURITY ALERT] Zero-Click Event Triggered!");
            Log.d(TAG, "[SECURITY ALERT] Transferring " + amount + " to " + targetAccount);
            
            // In a real app, this might trigger a network request or DB update.
            // In our simulation, the log entry is the proof of execution.
            
            processDummyTransaction(amount, targetAccount);
        }
    }

    private void processDummyTransaction(String amount, String account) {
        // Logic to update a local database or transaction list file
        Log.i(TAG, "Transaction processed successfully without user interaction.");
    }
}
