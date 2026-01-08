import time
import random
import sys

class MockAndroidSystem:
    def __init__(self):
        self.logs = []
        self.running = True
        print("\n[+] Initializing Mock Android Emulator...")
        time.sleep(1)
        print("[+] Device Booted (AVD: Pixel_6_API_33)")
        print("[+] Canara Bank App (com.mock.banking) is running in the background.")

    def log(self, level, tag, message):
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"{timestamp} {level}/{tag}: {message}"
        self.logs.append(log_entry)
        print(f"\033[90m{log_entry}\033[0m")

    def broadcast_intent(self, action, extras):
        self.log("D", "IntentService", f"Broadcasting Intent: {action}")
        time.sleep(0.5)
        # Simulate the receiver picking it up
        if action == "com.mock.bank.TRIGGER_TRANSFER":
            self.trigger_vulnerability(extras)

    def trigger_vulnerability(self, extras):
        self.log("W", "ZeroClickSim", "[CRITICAL] Zero-Click Event Received via Broadcast!")
        time.sleep(1)
        amount = extras.get("amount", "$1,000")
        to = extras.get("to_account", "ATTACKER-999")
        
        self.log("E", "ZeroClickSim", f"[SECURITY ALERT] Executing unauthorized transfer: {amount} -> {to}")
        time.sleep(0.5)
        self.log("I", "ZeroClickSim", "Transaction validated against system credentials (AUTOMATIC).")
        time.sleep(0.8)
        self.log("I", "ZeroClickSim", "SUCCESS: Funds moved. No user prompt displayed.")
        print("\n\033[91m[!] ALERT: Background attack successful. Data has been processed without user consent.\033[0m")

def run_simulation():
    emulator = MockAndroidSystem()
    
    print("\n" + "="*50)
    print("       ZERO-CLICK ATTACK SIMULATION ENGINE")
    print("="*50)
    print("\n[STEP 1] Monitoring for background events...")
    time.sleep(2)
    
    print("\n[STEP 2] Simulating Trigger (External Attack Payload)...")
    payload = {
        "amount": "$5,000",
        "to_account": "MaliciousNode_X"
    }
    
    # Simulate the Python script sending the intent via ADB
    time.sleep(2)
    emulator.broadcast_intent("com.mock.bank.TRIGGER_TRANSFER", payload)
    
    print("\n" + "="*50)
    print("             SIMULATION COMPLETE")
    print("="*50)
    print("\nResults: Check the logs above for 'ZeroClickSim' entries.")
    print("The app processed the 'TRIGGER_TRANSFER' intent automatically.")

if __name__ == "__main__":
    run_simulation()
