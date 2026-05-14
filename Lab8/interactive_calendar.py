import tkinter as tk
import calendar
from datetime import datetime

BG_COLOR = "#0f172a"
CARD_COLOR = "#1e293b"
GREEN = "#4ade80"
RED = "#ff6b6b"
WHITE = "white"
HOLIDAY = "#f59e0b"

months = [
    "Январь", "Февраль", "Март",
    "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь",
    "Октябрь", "Ноябрь", "Декабрь"
]

days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

holidays = {
    (1, 1): "🎄 Новый год",
    (2, 23): "🛡 День защитника Отечества",
    (3, 8): "🌸 Международный женский день",
    (5, 1): "🌷 Праздник Весны и Труда",
    (5, 9): "🎖 День Победы",
    (6, 12): "🇷🇺 День России",
    (11, 4): "✨ День народного единства"
}

now = datetime.now()
current_month = now.month
current_year = now.year

def draw_calendar():
    global current_month, current_year

    for widget in calendar_frame.winfo_children():
        widget.destroy()

    title_label.config(
        text=f"{months[current_month - 1]} {current_year}"
    )

    for col, day in enumerate(days):
        label = tk.Label(
            calendar_frame,
            text=day,
            font=("Arial", 14, "bold"),
            bg=CARD_COLOR,
            fg=GREEN,
            width=6,
            height=2
        )

        label.grid(row=0, column=col, padx=2, pady=2)

    cal = calendar.monthcalendar(
        current_year,
        current_month
    )

    today = datetime.now()

    for row_num, week in enumerate(cal, start=1):
        for col_num, day in enumerate(week):

            if day == 0:
                text = ""
            else:
                text = str(day)

            bg_color = "#111827"
            fg_color = WHITE

            if col_num == 5:
                fg_color = GREEN

            if col_num == 6:
                fg_color = RED

            if (current_month, day) in holidays:
                bg_color = HOLIDAY
                fg_color = "black"

            if (
                day == today.day and
                current_month == today.month and
                current_year == today.year
            ):
                bg_color = "#22c55e"
                fg_color = "white"

            label = tk.Label(
                calendar_frame,
                text=text,
                font=("Arial", 16, "bold"),
                bg=bg_color,
                fg=fg_color,
                width=6,
                height=3,
                relief="flat",
                cursor="hand2"
            )

            label.grid(
                row=row_num,
                column=col_num,
                padx=2,
                pady=2
            )

            label.bind(
                "<Enter>",
                lambda e, l=label: l.config(bg="#334155")
            )

            label.bind(
                "<Leave>",
                lambda e, l=label, d=day: reset_color(l, d)
            )

            if (current_month, day) in holidays:
                holiday_name = holidays[(current_month, day)]

                label.bind(
                    "<Button-1>",
                    lambda e, h=holiday_name:
                    show_holiday(h)
                )

def reset_color(label, day):
    if (current_month, day) in holidays:
        label.config(bg=HOLIDAY)
        return

    today = datetime.now()

    if (
        day == today.day and
        current_month == today.month and
        current_year == today.year
    ):
        label.config(bg="#22c55e")

    else:
        label.config(bg="#111827")

def show_holiday(name):
    holiday_label.config(
        text=f"Сегодня праздник: {name}"
    )

def next_month():
    global current_month, current_year

    current_month += 1

    if current_month > 12:
        current_month = 1
        current_year += 1

    draw_calendar()

def prev_month():
    global current_month, current_year

    current_month -= 1

    if current_month < 1:
        current_month = 12
        current_year -= 1

    draw_calendar()

def today_month():
    global current_month, current_year

    now = datetime.now()

    current_month = now.month
    current_year = now.year

    draw_calendar()

root = tk.Tk()

root.title("Интерактивный календарь")
root.geometry("1000x760")
root.config(bg=BG_COLOR)

header = tk.Label(
    root,
    text="📅 Интерактивный календарь",
    font=("Arial", 28, "bold"),
    bg=BG_COLOR,
    fg="white"
)

header.pack(pady=20)

top_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

top_frame.pack(pady=10)

prev_button = tk.Button(
    top_frame,
    text="◀ Предыдущий",
    command=prev_month,
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2"
)

prev_button.grid(row=0, column=0, padx=20)

title_label = tk.Label(
    top_frame,
    text="",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=GREEN
)

title_label.grid(row=0, column=1, padx=40)

next_button = tk.Button(
    top_frame,
    text="Следующий ▶",
    command=next_month,
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2"
)

next_button.grid(row=0, column=2, padx=20)

calendar_frame = tk.Frame(
    root,
    bg="#1f2937"
)

calendar_frame.pack(
    padx=20,
    pady=20
)

bottom_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

bottom_frame.pack(pady=10)

today_button = tk.Button(
    bottom_frame,
    text="📍 Сегодня",
    command=today_month,
    font=("Arial", 14, "bold"),
    bg=CARD_COLOR,
    fg=GREEN,
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2"
)

today_button.grid(row=0, column=0, padx=10)

holiday_label = tk.Label(
    root,
    text="Нажмите на праздничную дату",
    font=("Arial", 16),
    bg=BG_COLOR,
    fg="#cbd5e1"
)

holiday_label.pack(pady=20)
draw_calendar()
root.mainloop()