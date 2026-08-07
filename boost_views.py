import urllib.request
import concurrent.futures
import time
import sys
import random

URL = "https://komarev.com/ghpvc/?username=CodeCenturian"
TOTAL_REQUESTS = 1500
CONCURRENCY = 25

def get_random_ip():
    return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
]

success_count = 0
fail_count = 0

def fetch_view(request_num):
    global success_count, fail_count
    try:
        ip = get_random_ip()
        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": ip,
            "X-Real-IP": ip,
            "Client-IP": ip,
            "CF-Connecting-IP": ip,
            "X-Client-IP": ip,
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }
        req = urllib.request.Request(f"{URL}&v={time.time_ns()}_{request_num}", headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                success_count += 1
            else:
                fail_count += 1
    except Exception:
        fail_count += 1

def main():
    print("Starting Advanced IP-Header Spoofing Views Booster for CodeCenturian...")
    print(f"Target: {TOTAL_REQUESTS} requests with randomized IP headers ({CONCURRENCY} parallel threads)\n")
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(fetch_view, i) for i in range(1, TOTAL_REQUESTS + 1)]
        
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            elapsed = time.time() - start_time
            rate = completed / elapsed if elapsed > 0 else 0
            
            # Print live progress bar
            progress = (completed / TOTAL_REQUESTS) * 100
            bar_length = 30
            filled = int(bar_length * completed // TOTAL_REQUESTS)
            bar = '=' * filled + '-' * (bar_length - filled)
            
            sys.stdout.write(f"\r[{bar}] {progress:5.1f}% | Done: {completed}/{TOTAL_REQUESTS} | Success: {success_count} | Speed: {rate:.1f} req/s")
            sys.stdout.flush()
            
    print(f"\n\nDone in {time.time() - start_time:.2f} seconds!")
    print(f"Total Hits Sent: {success_count} Successful | {fail_count} Failed")

if __name__ == "__main__":
    main()
