import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline

# Load the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

# Define summarize function
def summarize_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Required", "Please enter text to summarize.")
        return

    try:
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, summary[0]['summary_text'])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Build GUI
root = tk.Tk()
root.title("AI Text Summarizer")
root.geometry("800x600")

tk.Label(root, text="Enter Text:", font=("Helvetica", 12)).pack(pady=5)
input_box = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD)
input_box.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

tk.Button(root, text="Summarize", command=summarize_text, font=("Helvetica", 12)).pack(pady=10)

tk.Label(root, text="Summary:", font=("Helvetica", 12)).pack(pady=5)
output_box = scrolledtext.ScrolledText(root, height=8, wrap=tk.WORD)
output_box.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

root.mainloop()
