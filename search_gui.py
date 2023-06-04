from tkinter import *
import tkinter.font as font
from search_engine_executor import SearchEngineExecutor


class SearchGUI:
    def __init__(self, window, search_engine_executor):
        self.__window = window
        self.__search_engine_executor = search_engine_executor
        self.__unified_background = "#333333"
        self.__unified_purple_color = "#8A2BE2"
        self.__search_input = None
        self.__output_text = None
        self.__compile_window_sections()

    def __compile_window_sections(self):
        self.__window.title("Search Engine")
        self.__window.geometry("800x800")
        self.__window.configure(bg=self.__unified_background)

        self.__build_header_section()
        self.__build_search_section()
        self.__build_output_section()

    def __build_header_section(self):
        bold25 = font.Font(size=25, weight=font.BOLD)
        var = StringVar()
        Label_header = Label(self.__window, textvariable=var, bg=self.__unified_background, font=bold25,
                             fg=self.__unified_purple_color)
        var.set("Doc Search Engine")
        Label_header.pack(pady=40)

    def __build_search_section(self):
        search_frame = Frame(self.__window, bg=self.__unified_background)

        self.__search_input = Entry(
            search_frame,
            font=("arial", 20),
            highlightthickness=4,
            width=40, bg="#aba9a9",
            fg="white"
        )
        self.__search_input.config(highlightbackground="grey", highlightcolor="grey")
        self.__search_input.grid(row=0, column=0)

        buttonText = StringVar()
        search_button = Button(search_frame,
                               textvariable=buttonText,
                               font=font.Font(size=17, weight=font.BOLD),
                               bg=self.__unified_purple_color, fg="white",
                               command=self.__search
                               )

        buttonText.set("Search")
        search_button.grid(row=0, column=1, padx=10)

        search_frame.pack(pady=40)

    def __search(self):
        search_index = self.__search_input.get()
        search_results = self.__search_engine_executor.document_search(search_index)
        title = self.__filter_search_result_title(search_results)
        paragraph1 = self.__filter_search_result_paragraph1(search_results)
        paragraph2 = self.__filter_search_result_paragraph2(search_results)

        self.__output_text.delete(1.0, END)

        self.__output_text.tag_add("header", "1.0", "1.4")
        self.__output_text.tag_add("body", "1.8", "1.14")
        self.__output_text.tag_configure(
            "header",
            background="yellow",
            foreground=self.__unified_purple_color,
            font=font.Font(size=27, weight=font.BOLD)
        )
        self.__output_text.tag_configure("body", background="#cfcccc", foreground="black")

        self.__output_text.insert(INSERT, title, "header")
        self.__output_text.insert(END, "\n")
        self.__output_text.insert(END, paragraph1, "body")
        self.__output_text.insert(END, "\n")
        self.__output_text.insert(END, paragraph2, "body")

    def __build_output_section(self):
        self.__output_text = Text(
            self.__window,
            background="#aba9a9",
            foreground="white",
            font=font.Font(size=17, weight=font.BOLD),
            highlightthickness=4,
            width=90,
            height=40,
        )

        self.__output_text.insert(index=INSERT, chars="Hey There! Search something \u263A")
        self.__output_text.config(highlightbackground="grey", highlightcolor="grey")

        self.__output_text.pack()

    def __filter_search_result_title(self, search_results):
        return search_results.get("title")

    def __filter_search_result_paragraph1(self, search_results):
        return search_results.get("paragraph1")

    def __filter_search_result_paragraph2(self, search_results):
        return search_results.get("paragraph2")


def main():
    window = Tk()
    search_engine_executor = SearchEngineExecutor()
    SearchGUI(window, search_engine_executor)
    window.mainloop()


if __name__ == "__main__":
    main()
