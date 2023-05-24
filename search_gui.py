from tkinter import *
import tkinter.font as font
from search_engine_executor import SearchEngineExecutor


class GUI:
    def __init__(self, window, search_engine_executor):
        self.__window = window
        self.__search_engine_executor = search_engine_executor
        self.__unified_background = "#333333"
        self.__unified_purple_color = "#8A2BE2"

        self.___compile_window_sections()

    def ___compile_window_sections(self):
        self.__window.title("GUI created with tkinter")
        self.__window.geometry("800x800")
        self.__window.configure(bg=self.__unified_background)

        self.__build_header_section()
        self.__build_search_section()

    def __build_header_section(self):
        bold25 = font.Font(size=25, weight=font.BOLD)
        var = StringVar()
        Label_header = Label(self.__window, textvariable=var, bg=self.__unified_background, font=bold25,
                             fg=self.__unified_purple_color)
        var.set("Doc Search Engine")
        Label_header.pack(pady=40)

    def __build_search_section(self):
        search_frame = Frame(self.__window, bg=self.__unified_background)

        search_input = Entry(search_frame, font=("arial", 20), highlightthickness=4, width=40, bg="#706f6f", fg="white")
        search_input.config(highlightbackground="grey", highlightcolor="grey")
        search_input.grid(row=0, column=0)

        buttonText = StringVar()
        search_button = Button(search_frame, textvariable=buttonText, font=font.Font(size=17, weight=font.BOLD),
                               bg=self.__unified_purple_color, fg="white")
        buttonText.set("Search")
        search_button.grid(row=0, column=1, padx=10)

        search_frame.pack(pady=40)

        search_index = search_input.get()
        print(search_index)

    def search(self, search_index):
        self.__search_engine_executor.document_search(search_index)

    def filter_search_result_title(self, search_results):
        return search_results.get("title")

    def filter_search_result_paragraph(self, search_results):
        return search_results.get("paragraph")


def main():
    window = Tk()
    search_engine_executor = SearchEngineExecutor()
    gui = GUI(window, search_engine_executor)
    window.mainloop()


if __name__ == "__main__":
    main()
