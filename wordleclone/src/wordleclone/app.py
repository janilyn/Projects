"""
My first application
"""
from ctypes import alignment
from tkinter import CENTER
from click import style
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW 
import random
import time

class Alphabet:
    def __init__(self):
        self.box= toga.Box(style=Pack(direction = ROW, alignment = CENTER, padding = (15,0)))
        self.alphalist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for i in self.alphalist:
            self.box.add(toga.Label(i, style=Pack(padding=(0,3),text_align = CENTER, background_color = "transparent", font_size = 10)))
    
    def find_index(self,letter):
        index = self.alphalist.index(letter.capitalize())
        return index

class LetterGrid:
    def __init__(self):
        self.box = toga.Box(style=Pack(direction = COLUMN, flex = 1, alignment = CENTER))
        
        for i in range(6):
            self.box.add(self.build_row())

    def build_row(self):
            box = toga.Box()
            box.style.direction = ROW
            for i in range(5):
                button = toga.Button('',  style=Pack(width = 50, height = 50, padding = (5,5), alignment = CENTER))
                button.style.color = 'white'
                button.style.font_size = 14
                button.style.font_weight = 'bold'
                box.add(button)

            return box
    
    def clear(self):
        for i in range(6):
            for j in range(5):
                self.box.children[i].children[j].style.background_color = 'transparent'
                self.box.children[i].children[j].label = ''

    def change_value(self, i, input,answer):
        ans = []
        check = [0,0,0,0,0]
        for j in range(5):
            ans.append(answer[j])

        for j in range(5):
            if input[j] == answer[j]:
                self.box.children[i].children[j].style.background_color = 'green'
                self.box.children[i].children[j].label = input[j].capitalize()
                check[j] = 1
                ans.pop(ans.index(input[j]))

        for j in range(5):
            if check[j] == 0 and input[j] in ans:
                self.box.children[i].children[j].style.background_color = 'goldenrod'
                ans.pop(ans.index(input[j]))
            elif check[j] == 0:
                self.box.children[i].children[j].style.background_color = 'gray'
            self.box.children[i].children[j].label = input[j].capitalize()

class WordPool:
    def wordle_answer(self, path):
        guess_list = open(str(path) + "\\words.txt", "r")
        lines = guess_list.read().splitlines()
        guess_list.close()

        random.seed(time.time())
        i = random.randint(0,len(lines)-1)
        self.answer = lines[i]

    def valid_guesses(self, path, Alphabet):
        guess_list = open(str(path) + "\\allowed_guesses.txt", "r")
        self.guess_words = guess_list.read().splitlines()
        guess_list.close()
        self.nguess = len(self.guess_words)
        self.guess_words_indices = []
        index = 0
        for i in Alphabet:
            for j in range(index ,len(self.guess_words)):
                if i.lower() == self.guess_words[j][0]:
                    self.guess_words_indices.append(j)
                    index = j
                    break 
    
    def isvalid(self, Alphabet, input):
        start = Alphabet.find_index(input[0])
        start_ind = self.guess_words_indices[start]
        if start_ind <25:
            end_ind = self.guess_words_indices[start+1]
        else:
            end_ind = self.nguess

        valid = 0
        for i in range(start_ind,end_ind):
            if input == self.guess_words[i]:
                valid = 1
                break

        return valid

class WordleClone(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN, padding = (0,15), alignment = CENTER))

        self.tries = 0
        
        # Input Box + Label
        top_box = toga.Box(style=Pack(direction=ROW, flex = 1))
        guess_label = toga.Label('Guess: ', style=Pack(padding=(13, 0, 0), font_size = 10))
        self.input = toga.TextInput(style=Pack(flex=1,padding=(10,0,0), font_size = 10))

        # Guess Button
        guess_button = toga.Button('Guess', on_press=self.guess_button_press, style=Pack(padding=(7,0), flex = 1, font_size = 10))

        # Middle Part (Alphabet + Grid)
        middle_box = toga.Box(style=Pack(direction = COLUMN, flex = 1, alignment = CENTER))
        self.alphabet = Alphabet()
        self.letters = LetterGrid()

        # Restart Button
        restart_button = toga.Button('Restart', on_press=self.restart_button_press, style=Pack(padding=(7,0), flex = 1, font_size = 10))

        self.wordsclass = WordPool()
        self.validity = self.wordsclass.valid_guesses(self.pathsapp, self.alphabet.alphalist)
        self.wordsclass.wordle_answer(self.paths.app)

        top_box.add(guess_label, self.input)
        middle_box.add(self.alphabet.box)
        middle_box.add(self.letters.box)
        main_box.add(top_box)
        main_box.add(guess_button)
        main_box.add(middle_box)
        main_box.add(restart_button)

        self.main_window = toga.MainWindow(title=self.formal_name,size=(640,550))
        self.main_window.content = main_box
        self.main_window.show()

    def guess_button_press(self,widget):
        if len(self.input.value) != 5:
            window = toga.Window()
            window.error_dialog(title="Invalid input", message="Please enter a 5 digit word!")
        elif self.input.value.isalpha() == False:
            window = toga.Window()
            window.error_dialog(title="Invalid input", message="Please only enter alphabetical characters!")
        elif self.wordsclass.isvalid(self.alphabet, self.input.value) == 0:
            window = toga.Window()
            window.error_dialog(title="Invalid input", message="Please enter a valid word!")
        else:
            self.letters.change_value(self.tries, self.input.value, self.wordsclass.answer)
            self.tries += 1

            if self.input.value.lower() == self.wordsclass.answer:
                window = toga.Window()
                window.info_dialog(title="Wordle", message="You win! Game over.")

            elif self.tries == 6:
                window = toga.Window()
                window.info_dialog(title="Wordle", message="You lose! The correct answer is " + self.wordsclass.answer +". Game over.")

            self.input.value = ''
            yield 0.01

    
    def restart_button_press(self,widget):
        self.tries = 0
        self.letters.clear()
        self.wordsclass.wordle_answer(self.paths.app)

        yield 0.01

def main():
    return WordleClone()
