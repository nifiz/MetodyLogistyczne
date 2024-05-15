import MainWindow

if __name__ == "__main__":
    app = MainWindow.App()
    app.title("Logistyka")
    app.configure(background="white")
    app.minsize(700, 600)
    app.maxsize(1024, 800)
    app.mainloop()