# langkah 1: masukan file yang akan dibandingkan. ada pattern, file yang akan diamati dan ada file text, file yang akan dibandingkan
# langkah 2: pecah/split semua kalimat di file pattern dengan tanda titik sebagai pemisah
# langkah 3: simpan semua kalimat yang dipecah dalam suatu array
# langkah 4: untuk semua kalimat yang ada di array, periksa apakah dapat ditemukan dalam file text menggunakan algoritma KMP
# langkah 5: hitung presentase kalimat yang plagiat dengan rumus = % plagiat = (# kalimat plagiat / # kalimat dalam pattern) * 100
    

from kmp_algorithm import *

import tkinter as tk
import customtkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox
import tkinter.scrolledtext as st
import docx2txt

source_dir = ""
compare_dir = ""
plagiarized_sentences = []

MAIN_WINDOW_SIZE = "1920x1080"

    
def check_plagiarism():
    # split the sentences into array with the full stop as the delimiter
    sentences_in_source = docx2txt.process(source_dir).split('.')
    compare_text = docx2txt.process(compare_dir)

    # remove the last empty sentence in the array pyth
    try:
        sentences_in_source.pop()
    except Exception:
        messagebox.showerror("Error", "One document is empty")
    
    for sentence in sentences_in_source:
        print(sentence)
        if KMP_search(compare_text, sentence) != -1:
        # if sentence in compare_text:
            plagiarized_sentences.append(sentence)


def get_source_dir():
    # want to modify the global variable, use the 'global' keyword
    global source_dir 
    source_dir = askopenfilename(filetypes=[('Microsoft Word', '*.docx')])
    print(source_dir)

def get_compare_dir():
    global compare_dir 
    compare_dir = askopenfilename(filetypes=[('Microsoft Word', '*.docx')])
    print(compare_dir)

def check_result(root):
    global source_dir, compare_dir
    if len(source_dir) and len(compare_dir):
        check_plagiarism()
        open_result_window(root)
    else:
        messagebox.showerror("Error", "You need to select the source file and the file you want to compare!")

def return_to_main_window(window):
    window.destroy()
    main_window()


def open_result_window(root):
    
    root.destroy()
    result_window = Tk()
    result_window.title('Simple Plagiarism Detector')
    # result_window.configure(background='black')
    # result_window.geometry(width= 1800, height= 1800)
    result_window.geometry('1920x1080')

    return_button =  Button(result_window, text='Return to Main Menu', command=lambda:return_to_main_window(root))
    # return_button.pack(side=TOP, ipadx=10, ipady=20 ,pady=(200, 50))
    return_button.pack(side=BOTTOM)

    source_file_path = Label(result_window, text=f"Source file: {source_dir.split('/')[-1]}", justify=CENTER)
    source_file_path.pack(side=TOP)

    compare_file_path = Label(result_window, text=f"File to compare: {compare_dir.split('/')[-1]}", justify=CENTER)
    compare_file_path.pack(side=TOP)

    plagiarized_amount_label = Label(result_window, text=f"Total sentences plagiarized: {len(plagiarized_sentences)}", justify=CENTER)
    plagiarized_amount_label.pack(side=TOP)

    plagiarized_text_label = Label(result_window, text=f"These are the plagiarized sentences found in both file", justify=CENTER)
    plagiarized_text_label.pack(side=TOP)

    
    plagiarized_text = st.ScrolledText(result_window, width = 800, height = 1000, font = ("Arial", 12), fg="black")
                            
    
    
    for s in plagiarized_sentences:
        plagiarized_text.insert(INSERT, s + '\n\n')

    plagiarized_text.pack(side=TOP, pady=10)
    plagiarized_text.configure(state='disabled')
    


    result_window.mainloop()

def main_window():
    # root window
    root = Tk()
    root.title("Simple Plagiarism Detector")
    # customtkinter.set_appearance_mode("dark")
    # customtkinter.set_default_color_theme("dark-blue")
    root.configure(bg='black')
    root.geometry(MAIN_WINDOW_SIZE)

    description = Label(root, text="Detecting plagiarism in two files\n\nUsing Knuth-Morris-Pratt algorithm (KMP).\n\nDeveloped by Fairo, Ihsan, Komang, and Rafi.", font=("Times New Roman", 20), justify=CENTER)
    description.place(x=675, y=100, anchor="center")

    # buttons and getting the file's directory
    select_file_source_btn = Button(root, text='Select Source File', command=lambda:get_source_dir())
    select_file_source_btn.pack(side=TOP, ipadx=50, ipady=20 ,pady=(300, 20))

    select_file_compare_btn = Button(root, text='Select File To Compare', command=lambda:get_compare_dir())
    select_file_compare_btn.pack(side=TOP, ipadx=35, ipady=20, pady=20)

    check_result_btn = Button(root, text='Check Result', command=lambda:check_result(root))
    check_result_btn.pack(side=TOP, ipadx=60, ipady=20, pady=20)

    about_us_btn = Button(root, text='About us')
    about_us_btn.pack(side=TOP, ipadx=60, ipady=20, pady=20)

    root.config(bg="#ffffff")

    root.mainloop()

def create_jump_table(pattern):
    # Inisialisasi semua elemen dalam tabel menjadi 0 
    table = [0] * len(pattern)
    j = 0

    # Lakukan iterasi dari 1 - len(pattern)
    i = 1
    while i < len(pattern):
        # Jika karakter ke-i dan ke-j sama, increment tabel lombat
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = table[j - 1]
            else:
                table[i] = 0
                i += 1
    return table

# Melakukan pencarian string dengan algoritma KMP
# Return True jika pattern ditemukan dalam teks, return false jika tidak

main_window()