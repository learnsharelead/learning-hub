import requests
import time
import sys

# List of apps to keep awake
APPS = [
    "https://learnsharelead.streamlit.app/",
    "https://python-mastery.streamlit.app/",
    "https://learn-artificial-intelligence.streamlit.app/",
    "https://ai-hacks.streamlit.app/",
    "https://automation-testing-academy.streamlit.app/",
    "https://performance-testing.streamlit.app/",
    "https://coach-sushma.streamlit.app/",
    "https://finance-india.streamlit.app/",
    "https://ai-model-hunter.streamlit.app/",
    "https://website-ai-agent.streamlit.app/",
    "https://ppt-automation.streamlit.app/",
    "https://booksbrief.streamlit.app/"
]

def wake_app(url, max_retries=3):
    print(f"Pinging {url}...", end=" ", flush=True)
    
    for attempt in range(max_retries):
        try:
            # Use a real user-agent to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            }
            # Increased timeout to 60s because sleeping apps take time to boot
            response = requests.get(url, headers=headers, timeout=60)
            
            if response.status_code == 200:
                print(f"✅ Awake (200 OK)")
                return True
            else:
                print(f"⚠️ Status {response.status_code}", end="... ")
                
        except requests.exceptions.Timeout:
            print(f"⏳ Timeout (Attempt {attempt+1}/{max_retries})", end="... ")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Error (Attempt {attempt+1}/{max_retries})", end="... ")
        except Exception as e:
            print(f"❌ Error: {e}", end="... ")
            
        # Wait a bit before retrying
        time.sleep(5)
    
    print("❌ Failed after retries.")
    return False

def main():
    print("--- Starting Keep-Alive Routine ---")
    results = []
    
    for app in APPS:
        success = wake_app(app)
        results.append(success)
        # Small delay to be nice to the network
        time.sleep(2)
        
    print("--- Summary ---")
    success_count = sum(results)
    total = len(APPS)
    print(f"Successfully pinged {success_count}/{total} apps.")
    
    if success_count < total:
        print("Some apps might still be sleeping or have issues.")
        # We don't exit with error to avoid failing the whole workflow if just one app is flaky
        # but you could sys.exit(1) if strictness is required.
    
if __name__ == "__main__":
    main()
