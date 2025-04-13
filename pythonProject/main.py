# add_category_form.py
import tkinter as tk
from tkinter import messagebox

class AddCategoryForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Добавить новую категорию")

        # Метка и поле для ввода названия категории
        self.label_name = tk.Label(self, text="Название:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Метка и поле для ввода описания категории
        self.label_desc = tk.Label(self, text="Описание:")
        self.label_desc.grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(self)
        self.entry_desc.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка для добавления категории
        self.add_button = tk.Button(self, text="Добавить", command=self.add_category)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def add_category(self):
        name = self.entry_name.get().strip()
        description = self.entry_desc.get().strip()

        if not name:
            messagebox.showerror("Ошибка", "Название категории не может быть пустым.")
            return

        # Здесь будет вызов метода для добавления категории в базу
        # Например, функция (из модуля database) create_category(name, description)
        from database import create_category

        category_id = create_category(name, description)
        if category_id:
            messagebox.showinfo("Успех", f"Категория '{name}' успешно добавлена с ID {category_id}!")
            self.destroy()  # Закрыть окно после успешного добавления
        else:
            messagebox.showerror("Ошибка", "Невозможно добавить категорию в базу данных.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    AddCategoryForm(root)
    root.mainloop()