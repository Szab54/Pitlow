import time
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv, set_key
import pygame
from art import *

load_dotenv()

def text_to_speech(text):
    api_key = os.getenv('API_KEY')
    gtts_model = os.getenv('GTTS-MODEL')

    allowed_models = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    if gtts_model not in allowed_models:
        raise ValueError(f"Érvénytelen hang model: {gtts_model}. Az érvényes modelekből {allowed_models}.")

    model_hang = str(gtts_model)

    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        voice=model_hang,
        input=text,
    )
    response.stream_to_file("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def gpt_conf():
    gpt_prompt = os.getenv('GPT-PROMPT')
    print("-------{ GPT Konfigurálás }-------")
    print(f"Jelelegi prompt: {gpt_prompt}")
    print("[1] System prompt modósítása")
    print("[2] Eredeti prompt beállítása")
    print("[0] Kilépés")
    user_inpu = input("Válassz: ")
    if user_inpu == "1":
        print(f"Jelelegi prompt: {gpt_prompt}")
        modify = input("Módosítás? (y/n): ")
        if modify == "n":
            gpt_conf()
        elif modify == "y":
            print("Add meg az új prompt-ot!")
            prompt_modifyed = input("> ")
            if prompt_modifyed == "":
                print("[HIBA] Megszakítva!")
                gpt_conf()
            os.environ['GPT-PROMPT'] = prompt_modifyed
            set_key('.env', 'GPT-PROMPT', prompt_modifyed)
            print("[OK] Végrehajtva!")
            gpt_conf()
        else:
            print("[HIBA] Érvénytelen választás...")
            gpt_conf()
    elif user_inpu == "0":
        menu()
    elif user_inpu == "2":
        eredeti_prompt = "Te egy segitő bot vagy akit Swar-nak hívnak és alap feltételeket teljesítesz nem irsz py,js,stb.. kódokat. Használj emojikat"
        os.environ['GPT-PROMPT'] = eredeti_prompt
        set_key('.env', 'GPT-PROMPT', eredeti_prompt)
        print("[OK] Végrehajtva!")
        gpt_conf()
    else:
        print("[HIBA] Érvénytelen választás...")
        gpt_conf()
def gtts_hang():
    ggts = os.getenv('GTTS')
    if ggts == "disabled":
        print("[HIBA] A GTTS-es ki van kapcsolva! Kapcsold be a Rog-ban!")
        menu()
    else:
        print("-------{ GTTS Hang kiválasztása }-------")
        print("[1] Alloy - fiú")
        print("[2] Onyx - fiú")
        print("[3] Echo - fiú")
        print("[4] Fable - fiú")
        print("[5] Nova - lány")
        print("[6] Shimmer - fiú")
        print("[0] Kilépés")
        gtts_model_pick = input("Válassz: ")
        if gtts_model_pick == "1":
            gtts_ecccc = "alloy"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "2":
            gtts_ecccc = "onyx"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "3":
            gtts_ecccc = "echo"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "4":
            gtts_ecccc = "fable"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "5":
            gtts_ecccc = "nova"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "6":
            gtts_ecccc = "shimmer"
            os.environ['GTTS-MODEL'] = gtts_ecccc
            set_key('.env', 'GTTS-MODEL', gtts_ecccc)
        elif gtts_model_pick == "0":
            menu()
        else:
            print("[HIBA] Érvénytelen választás...")
            gtts_hang()
        gtts_hang()

def handle_gtts():
    gtts_t = os.getenv('GTTS')

    if gtts_t == "disabled":
        gtts_ecccc = "enabled"
        os.environ['GTTS'] = gtts_ecccc
        set_key('.env', 'GTTS', gtts_ecccc)

    elif gtts_t == "enabled":
        gtts_ecccc = "disabled"
        os.environ['GTTS'] = gtts_ecccc
        set_key('.env', 'GTTS', gtts_ecccc)
    menu()

def run():
    api_key = os.getenv('API_KEY')
    model = os.getenv('MODEL')
    gtts = os.getenv('GTTS')
    gpt_prompt = os.getenv('GPT-PROMPT')

    client = OpenAI(api_key=api_key)

    user = input("Te: ")
    if user == "exit":
        print("[OK] Kilépés...")
        menu()
    else:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",
                 "content": gpt_prompt},
                {"role": "user", "content": user},
            ],
        )
        bot_res = response.choices[0].message.content
        print(f"Bot: {bot_res}")
        if gtts == "enabled":
            text_to_speech(bot_res)
        else:
            run()
        run()


def model_picker():
    print("-------{ Model kiválasztása }-------")
    model = os.getenv('MODEL')
    print(f"Model: {model}")
    print("[1] GPT-4o")
    print("[2] GPT-4")
    print("[0] Kilépés")
    model_pick = input("Válassz: ")
    if model_pick == "1":
        model_cc = 'gpt-4o'
        os.environ['MODEL'] = model_cc
        set_key('.env', 'MODEL', model_cc)
        print("[API] Mentve")
        model_picker()
    elif model_pick == "2":
        model_cc = 'gpt-4'
        os.environ['MODEL'] = model_cc
        set_key('.env', 'MODEL', model_cc)
        print("[API] Mentve")
        model_picker()
    elif model_pick == "0":
        menu()
    else:
        print("[HIBA] Érvénytelen választás...")
        model_picker()

def menu():
    gtts = os.getenv('GTTS')
    if gtts == "disabled":
        gtts_men = "ki"
    elif gtts == "enabled":
        gtts_men = "be"
    model = os.getenv('MODEL')

    model_gtts = os.getenv("GTTS-MODEL")

    print("")
    print("-------{ OpenAI Rog }-------")
    print(f"[1] Model kiválasztása ({model})")
    print(f"[2] GTTS kezelése ({gtts_men})")
    if gtts_men == "ki":
        print("[3] GTTS Hang kiválasztása (KIKAPCSOLVA)")
    else:
        print(f"[3] GTTS Hang kiválasztása ({model_gtts})")
    print("[4] GPT Konfigurálás")
    print("[0] Kilépés")
    print("[RUN] Chat inditása")
    user_input = input("Válassz: ")
    if user_input == "0":
        print("Kilépés... [5 másodperc]")
        time.sleep(5)
        exit("Ha ezt látod, akkor ügyes vagy, good job! :))")
    elif user_input == "1":
        model_picker()
    elif user_input == "RUN":
        run()
    elif user_input == "2":
        handle_gtts()
    elif user_input == "3":
        gtts_hang()
    elif user_input == "4":
        gpt_conf()
    else:
        print("[HIBA] Érvénytelen választás...")
        menu()

def mask_string_middle(input_string):
    length = len(input_string)
    if length <= 2:
        # Ha a szöveg túl rövid, csak visszaadjuk
        return input_string

    # Kiszámoljuk a középső részt
    start = length // 4
    end = length - start

    masked_part = input_string[:start] + 'x' * (end - start) + input_string[end:]
    return masked_part

def check_internet_connection(url='https://www.google.com/'):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

if check_internet_connection():
    ascii_art = text2art("Pitlow")
    print(ascii_art)
    print("")
    print("[+] Van internetkapcsolat...")
    print("[+] OpenAI")
    print("")
    api_key = os.getenv('API_KEY')
    if not api_key or api_key.lower() == "none":
        print("[INFO] Itt: https://platform.openai.com/api-keys (Bejelentkezés szükséges)")
        openai_key = input("OpenAI API Key: ")
        if openai_key.startswith("sk-"):
            os.environ['API_KEY'] = openai_key
            set_key('.env', 'API_KEY', openai_key)
            api_key = os.getenv('API_KEY')

            print("[OK] API Kulcs Mentve")
            print("")
            #client = OpenAI(api_key=api_key)
            menu()
        elif openai_key == "":
            print("[HIBA] Ez egy nem érvényes kulcs!")
            print("Próbáld újra!")
            print("Kilépés... [5 másodperc]")
            time.sleep(5)
            exit()
        else:
            print("[HIBA] Ez egy nem érvényes kulcs!")
            print("Próbáld újra!")
            print("Kilépés... [5 másodperc]")
            time.sleep(5)
            exit()

    else:
        print("[OK] API kulcs érzékelve!")
        api_key = os.getenv('API_KEY')
        masked_output = mask_string_middle(api_key)
        print(f"[API] Kulcs: {masked_output}")
        menu()
else:
    print("[-] Nincs internetkapcsolat...")
    print("Csatlakozz egy internet kapcsolathoz!")
    print("Kilépés... [5 másodperc]")
    time.sleep(5)
    exit("Ha ezt látod, akkor ügyes vagy, good job! :))")