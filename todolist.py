import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.tasks = []
        
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial 16  bold"), width=10 , bd= '5',bg='green', fg='black') 
 
        self.title_label.pack(pady=10,side='top')
        
        self.listbox = tk.Listbox(root, width=30, height=10,  bd=5 , font=("arial 20 italic bold"))
        self.listbox.pack(pady=20)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task ,font=('sarif 20  italic') , width=10 ,bd=2,bg='green',fg='black') 
        self.add_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task,font=('sarif 20 italic') , width=10 , bd=2 ,bg='green',fg='black')
        self.remove_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Exit", command=root.quit,font=('sarif 20 italic') , width=10 , bd=2,bg='green',fg='black')
        self.quit_button.pack(pady=20)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter a task:")
        if task:
            self.tasks.append(task)
            self.update_listbox()

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove!")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    app = ToDoApp(root)
    root.mainloop()