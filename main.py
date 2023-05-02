from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Control App')
root.geometry("600x400")

fig, ax = plt.subplots()

# screen open function
def open_button_view():
    hide_all_frames()
    button_screen_frame.pack(fill="both", padx=50, pady=50 , expand=1)
    toggle_pump1_flag = true;
    toggle_pump2_flag = true;
    toggle_pump3_flag = true;
    toggle_pump4_flag = true;
    toggle_pump5_flag = true;
    toggle_pump6_flag = true;
    
    def toggle_pump1():
        toggle_pump1_flag = not toggle_pump1_flag
        
    def toggle_pump2():
        toggle_pump2_flag = not toggle_pump1_flag
        
    def toggle_pump3():
        toggle_pump3_flag = not toggle_pump1_flag
        
    def toggle_pump4():
        toggle_pump4_flag = not toggle_pump1_flag
        
    def toggle_pump5():
        toggle_pump5_flag = not toggle_pump1_flag
        
    def toggle_pump6():
        toggle_pump6_flag = not toggle_pump1_flag    
    
    # Control Pump 1
    if (toggle_pump1_flag):
        pump1_label = Label(graph_screen_frame, text="Pump 1: ")
        pump1_button_on = Button(graph_screen_frame, text="On", command=toggle_pump1)
        pump1_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump1)
        pump1_label.grid(row=0, column=0)
        pump1_button_on.grid(row=0, column=1)
        pump1_button_off.grid(row=0, column=2)
    else:
        pump1_label = Label(graph_screen_frame, text="Pump 1: ")
        pump1_button_on = Button(graph_screen_frame, text="On", command=toggle_pump1)
        pump1_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump1)
        pump1_label.grid(row=0, column=0)
        pump1_button_on.grid(row=0, column=1)
        pump1_button_off.grid(row=0, column=2)
    
    # Control Pump 1
    if (toggle_pump2_flag):
        pump1_label = Label(graph_screen_frame, text="Pump 2: ")
        pump2_button_on = Button(graph_screen_frame, text="On", command=toggle_pump2)
        pump2_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump2)
        pump2_label.grid(row=1, column=0)
        pump2_button_on.grid(row=1, column=1)
        pump2_button_off.grid(row=1, column=2)
    else:
        pump2_label = Label(graph_screen_frame, text="Pump 2: ")
        pump2_button_on = Button(graph_screen_frame, text="On", command=toggle_pump2)
        pump2_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump2)
        pump2_label.grid(row=1, column=0)
        pump2_button_on.grid(row=1, column=1)
        pump2_button_off.grid(row=1, column=2)
    
    # Control Pump 3    
    if (toggle_pump3_flag):
        pump3_label = Label(graph_screen_frame, text="Pump 3: ")
        pump3_button_on = Button(graph_screen_frame, text="On", command=toggle_pump3)
        pump3_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump3)
        pump3_label.grid(row=2, column=0)
        pump3_button_on.grid(row=2, column=1)
        pump3_button_off.grid(row=2, column=2)
    else:
        pump3_label = Label(graph_screen_frame, text="Pump 3: ")
        pump3_button_on = Button(graph_screen_frame, text="On", command=toggle_pump3)
        pump3_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump3)
        pump3_label.grid(row=2, column=0)
        pump3_button_on.grid(row=2, column=1)
        pump3_button_off.grid(row=2, column=2)
        
    # Control Pump 4
    if (toggle_pump4_flag):
        pump4_label = Label(graph_screen_frame, text="Pump 4: ")
        pump4_button_on = Button(graph_screen_frame, text="On", command=toggle_pump4)
        pump4_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump4)
        pump4_label.grid(row=3, column=0)
        pump4_button_on.grid(row=3, column=1)
        pump4_button_off.grid(row=3, column=2)
    else:
        pump4_label = Label(graph_screen_frame, text="Pump 4: ")
        pump4_button_on = Button(graph_screen_frame, text="On", command=toggle_pump4)
        pump4_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump4)
        pump4_label.grid(row=3, column=0)
        pump4_button_on.grid(row=3, column=1)
        pump4_button_off.grid(row=3, column=2)
    
    # Control Pump 5
    if (toggle_pump5_flag):
        pump5_label = Label(graph_screen_frame, text="Pump 5: ")
        pump5_button_on = Button(graph_screen_frame, text="On", command=toggle_pump5)
        pump5_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump5)
        pump5_label.grid(row=4, column=0)
        pump5_button_on.grid(row=4, column=1)
        pump5_button_off.grid(row=4, column=2)
    else:
        pump5_label = Label(graph_screen_frame, text="Pump 5: ")
        pump5_button_on = Button(graph_screen_frame, text="On", command=toggle_pump5)
        pump5_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump5)
        pump5_label.grid(row=4, column=0)
        pump5_button_on.grid(row=4, column=1)
        pump5_button_off.grid(row=4, column=2) 
        
    # Control Pump 6
    if (toggle_pump6_flag):
        pump6_label = Label(graph_screen_frame, text="Pump 6: ")
        pump6_button_on = Button(graph_screen_frame, text="On", command=toggle_pump6)
        pump6_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump6)
        pump6_label.grid(row=5, column=0)
        pump6_button_on.grid(row=5, column=1)
        pump6_button_off.grid(row=5, column=2)
    else:
        pump6_label = Label(graph_screen_frame, text="Pump 6: ")
        pump6_button_on = Button(graph_screen_frame, text="On", command=toggle_pump6)
        pump6_button_off = Button(graph_screen_frame, text="Off", command=toggle_pump6)
        pump6_label.grid(row=5, column=0)
        pump6_button_on.grid(row=5, column=1)
        pump6_button_off.grid(row=5, column=2)    

# draw fraph function
def open_graph_view():
    hide_all_frames()
    graph_screen_frame.pack(fill="both", padx=50, pady=50)
    def graph():
        #read data
        data = np.random.normal(200000, 100000, 50000)
        plt.hist(data, 50)
        plt.show()
        
    graph1_button = Button(graph_screen_frame, text="Graph 1", command=graph)
    graph1_button.grid(row=0, column=0)
    
    graph2_button = Button(graph_screen_frame, text="Graph 2", command=graph)
    graph2_button.grid(row=0, column=1)
   
# Hide all frames when open another screnn
def hide_all_frames():
    button_screen_frame.pack_forget()
    graph_screen_frame.pack_forget()


my_menu = Menu(root)
root.config(menu=my_menu)

screen_menu = Menu(my_menu)
my_menu.add_cascade(label="Screen", menu=screen_menu)
screen_menu.add_command(label="Control button view", command=open_button_view)
screen_menu.add_command(label="Graph view", command=open_graph_view)

# Menu Frame
button_screen_frame = Frame(root, width=600, height=400)
graph_screen_frame = Frame(root, width=600, height=400)

root.mainloop()

