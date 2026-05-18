from pathlib import Path
import sqlite3
from tkinter import Tk, ttk, StringVar, IntVar

APP_DIR = Path.cwd()
DB_PATH = APP_DIR / 'pixelharvester.db'
SUBREDDIT_FILE = APP_DIR / 'subreddits' / 'scenic_wallpapers.txt'


class Database:
    def __init__(self, path: Path):
        self.conn = sqlite3.connect(path)
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS downloaded_media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                media_url TEXT UNIQUE,
                subreddit TEXT,
                media_type TEXT,
                aspect_ratio TEXT,
                local_path TEXT,
                pulled_at REAL
            )
        ''')
        self.conn.commit()


class PixelHarvesterGUI:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title('PixelHarvester')
        self.root.geometry('900x600')

        self.sort_mode = StringVar(value='top')
        self.time_filter = StringVar(value='month')
        self.minimum_upvotes = IntVar(value=250)

        self.build_ui()

    def build_ui(self):
        frame = ttk.Frame(self.root, padding=12)
        frame.pack(fill='both', expand=True)

        header = ttk.Label(
            frame,
            text='PixelHarvester - Scenic Wallpaper Collector',
            font=('Segoe UI', 18, 'bold')
        )
        header.pack(anchor='w', pady=(0, 12))

        options = ttk.LabelFrame(frame, text='Scan Options', padding=10)
        options.pack(fill='x')

        ttk.Label(options, text='Sort Mode').grid(row=0, column=0, sticky='w')
        ttk.Combobox(
            options,
            textvariable=self.sort_mode,
            values=['hot', 'new', 'top', 'rising'],
            state='readonly',
            width=15
        ).grid(row=0, column=1, padx=6, pady=4)

        ttk.Label(options, text='Time Filter').grid(row=0, column=2, sticky='w')
        ttk.Combobox(
            options,
            textvariable=self.time_filter,
            values=['day', 'week', 'month', 'year', 'all'],
            state='readonly',
            width=15
        ).grid(row=0, column=3, padx=6, pady=4)

        ttk.Label(options, text='Minimum Upvotes').grid(row=0, column=4, sticky='w')
        ttk.Spinbox(
            options,
            from_=0,
            to=100000,
            textvariable=self.minimum_upvotes,
            width=10
        ).grid(row=0, column=5, padx=6, pady=4)

        subreddits_frame = ttk.LabelFrame(frame, text='Scenic Wallpaper Sources', padding=10)
        subreddits_frame.pack(fill='both', expand=True, pady=12)

        self.subreddit_list = ttk.Treeview(subreddits_frame, columns=('subreddit',), show='headings')
        self.subreddit_list.heading('subreddit', text='Subreddit')
        self.subreddit_list.pack(fill='both', expand=True)

        if SUBREDDIT_FILE.exists():
            for line in SUBREDDIT_FILE.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if line:
                    self.subreddit_list.insert('', 'end', values=(line,))

        controls = ttk.Frame(frame)
        controls.pack(fill='x')

        ttk.Button(controls, text='Start Scan (placeholder)').pack(side='left')
        ttk.Button(controls, text='Wallpaper Rotation (planned)').pack(side='left', padx=8)


def main():
    Database(DB_PATH)
    root = Tk()
    PixelHarvesterGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
