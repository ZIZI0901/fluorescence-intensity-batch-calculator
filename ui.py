
import tkinter as tk
from tkinter import filedialog
from calculator import process_images, save_data
import os

def select_folder(entry_address):
    folder_selected = filedialog.askdirectory()
    entry_address.delete(0, tk.END)
    entry_address.insert(0, folder_selected)

def process_images_and_save(entry_address, entry_threshold):
    try:
        file_address = entry_address.get()
        
        threshold_str = entry_threshold.get().strip()
        if not file_address:
            raise ValueError("请输入文件地址")
        if not threshold_str:
            raise ValueError("请输入阈值")

        threshold = int(entry_threshold.get())
        output_path = f"{os.path.dirname(file_address)}/{os.path.basename(file_address)}.xlsx"
        
        df = process_images(file_address, threshold)
        save_data(df, output_path)
        
        label_result.config(text=f"数据已成功导出到 {output_path} 文件中！")
        
    except Exception as e:
        label_result.config(text=f"发生错误：{str(e)}")

app = tk.Tk()
app.title("批量荧光分析")

label_address = tk.Label(app, text="文件地址：", anchor='e')
label_address.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_address = tk.Entry(app, width=40)
entry_address.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky='we')
button_address = tk.Button(app, text="选择文件夹", command=lambda: select_folder(entry_address))
button_address.grid(row=0, column=4, padx=10, pady=10)

label_threshold = tk.Label(app, text="阈值：", anchor='e')
label_threshold.grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_threshold = tk.Entry(app, width=10)
entry_threshold.grid(row=1, column=1, padx=10, pady=10, sticky='we')
entry_threshold.insert(0, "0")
entry_threshold.config({'fg': 'grey'})

button_process = tk.Button(app, text="处理图像", command=lambda: process_images_and_save(entry_address, entry_threshold))
button_process.grid(row=1, column=2, padx=10, pady=10)

label_result = tk.Label(app, text="", anchor='w')
label_result.grid(row=2, column=0, columnspan=10, padx=10, pady=10, sticky='we')

app.mainloop()
