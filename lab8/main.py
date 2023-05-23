import sys
from os import getenv

import psycopg2
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication, QTabWidget, QVBoxLayout, QWidget

from database_tab import QDatabaseTab, QDatabaseTabItem
from database_table_widget import QDatabaseTableWidget

load_dotenv()


class MainWindow(QWidget):
    def init(self):
        super().init()
        self._connect_to_db()
        self.setWindowTitle("Schedule")

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)

        self.tabs.addTab(
            QDatabaseTab([QDatabaseTabItem(QDatabaseTableWidget(self.conn, "bot", "subject"))]), "Предметы"
        )

        self.tabs.addTab(
            QDatabaseTab([QDatabaseTabItem(QDatabaseTableWidget(self.conn, "bot", "teacher"))]), "Учителя"
        )

        self.tabs.addTab(
            QDatabaseTab(
                [
                    QDatabaseTabItem(
                        QDatabaseTableWidget(self.conn, "bot", "timetable", f"day={i} ORDER BY week, id"), f"День #{i}"
                    )
                    for i in range(1, 6)
                ]
            ),
            "Расписание",
        )

        self.vbox.addWidget(self.tabs)
        self.setLayout(self.vbox)

    def _connect_to_db(self):
        self.conn = psycopg2.connect(
            database="tgbot_db",
            user="postgres",
            password="152535",
            host="localhost",
            port="5432"
        )
        self.conn.setsession(autocommit=True)
        self.cursor = self.conn.cursor()


def main():
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec())


if name == "main":
    main()