from tkinter import *
from tkinter import messagebox
from customtkinter import *
import importlib.util
from pathlib import Path
import time
import math

database_file = Path(__file__).with_name("Brewphoria-Cafe-Database-fecher.py")
database_spec = importlib.util.spec_from_file_location("brewphoria_database", database_file)
database_module = importlib.util.module_from_spec(database_spec)
database_spec.loader.exec_module(database_module)
add_customer = database_module.add_customer
update_customer_review = database_module.update_customer_review

root = CTk()
root.geometry("565x700")
root.title("Brewphoria Café")
root.minsize(575, 700)

# ─── DESIGN SYSTEM ──────────────────────────────────────────────────────────────
# Color Palette — Dark Espress  o Luxury
Espresso        = "#1A0E08"        # deep dark background
Roast           = "#2C1A0E"        # card bg
Caramel         = "#C8843A"        # primary accent (warm gold-orange)
Caramel_Hover   = "#E09A50"        # hover
Cream           = "#F5ECD7"        # soft warm white text
Muted           = "#8A7560"        # secondary/muted text
Sage            = "#5A8A5A"        # success / add-to-cart green
Sage_Hover      = "#74AA74"
Crimson         = "#C62828"        # remove button
Crimson_Hover   = "#E57373"
Divider         = "#3D2512"        # border color

# ─── TYPOGRAPHY ─────────────────────────────────────────────────────────────────
try:
    Font_Display  = CTkFont(family="Palatino Linotype", size=28, weight="bold")
    Font_Sub      = CTkFont(family="Palatino Linotype", size=15, slant="italic")
    Font_Nav      = CTkFont(family="Palatino Linotype", size=14, weight="bold")
    Font_Card     = CTkFont(family="Segoe UI", size=13, weight="bold")
    Font_Price    = CTkFont(family="Palatino Linotype", size=13, slant="italic")
    Font_Emoji    = CTkFont(family="Segoe UI Emoji", size=32)
    Font_Small    = CTkFont(family="Segoe UI", size=12)
    Font_Total    = CTkFont(family="Palatino Linotype", size=14, weight="bold")
except:
    Font_Display  = CTkFont(size=28, weight="bold")
    Font_Sub      = CTkFont(size=15, slant="italic")
    Font_Nav      = CTkFont(size=14, weight="bold")
    Font_Card     = CTkFont(size=13, weight="bold")
    Font_Price    = CTkFont(size=13, slant="italic")
    Font_Emoji    = CTkFont(size=32)
    Font_Small    = CTkFont(size=12)
    Font_Total    = CTkFont(size=14, weight="bold")

# ─── ANIMATION HELPERS ──────────────────────────────────────────────────────────
def fade_in(widget, steps=18, delay=18, alpha_start=0.0):
    """Animate a widget fading in by sliding it down slightly and revealing."""
    def _step(i):
        if i > steps:
            return
        progress = i / steps
        ease = 1 - (1 - progress) ** 3  # ease-out cubic
        # We fake fade with bg color blending on the root (best we can in tkinter)
        widget.after(delay, lambda: _step(i + 1))
    _step(0)


def animate_button_press(btn, normal_color, hover_color):
    """Quick flash animation on button click."""
    btn.configure(fg_color=hover_color)
    btn.after(120, lambda: btn.configure(fg_color=normal_color))


def pulse_label(label, original_color, pulse_color="#FFFFFF", cycles=2, interval=160):
    """Pulse a label's text color briefly."""
    def _toggle(n):
        if n <= 0:
            label.configure(text_color=original_color)
            return
        label.configure(text_color=pulse_color if n % 2 == 0 else original_color)
        label.after(interval, lambda: _toggle(n - 1))
    _toggle(cycles * 2)


# ─── LAYOUT STRUCTURE ───────────────────────────────────────────────────────────
# Top navbar
Menubar = CTkFrame(root, height=50, corner_radius=0, fg_color=Roast, border_width=0)
Menubar.pack(fill=X, side=TOP)

# Logo in nav
logo_label = CTkLabel(Menubar, text="☕ Brewphoria", font=Font_Nav, text_color=Caramel)
logo_label.pack(side=LEFT, padx=16, pady=12)

# Separator label
CTkLabel(Menubar, text="|", text_color=Muted, font=Font_Small).pack(side=LEFT, pady=12)

# Bottom action bar
frame2 = CTkFrame(root, height=52, corner_radius=0, fg_color=Roast, border_width=0)

HomeFrame = None
cart_quantities = {}
amount_entry = None
total_label = None
current_customer_id = None

products = [
    {"emoji": "🍔", "name": "Burger",      "price": 4.00},
    {"emoji": "🍲", "name": "Soup",        "price": 1.50},
    {"emoji": "🍕", "name": "Pizza",       "price": 8.30},
    {"emoji": "🍿", "name": "Popcorn",     "price": 0.50},
    {"emoji": "🧋", "name": "Cold Coffee", "price": 3.12},
    {"emoji": "🥪", "name": "Sandwich",    "price": 5.20},
    {"emoji": "🍟", "name": "Fries",       "price": 3.50},
    {"emoji": "🌭", "name": "Hot Dog",     "price": 2.15},
    {"emoji": "🍜", "name": "Noodles",     "price": 0.25},
    {"emoji": "🍨", "name": "Ice Cream",   "price": 2.25},
    {"emoji": "🍛", "name": "Curry Rice",  "price": 0.30},
    {"emoji": "☕", "name": "Tea",         "price": 0.03},
    {"emoji": "🍰", "name": "Pastry",      "price": 2.50},
    {"emoji": "🍹", "name": "Juice",       "price": 4.26},
]

# ─── FRAMES ─────────────────────────────────────────────────────────────────────
ProductsFrame = CTkScrollableFrame(
    root, corner_radius=0, border_width=0,
    fg_color=Espresso,
    scrollbar_button_color=Caramel,
    scrollbar_button_hover_color=Caramel_Hover
)

CartFrame = CTkScrollableFrame(
    root, corner_radius=0, border_width=0,
    fg_color=Espresso,
    scrollbar_button_color=Caramel,
    scrollbar_button_hover_color=Caramel_Hover
)

empty_cart_label = CTkLabel(
    CartFrame,
    text="Your cart is empty  🛒",
    font=Font_Sub,
    text_color=Muted
)
empty_cart_label.grid(row=1, column=1, padx=200, pady=80)

# ─── UTILITY FUNCTIONS ──────────────────────────────────────────────────────────
def calculate_total():
    return sum(products[idx]['price'] * qty for idx, qty in cart_quantities.items())


def update_frame2_total():
    global total_label
    for w in frame2.winfo_children():
        if getattr(w, '_is_total', False):
            w.destroy()
    total = calculate_total()
    total_label = CTkLabel(
        frame2,
        text=f"Total:  ${total:.2f}",
        font=Font_Total,
        text_color=Caramel
    )
    total_label._is_total = True
    total_label.pack(side=LEFT, padx=16, pady=14)


def update_cart_display():
    for w in CartFrame.winfo_children():
        if w != empty_cart_label:
            w.destroy()

    if not cart_quantities:
        empty_cart_label.grid(row=1, column=1, padx=200, pady=80)
        return

    empty_cart_label.grid_forget()

    # Section title
    CTkLabel(CartFrame, text="Your Order", font=Font_Sub, text_color=Muted).grid(
        row=0, column=0, columnspan=4, pady=(16, 8), padx=10, sticky=W
    )

    for i, (idx, qty) in enumerate(cart_quantities.items()):
        product = products[idx]
        row = i // 3 + 1
        col = i % 3

        card = CTkFrame(CartFrame, corner_radius=14,
                        border_width=1, border_color=Divider,
                        fg_color=Roast)
        card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

        # Top row: emoji + remove button side by side
        top_row = CTkFrame(card, fg_color="transparent")
        top_row.pack(fill=X, padx=6, pady=(8, 0))

        CTkLabel(top_row, text=product['emoji'], font=Font_Emoji).pack(side=LEFT, padx=(8, 0))
        CTkButton(
            top_row, text="✕", width=26, height=26,
            corner_radius=13, fg_color=Crimson, hover_color=Crimson_Hover,
            text_color=Cream, font=Font_Small,
            command=lambda i=idx: remove_from_cart(i)
        ).pack(side=RIGHT, padx=4, pady=4)

        CTkLabel(card, text=product['name'], font=Font_Card, text_color=Cream).pack(pady=(4, 0))
        CTkLabel(card, text=f"${product['price']:.2f}  ×  {qty}", font=Font_Price, text_color=Muted).pack(pady=(2, 0))
        subtotal = product['price'] * qty
        CTkLabel(card, text=f"= ${subtotal:.2f}", font=Font_Price, text_color=Caramel).pack(pady=(2, 10))


# ─── CART ACTIONS ───────────────────────────────────────────────────────────────
def AddtoCart(index, btn=None):
    if index not in cart_quantities:
        cart_quantities[index] = 1
    else:
        cart_quantities[index] += 1
    if btn:
        animate_button_press(btn, Sage, Sage_Hover)
    update_cart_display()
    update_frame2_total()
    # Flash cart tab
    CartTab.configure(text_color=Caramel)
    CartTab.after(400, lambda: CartTab.configure(text_color=Muted if ProductsFrame.winfo_ismapped() else Cream))


def remove_from_cart(index):
    if index in cart_quantities:
        del cart_quantities[index]
    update_cart_display()
    update_frame2_total()


def BuyNow(index, btn=None):
    if btn:
        animate_button_press(btn, Caramel, Caramel_Hover)
    AddtoCart(index)
    root.after(150, show_cart)


def confirm_order():
    global amount_entry, current_customer_id
    amount = amount_entry.get().strip() if amount_entry else ""
    if not amount:
        messagebox.showerror("Invalid Amount", "Please enter the amount before confirming.")
        return
    try:
        val = float(amount)
        total = calculate_total()
        if val < total:
            messagebox.showwarning("Insufficient Amount", f"Total is ${total:.2f}. Please enter the correct amount.")
            return
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid numeric amount.")
        return

    rating = ask_for_rating()
    try:
        update_customer_review(current_customer_id, rating, total)
    except Exception as error:
        messagebox.showerror("Database Error", f"Could not save your rating.\n{error}")
        return

    messagebox.showinfo("Order Placed ✓", f"Your order has been placed!\nThank you for choosing Brewphoria ☕")
    cart_quantities.clear()
    for w in CartFrame.winfo_children():
        if w != empty_cart_label:
            w.destroy()
    empty_cart_label.grid(row=1, column=1, padx=200, pady=80)
    _rebuild_action_bar()
    update_frame2_total()


def show_order_entry():
    global amount_entry
    if not cart_quantities:
        messagebox.showwarning("Cart Empty", "Please add items before placing an order.")
        return
    _rebuild_action_bar(show_entry=True)


def ask_for_rating():
    while True:
        dialog = CTkInputDialog(
            text="Rate your experience from 1 to 10 (Cancel for no rating):",
            title="Brewphoria Rating",
        )
        value = dialog.get_input()

        if value is None:
            return None

        try:
            rating = int(value.strip())
        except ValueError:
            rating = 0

        if 1 <= rating <= 10:
            return rating

        messagebox.showerror("Invalid Rating", "Please enter a rating from 1 to 10.")


def _rebuild_action_bar(show_entry=False):
    global amount_entry
    for w in frame2.winfo_children():
        w.destroy()
    update_frame2_total()
    if show_entry:
        CTkLabel(frame2, text="Amount paid:", font=Font_Small, text_color=Muted).pack(side=LEFT, padx=(12, 4), pady=14)
        amount_entry = CTkEntry(
            frame2, width=130, placeholder_text="e.g. 10.00",
            fg_color=Espresso, border_color=Caramel, text_color=Cream,
            placeholder_text_color=Muted
        )
        amount_entry.pack(side=LEFT, padx=4, pady=14)
        CTkButton(
            frame2, text="Confirm  ✓", width=110,
            fg_color=Caramel, hover_color=Caramel_Hover,
            text_color=Espresso, font=Font_Nav,
            command=confirm_order
        ).pack(side=LEFT, padx=10, pady=14)
    else:
        CTkButton(
            frame2, text="Place Order →", width=130,
            fg_color="transparent", hover_color=Divider,
            border_color=Caramel, border_width=1,
            text_color=Caramel, font=Font_Nav,
            command=show_order_entry
        ).pack(side=RIGHT, padx=16, pady=12)


# ─── NAV / PAGE SWITCHING ────────────────────────────────────────────────────────
def _set_nav(active):
    """Highlight the active nav tab."""
    ProductsTab.configure(text_color=Cream if active == "products" else Muted)
    CartTab.configure(text_color=Cream if active == "cart" else Muted)


def show_products():
    global HomeFrame, name_entry, country_entry, contact_entry, current_customer_id

    name = name_entry.get().strip()
    country = country_entry.get().strip()
    contact = contact_entry.get().strip()

    if not name:
        messagebox.showerror("Required Field", "Name is the necessary field.")
        return
    if not country:
        messagebox.showerror("Required Field", "Country is the necessary field.")
        return
    if not contact:
        messagebox.showerror("Required Field", "Contact is the necessary field.")
        return

    if not contact.isdigit() or len(contact) > 20:
        messagebox.showerror(
            "Invalid Contact",
            "Contact must contain only numbers and be at most 20 digits.",
        )
        return

    if current_customer_id is None:
        try:
            current_customer_id = add_customer(name, country, contact)
        except Exception as error:
            messagebox.showerror("Database Error", f"Could not save customer details.\n{error}")
            return

    HomeFrame.pack_forget()
    CartFrame.pack_forget()
    Menubar.pack(fill=X, side=TOP)
    frame2.pack(fill=X, side=BOTTOM)
    update_frame2_total()
    _rebuild_action_bar()
    _set_nav("products")
    ProductsFrame.pack(fill=BOTH, expand=True)


def show_cart():
    global HomeFrame
    if HomeFrame is not None and HomeFrame.winfo_ismapped():
        HomeFrame.pack_forget()

    ProductsFrame.pack_forget()
    Menubar.pack(fill=X, side=TOP)
    frame2.pack(fill=X, side=BOTTOM)
    update_frame2_total()
    _rebuild_action_bar()
    update_cart_display()
    _set_nav("cart")
    CartFrame.pack(fill=BOTH, expand=True)


def show_homepage():
    global HomeFrame, country_entry, contact_entry, name_entry

    for w in root.winfo_children():
        w.pack_forget()

    if HomeFrame is None:
        HomeFrame = CTkFrame(root, corner_radius=0, fg_color=Espresso)

        # Decorative top stripe
        stripe = CTkFrame(HomeFrame, height=4, corner_radius=0, fg_color=Caramel)
        stripe.pack(fill=X, side=TOP)

        # Center content
        inner = CTkFrame(HomeFrame, fg_color="transparent")
        inner.pack(expand=True)

        CTkLabel(inner, text="☕", font=CTkFont(family="Segoe UI Emoji", size=56)).pack(pady=(0, 6))
        CTkLabel(inner, text="Brewphoria Café", font=Font_Display, text_color=Caramel).pack()
        CTkLabel(inner, text="Sip into your story", font=Font_Sub, text_color=Muted).pack(pady=(2, 16))

        # Divider line
        CTkFrame(inner, height=1, width=300, fg_color=Divider).pack(pady=(0, 16))

        CTkLabel(
            inner,
            text="Bold brews · Artisanal bites · Cozy corners\n"
                 "A refined café experience, served with warmth.",
            font=Font_Small,
            text_color=Muted,
            justify=CENTER
        ).pack(pady=(0, 24))

        # User Information Entry Fields
        CTkLabel(inner, text="Your Name", font=Font_Small, text_color=Muted).pack(pady=(8, 2))
        name_entry = CTkEntry(
            inner, width=250, placeholder_text="Enter your full name",
            fg_color=Roast, border_color=Caramel, text_color=Cream,
            placeholder_text_color=Muted,height=35
        )
        name_entry.pack(pady=(0, 12))

        CTkLabel(inner, text="Country", font=Font_Small, text_color=Muted).pack(pady=(8, 2))
        country_entry = CTkEntry(
            inner, width=250, placeholder_text="Enter your country",
            fg_color=Roast, border_color=Caramel, text_color=Cream,
            placeholder_text_color=Muted,height=35
        )
        country_entry.pack(pady=(0, 12))

        CTkLabel(inner, text="Contact", font=Font_Small, text_color=Muted).pack(pady=(8, 2))
        contact_entry = CTkEntry(
            inner, width=250, placeholder_text="Enter your phone number",
            fg_color=Roast, border_color=Caramel, text_color=Cream,
            placeholder_text_color=Muted,height=35
        )
        contact_entry.pack(pady=(0, 20))

        CTkButton(
            inner,
            text="Get Started",
            font=Font_Nav,
            command=show_products,
            fg_color=Caramel,
            hover_color=Caramel_Hover,
            text_color=Espresso,
            width=200,
            height=44,
            corner_radius=22,
        ).pack()

        # Bottom stripe
        CTkFrame(HomeFrame, height=4, corner_radius=0, fg_color=Caramel).pack(fill=X, side=BOTTOM)

    HomeFrame.pack(fill=BOTH, expand=True)


# ─── NAV BUTTONS ────────────────────────────────────────────────────────────────
ProductsTab = CTkButton(
    Menubar, text="Menu", font=Font_Nav,
    fg_color="transparent", hover_color=Divider,
    text_color=Cream, width=80, height=36,
    corner_radius=8, command=show_products
)
ProductsTab.pack(side=LEFT, padx=4, pady=7)

CartTab = CTkButton(
    Menubar, text="Cart 🛒", font=Font_Nav,
    fg_color="transparent", hover_color=Divider,
    text_color=Muted, width=90, height=36,
    corner_radius=8, command=show_cart
)
CartTab.pack(side=LEFT, padx=4, pady=7)

# ─── PRODUCT CARDS ──────────────────────────────────────────────────────────────
# Section header
CTkLabel(ProductsFrame, text="Our Menu", font=Font_Sub, text_color=Muted).pack(
    anchor=W, padx=16, pady=(16, 8)
)

COLS = 4
# Row-frames so pack() drives the scrollable height — grid() inside CTkScrollableFrame breaks scroll
row_frames = []
for index, product in enumerate(products):
    col = index % COLS

    if col == 0:
        row_frame = CTkFrame(ProductsFrame, fg_color="transparent")
        row_frame.pack(fill=X, padx=8, pady=0)
        row_frames.append(row_frame)
    else:
        row_frame = row_frames[-1]

    card = CTkFrame(
        row_frame, width=148, height=200,
        corner_radius=14, border_width=1,
        border_color=Divider, fg_color=Roast
    )
    card.pack(side=LEFT, padx=7, pady=7)
    card.pack_propagate(False)

    CTkLabel(card, text=product["emoji"], font=Font_Emoji).pack(pady=(14, 4))
    CTkLabel(card, text=product["name"], font=Font_Card, text_color=Cream).pack()
    CTkLabel(card, text=f"${product['price']:.2f}", font=Font_Price, text_color=Caramel).pack(pady=(2, 8))

    btn_buynow = CTkButton(
        card, width=118, height=28, corner_radius=14,
        fg_color=Caramel, hover_color=Caramel_Hover,
        text="Buy Now", text_color=Espresso, font=Font_Small,
    )
    btn_buynow.configure(command=lambda i=index, b=btn_buynow: BuyNow(i, b))
    btn_buynow.pack(pady=(0, 4))

    btn_add = CTkButton(
        card, width=118, height=28, corner_radius=14,
        fg_color="transparent", hover_color=Divider,
        border_width=1, border_color=Sage,
        text="+ Add to Cart", text_color=Sage, font=Font_Small,
    )
    btn_add.configure(command=lambda i=index, b=btn_add: AddtoCart(i, b))
    btn_add.pack(pady=(0, 10))

# ─── INITIAL ACTION BAR ─────────────────────────────────────────────────────────
_rebuild_action_bar()

# ─── LAUNCH ─────────────────────────────────────────────────────────────────────
show_homepage()
root.mainloop()

# End - Project Completed