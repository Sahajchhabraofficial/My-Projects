from tkinter import *
from customtkinter import *
import csv
from tkinter import messagebox as tmsg

"""Modern Student Management System with CustomTkinter"""

# Color Scheme
COLOR_BG = "#121826"
COLOR_SECONDARY = "#1E293B"
COLOR_ACCENT = "#3B82F6"
COLOR_SUCCESS = "#22C55E"
COLOR_WARNING = "#F59E0B"
COLOR_DANGER = "#EF4444"
COLOR_TEXT = "#F8FAFC"
COLOR_TEXT_SECONDARY = "#94A3B8"

class Student_App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x750")
        self.title("Student Management System")
        self.minsize(700, 500)
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        
        # Configure window background
        self.configure(fg_color=COLOR_BG)


    def HomePage(self):
        """Main dashboard with feature cards"""
        background = CTkFrame(self, fg_color=COLOR_BG, bg_color="transparent")
        background.pack(expand=True, fill=BOTH, padx=0, pady=0)

        # -- FONTS ----------------------------------------------------------------
        title_font = CTkFont(family="Segoe UI", size=42, weight="bold")
        emoji_font = CTkFont(family="Segoe UI Emoji", size=70, weight="bold")
        feature_title_font = CTkFont(family="Segoe UI", size=22, weight="bold")
        feature_button_font = CTkFont(family="Segoe UI", size=18, weight="bold")

        # -- HEADER ----------------------------------------------------------------
        header_frame = CTkFrame(background, fg_color=COLOR_SECONDARY, bg_color="transparent", corner_radius=0)
        header_frame.pack(fill=X, padx=0, pady=0)

        # Top bar with quit button
        top_bar = CTkFrame(header_frame, fg_color=COLOR_SECONDARY, bg_color="transparent")
        top_bar.pack(fill=X, padx=20, pady=15)
        
        quit_btn = CTkButton(
            top_bar,
            text="✕",
            font=CTkFont(family="Segoe UI", size=20),
            width=40,
            height=40,
            fg_color="transparent",
            text_color=COLOR_TEXT_SECONDARY,
            hover_color=COLOR_DANGER,
            command=self.Quit_App,
            corner_radius=8
        )
        quit_btn.pack(side=RIGHT)

        # Title section
        title_section = CTkFrame(header_frame, fg_color=COLOR_SECONDARY, bg_color="transparent")
        title_section.pack(fill=X, padx=20, pady=(10, 20))

        CTkLabel(
            title_section,
            text="🧑‍🎓",
            font=emoji_font,
            text_color=COLOR_ACCENT,
            bg_color="transparent"
        ).pack(pady=(0, 10))

        CTkLabel(
            title_section,
            text="Student Management System",
            font=title_font,
            text_color=COLOR_TEXT,
            bg_color="transparent"
        ).pack()

        CTkLabel(
            title_section,
            text="Manage student records efficiently",
            font=CTkFont(family="Segoe UI", size=14),
            text_color=COLOR_TEXT_SECONDARY,
            bg_color="transparent"
        ).pack(pady=(5, 0))

        # -- FEATURES SECTION ----------------------------------------------------------------
        features_container = CTkFrame(background, fg_color=COLOR_BG, bg_color="transparent")
        features_container.pack(fill=BOTH, expand=True, padx=30, pady=30)

        # Create a scrollable frame for features
        features_scroll = CTkScrollableFrame(
            features_container,
            fg_color=COLOR_BG,
            bg_color="transparent",
            label_text="Features",
            label_font=CTkFont(family="Segoe UI", size=18, weight="bold"),
            label_text_color=COLOR_TEXT
        )
        features_scroll.pack(fill=BOTH, expand=True)

        # Feature Cards Grid
        cards_frame = CTkFrame(features_scroll, fg_color=COLOR_BG, bg_color="transparent")
        cards_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Feature 1 - Register (Blue/Accent)
        self._create_feature_card(
            cards_frame,
            row=0, col=0,
            emoji="➕",
            title="Register Student",
            description="Add new student records",
            button_text="Register",
            bg_color=COLOR_ACCENT,
            command=self.Register_Student,
            font=feature_button_font
        )

        # Feature 2 - Update (Green/Success)
        self._create_feature_card(
            cards_frame,
            row=0, col=1,
            emoji="✏️",
            title="Update Student",
            description="Modify student information",
            button_text="Update",
            bg_color=COLOR_SUCCESS,
            command=self.Update_Student,
            font=feature_button_font
        )

        # Feature 3 - Delete (Red/Danger)
        self._create_feature_card(
            cards_frame,
            row=1, col=0,
            emoji="🗑️",
            title="Delete Student",
            description="Remove student records",
            button_text="Delete",
            bg_color=COLOR_DANGER,
            command=self.Delete_Student,
            font=feature_button_font
        )

        # Feature 4 - Search (Orange/Warning)
        self._create_feature_card(
            cards_frame,
            row=1, col=1,
            emoji="🔍",
            title="Search Student",
            description="Find student information",
            button_text="Search",
            bg_color=COLOR_WARNING,
            command=self.Search_Student,
            font=feature_button_font
        )

    def _create_feature_card(self, parent, row, col, emoji, title, description, button_text, bg_color, command, font):
        """Helper method to create a feature card"""
        card_frame = CTkFrame(
            parent,
            fg_color=COLOR_SECONDARY,
            bg_color="transparent",
            corner_radius=15,
            border_width=1,
            border_color=bg_color
        )
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

        # Set column weights for grid
        parent.grid_columnconfigure(col, weight=1)
        parent.grid_rowconfigure(row, weight=1)

        # Emoji
        CTkLabel(
            card_frame,
            text=emoji,
            font=CTkFont(family="Segoe UI Emoji", size=50),
            text_color=bg_color,
            bg_color="transparent"
        ).pack(pady=(20, 10))

        # Title
        CTkLabel(
            card_frame,
            text=title,
            font=CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color=COLOR_TEXT,
            bg_color="transparent"
        ).pack(pady=(0, 5))

        # Description
        CTkLabel(
            card_frame,
            text=description,
            font=CTkFont(family="Segoe UI", size=12),
            text_color=COLOR_TEXT_SECONDARY,
            bg_color="transparent"
        ).pack(pady=(0, 20))

        # Button
        btn = CTkButton(
            card_frame,
            text=button_text,
            font=font,
            fg_color=bg_color,
            text_color="white",
            hover_color=self._lighten_color(bg_color),
            command=command,
            width=150,
            height=45,
            corner_radius=10
        )
        btn.pack(pady=(0, 20))

    def _lighten_color(self, hex_color):
        """Lighten a hex color for hover effects"""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        
        r = min(255, int(r * 1.2))
        g = min(255, int(g * 1.2))
        b = min(255, int(b * 1.2))
        
        return f"#{r:02x}{g:02x}{b:02x}"

    def Register_Student(self):
        """Register a new student"""
        print("Register Student Called")
        window = CTkToplevel(self)
        window.geometry("550x700")
        window.title("Register Student")
        window.configure(fg_color=COLOR_BG)
        set_appearance_mode("dark")

        # -- FONTS --------------------------------------------------------------------------------------- 
        heading_font = CTkFont(family="Segoe UI", size=24, weight="bold")
        label_font = CTkFont(family="Segoe UI", size=13)
        button_font = CTkFont(family="Segoe UI", size=16, weight="bold")

        # -- HEADER ----------------------------------------------------------------
        header_frame = CTkFrame(window, fg_color=COLOR_SECONDARY, corner_radius=0, height=70)
        header_frame.pack(fill=X, padx=0, pady=0)

        CTkLabel(
            header_frame,
            text="➕ Register New Student",
            font=heading_font,
            text_color=COLOR_TEXT
        ).pack(pady=15)

        # -- MAIN CONTENT ----------------------------------------------------------------- 
        content_frame = CTkScrollableFrame(
            window,
            fg_color=COLOR_BG,
            bg_color="transparent"
        )
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        def insert_details(name, roll, Class, section, percentage):
            name = name.get()
            roll = int(roll.get())
            Class = int(Class.get())
            section = section.get()
            percentage = float(percentage.get())

            with open("Student-Database.csv", 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, roll, Class, section, percentage])

            tmsg.showinfo("Success", "Successfully registered student details", parent=window)
            window.destroy()

        # Name
        CTkLabel(content_frame, text="Student's Name", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
        Name = CTkEntry(
            content_frame,
            placeholder_text="eg. Avinash Kumar",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Name.pack(pady=(0, 15), fill=X)

        # Roll Number
        CTkLabel(content_frame, text="Student's Roll Number", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Roll = CTkEntry(
            content_frame,
            placeholder_text="eg. 1005",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Roll.pack(pady=(0, 15), fill=X)

        # Class and Section in a row
        class_section_frame = CTkFrame(content_frame, fg_color="transparent")
        class_section_frame.pack(fill=X, pady=(0, 15))

        CTkLabel(class_section_frame, text="Class", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Class = CTkEntry(
            class_section_frame,
            placeholder_text="eg. 12",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Class.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        CTkLabel(class_section_frame, text="Section", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Section = CTkEntry(
            class_section_frame,
            placeholder_text="eg. A",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Section.pack(side=LEFT, fill=BOTH, expand=True)

        # Percentage
        CTkLabel(content_frame, text="Last Year Percentage", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
        Percentage = CTkEntry(
            content_frame,
            placeholder_text="eg. 85.5",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Percentage.pack(pady=(0, 30), fill=X)

        # Submit Button
        CTkButton(
            content_frame,
            text="✓ Register Student",
            font=button_font,
            fg_color=COLOR_SUCCESS,
            text_color="white",
            hover_color=self._lighten_color(COLOR_SUCCESS),
            command=lambda: insert_details(Name, Roll, Class, Section, Percentage),
            height=50,
            corner_radius=10
        ).pack(pady=(0, 15), fill=X)

    def Update_Student(self):
        """Update an existing student"""
        print("Update Student Called")
        window = CTkToplevel(self)
        window.geometry("550x500")
        window.title("Update Student")
        window.configure(fg_color=COLOR_BG)
        set_appearance_mode("dark")

        # -- FONTS -------------------------------------------------
        heading_font = CTkFont(family="Segoe UI", size=24, weight="bold")
        label_font = CTkFont(family="Segoe UI", size=13)
        button_font = CTkFont(family="Segoe UI", size=16, weight="bold")

        # -- HELPER FUNCTIONS ------------------------------------------------
        def find_student(nam, roll):
            nam = nam.get()
            roll = roll.get()
            file = open("Student-Database.csv", 'r', newline="", encoding='utf-8')
            reader = csv.reader(file)
            for students in reader:
                if students[0] == nam and students[1] == roll:
                    print("Student Found!")
                    tmsg.showinfo("Success", "Student Found in the database", parent=window)
                    show_append_page(nam, roll, students[4], students[2], students[3])
                    file.close()
                    return
            file.close()
            tmsg.showerror("Error", "Student not found in the database", parent=window)

        def show_append_page(nam, rol, per, clas, sec):
            all_widgets = window.winfo_children()
            for widgets in all_widgets:
                widgets.destroy()

            # New header
            header_frame = CTkFrame(window, fg_color=COLOR_SECONDARY, corner_radius=0, height=70)
            header_frame.pack(fill=X, padx=0, pady=0)

            CTkLabel(
                header_frame,
                text="✏️ Update Student Information",
                font=heading_font,
                text_color=COLOR_TEXT
            ).pack(pady=15)

            content_frame = CTkScrollableFrame(
                window,
                fg_color=COLOR_BG,
                bg_color="transparent"
            )
            content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

            CTkLabel(content_frame, text="Student's Name", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
            Name = CTkEntry(
                content_frame,
                placeholder_text=f"{nam}",
                height=45,
                border_width=2,
                border_color=COLOR_ACCENT,
                fg_color=COLOR_SECONDARY,
                text_color=COLOR_TEXT,
                corner_radius=8
            )
            Name.pack(pady=(0, 15), fill=X)

            CTkLabel(content_frame, text="Student's Roll", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
            Roll = CTkEntry(
                content_frame,
                placeholder_text=f"{rol}",
                height=45,
                border_width=2,
                border_color=COLOR_ACCENT,
                fg_color=COLOR_SECONDARY,
                text_color=COLOR_TEXT,
                corner_radius=8
            )
            Roll.pack(pady=(0, 15), fill=X)

            class_section_frame = CTkFrame(content_frame, fg_color="transparent")
            class_section_frame.pack(fill=X, pady=(0, 15))

            CTkLabel(class_section_frame, text="Class", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
            Class = CTkEntry(
                class_section_frame,
                placeholder_text=f"{clas}",
                height=45,
                border_width=2,
                border_color=COLOR_ACCENT,
                fg_color=COLOR_SECONDARY,
                text_color=COLOR_TEXT,
                corner_radius=8
            )
            Class.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

            CTkLabel(class_section_frame, text="Section", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
            Section = CTkEntry(
                class_section_frame,
                placeholder_text=f"{sec}",
                height=45,
                border_width=2,
                border_color=COLOR_ACCENT,
                fg_color=COLOR_SECONDARY,
                text_color=COLOR_TEXT,
                corner_radius=8
            )
            Section.pack(side=LEFT, fill=BOTH, expand=True)

            CTkLabel(content_frame, text="Last Year Percentage", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
            Percentage = CTkEntry(
                content_frame,
                placeholder_text=f"{per}",
                height=45,
                border_width=2,
                border_color=COLOR_ACCENT,
                fg_color=COLOR_SECONDARY,
                text_color=COLOR_TEXT,
                corner_radius=8
            )
            Percentage.pack(pady=(0, 30), fill=X)

            updated_lst = [Name, Roll, Class, Section, Percentage]
            old_lst = [nam, rol, clas, sec, per]
            
            CTkButton(
                content_frame,
                text="✓ Save Changes",
                font=button_font,
                fg_color=COLOR_SUCCESS,
                text_color="white",
                hover_color=self._lighten_color(COLOR_SUCCESS),
                command=lambda: insert_details(old_lst, updated_lst),
                height=50,
                corner_radius=10
            ).pack(pady=(0, 15), fill=X)

        def insert_details(old, new):
            with open("Student-Database.csv", 'a', newline="") as file:
                writer = csv.writer(file)
                if new[0].get() != "":
                    old[0] = new[0].get()
                if new[1].get() != "":
                    old[1] = new[1].get()
                if new[2].get() != "":
                    old[2] = new[2].get()
                if new[3].get() != "":
                    old[3] = new[3].get()
                if new[4].get() != "":
                    old[4] = new[4].get()
                writer.writerow(old)
                tmsg.showinfo("Success", "Student Updated in the Database", parent=window)
                window.destroy()

        # -- MAIN CONTENT -----------------------------------------------------------------
        header_frame = CTkFrame(window, fg_color=COLOR_SECONDARY, corner_radius=0, height=70)
        header_frame.pack(fill=X, padx=0, pady=0)

        CTkLabel(
            header_frame,
            text="✏️ Update Student",
            font=heading_font,
            text_color=COLOR_TEXT
        ).pack(pady=15)

        content_frame = CTkScrollableFrame(
            window,
            fg_color=COLOR_BG,
            bg_color="transparent"
        )
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        CTkLabel(content_frame, text="Student's Name", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
        Name = CTkEntry(
            content_frame,
            placeholder_text="eg. Avinash Kumar",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Name.pack(pady=(0, 15), fill=X)

        CTkLabel(content_frame, text="Student's Roll Number", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Roll = CTkEntry(
            content_frame,
            placeholder_text="eg. 120XX",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Roll.pack(pady=(0, 30), fill=X)

        CTkButton(
            content_frame,
            text="🔍 Find Student",
            font=button_font,
            fg_color=COLOR_ACCENT,
            text_color="white",
            hover_color=self._lighten_color(COLOR_ACCENT),
            command=lambda: find_student(Name, Roll),
            height=50,
            corner_radius=10
        ).pack(pady=(0, 15), fill=X)

    def Delete_Student(self):
        """Delete a student record"""
        print("Delete a Student Called")
        window = CTkToplevel(self)
        window.geometry("550x450")
        window.title("Delete Student")
        window.configure(fg_color=COLOR_BG)
        set_appearance_mode("dark")

        # -- FONTS -------------------------------------------------------------------
        heading_font = CTkFont(family="Segoe UI", size=24, weight="bold")
        label_font = CTkFont(family="Segoe UI", size=13)
        button_font = CTkFont(family="Segoe UI", size=16, weight="bold")

        # -- HELPER FUNCTIONS -----------------------------------------------------------
        def delete_student(nam, rol):
            nam = nam.get()
            rol = rol.get()
            rows = []
            found = False
            
            with open("Student-Database.csv", 'r', newline="", encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] == nam and row[1] == rol:
                        found = True
                    else:
                        rows.append(row)

            if found:
                with open("Student-Database.csv", 'w', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                tmsg.showinfo("Success", f"The Student: {nam} Successfully deleted", parent=window)
                window.destroy()
            else:
                tmsg.showerror("Error", "Student not found", parent=window)

        # -- HEADER ----------------------------------------------------------------
        header_frame = CTkFrame(window, fg_color=COLOR_SECONDARY, corner_radius=0, height=70)
        header_frame.pack(fill=X, padx=0, pady=0)

        CTkLabel(
            header_frame,
            text="🗑️ Delete Student",
            font=heading_font,
            text_color=COLOR_TEXT
        ).pack(pady=15)

        # -- MAIN CONTENT -----------------------------------------------------------
        content_frame = CTkScrollableFrame(
            window,
            fg_color=COLOR_BG,
            bg_color="transparent"
        )
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Warning message
        warning_frame = CTkFrame(
            content_frame,
            fg_color=COLOR_SECONDARY,
            corner_radius=8,
            border_width=2,
            border_color=COLOR_DANGER
        )
        warning_frame.pack(pady=(0, 20), fill=X)

        CTkLabel(
            warning_frame,
            text="⚠️  This action cannot be undone",
            font=CTkFont(family="Segoe UI", size=12),
            text_color=COLOR_DANGER
        ).pack(pady=10)

        CTkLabel(content_frame, text="Student's Name", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
        Name = CTkEntry(
            content_frame,
            placeholder_text="eg. Avinash Kumar",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Name.pack(pady=(0, 15), fill=X)

        CTkLabel(content_frame, text="Student's Roll Number", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Roll = CTkEntry(
            content_frame,
            placeholder_text="eg. 120XX",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Roll.pack(pady=(0, 30), fill=X)

        CTkButton(
            content_frame,
            text="🗑️ Delete Student",
            font=button_font,
            fg_color=COLOR_DANGER,
            text_color="white",
            hover_color=self._lighten_color(COLOR_DANGER),
            command=lambda: delete_student(Name, Roll),
            height=50,
            corner_radius=10
        ).pack(pady=(0, 15), fill=X)

    def Search_Student(self):
        """Search for a student"""
        print("Search Student Called")
        window = CTkToplevel(self)
        window.geometry("550x450")
        window.title("Search Student")
        window.configure(fg_color=COLOR_BG)
        set_appearance_mode("dark")

        # -- FONTS -------------------------------------------------------------------
        heading_font = CTkFont(family="Segoe UI", size=24, weight="bold")
        label_font = CTkFont(family="Segoe UI", size=13)
        button_font = CTkFont(family="Segoe UI", size=16, weight="bold")

        # -- HELPER FUNCTIONS -----------------------------------------------------------
        def search_student(nam, roll):
            nam = nam.get()
            roll = roll.get()
            file = open("Student-Database.csv", 'r', newline="", encoding='utf-8')
            reader = csv.reader(file)
            for students in reader:
                if students[0] == nam and students[1] == roll:
                    print("Student Found!")
                    tmsg.showinfo("Success", "Student Found in the database", parent=window)
                    file.close()
                    return
            file.close()
            tmsg.showerror("Not Found", "Student not found in the database", parent=window)

        # -- HEADER ----------------------------------------------------------------
        header_frame = CTkFrame(window, fg_color=COLOR_SECONDARY, corner_radius=0, height=70)
        header_frame.pack(fill=X, padx=0, pady=0)

        CTkLabel(
            header_frame,
            text="🔍 Search Student",
            font=heading_font,
            text_color=COLOR_TEXT
        ).pack(pady=15)

        # -- MAIN CONTENT -----------------------------------------------------------
        content_frame = CTkScrollableFrame(
            window,
            fg_color=COLOR_BG,
            bg_color="transparent"
        )
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        CTkLabel(content_frame, text="Student's Name", font=label_font, text_color=COLOR_TEXT).pack(pady=(15, 5), anchor="w")
        Name = CTkEntry(
            content_frame,
            placeholder_text="eg. Avinash Kumar",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Name.pack(pady=(0, 15), fill=X)

        CTkLabel(content_frame, text="Student's Roll Number", font=label_font, text_color=COLOR_TEXT).pack(pady=(0, 5), anchor="w")
        Roll = CTkEntry(
            content_frame,
            placeholder_text="eg. 120XX",
            height=45,
            border_width=2,
            border_color=COLOR_ACCENT,
            fg_color=COLOR_SECONDARY,
            text_color=COLOR_TEXT,
            corner_radius=8
        )
        Roll.pack(pady=(0, 30), fill=X)

        CTkButton(
            content_frame,
            text="🔍 Search Student",
            font=button_font,
            fg_color=COLOR_WARNING,
            text_color="white",
            hover_color=self._lighten_color(COLOR_WARNING),
            command=lambda: search_student(Name, Roll),
            height=50,
            corner_radius=10
        ).pack(pady=(0, 15), fill=X)

    def Quit_App(self):
        """Close the application"""
        print("App Closed")
        self.destroy()


if __name__ == "__main__":
    app = Student_App()
    app.HomePage()
    app.mainloop()
