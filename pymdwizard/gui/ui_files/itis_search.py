# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itis_search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ItisSearchWidget(object):
    def setupUi(self, ItisSearchWidget):
        ItisSearchWidget.setObjectName(_fromUtf8("ItisSearchWidget"))
        ItisSearchWidget.resize(1010, 608)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ItisSearchWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(ItisSearchWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtGui.QFrame.Box)
        self.splitter.setFrameShadow(QtGui.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 5, 5, 7)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_search_term = QtGui.QLabel(self.widget)
        self.label_search_term.setObjectName(_fromUtf8("label_search_term"))
        self.horizontalLayout.addWidget(self.label_search_term)
        self.search_term = QtGui.QLineEdit(self.widget)
        self.search_term.setObjectName(_fromUtf8("search_term"))
        self.horizontalLayout.addWidget(self.search_term)
        self.button_search = QtGui.QPushButton(self.widget)
        self.button_search.setObjectName(_fromUtf8("button_search"))
        self.horizontalLayout.addWidget(self.button_search)
        self.label_search_type = QtGui.QLabel(self.widget)
        self.label_search_type.setAccessibleName(_fromUtf8(""))
        self.label_search_type.setObjectName(_fromUtf8("label_search_type"))
        self.horizontalLayout.addWidget(self.label_search_type)
        self.combo_search_type = QtGui.QComboBox(self.widget)
        self.combo_search_type.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.combo_search_type.setObjectName(_fromUtf8("combo_search_type"))
        self.combo_search_type.addItem(_fromUtf8(""))
        self.combo_search_type.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.combo_search_type)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_search_results = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_search_results.setFont(font)
        self.label_search_results.setObjectName(_fromUtf8("label_search_results"))
        self.horizontalLayout_6.addWidget(self.label_search_results)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.table_results = QtGui.QTableView(self.widget)
        self.table_results.setLineWidth(1)
        self.table_results.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_results.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_results.setSortingEnabled(True)
        self.table_results.setObjectName(_fromUtf8("table_results"))
        self.table_results.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_results)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_add_taxon = QtGui.QPushButton(self.widget)
        self.button_add_taxon.setObjectName(_fromUtf8("button_add_taxon"))
        self.horizontalLayout_2.addWidget(self.button_add_taxon)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.layout_include = QtGui.QVBoxLayout(self.horizontalLayoutWidget)
        self.layout_include.setContentsMargins(0, -1, -1, 0)
        self.layout_include.setSpacing(0)
        self.layout_include.setObjectName(_fromUtf8("layout_include"))
        self.frame_include = QtGui.QFrame(self.horizontalLayoutWidget)
        self.frame_include.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_include.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_include.setObjectName(_fromUtf8("frame_include"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_include)
        self.verticalLayout_6.setMargin(2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.layout_include2 = QtGui.QVBoxLayout()
        self.layout_include2.setSpacing(0)
        self.layout_include2.setObjectName(_fromUtf8("layout_include2"))
        self.label_include_item = QtGui.QLabel(self.frame_include)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_include_item.setFont(font)
        self.label_include_item.setObjectName(_fromUtf8("label_include_item"))
        self.layout_include2.addWidget(self.label_include_item)
        self.table_include = QtGui.QTableView(self.frame_include)
        self.table_include.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.table_include.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_include.setSortingEnabled(True)
        self.table_include.setObjectName(_fromUtf8("table_include"))
        self.table_include.verticalHeader().setVisible(False)
        self.layout_include2.addWidget(self.table_include)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.button_remove_selected = QtGui.QPushButton(self.frame_include)
        self.button_remove_selected.setObjectName(_fromUtf8("button_remove_selected"))
        self.horizontalLayout_7.addWidget(self.button_remove_selected)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.layout_include2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.layout_include2)
        self.layout_include.addWidget(self.frame_include)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.button_gen_fgdc = QtGui.QPushButton(ItisSearchWidget)
        self.button_gen_fgdc.setObjectName(_fromUtf8("button_gen_fgdc"))
        self.horizontalLayout_3.addWidget(self.button_gen_fgdc)
        self.check_include_common = QtGui.QCheckBox(ItisSearchWidget)
        self.check_include_common.setObjectName(_fromUtf8("check_include_common"))
        self.horizontalLayout_3.addWidget(self.check_include_common)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ItisSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(ItisSearchWidget)

    def retranslateUi(self, ItisSearchWidget):
        ItisSearchWidget.setWindowTitle(_translate("ItisSearchWidget", "ITIS Search", None))
        self.label_search_term.setText(_translate("ItisSearchWidget", "Search Term:", None))
        self.search_term.setToolTip(_translate("ItisSearchWidget", "terms to search ITIS for", None))
        self.button_search.setToolTip(_translate("ItisSearchWidget", "Perform search of ITIS", None))
        self.button_search.setText(_translate("ItisSearchWidget", "Seach ITIS", None))
        self.label_search_type.setToolTip(_translate("ItisSearchWidget", "The type of ITIS search to perform (Scientific or Common name)", None))
        self.label_search_type.setText(_translate("ItisSearchWidget", "Search Type:", None))
        self.combo_search_type.setToolTip(_translate("ItisSearchWidget", "Search ITIS on common or scientific name", None))
        self.combo_search_type.setItemText(0, _translate("ItisSearchWidget", "Common name", None))
        self.combo_search_type.setItemText(1, _translate("ItisSearchWidget", "Scientific name", None))
        self.label_search_results.setToolTip(_translate("ItisSearchWidget", "Results from the ITIS common or scientific name search", None))
        self.label_search_results.setText(_translate("ItisSearchWidget", "Search Results:", None))
        self.button_add_taxon.setToolTip(_translate("ItisSearchWidget", "Add the selected item above to the list of include species (right)", None))
        self.button_add_taxon.setText(_translate("ItisSearchWidget", "Add Selection", None))
        self.label_include_item.setToolTip(_translate("ItisSearchWidget", "List of taxons to include in the taxonomy section", None))
        self.label_include_item.setText(_translate("ItisSearchWidget", "Items to include:", None))
        self.button_remove_selected.setToolTip(_translate("ItisSearchWidget", "Remove selected items from list above", None))
        self.button_remove_selected.setText(_translate("ItisSearchWidget", "Remove Selection", None))
        self.button_gen_fgdc.setToolTip(_translate("ItisSearchWidget", "Create a FGDC taxonomy section with the items in the above list", None))
        self.button_gen_fgdc.setText(_translate("ItisSearchWidget", "Generate Taxonomy Section", None))
        self.check_include_common.setToolTip(_translate("ItisSearchWidget", "Include common names in FGDC taxonomy section (optional elements)", None))
        self.check_include_common.setText(_translate("ItisSearchWidget", "Include Common Names", None))

