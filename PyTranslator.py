from googletrans import Translator
import customtkinter as ctk
from tkinter import *

testo_tradotto=None

def _traduzione(testo, lingua_traduzione):
    global testo_tradotto
    translator=Translator()
    lingua=translator.detect(testo)
    lingue_disponibili = {
        'af': 'afrikaans',
        'sq': 'albanese',
        'am': 'amarico',
        'ar': 'arabo',
        'hy': 'armeno',
        'az': 'azerbaigiano',
        'eu': 'basco',
        'be': 'bielorusso',
        'bn': 'bengalese',
        'bs': 'bosniaco',
        'bg': 'bulgaro',
        'ca': 'catalano',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'cinese (semplificato)',
        'zh-tw': 'cinese (tradizionale)',
        'co': 'corso',
        'hr': 'croato',
        'cs': 'ceco',
        'da': 'danese',
        'nl': 'olandese',
        'en': 'inglese',
        'eo': 'esperanto',
        'et': 'estone',
        'tl': 'filippino',
        'fi': 'finlandese',
        'fr': 'francese',
        'fy': 'frisone',
        'gl': 'galiziano',
        'ka': 'georgiano',
        'de': 'tedesco',
        'el': 'greco',
        'gu': 'gujarati',
        'ht': 'creolo haitiano',
        'ha': 'hausa',
        'haw': 'hawaiano',
        'iw': 'ebraico',
        'he': 'ebraico',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'ungherese',
        'is': 'islandese',
        'ig': 'igbo',
        'id': 'indonesiano',
        'ga': 'irlandese',
        'it': 'italiano',
        'ja': 'giapponese',
        'jw': 'giavanese',
        'kn': 'kannada',
        'kk': 'kazako',
        'km': 'khmer',
        'ko': 'coreano',
        'ku': 'curdo (kurmanji)',
        'ky': 'kirghiso',
        'lo': 'lao',
        'la': 'latino',
        'lv': 'lettone',
        'lt': 'lituano',
        'lb': 'lussemburghese',
        'mk': 'macedone',
        'mg': 'malgascio',
        'ms': 'malese',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolo',
        'my': 'birmano',
        'ne': 'nepalese',
        'no': 'norvegese',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persiano',
        'pl': 'polacco',
        'pt': 'portoghese',
        'pa': 'punjabi',
        'ro': 'rumeno',
        'ru': 'russo',
        'sm': 'samoano',
        'gd': 'gaelico scozzese',
        'sr': 'serbo',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'singalese',
        'sk': 'slovacco',
        'sl': 'sloveno',
        'so': 'somalo',
        'es': 'spagnolo',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'svedese',
        'tg': 'tagiko',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turco',
        'uk': 'ucraino',
        'ur': 'urdu',
        'ug': 'uiguro',
        'uz': 'uzbeko',
        'vi': 'vietnamita',
        'cy': 'gallese',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    }
    
    lingua_traduzione=lingua_traduzione.lower()

    if lingua_traduzione in lingue_disponibili.values():
        codice_lingua=next((codice for codice, lingua_nome in lingue_disponibili.items() if lingua_nome == lingua_traduzione), None)
        traduzione=translator.translate(testo, src=lingua.lang, dest=codice_lingua)
        testo_tradotto.config(state=NORMAL)
        testo_tradotto.delete(1.0, END)
        testo_tradotto.insert(INSERT, f'Traduzione in {lingue_disponibili[codice_lingua]}: "{traduzione.text}"')
        testo_tradotto.config(state=DISABLED)
    else:
        pass

def gui():
    global testo_tradotto

    gui=ctk.CTk()
    gui.title("PyTranslator")
    gui.resizable(False,False)
    gui.geometry("320x502")

    righe=20
    colonne=9

    for riga in range(righe):
        gui.rowconfigure(riga,weight=1)

    for colonna in range(colonne):
        gui.columnconfigure(colonna,weight=1)

    ctk.CTkLabel(gui, text="TRADUTTORE", font=("Helvetica", 24)).grid(row=1, column=4)

    entry=ctk.CTkEntry(gui, placeholder_text="Inserire qui il testo nella tua lingua")
    entry.grid(row=3, column=2, columnspan=5, sticky="nsew")

    entry2=ctk.CTkEntry(gui, placeholder_text="Inserire la lingua in cui si vuole tradurre")
    entry2.grid(row=5, column=2, columnspan=5, sticky="nsew")

    ctk.CTkButton(gui, text="Traduci", command=lambda: _traduzione(entry.get(), entry2.get())).grid(row=7, column=4)

    testo_tradotto=Text(gui, height=10,font=("Helvetica", 12),wrap=WORD,bd=0, bg="#242525",highlightthickness=0, fg="white")
    testo_tradotto.grid(row=10, column=2, columnspan=5, sticky="nsew")
    testo_tradotto.config(state=DISABLED)

    gui.mainloop()

if __name__ == "__main__":
    gui()
