import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Дані для побудови графіків (припустимі дані)
days = ['День 1', 'День 2 (вихідний день)', 'День 3 (вихідний день)', 'День 4', 'День 5', 'День 6']
temperature = [20, 23, 23, 24, 19, 16]  # Температура в градусах Цельсія
feels_like = [20, 23, 23, 24, 19, 16]   # Відчутна температура в градусах Цельсія
wind_speed = [3.6, 3.8, 3.0, 3.1, 4.0, 3.9]    # Швидкість вітру в м/с
humidity = [52, 47, 55, 52, 60, 53]      # Вологість відсотками

def plot_line_chart():
    """Побудова лінійних графіків."""
    fig, ax = plt.subplots(figsize=(8, 6))

    # Графік температури
    ax.plot(days, temperature, label='Температура', linestyle='-', color='navy')

    # Графік відчутної температури
    ax.plot(days, feels_like, label='Відчуваєтся, як', linestyle='--', color='greenyellow')

    ax.set_title('Прогноз погоди для Парижа, Франція')
    ax.set_xlabel('Дні')
    ax.set_ylabel('Температура (°C)')
    ax.legend()
    ax.grid(True)

    return fig

def plot_column_chart():
    """Побудова стовпчастої діаграми для швидкості вітру."""
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.bar(days, wind_speed, color='plum')

    ax.set_title('Прогноз швидкості вітру для Парижа, Франція')
    ax.set_xlabel('Дні')
    ax.set_ylabel('Швидкість вітру (м/с)')
    ax.grid(True)

    return fig

def plot_pie_chart():
    """Побудова кругової діаграми для вологості."""
    fig, ax = plt.subplots(figsize=(8, 8))

    colors = ['sandybrown', 'lightcoral', 'lightcoral', 'lightpink', 'plum', 'palegreen']

    wedges, texts, autotexts = ax.pie(humidity, labels=days, autopct='%1.1f%%', startangle=140, colors=colors)

    # Змінює колір тексту на білий та встановлює відсоток вологості всередині кожної ячейки
    for autotext, h in zip(autotexts, humidity):
        autotext.set_color('white')
        autotext.set_text(f'{h}%')

    ax.set_title('Прогноз вологості для Парижа, Франція')

    return fig

def update_chart(event):
    """Оновлення графіка при зміні типу графіка."""
    global canvas

    if canvas:
        canvas.get_tk_widget().destroy()

    chart_type = chart_selector.get()

    if chart_type == 'Лінійна діаграма':
        fig = plot_line_chart()
    elif chart_type == 'Стовпчаста діаграма':
        fig = plot_column_chart()
    elif chart_type == 'Кругова діаграма':
        fig = plot_pie_chart()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
root.title("Weather Charts")
root.geometry("800x600")
root.configure(bg='white')  # Встановлює білий фон для вікна

# Варіанти вибору типу графіка
chart_types = ['Лінійна діаграма', 'Стовпчаста діаграма', 'Кругова діаграма']
chart_selector = tk.StringVar(root)
chart_selector.set(chart_types[0])

# Меню для вибору типу графіка
chart_menu = tk.OptionMenu(root, chart_selector, *chart_types, command=update_chart)
chart_menu.pack(pady=10)

canvas = None
update_chart(None)

root.mainloop()
