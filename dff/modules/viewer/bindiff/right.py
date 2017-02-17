# DFF -- An Open Source Digital Forensics Framework
# Copyright (C) 2009-2013 ArxSys
# This program is free software, distributed under the terms of
# the GNU General Public License Version 2. See the LICENSE file
# at the top of the source tree.
# 
# See http://www.digital-forensic.org for more information about this
# project. Please do not directly contact any of the maintainers of
# DFF for assistance; the project provides a web site, mailing lists
# and IRC channels for your use.
# 
# Author(s):
#  Jeremy Mounier <jmo@digital-forensic.org>
#
from PyQt4.QtCore import QString, Qt, SIGNAL
from PyQt4.QtGui import QWidget, QFont, QColor, QTabWidget

from dff.modules.bindiff.goto import *

class righTab(QTabWidget):
    def __init__(self, parent):
        QTabWidget.__init__(self)
        self.init(parent)
        self.initShape()

    def init(self, parent):
        self.bdiff = parent

    def initShape(self):
        #Add Value tab
        self.setTabPosition(QTabWidget.East)

        self.goto = goto(self.bdiff)

        self.insertTab(0, self.goto, "Goto")