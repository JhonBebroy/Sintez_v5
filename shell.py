from tkinter import *
import asyncio
import pyaudio as pa

import Samples

DURATION_TONE = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

OCT_NUMBER = 3
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPE = "sinus"
GENERATION_TYPES = ["sinus", "saw", 'guitar']
EFFECTS = {'distortion': 1}

NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Hb", "H", "C"]
WHITE_NOTES = 8

FONT = "Arial 16"

pressed_keys = set()


def keydown(event):
    global pressed_keys
    pressed_keys.add(event.keysym)


def keyup(event):
    global pressed_keys
    pressed_keys.discard(event.keysym)


def oct_change(side):
    global OCT_NUMBER
    OCT_NUMBER = (OCT_NUMBER + side) % len(OCTAVES)
    label_octnumber.config(text=f"{(OCTAVES[OCT_NUMBER])}")


def gen_change():
    global GENERATION_TYPE
    GENERATION_TYPE = GENERATION_TYPES[(GENERATION_TYPES.index(GENERATION_TYPE) + 1) % len(GENERATION_TYPES)]
    btn_gen_change.config(text=f"{GENERATION_TYPE}")


def dist_change():
    pass


def metronome_switch():
    pass


def play_note_by_btn(note):
    print(note)


window = Tk()
window.title("FL studio")
window.geometry("960x540")

label_octnumber = Label(window, text=f"{(OCTAVES[OCT_NUMBER])}", font=FONT, bg="black", fg="white")
label_octnumber.place(relx=0.26, rely=0, relwidth=0.48, relheight=0.09)
btn_oct_plus = Button(window, text="Oct+", font=FONT, bg="#00FFFF", fg="black",
                      activebackground="#00DDDD", activeforeground="black", command=lambda: oct_change(1))
btn_oct_plus.place(relx=0.875, rely=0.9, relwidth=0.125, relheight=0.1)
btn_oct_minus = Button(window, text="Oct-", font=FONT, bg="#00FFFF", fg="black",
                       activebackground="#00DDDD", activeforeground="black", command=lambda: oct_change(-1))
btn_oct_minus.place(relx=0, rely=0.9, relwidth=0.125, relheight=0.1)

btn_gen_change = Button(window, text=f"{GENERATION_TYPE}", font=FONT, bg="#00FFFF", fg="black",
                        activebackground="#00DDDD", activeforeground="black", command=gen_change)
btn_gen_change.place(relx=0.38, rely=0.1, relwidth=0.24, relheight=0.09)

label_dist = Label(window, text="Distortion:", font=FONT, bg="black", fg="white")
label_dist.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.09)
scale_dist = Scale(window, from_=10, to=100, orient="horizontal")
scale_dist.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.09)
btn_dist_change = Button(window, text="Set", font=FONT, bg="#00FFFF", fg="black", activebackground="#00DDDD",
                         activeforeground="black", command=dist_change)
btn_dist_change.place(relx=0.63, rely=0.1, relwidth=0.11, relheight=0.09)

label_metronome = Label(window, text="Metronome frequency:", font=FONT, bg="black", fg="white")
label_metronome.place(relx=0, rely=0, relwidth=0.25, relheight=0.09)
entry_metronome = Entry(window, justify="center", font=FONT)
entry_metronome.place(relx=0., rely=0.1, relwidth=0.25, relheight=0.09)
btn_metronome_switch = Button(window, text="Set", font=FONT, bg="#00FFFF", fg="black", activebackground="#00DDDD",
                              activeforeground="black", command=metronome_switch)
btn_metronome_switch.place(relx=0.26, rely=0.1, relwidth=0.11, relheight=0.09)

buttons = []
offset = 0
for note in NOTES:
    if len(note) == 1:
        buttons.append(Button(window, text=note, font=FONT, bg="white", fg="black", activebackground="#777777",
                              activeforeground="black", command=lambda arg=note: play_note_by_btn(arg)))
        buttons[-1].place(relx=0 + offset * (1 / WHITE_NOTES), rely=0.2, relwidth=1 / WHITE_NOTES, relheight=0.69)
        offset += 1
offset = 0
for note in NOTES:
    if len(note) == 2:
        buttons.append(Button(window, text=note, font=FONT, bg="black", fg="white", activebackground="#777777",
                              activeforeground="white", command=lambda arg=note: play_note_by_btn(arg)))

        if offset == 2:
            offset = 3
        if offset == 6:
            offset = 7
        if offset == 9:
            offset = 10

        buttons[-1].place(relx=(1 / WHITE_NOTES) * 0.68 + offset * (1 / WHITE_NOTES), rely=0.2,
                          relwidth=(1 / WHITE_NOTES) * 0.64, relheight=0.34)
        offset += 1

# Генерируем тона с заданной длительностью
generator = Samples.Generator(S_16BIT, SAMPLE_RATE, GENERATION_TYPES, GENERATION_TYPE, EFFECTS, OCT_NUMBER, False)
tones = generator.generate_tones(DURATION_TONE)
# Инициализируем
py_audio = pa.PyAudio()
# Создаём поток для вывода
stream = py_audio.open(format=py_audio.get_format_from_width(width=2),
                       channels=2, rate=SAMPLE_RATE, output=True, frames_per_buffer=100000)

window.bind("<KeyPress>", keydown)
window.bind("<KeyRelease>", keyup)

window.mainloop()
