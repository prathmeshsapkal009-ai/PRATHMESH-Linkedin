import tkinter as tk
import qrcode
import os

if not os.path.exists("downloads"):
    os.mkdir("downloads")

def submit_text():
    user_input = entry.get().strip()
    file_name = filename_entry.get().strip()

    if not user_input or not file_name:
        status_var.set("Please enter both text and file name")
        return

    print("You entered:", user_input)

    file_path = f"downloads/{file_name}.png"
    qr = qrcode.QRCode()
    qr.add_data(user_input)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    print(f"QRCode saved as {file_path}")
    listbox.insert(tk.END, f"{file_name}.png → {user_input}")

    entry.delete(0, tk.END)
    filename_entry.delete(0, tk.END)
    entry.focus_set()

    status_var.set(f"QR code '{file_name}.png' generated successfully!")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("420x350")
root.configure(bg="#8dffa0")  

tk.Label(root, text="Enter text for QR:", font=("Arial", 12), bg="#daffe0").pack(pady=(10, 4))
entry = tk.Entry(root, width=35, font=("Arial", 12), bg="#daffe0", fg="#000000")
entry.pack(pady=4)
entry.focus_set()

tk.Label(root, text="Enter file name (without .png):", font=("Arial", 12), bg="#daffe0").pack(pady=(10, 4))
filename_entry = tk.Entry(root, width=35, font=("Arial", 12), bg="#daffe0", fg="#000000")
filename_entry.pack(pady=4)

submit_button = tk.Button(root, text="Generate QR", command=submit_text,
                          font=("Arial", 12), bg="#daffe0", fg="#000000", activebackground="#87cefa")
submit_button.pack(pady=10)

status_var = tk.StringVar(value="Waiting for input...")
tk.Label(root, textvariable=status_var, font=("Arial", 10), bg="#daffe0", fg="#333333").pack(pady=5)

tk.Label(root, text="Generated QR Codes:", font=("Arial", 11, "bold"), bg="#daffe0").pack(pady=(8, 4))
listbox = tk.Listbox(root, width=50, height=8, bg="#daffe0", fg="#000000")
listbox.pack(pady=6)

root.mainloop()