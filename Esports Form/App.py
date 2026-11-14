import tkinter as tk
import customtkinter as ctk
import mysql.connector as msc
from tkinter import messagebox as msg

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

Window = ctk.CTk()
Window.title("Esports Tournament Registration")
Window.geometry("1080x850")
Window.minsize(900, 760)
Window.configure(fg_color="#0B1120")
Window.grid_columnconfigure(0, weight=1)
Window.grid_rowconfigure(0, weight=1)

Page = ctk.CTkFrame(Window, fg_color="transparent")
Page.grid(row=0, column=0, sticky="nsew", padx=32, pady=28)
Page.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(
    Page,
    text="ESPORTS  /  PLAYER REGISTRATION",
    font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
    text_color="#60A5FA",
).pack(pady=(8, 10))
ctk.CTkLabel(
    Page,
    text="Join the tournament",
    font=ctk.CTkFont(family="Segoe UI", size=34, weight="bold"),
    text_color="#F8FAFC",
).pack()
ctk.CTkLabel(
    Page,
    text="Add your player details below to get started.",
    font=ctk.CTkFont(family="Segoe UI", size=15),
    text_color="#94A3B8",
).pack(pady=(8, 24))

Register_Frame = ctk.CTkFrame(
    Page,
    fg_color="#111C30",
    corner_radius=18,
    border_width=1,
    border_color="#24324A",
)
Register_Frame.pack(fill="x", padx=48, pady=(0, 18))
Register_Frame.grid_columnconfigure(0, weight=1, uniform="fields")
Register_Frame.grid_columnconfigure(1, weight=1, uniform="fields")

ctk.CTkLabel(
    Register_Frame,
    text="Player information",
    font=ctk.CTkFont(family="Segoe UI", size=19, weight="bold"),
    text_color="#F1F5F9",
).grid(row=0, column=0, columnspan=2, sticky="w", padx=30, pady=(26, 20))

connection=msc.connect(host="localhost",database="esports", user="root",password="FaceAttendBy$ahaj")
cursor=connection.cursor()


def add_field(label, row, column, placeholder):
    field = ctk.CTkFrame(Register_Frame, fg_color="transparent")
    field.grid(row=row, column=column, sticky="ew", padx=(30, 14) if column == 0 else (14, 30), pady=10)
    field.grid_columnconfigure(0, weight=1)
    ctk.CTkLabel(
        field,
        text=label,
        font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
        text_color="#CBD5E1",
    ).grid(row=0, column=0, sticky="w", pady=(0, 7))
    entry = ctk.CTkEntry(
        field,
        height=44,
        corner_radius=10,
        fg_color="#0B1425",
        border_color="#33445F",
        text_color="#F8FAFC",
        placeholder_text=placeholder,
        placeholder_text_color="#64748B",
        font=ctk.CTkFont(family="Segoe UI", size=14),
    )
    entry.grid(row=1, column=0, sticky="ew")
    return entry


Name = add_field("FULL NAME", 1, 0, "Enter your name")
Age = add_field("AGE", 1, 1, "Enter your age")

game_field = ctk.CTkFrame(Register_Frame, fg_color="transparent")
game_field.grid(row=2, column=0, sticky="ew", padx=(30, 14), pady=10)
game_field.grid_columnconfigure(0, weight=1)
ctk.CTkLabel(
    game_field,
    text="MAIN GAME",
    font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
    text_color="#CBD5E1",
).grid(row=0, column=0, sticky="w", pady=(0, 7))
Games = ["Select a game", "Valorant", "BGMI", "Free Fire", "Mobile Legends", "Call of Duty", "CSGO"]
Selected_Game = ctk.CTkOptionMenu(
    game_field,
    values=Games,
    height=44,
    corner_radius=10,
    fg_color="#1D4ED8",
    button_color="#2563EB",
    button_hover_color="#1E40AF",
    dropdown_fg_color="#111C30",
    dropdown_hover_color="#1E3A5F",
    text_color="#F8FAFC",
    font=ctk.CTkFont(family="Segoe UI", size=14),
    dropdown_font=ctk.CTkFont(family="Segoe UI", size=14),
)
Selected_Game.grid(row=1, column=0, sticky="ew")

E_mail = add_field("EMAIL ADDRESS", 2, 1, "you@example.com")
In_Game_Name = add_field("IN-GAME NAME", 3, 0, "Your player name")
In_Game_Role = add_field("IN-GAME ROLE", 3, 1, "e.g. Support, Entry")

gender_field = ctk.CTkFrame(Register_Frame, fg_color="transparent")
gender_field.grid(row=4, column=0, columnspan=2, sticky="ew", padx=30, pady=(12, 24))
ctk.CTkLabel(
    gender_field,
    text="GENDER",
    font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
    text_color="#CBD5E1",
).pack(anchor="w", pady=(0, 9))
gender_options = ctk.CTkFrame(gender_field, fg_color="transparent")
gender_options.pack(anchor="w")
Gender = tk.StringVar(value="")
ctk.CTkRadioButton(
    gender_options,
    text="Male",
    variable=Gender,
    value="Male",
    font=ctk.CTkFont(family="Segoe UI", size=14),
    text_color="#E2E8F0",
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    border_color="#64748B",
).pack(side="left", padx=(0, 28))
ctk.CTkRadioButton(
    gender_options,
    text="Female",
    variable=Gender,
    value="Female",
    font=ctk.CTkFont(family="Segoe UI", size=14),
    text_color="#E2E8F0",
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    border_color="#64748B",
).pack(side="left")


def Submit(Name, Age, E_mail,  In_Game_Name, In_Game_Role):
    Name=Name.get()
    Age=Age.get()
    E_mail=E_mail.get()
    In_Game_Name=In_Game_Name.get()
    In_Game_Role=In_Game_Role.get()
    gender = Gender.get() or None
    if Name != "" and Age != "" and gender is not None and E_mail != "" and In_Game_Role != "" and In_Game_Name != "":
        query = """INSERT INTO registerd_players
                   (name, age, e_mail, in_game_name, in_game_role, gender)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (Name, Age, E_mail, In_Game_Name, In_Game_Role, gender))
        connection.commit()

        msg.showinfo("You're Registered", "You are Registered to the Esport Tournament successfully")
        print("Account Details Inserted Successfully")
    else:
        msg.showerror("You're not Registered", "Please attend all the Required Fields!")
        print("Please attend all the Required fields")
    

ctk.CTkButton(
    Page,
    command=lambda: Submit(Name, Age, E_mail, In_Game_Name, In_Game_Role),
    text="Submit registration",
    height=50,
    width=300,
    corner_radius=12,
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
).pack(pady=(0, 12))
ctk.CTkLabel(
    Page,
    text="Please make sure your player details are accurate.",
    font=ctk.CTkFont(family="Segoe UI", size=12),
    text_color="#64748B",
).pack()


Window.mainloop()