import MainWindow

if __name__ == "__main__":
    app = MainWindow.App()
    app.mainloop()

# import Prawdopodobienstwa
# import matplotlib.pyplot as plt
#
# days = 20
# data = Prawdopodobienstwa.TOTAL(days)
#
# categories = ['TOTAL', 'ULG95', 'DK', 'ULTSU', 'ULTDK']
# transformed_data = {category: [] for category in categories}
#
# for key in data:
#     for entry in data[key]:
#         for category in categories:
#             if category in entry:
#                 transformed_data[category].append(entry[category])
#
# colors = ['blue', 'green', 'red', 'purple', 'orange']
#
# # Tworzenie wykresów
# fig, axs = plt.subplots(len(categories), figsize=(10, 15))
#
# for idx, category in enumerate(categories):
#     axs[idx].plot(range(1, days+1), transformed_data[category], marker='o', label=category, color=colors[idx])
#     axs[idx].set_xlabel('Dni dostaw')
#     axs[idx].set_ylabel('Dane dostaw')
#     axs[idx].legend()
#     axs[idx].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
#
# plt.tight_layout()
# plt.show()
