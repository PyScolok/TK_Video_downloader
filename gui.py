import tkinter as tk
import re

from video_downloader import VideoDownloader
from settings import FONT


class Gui:
    def __init__(self, window):
        self.downloader = None
        self.window = window

        # configuring frames
        self.start_frame = tk.Frame(self.window)
        self.left_work_frame = tk.Frame(self.window, width=500)
        self.right_work_frame = tk.Frame(self.window, width=220)

        # configuring start_frame content
        self.url_input_field = tk.Entry(self.start_frame, font=FONT)
        self.accept_button = tk.Button(self.start_frame, text='Accept', width=15, height=2, font=FONT, command=self.accept_button_handler)

        # configuring left_work_frame content
        self.preview_img = tk.PhotoImage(format='png', width=480, height=360)
        self.image_label = tk.Label(self.left_work_frame, image=self.preview_img)
        self.image_label.image_ref = self.preview_img
        self.video_title_label = tk.Label(self.left_work_frame, font=FONT, wraplength=350, text='')

        # configuring right_work_frame content
        self.resolutions_box = tk.Spinbox(self.right_work_frame, values=())
        self.right_text_label = tk.Label(self.right_work_frame, text='Available resolutions: ')
        self.download_button = tk.Button(self.right_work_frame, text='Download', width=15, height=1, font=FONT, command=self.download_video)

    def change_frame(self):
        self.downloader_init()
        self.place_work_frame()
    
    def downloader_init(self):
        url = self.url_input_field.get()
        self.downloader = VideoDownloader(url)
        self.downloader.get_preview_image()
    
    def download_video(self):
        resolution = self.resolutions_box.get()
        self.downloader.download(resolution)

    def place_start_frame(self):
        self.left_work_frame.pack_forget()
        self.right_work_frame.pack_forget()
        self.start_frame.pack(fill="both", side="top", expand=True)
        self.place_start_content()

    def place_start_content(self):
        self.url_input_field.place(anchor=tk.CENTER, relx=0.5, rely=0.5, width=540, height=30)
        self.accept_button.place(anchor=tk.CENTER, relx=0.5, rely=0.7)
        self.url_input_field.insert(tk.END, 'Enter video URL here...')

    def place_left_work_content(self):
        self.image_label.pack(side='top', anchor='nw')
        self.video_title_label.pack(side='top', anchor='center', expand=False, fill='y')
        self.video_title_label.configure(text = self.downloader.get_title())

    def place_right_work_content(self):
        self.right_text_label.place(x=0, y=10)
        self.resolutions_box.place(x=0, y=40)
        self.download_button.place(x=0, y=380, width=190)

    def place_work_frame(self):
        self.start_frame.pack_forget()
        self.left_work_frame.pack(fill='y', padx=10, pady=10, side='left')
        self.place_left_work_content()
        self.right_work_frame.pack(fill='both', expand=True, padx=10, pady=10, side='left')
        self.place_right_work_content()
        self.preview_img.configure(file='./img/preview.png')
        self.fill_res_box()

    def fill_res_box(self):
        res_list = tuple(res for res in self.downloader.get_all_res())
        self.resolutions_box.configure(values=res_list, state='readonly')
        
    def accept_button_handler(self):
        pattern = r'^http(s)?:\/\/(?:www\.)?youtube.com\/watch\?(?=.*v=\w{11})(?:\S+)?$'
        if re.fullmatch(pattern, self.url_input_field.get()):
            self.change_frame()
        else:
            self.url_input_field.delete(0, 'end')
            self.url_input_field.insert(tk.END, 'Entered URL is not valid!!!')


