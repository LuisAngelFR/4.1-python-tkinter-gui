import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")
        self.root.geometry("400x500")
        self.root.resizable(True, True)

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        """Crea los widgets principales de la aplicación"""
        tk.Label(self.root, text="Lista de Tareas", font=("Arial", 16)).pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=45, height=10)
        self.task_listbox.pack(pady=10)

        self.create_action_buttons()

    def create_action_buttons(self):
        """Crea los botones de acción para la lista"""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        delete_button = tk.Button(frame, text="Eliminar Tarea", command=self.delete_task)
        delete_button.grid(row=0, column=0, padx=5)

        mark_button = tk.Button(frame, text="Marcar como Completada", command=self.mark_task)
        mark_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        """Añadir una tarea a la lista"""
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor ingresa una tarea.")

    def delete_task(self):
        """Eliminar la tarea seleccionada"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Selección Inválida", "Por favor selecciona una tarea.")

    def mark_task(self):
        """Marcar una tarea como completada"""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            if task.startswith("✔"):
                return
            self.tasks[selected_index] = f"✔ {task}"
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Selección Inválida", "Por favor selecciona una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
