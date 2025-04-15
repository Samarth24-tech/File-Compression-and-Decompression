import tkinter as tk
from tkinter import filedialog, messagebox
from huffman import HuffmanCoding

class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman File Compressor/Decompressor")
        self.root.geometry("400x250")

        self.huffman = HuffmanCoding()

        tk.Label(root, text="Text File Compression using Huffman Coding", font=("Arial", 14), wraplength=350).pack(pady=20)

        tk.Button(root, text="Compress File", command=self.compress_file, width=30).pack(pady=10)
        tk.Button(root, text="Decompress File", command=self.decompress_file, width=30).pack(pady=10)

    def compress_file(self):
        file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        output_path = self.huffman.compress(file_path)
        messagebox.showinfo("Success", f"File compressed and saved as:\n{output_path}")

    def decompress_file(self):
        file_path = filedialog.askopenfilename(title="Select a .bin file", filetypes=[("Binary Files", "*.bin")])
        if not file_path:
            return
        output_path = self.huffman.decompress(file_path)
        messagebox.showinfo("Success", f"File decompressed and saved as:\n{output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanApp(root)
    root.mainloop()
