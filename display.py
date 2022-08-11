from data_filter import Data_filter
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)


class View(tk.Tk):

    def __init__(self, dataset):
        super().__init__()

        self.frame = tk.Frame()
        self.resizable(True, True)

        self.list_gender = []
        self.list_level = []
        self.list_exp = []
        self.list_group = []
        self.list_sub = []
        self.point_sub = 0
        self.state_sub = True
        self.filters_file = Data_filter(dataset, list_gender=self.list_gender, list_sec=self.list_level,
                                        list_level=self.list_exp, list_exp=self.list_group, min_sub=self.point_sub,
                                        status_sub=self.state_sub)
        self.your_selected = ''
        self.dic_level = {}
        self.text_find = tk.StringVar()
        self.gender_male = tk.IntVar()
        self.gender_female = tk.IntVar()

        self.title('yo')
        self.create_widgets()

    def create_widgets(self):
        # Filter gender frame
        frame_gender = ttk.Frame(self.frame)
        frame_level = ttk.Frame(self.frame)
        frame_exp = ttk.Frame(self.frame)
        frame_group = ttk.Frame(self.frame)
        self.frame_view_board = ttk.Frame(self.frame, padding=(3, 3, 12, 12))
        self.frame_search = ttk.Frame(self.frame)
        self.frame_g = ttk.Frame(self.frame)
        self.frame_sub = ttk.Frame(self.frame)

        # label Frame
        label_frame_gender = tk.LabelFrame(frame_gender, text="Gender", padx=10, pady=10, font=('Arial 8 bold'))
        label_frame_level = tk.LabelFrame(frame_level, text=" Parental level of education ", padx=10, pady=10,
                                          font=('Arial 8 bold'))
        self.label_frame_exp = tk.LabelFrame(frame_exp, text="Experienced in writing code", padx=10, pady=10,
                                             font=('Arial 8 bold'))
        self.label_frame_group = tk.LabelFrame(frame_group, text="Group sec", padx=10, pady=10, font=('Arial 8 bold'))
        self.label_frame_g1 = tk.LabelFrame(self.frame_g, padx=10, pady=10)
        self.label_frame_g2 = tk.LabelFrame(self.frame_g, padx=10, pady=10)
        self.label_frame_sub = tk.LabelFrame(self.frame_sub, text="Subject", padx=10, pady=10, font=('Arial 8 bold'))
        self.label_frame_search = tk.LabelFrame(self.frame_search, text="Search Name", padx=10, pady=10,
                                                font=('Arial 8 bold'))
        # widget
        gender_male = ttk.Checkbutton(label_frame_gender, text='male', variable=self.gender_male, onvalue=1,
                                      offvalue=0, command=self.com_gender)
        gender_female = ttk.Checkbutton(label_frame_gender, text='female', variable=self.gender_female, onvalue=1,
                                        offvalue=0, command=self.com_gender)

        gender_male.grid(row=0, column=0, sticky=tk.W)
        gender_female.grid(row=1, column=0, sticky=tk.W)

        self.exp_widget(self.filters_file)
        self.group_widget(self.filters_file)
        self.sub_wid()
        self.tree_wid = self.tree_view(self.filters_file.dataset)
        self.search_wid()
        self.g1_wid()
        self.g2_wid()
        self.columns_level = [
            " bachelor's degree ",
            " some college ",
            " master's degree ",
            " associate's degree ",
            " high school ",
            " some high school "
        ]

        for index, level in enumerate(sorted(self.columns_level)):
            self.dic_level[level] = ttk.Checkbutton(label_frame_level, text=level, onvalue=level,
                                                    offvalue=level + "_off", command=self.com_level)
            self.dic_level[level].var = tk.StringVar()
            self.dic_level[level]["variable"] = self.dic_level[level].var
            self.dic_level[level].grid(row=index, column=0, sticky=tk.W)

        # set pos widget labelFrame
        label_frame_gender.pack(expand=True, fill=tk.BOTH)
        label_frame_level.pack(expand=True, fill=tk.BOTH)
        self.label_frame_exp.pack(expand=True, fill=tk.BOTH)
        self.label_frame_group.pack(expand=True, fill=tk.BOTH)
        self.label_frame_sub.pack(expand=True, fill=tk.BOTH)
        self.label_frame_g1.grid(row=0, column=0, padx=10, pady=8, sticky=tk.NSEW)
        self.label_frame_g2.grid(row=0, column=1, padx=10, pady=8, sticky=tk.NSEW)
        self.label_frame_search.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        # set pos of every Frame of widget
        self.frame_search.grid(row=0, column=0, padx=10, pady=8, sticky=tk.NSEW)
        frame_gender.grid(row=1, column=0, padx=10, pady=8, sticky=tk.NSEW, rowspan=1)
        frame_level.grid(row=2, column=0, padx=10, pady=8, sticky=tk.NSEW)
        self.frame_view_board.grid(row=0, column=1, padx=10, pady=8, sticky=tk.NSEW, rowspan=9)
        frame_group.grid(row=3, column=0, padx=10, pady=8, sticky=tk.NSEW)
        frame_exp.grid(row=4, column=0, padx=10, pady=8, sticky=tk.NSEW)
        self.frame_sub.grid(row=5, column=0, padx=10, pady=8, sticky=tk.NSEW)
        self.frame_g.grid(row=3, column=1, padx=10, pady=8, sticky=tk.NSEW, rowspan=3)
        ttk.Button(self.frame, text="Apply", command=self.com_last_filter).grid(row=6, column=0, padx=10, pady=10,
                                                                                sticky=tk.NSEW)

        # add all widget in screen
        row_i, col_i = self.frame.grid_size()
        for row in range(row_i):
            self.frame.rowconfigure(row, weight=1)
        for col in range(col_i):
            self.frame.columnconfigure(col, weight=1)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def com_last_filter(self):
        self.text_find.set('')
        self.filters_file.list_gender = self.list_gender
        self.filters_file.list_level = self.list_level
        self.filters_file.list_exp = self.list_exp
        self.filters_file.list_sec = self.list_group
        self.filters_file.status_sub = self.state_sub
        self.filters_file.min_sub = self.point_sub
        self.filters_file.list_sub = self.list_sub

        self.filters_file.edit_data()

        for item in self.tree_wid.get_children():  # used self.tree instead
            self.tree_wid.delete(item)
        self.insert_data_tree(self.filters_file.dataset, self.tree_wid)
        self.filters_file.dataset = self.filters_file.dataset_origin

    def search_wid(self):
        self.wid_entry_search = tk.Entry(self.label_frame_search, textvariable=self.text_find)
        self.text_find.trace("w", lambda a, b, c: self.com_search())
        self.wid_entry_search.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

    def g1_wid(self):
        combo_g1_wid = ttk.Combobox(self.label_frame_g1,
                                    values=list(self.filters_file.dataset_origin.iloc[:, 6:].columns))
        combo_g1_wid.set("discrete math score")
        combo_g1_wid['state'] = 'readonly'

        figure1 = plt.Figure(figsize=(6, 5), dpi=82)
        ax = figure1.add_subplot(111)
        ax.set_xlabel("Score")
        ax.set_ylabel("Frequency")
        ax.set_title(f"Histogram of discrete math score")
        ax.hist(list(self.filters_file.dataset_origin["discrete math score"]),
                list(range(0, 101, 3)), edgecolor="black", alpha=0.5)
        canvas = FigureCanvasTkAgg(figure1, self.label_frame_g1)

        # NavigationToolbar2Tk(canvas, self.label_frame_g1)
        def histo_plot(event):
            figure1.clear()
            new = figure1.add_subplot(111)
            new.set_xlabel("Score")
            new.set_ylabel("Frequency")
            new.set_title(f"Histogram of {event.widget.get()}")
            new.hist(list(self.filters_file.dataset_origin[event.widget.get()]),
                     list(range(0, 101, 3)), edgecolor="black", alpha=0.5,)
            canvas.draw_idle()
            
        text = ttk.Label(self.label_frame_g1,
                         text="                                                   Please select the Subject you want "
                              "to show ",
                         font=("Arial", 8), foreground="gray")
        text.grid(row=1, column=0, sticky=tk.NSEW)
        combo_g1_wid.bind("<<ComboboxSelected>>", histo_plot)
        combo_g1_wid.grid(row=2, column=0, padx=10, pady=18, sticky=tk.NSEW, )
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW, )

    def g2_wid(self):
        # create figure
        figure1 = plt.Figure(figsize=(6, 5), dpi=83)

        # add graph in picture
        ax = figure1.subplots()
        ax.pie([1], labels=["Name Subjects"], shadow=True, autopct='%1.1f%%',
               startangle=90, labeldistance=1.375)

        figure1.legend()
        canvas = FigureCanvasTkAgg(figure1, self.label_frame_g2)

        def pie_plot():
            if self.your_selected != "":
                figure1.clear()
                list_label = list(self.filters_file.dataset_origin.iloc[:, 6:].columns)
                list_all_point_select = self.your_selected["values"][6:]
                new = figure1.subplots()
                new.pie(list_all_point_select, labels=list_label, shadow=True, autopct='%1.1f%%',
                        startangle=90, labeldistance=1.1)
                new.set_title(f"Student_id : {self.your_selected['values'][0]} \n"
                              f"Name : {self.your_selected['values'][1]}")
                canvas.draw_idle()

        # setpos
        text = ttk.Label(self.label_frame_g2,
                         text="                                                   Please select the students you want "
                              "to show ",
                         font=("Arial", 8), foreground="gray")

        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW, )
        ttk.Button(self.label_frame_g2, text="Plot", command=pie_plot).grid(row=2, column=0, sticky=tk.NSEW, padx=10,
                                                                            pady=10, )
        text.grid(row=1, column=0, sticky=tk.NSEW)

    def exp_widget(self, dataset):
        orig_data = dataset.dataset_origin
        type_col_name = list(set(orig_data['Experienced in writing code']))
        dict_exp = {}
        for index, name_type in enumerate(type_col_name):
            text_v = tk.StringVar()
            wid = ttk.Checkbutton(self.label_frame_exp, text=name_type, variable=text_v, onvalue=name_type,
                                  offvalue="",
                                  command=lambda: self.com_exp(dic_wid_index=dict_exp, list_col_name=type_col_name))
            wid.ver = text_v
            dict_exp[wid] = index
            wid.grid(row=index, column=0, sticky=tk.W)

    def group_widget(self, dataset):
        orig_data = dataset.dataset_origin
        lst = list(set(orig_data['group_sec']))
        type_col_name = sorted(lst)
        dict_grop = {}
        for index, name_type in enumerate(type_col_name):
            text_v = tk.StringVar()
            wid = ttk.Checkbutton(self.label_frame_group, text=name_type, variable=text_v, onvalue=name_type,
                                  offvalue="",
                                  command=lambda: self.com_group(dic_wid_index=dict_grop, list_col_name=type_col_name))
            # text_v.set(name_type) # widget on ระวัง
            wid.ver = text_v
            dict_grop[wid] = index
            wid.grid(row=index, column=0, sticky=tk.W)

    def sub_wid(self):
        type_col_name = list(self.filters_file.dataset_origin.iloc[:, 6:].columns)
        dict_sub = {}
        for index, name_type in enumerate(type_col_name):
            text_v = tk.StringVar()
            wid = ttk.Checkbutton(self.label_frame_sub, text=name_type, variable=text_v, onvalue=name_type,
                                  offvalue="",
                                  command=lambda: self.com_sub(dic_wid_index=dict_sub, list_col_name=type_col_name))
            wid.ver = text_v
            dict_sub[wid] = index
            wid.grid(row=index, column=0, sticky=tk.W)

        def set_point(event):
            self.point_sub = scl.get()
            # print(self.point_sub)

        scl = tk.Scale(self.label_frame_sub, from_=0, to=100, orient=tk.HORIZONTAL, command=set_point)
        scl.set(0)
        scl.grid(column=0, row=9, sticky=tk.NSEW)

        def get_status(event):
            if var1.get() == "Minimum score":
                self.state_sub = True
            elif var1.get() == "Maximum score":
                self.state_sub = False

        var1 = tk.StringVar()
        var1.set("Minimum score")
        options = ["Minimum score", "Maximum score"]

        label = ttk.Label(self.label_frame_sub, text="Status mode",font=('Arial 8 bold'))
        label.grid(column=0, row=7, sticky=tk.NSEW, padx=3, pady=3)

        cb = ttk.Combobox(self.label_frame_sub, textvariable=var1, values=options)
        cb.bind('<<ComboboxSelected>>', get_status)
        cb.grid(column=0, row=8, sticky=tk.NSEW, padx=3, pady=3)

    def tree_view(self, dataset):
        """
        show view board everytime when change DataFrame from filter
        :param dataset: DataFrame
        """
        # Tree_board
        main_columns_t = tuple(dataset.columns)
        view_board_tree = ttk.Treeview(self.frame_view_board, columns=main_columns_t, show='headings', height=15,
                                       selectmode="browse")

        def selectItem(a):
            curItem = view_board_tree.focus()
            self.your_selected = view_board_tree.item(curItem)

        view_board_tree.bind('<ButtonRelease-1>', selectItem)

        for main_col in range(len(main_columns_t)):
            view_board_tree.heading(main_columns_t[main_col], text=main_columns_t[main_col])
            view_board_tree.column(main_columns_t[main_col], anchor=tk.CENTER, stretch=True, width=100, minwidth=10)

        self.insert_data_tree(dataset, view_board_tree)

        return view_board_tree

    def insert_data_tree(self, dataset, view_board_tree):
        # insert list data in widgets tree
        for row in range(len(dataset)):
            val = tuple(dataset.iloc[row])
            view_board_tree.insert('', tk.END, values=val)

        scrollbar_y = ttk.Scrollbar(self.frame_view_board, orient=tk.VERTICAL, command=view_board_tree.yview)
        view_board_tree.configure(yscrollcommand=scrollbar_y.set)

        view_board_tree.grid(row=0, column=0, )
        scrollbar_y.grid(row=0, column=1, sticky='ns')

    def com_group(self, dic_wid_index, list_col_name):
        lst = []
        for wid, index in dic_wid_index.items():
            if wid.ver.get() in list_col_name:
                lst.append(wid.ver.get())
        self.list_group = lst

    def com_sub(self, dic_wid_index, list_col_name):
        lst = []
        for wid, index in dic_wid_index.items():
            if wid.ver.get() in list_col_name:
                lst.append(wid.ver.get())
        self.list_sub = lst

    def com_exp(self, dic_wid_index, list_col_name):
        lst = []
        for wid, index in dic_wid_index.items():
            if wid.ver.get() in list_col_name:
                lst.append(wid.ver.get())
        self.list_exp = lst

    def com_level(self):
        lst = []
        for name, wid_click in self.dic_level.items():
            if wid_click.var.get() in self.columns_level:  # {wid_checkbutton() : name}
                lst.append(name)
        self.list_level = lst

    def com_gender(self):
        if self.gender_male.get() == 1:
            self.list_gender.append("male")
        elif self.gender_male.get() == 0:
            if "male" in self.list_gender:
                self.list_gender.remove("male")

        if self.gender_female.get() == 1:
            self.list_gender.append("female")
        elif self.gender_female.get() == 0:
            if "female" in self.list_gender:
                self.list_gender.remove("female")

    def com_search(self):
        for item in self.tree_wid.get_children():  # used self.tree instead
            self.tree_wid.delete(item)

        new_data_frame = self.filters_file.dataset[
            self.filters_file.dataset['Name'].str.contains(self.wid_entry_search.get().capitalize(), na=False)]

        if len(self.wid_entry_search.get()) == 0:
            new_data_frame = self.filters_file.dataset
        self.insert_data_tree(new_data_frame, self.tree_wid)
