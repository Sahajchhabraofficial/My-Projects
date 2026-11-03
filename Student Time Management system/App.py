import calendar
import datetime
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
        self._create_layout()
        self._clear_content()
        ProfileFrame = CTkScrollableFrame(self.ContentFrame, fg_color="black")
        ProfileFrame.pack(expand=True, fill=BOTH)
        CTkLabel(
            ProfileFrame,
            text="👤 Sahaj Chhabra",
            font=CTkFont(family="@Microsoft YaHei", weight="bold", size=38),
            bg_color="transparent",
            fg_color="black",
        ).pack(side=TOP, pady=(30, 12))
        CTkLabel(
            ProfileFrame,
            text="Student Account",
            font=CTkFont(size=18),
            text_color="#E1DCE8",
            bg_color="transparent",
            fg_color="black",
        ).pack(side=TOP, pady=8)
        InfoFrame=CTkFrame(ProfileFrame, width=200, height=50, border_color="white", border_width=1, bg_color="transparent", fg_color="#88FFB0")
        InfoFrame.pack(side=TOP, padx=10, pady=10, fill=X)
        PIFont=CTkFont(family="Candara", weight="bold", size=30)
        PIFont_subtitle=CTkFont(family="Candara", weight="normal", size=23)
        CTkLabel(InfoFrame, text="Personal Information", font=PIFont, text_color="black").grid(row=1, column=1, pady=5, padx=5)
        CTkLabel(InfoFrame, text="Name: Sahaj Chhbara", font=PIFont_subtitle, text_color="black").grid(row=2, column=1, padx=5, pady=5)
        CTkLabel(InfoFrame, text="Class: 12th A", font=PIFont_subtitle, text_color="black").grid(row=2, column=2, padx=5, pady=5)
        CTkLabel(InfoFrame, text="Stream: PCM + CS", font=PIFont_subtitle, text_color="black").grid(row=3, column=1, padx=5, pady=5)
        CTkLabel(InfoFrame, text="Age: 17", font=PIFont_subtitle, text_color="black").grid(row=3, column=2, padx=5, pady=5)

        SettingsFrame=CTkFrame(ProfileFrame, width=200, height=50, border_color="white", border_width=1, bg_color="transparent", fg_color="#2FD33C")
        SettingsFrame.pack(side=TOP, padx=10, pady=10, fill=X)
        CTkLabel(SettingsFrame, text="App Preferences", font=PIFont, text_color="black").grid(row=1, column=1, pady=5, padx=5)
        CTkLabel(SettingsFrame, text="Theme: ", font=PIFont_subtitle, text_color="black").grid(row=2, column=1, pady=5, padx=5)
        CTkButton(SettingsFrame, text="Light", corner_radius=12, bg_color="transparent", fg_color="#EBE6FF", text_color="black", border_color="black", border_width=1, hover=False).grid(row=2, column=2, padx=3, pady=3)
        CTkButton(SettingsFrame, text="Dark", corner_radius=12, bg_color="transparent", fg_color="#2A292E", text_color="white", border_color="white", border_width=1, hover=False).grid(row=2, column=3, padx=3, pady=3)
        CTkLabel(SettingsFrame, text="Notifications: ", font=PIFont_subtitle, text_color="black").grid(row=3, column=1, pady=5, padx=5)
        CTkCheckBox(SettingsFrame, width=100, height=24, checkbox_height=24, corner_radius=12, border_color="blue", border_width=1, bg_color="transparent", fg_color="blue", text="Enable", font=PIFont_subtitle, text_color="white").grid(row=3, column=2, padx=5, pady=5)

        StatsFrame=CTkFrame(ProfileFrame, width=200, height=50, border_color="white", border_width=1, bg_color="transparent", fg_color="#CD2FD3")
        StatsFrame.pack(side=TOP, padx=10, pady=10, fill=X)
        SFFont=CTkFont(family="Seoge UI Emoji", size=20, weight='normal')
        CTkLabel(StatsFrame, text="Study Statistics", font=PIFont, text_color="black").grid(row=0, column=1, pady=5, padx=5)
        TaskFrame=CTkFrame(StatsFrame, border_color="green", border_width=2, bg_color="transparent", fg_color="#9BFFA0")
        TaskFrame.grid(padx=10, pady=5, row=1, column=1)
        CTkLabel(TaskFrame, text="✅ Total Completed Tasks", font=SFFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        CTkLabel(TaskFrame, text="3", font=PIFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        StudyHoursFrame=CTkFrame(StatsFrame, border_color="blue", border_width=2, bg_color="transparent", fg_color="#7AB2FC")
        StudyHoursFrame.grid(pady=10, padx=5, row=1, column=2)
        CTkLabel(StudyHoursFrame, text="⌚ Total Study Hours", font=SFFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        CTkLabel(StudyHoursFrame, text="12", font=PIFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        StreakFrame=CTkFrame(StatsFrame, border_color="purple", border_width=2, bg_color="transparent", fg_color="#DB9DFF")
        StreakFrame.grid(pady=10, padx=5, row=2, column=1)
        CTkLabel(StreakFrame, text="🔥 Current Study Streak", font=SFFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        CTkLabel(StreakFrame, text="3", font=PIFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        UpcomingExamFrame=CTkFrame(StatsFrame, border_color="yellow", border_width=2, bg_color="transparent", fg_color="#F5FF9D")
        UpcomingExamFrame.grid(pady=10, padx=5, row=2, column=2)
        CTkLabel(UpcomingExamFrame, text="🗓️ Upcoming Exams", font=SFFont, text_color="black").pack(side=TOP, padx=3, pady=3)
        CTkLabel(UpcomingExamFrame, text="1", font=PIFont, text_color="black").pack(side=TOP, padx=3, pady=3)

    def YourTasks(self):
        self._show_page("✅ Your Tasks", "View and manage your tasks")
        BackgroundFrame=CTkScrollableFrame(self.ContentFrame, border_color="white", border_width=2, width=200, height=200, corner_radius=14, bg_color="transparent", fg_color="black")
        BackgroundFrame.pack(pady=12, padx=12, fill=BOTH)
        def AddTask():
            name_dialog = CTkInputDialog(
                fg_color="white",
                text="Enter Task name",
                text_color="black",
                button_fg_color="green",
                button_hover_color="#167A16",
                button_text_color="white",
                entry_border_color="black",
                entry_fg_color="white",
                entry_text_color="black",
                title="Enter name of task",
                font=ATFont,
            )
            task_name = name_dialog.get_input()
            if task_name is None:
                return

            desc_dialog = CTkInputDialog(
                fg_color="white",
                text="Enter Description",
                text_color="black",
                button_fg_color="green",
                button_hover_color="#167A16",
                button_text_color="white",
                entry_border_color="black",
                entry_fg_color="white",
                entry_text_color="black",
                title="Enter task description",
                font=ATFont,
            )
            description = desc_dialog.get_input()
            if description is None:
                return

            def cancelTask():
                pass
            TaskFont=CTkFont(family="Cascadia Code", size=23, weight="bold")
            TaskFont_subtitle=CTkFont(family="Cascadia Code", size=23, weight="normal", slant="italic")
            task=CTkFrame(BackgroundFrame, width=250, height=30, border_width=2, border_color="white", bg_color="transparent", fg_color="black")
            task.pack(side=TOP, fill=X)
            CTkButton(task, border_color="white", border_width=1,width=50, bg_color="transparent", fg_color="black", text="x", command=cancelTask).pack(side=RIGHT, padx=3, pady=3)
            CTkLabel(task, text=task_name, text_color="white", font=TaskFont).pack(side=LEFT, padx=7, pady=7)
            CTkLabel(task, text=description, text_color="white", font=TaskFont_subtitle).pack(padx=7, pady=7)

        ATFont=CTkFont(family="Cascadia Code", size=23, weight="bold")
        CTkButton(BackgroundFrame, text="+ Add Task", font=ATFont, command=AddTask).pack(padx=5, pady=5)

    def StudyCalendar(self):
        self._create_layout()
        self._clear_content()

        CTkLabel(
            self.ContentFrame,
            text="📅 Study Calendar",
            font=CTkFont(family="@Microsoft YaHei", weight="bold", size=38),
        ).pack(pady=(25, 5))
        CTkLabel(
            self.ContentFrame,
            text="Choose a date",
            font=CTkFont(size=18),
            text_color="#E1DCE8",
        ).pack(pady=(0, 12))

        today = datetime.date.today()
        current_year, current_month = today.year, today.month
        calendar_frame = CTkFrame(
            self.ContentFrame,
            width=560,
            height=480,
            fg_color=("#F2F2F2", "#242424"),
            border_width=1,
            border_color=("#D0D0D0", "#444444"),
            corner_radius=16,
        )
        calendar_frame.pack(expand=True, padx=30, pady=10)
        calendar_frame.pack_propagate(False)

        navigation = CTkFrame(calendar_frame, fg_color="transparent")
        navigation.pack(fill=X, padx=16, pady=(14, 8))
        month_label = CTkLabel(navigation, text="", font=CTkFont(size=28, weight="bold"))
        month_label.pack(side=LEFT, expand=True, padx=8)

        def change_month(offset):
            nonlocal current_year, current_month
            current_month += offset
            if current_month < 1:
                current_month = 12
                current_year -= 1
            elif current_month > 12:
                current_month = 1
                current_year += 1
            update_calendar()

        CTkButton(
            navigation, text="<", width=56, height=50, font=CTkFont(size=18),
            command=lambda: change_month(-1)
        ).pack(side=LEFT)
        CTkButton(
            navigation, text=">", width=56, height=50, font=CTkFont(size=18),
            command=lambda: change_month(1)
        ).pack(side=RIGHT)

        days_frame = CTkFrame(calendar_frame, fg_color="transparent")
        days_frame.pack(fill=X, padx=18)
        for column, day_name in enumerate(("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")):
            CTkLabel(
                days_frame, text=day_name, font=CTkFont(size=18, weight="bold"),
                text_color="gray",
            ).grid(row=0, column=column, padx=5, pady=5)
            days_frame.grid_columnconfigure(column, weight=1)

        dates_frame = CTkFrame(calendar_frame, fg_color="transparent")
        dates_frame.pack(fill=BOTH, expand=True, padx=18, pady=(4, 14))
        for column in range(7):
            dates_frame.grid_columnconfigure(column, weight=1)
        for row in range(6):
            dates_frame.grid_rowconfigure(row, weight=1)

        status_label = CTkLabel(
            self.ContentFrame, text="Selected Date: None", font=CTkFont(size=14)
        )
        status_label.pack(pady=12)

        def select_date(day):
            selected = datetime.date(current_year, current_month, day)
            status_label.configure(text=f"Selected Date: {selected:%d-%B-%Y}")

        def update_calendar():
            month_label.configure(
                text=f"{calendar.month_name[current_month]} {current_year}"
            )
            for widget in dates_frame.winfo_children():
                widget.destroy()

            for row, week in enumerate(calendar.monthcalendar(current_year, current_month)):
                for column, day in enumerate(week):
                    if day == 0:
                        continue
                    is_today = (
                        current_year == today.year
                        and current_month == today.month
                        and day == today.day
                    )
                    CTkButton(
                        dates_frame,
                        text=str(day),
                        width=56,
                        height=53,
                        fg_color="#2b719e" if is_today else ("#3B8ED0", "#1F6AA5"),
                        border_width=2 if is_today else 0,
                        font=CTkFont(size=17),
                        command=lambda selected_day=day: select_date(selected_day),
                    ).grid(row=row, column=column, padx=4, pady=4, sticky="nsew")

        update_calendar()

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
