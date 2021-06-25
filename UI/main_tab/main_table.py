from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from db.alchemy import DatabaseHandler


class MainTable(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        # Button widget to hold "SCAN" and "PACK" buttons
        self.button_widget = QWidget()
        self.refresh_button = QPushButton("SCAN")
        self.refresh_button.clicked.connect(self.on_scan_clicked)
        self.pack_button = QPushButton("PACK")
        self.pack_button.clicked.connect(self.on_pack_clicked)
        self.live_pack_text = QLabel("Live Pack Assets")
        self.live_pack_checkbox = QCheckBox()

        self.button_widget.layout = QHBoxLayout(self.button_widget)
        self.button_widget.layout.addWidget(self.refresh_button)
        self.button_widget.layout.addWidget(self.pack_button)
        self.button_widget.layout.addWidget(self.live_pack_text)
        self.button_widget.layout.addWidget(self.live_pack_checkbox)

        # Displays table of assets
        self.asset_table = QTableWidget(50, 5)
        self.asset_table.verticalHeader().setVisible(False)
        self.asset_table.horizontalHeader().setSectionResizeMode(
            QHeaderView(Qt.Orientation.Horizontal).Stretch
        )
        self.asset_table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.asset_table.setHorizontalHeaderLabels(
            ["Asset Name", "Packing Group", "Output Path", "Date Modified", "Status"]
        )
        dbh = DatabaseHandler()
        for i, pg in enumerate(dbh.get_all_packing_groups_ordered()):
            self.asset_table.setItem(i, 0, QTableWidgetItem(pg.Asset.name))
            self.asset_table.setItem(i, 1, QTableWidgetItem(pg.PackingGroup.identifier))
            self.asset_table.setItem(
                i,
                3,
                QTableWidgetItem(pg.PackingGroup.date.strftime("%m/%d/%Y, %H:%M:%S")),
            )
            self.asset_table.setItem(i, 4, QTableWidgetItem(pg.PackingGroup.status))

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.button_widget)
        self.layout.addWidget(self.asset_table)

    def on_scan_clicked(self):
        pass

    def on_pack_clicked(self):
        pass
