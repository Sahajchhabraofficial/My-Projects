from tkinter import *
from customtkinter import *
import mysql.connector as msc

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1048x700")
        self.minsize(900, 700)
        self.title("Student Time Managemant system")

    def Database_Connection():
        connection=msc.connect(hostname="localhost", user="root", password="FaceAttendBy$ahaj")
        cursor=connection.cursor()
        Query="""CREATE DATABASE STMS"""
        QUERY1="""CREATE TABLE USERS(
                NAME VARCHAR(255) NOT NULL,
                ID INT PRIMARY KEY,
                STUDY_HOURS INT NOT NULL,
                TASKS COMPLETED INT NOT NULL, 
                TOTAL_FOCUS_TIME INT NOT NULL,
                STUDY_STREAK INT NOT NULL""" 
        QUERY2=""
        cursor.execute(QUERY1)

    def Dashboard(self):
        print("DashBoard Clicked")
        self._create_layout()
        self._clear_content()

        # == Dashboard UI =======================================================
        Font=CTkFont(family="@Microsoft YaHei", weight="bold", size=50)
        CTkLabel(
            self.ContentFrame,
            text="🌆 Good Evening, Sahaj!",
            font=Font,
            bg_color="transparent",
            fg_color="black",
        ).pack(side=TOP, pady=10)

        CardsFrame = CTkFrame(self.ContentFrame, fg_color="transparent")
        CardsFrame.pack(side=TOP, fill=X, padx=18, pady=(18, 10))

        card_data = [
            ("📚", "Study Hours", "Track your learning progress",8 , "#49306B"),
            ("✅", "Tasks Completed", "Celebrate what you achieve",10,  "#285B53"),
            ("⏳", "Focus Time", "Make every minute count",20 ,"#76502D"),
            ("🔥", "Study Streak", "Stay on top of your priorities", 5, "#3C4F75"),
        ]
        for icon, title, subtitle, value, color in card_data:
            card = CTkFrame(
                CardsFrame,
                fg_color=color,
                corner_radius=18,
                border_width=1,
                border_color="#74658A",
                height=170,
            )
            card.pack(side=LEFT, expand=True, fill=BOTH, padx=8)
            card.pack_propagate(True)
            CTkLabel(card, text=icon, font=CTkFont(size=30)).pack(anchor="w", padx=18, pady=(17, 5))
            CTkLabel(card, text=value, font=CTkFont(size=30, weight='bold')).pack(anchor='w', padx=10, pady=10)
            CTkLabel(card, text=title, font=CTkFont(size=19, weight="bold")).pack(anchor="w", padx=18, pady=3)
            CTkLabel(card, text=subtitle, font=CTkFont(size=12), text_color="#E1DCE8").pack(
                anchor="w", padx=18, pady=(2, 14)
            )

    def _create_layout(self):
        if hasattr(self, "ContentFrame"):
            return

        self.BackgroundFrame = CTkFrame(
            self,
            border_color="white",
            border_width=1,
            bg_color="transparent",
            fg_color="black",
        )
        self.BackgroundFrame.pack(expand=True, fill=BOTH)
        self.NAVFrame = CTkFrame(
            self.BackgroundFrame,
            border_color="white",
            border_width=1,
            bg_color="transparent",
            fg_color="purple",
            width=250,
        )
        self.NAVFrame.pack(pady=3, padx=3, side=LEFT, fill=Y)
        CTkLabel(
            self.NAVFrame,
            text="⏰STMS",
            font=CTkFont(family="@Microsoft YaHei", weight="bold", size=50),
        ).pack(side=TOP, pady=12, padx=(5, 10))

        self.ContentFrame = CTkFrame(self.BackgroundFrame, fg_color="black")
        self.ContentFrame.pack(side=LEFT, expand=True, fill=BOTH)

        emoji = CTkFont(family="Seoge UI Emoji", weight="normal", size=20)
        navigation = [
            ("🛖 DashBoard", self.Dashboard),
            ("✅ Your Tasks", self.YourTasks),
            ("📅 Study Calendar", self.StudyCalendar),
            ("⏳ Focus Timer", self.FocusTimer),
            ("👤 Profile", self.Profile),
        ]
        for text, command in navigation:
            CTkButton(
                self.NAVFrame,
                text=text,
                font=emoji,
                height=30,
                width=40,
                corner_radius=10,
                bg_color="transparent",
                fg_color="purple",
                hover_color="green",
                command=command,
                border_color="white",
                border_width=1,
            ).pack(side=TOP, pady=7, padx=10, fill=X, ipadx=15)

    def _clear_content(self):
        for widget in self.ContentFrame.winfo_children():
            widget.destroy()

    def _show_page(self, title, description):
        self._create_layout()
        self._clear_content()
        CTkLabel(
            self.ContentFrame,
            text=title,
            font=CTkFont(family="@Microsoft YaHei", weight="bold", size=38),
            bg_color="transparent",
            fg_color="black",
        ).pack(side=TOP, pady=(30, 12))
        CTkLabel(
            self.ContentFrame,
            text=description,
            font=CTkFont(size=18),
            text_color="#E1DCE8",
            bg_color="transparent",
            fg_color="black",
        ).pack(side=TOP, pady=8)

    def Profile(self):
        self._show_page("👤 Sahaj Chhabra", "Student Account")
        InfoFrame=CTkFrame(self.ContentFrame, width=200, height=50, border_color="white", border_width=1, bg_color="transparent", fg_color="#88FFB0")
        InfoFrame.pack(side=TOP, padx=10, pady=10, fill=X)
        PIFont=CTkFont(family="Candara", weight="bold", size=30)
        CTkLabel(InfoFrame, text="Personal Information", font=PIFont, text_color="black").grid(row=1, column=1, pady=5, padx=5)
        CTkLabel(InfoFrame, )
        

    def YourTasks(self):
        self._show_page("✅ Your Tasks", "View and manage your tasks")

    def StudyCalendar(self):
        self._show_page("📅 Study Calendar", "View your study calendar")

    def FocusTimer(self):
        self._show_page("⏳ Focus Timer", "Manage your focused study sessions")
        if getattr(self, "_timer_after_id", None):
            self.after_cancel(self._timer_after_id)
            self._timer_after_id = None

        timer_font = CTkFont(family="Bernard MT Condensed", size=64, weight="bold")
        control_font = CTkFont(family="Bernard MT Condensed", size=20)
        self._timer_remaining = 0
        self._timer_total = 0
        self._timer_running = False

        time_display = CTkLabel(self.ContentFrame, text="00:00:00", font=timer_font)
        time_display.pack(pady=(25, 15))
        duration_entry = CTkEntry(
            self.ContentFrame, width=220, height=42, corner_radius=12,
            placeholder_text="Enter a duration", font=control_font,
        )
        duration_entry.pack(pady=8)
        time_unit = CTkOptionMenu(
            self.ContentFrame, width=150, height=36, corner_radius=12,
            values=["Seconds", "Minutes", "Hours"], font=control_font,
        )
        time_unit.pack(pady=8)
        progress = CTkProgressBar(
            self.ContentFrame, width=300, height=17, corner_radius=12,
            progress_color="green",
        )
        progress.set(0)
        progress.pack(pady=15)
        status = CTkLabel(self.ContentFrame, text="Set a duration and start.", font=CTkFont(size=14))
        status.pack(pady=5)

        def format_time(seconds):
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"

        def tick():
            self._timer_after_id = None
            if not self._timer_running or not time_display.winfo_exists():
                return
            self._timer_remaining -= 1
            time_display.configure(text=format_time(self._timer_remaining))
            progress.set(1 - self._timer_remaining / self._timer_total)
            if self._timer_remaining <= 0:
                self._timer_running = False
                self._timer_remaining = 0
                progress.set(1)
                status.configure(text="Timer complete!")
            else:
                self._timer_after_id = self.after(1000, tick)

        def start_timer():
            if self._timer_running:
                return
            if self._timer_remaining <= 0:
                try:
                    duration = int(duration_entry.get().strip())
                    if duration <= 0:
                        raise ValueError
                except ValueError:
                    status.configure(text="Enter a positive whole number.")
                    return
                multiplier = {"Seconds": 1, "Minutes": 60, "Hours": 3600}[time_unit.get()]
                self._timer_total = duration * multiplier
                self._timer_remaining = self._timer_total
                time_display.configure(text=format_time(self._timer_remaining))
                progress.set(0)
            self._timer_running = True
            status.configure(text="Timer running…")
            self._timer_after_id = self.after(1000, tick)

        def pause_timer():
            self._timer_running = False
            if getattr(self, "_timer_after_id", None):
                self.after_cancel(self._timer_after_id)
                self._timer_after_id = None
            status.configure(text="Timer paused.")

        def reset_timer():
            self._timer_running = False
            if getattr(self, "_timer_after_id", None):
                self.after_cancel(self._timer_after_id)
                self._timer_after_id = None
            self._timer_remaining = 0
            self._timer_total = 0
            time_display.configure(text="00:00:00")
            progress.set(0)
            status.configure(text="Set a duration and start.")

        CTkButton(
            self.ContentFrame, width=150, height=36, text="Start Timer",
            fg_color="green", hover_color="#3F912B", font=control_font,
            command=start_timer,
        ).pack(padx=10, pady=7)
        CTkButton(
            self.ContentFrame, width=150, height=36, text="Pause Timer",
            fg_color="blue", hover_color="#283BA8", font=control_font,
            command=pause_timer,
        ).pack(padx=10, pady=7)
        CTkButton(
            self.ContentFrame, width=150, height=36, text="Reset Timer",
            fg_color="red", hover_color="#A82828", font=control_font,
            command=reset_timer,
        ).pack(padx=10, pady=7)


if __name__=="__main__":
    window=App()
    window.Dashboard()
    window.mainloop()
