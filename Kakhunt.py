import tkinter as tk

import subprocess

from tkinter import messagebox

from tkinter import filedialog



class Application(tk.Frame):

    

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master

        self.master.title("KAK- Ravaan*(Private Tool- MADE BY RAVAAN:))")

        self.pack()

        self.create_widgets()

        self.generated_urls = ''

        self.original_urls = ''



        # Set window properties

        self.master.resizable(width=False, height=False)

        self.master.attributes('-fullscreen', False)



    def create_widgets(self):

        # Create a frame for the URL input

        url_frame = tk.Frame(self)

        url_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)



        url_label = tk.Label(url_frame, text="Enter URL:")

        url_label.pack(side=tk.LEFT, padx=5)



        self.url_entry = tk.Entry(url_frame)

        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)



        # Create a button to show instructions

        instr_button = tk.Button(self, text="How to use", bg="orange", command=self.show_instructions)

        instr_button.pack(side=tk.TOP, padx=5, pady=5)



        # Create a frame for the output text

        output_frame = tk.Frame(self)

        output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)



        self.output_text = tk.Text(output_frame)

        self.output_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



        # Create a button to run the tool

        run_button = tk.Button(self, text="Run Waybackurls", bg="red", command=self.run_waybackurls)

        self.url_entry.bind("<Return>", lambda event: self.run_waybackurls())

        run_button.pack(side=tk.TOP, padx=5, pady=5)



        # Create buttons to filter by file extension

        self.extensions = ['.js', '.py', '.mysql', '.env', '.json', '.db', '.pem', '.bak', '.php', '.xml', '.yml', '.yaml', '.txt', '.png', '.jpg', '.mp4', '.gz', '.log', '.env', '.html', '.cfg', '.php', '.sh', '.pdf', '.xls', '.config', '.csv', '.sqlite', '.sql', '.tmp']

        self.filter_buttons = []

        for extension in self.extensions:

            button = tk.Button(self, text=f"{extension}", command=lambda ext=extension: self.filter_output(ext))

            button.pack(side=tk.LEFT, padx=2, pady=2)

            self.filter_buttons.append(button)



        # Create an Export button

        export_button = tk.Button(self, text="Export", command=self.export_output, bg="green")

        export_button.pack(side=tk.TOP, padx=5, pady=5)



    def show_instructions(self):

        instructions = "This Tool uses waybackurls by Tomnomnom as a engine and Filters Ravaan uses for WAPT. Simply Enter the Url in the Enter URL: https://foo.com, Next you can apply filter and Export the URLs"

        messagebox.showinfo("Instructions", instructions)



    



    def run_waybackurls(self):

        self.generated_urls = subprocess.check_output(f"waybackurls {self.url_entry.get()}", shell=True).decode("utf-8")

        self.original_urls = self.generated_urls

        self.output_text.delete("1.0", tk.END)

        self.output_text.insert(tk.END, self.generated_urls)



    def filter_output(self, extension):

        if self.generated_urls == '':

            tk.messagebox.showerror("Error", "Please run the tool first to generate URLs.")

            return



        # Check if the same filter has been applied previously

        if hasattr(self, 'last_filter') and self.last_filter == extension:

            self.generated_urls = self.original_urls

            delattr(self, 'last_filter')

        else:

            # Filter URLs by extension

            filtered_output = ""

            for line in self.original_urls.split("\n"):

                if line.endswith(extension):

                    filtered_output += line + "\n"

            # Check if the filtered output is empty

            if filtered_output == "":

                tk.messagebox.showinfo("Info", f"No URLs found with extension {extension}.")

                return

            self.generated_urls = filtered_output

            self.last_filter = extension



        # Update output text

        self.output_text.delete("1.0", tk.END)

        self.output_text.insert(tk.END, self.generated_urls)



    def export_output(self):

        if self.generated_urls == '':

            messagebox.showerror("Error", "Please run the tool first to generate URLs.")

            return



        filename = filedialog.asksaveasfilename(defaultextension=".txt",

                                                filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

        if filename:

            with open(filename, 'w') as f:

                f.write(self.generated_urls)

            messagebox.showinfo("Success", f"URLs successfully exported to {filename}.")



root = tk.Tk()

app = Application(master=root)

app.mainloop()

