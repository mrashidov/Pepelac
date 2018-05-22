#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
appName = 'Pepelac'
appVer = '0.1'
#
LICENSE = """
This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses
"""

import sys
import os
import signal # import module for send signal CTRL+C causes a signal to be sent to the process
import stylesheet
from PyQt5.QtCore import *
from PyQt5.QtGui import (QDesktopServices, QIcon, QCursor, QMouseEvent)
from PyQt5.QtWidgets import (QMenu, QApplication, QWidget, QSystemTrayIcon,
                             QGraphicsDropShadowEffect,  QAction, qApp)
from PyQt5 import uic


""" Class of Main window 
"""
class PepelacWindow(QWidget):
    # Define a new signall 
    previousPositionChanged = pyqtSignal()
    
    def __init__(self):
        super ().__init__()
        # Load UI of .ui file
        uic.loadUi('interface.ui', self)
        # Init mouse tracking
        self.setMouseTracking(True)
        # Iit action mouse button
        self.m_leftMouseButtonPressed = None        
        # Create tray icon
        self.iconTray()
        # Create menu for "setting_menu"
        self.SettingMenu()
        # init Pepelac UI
        self.initUI()
    
    # Linux Tray
    def iconTray(self):        
        # Init QSystemTrayIcon
        icon = './icons/sputnik.png' # сделать динамическую смену иконки
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon))
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.trayIconActivated)
   
    def moveToTray(self):
        cursor = QCursor()
        self.show()
        self.move(cursor.pos())
        #print(self.pos())

    def trayIconActivated(self, reason):
        if reason == self.tray_icon.Trigger: 	
            if self.isHidden():
                self.moveToTray()
                self.activateWindow()
            else:
                self.hide()
    
    # Creat Setting Menu
    def SettingMenu(self):
        setting_action = QAction('Настройка', self)
        quastions_action = QAction('Справка', self)
        quit_action = QAction('Выход', self)

        setting_action.triggered.connect(self.openSettingWindow)
        quastions_action.triggered.connect(self.quastions)
        quit_action.triggered.connect(qApp.quit)
        
        self.menu = QMenu()
        self.menu.addAction(setting_action)
        self.menu.addAction(quastions_action)
        self.menu.addAction(quit_action)
        self.setting_menu.setMenu(self.menu)

    # Item Quastion
    def quastions(self):
        pass

    def openSettingWindow(self):
        pass

    def initUI(self):
        # Hide decoration of window
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint )

        # Transparent Mainwidget
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(9)
        shadow.setOffset(0)
        self.pepelac.setGraphicsEffect(shadow)
        
        # Window style
        self.setStyleSheet(stylesheet.getWindowStyleSheet())
        # Icon Sputnik 
        self.sputnik_icon.setStyleSheet(stylesheet.getSputnikIconeSheet())
        # Button Open YD folder
        self.open_folder.setStyleSheet(stylesheet.getOpenFolderBtnleSheet())
        # Button Open Browser
        self.open_browser.setStyleSheet(stylesheet.getOpenBrowserBtnleSheet())
        # Button Photos in Browser
        self.open_photos.setStyleSheet(stylesheet.getOpenPhotosBtnleSheet())
        # Button Notification
        self.notif.setStyleSheet(stylesheet.getOpenNotifBtnleSheet())
        # Button Settings
        self.setting_menu.setStyleSheet(stylesheet.getOpenSettingBtnleSheet())
        # Button Status
        self.status_btn.setStyleSheet(stylesheet.getStatusBtnSyncleSheet())
        # Screen shot
        self.skreenshot.setStyleSheet(stylesheet.getScreenShotSheet())
        # Status
        self.status.setStyleSheet(stylesheet.getStatusSheet())
        # SyncList
        self.synclist.setStyleSheet(stylesheet.getSynclistSheet())


        # Signals and Slots
        self.open_folder.clicked.connect(self.openFolderYD)
        self.open_browser.clicked.connect(lambda: self.openBrowser('https://disk.yandex.com'))
        self.open_photos.clicked.connect(lambda: self.openPhotos('https://disk.yandex.com/client/photo'))
        self.notif.clicked.connect(lambda: self.openNotif('https://disk.yandex.ru/client/recent'))
        self.setting_menu.clicked.connect(self.SettingMenu)
        self.status_btn.clicked.connect(self.start_Stop)

    def openFolderYD(self):
        # Open Yandex Disk folder
        YDfolder = self.getFolderUrl()
        # YDfolder = 'D:/' # Временно
        QDesktopServices.openUrl(QUrl(YDfolder))
    
    def openBrowser(self, url):
        # Open Yandex Disk in browser
        self.url = url
        QDesktopServices.openUrl(QUrl(url))

    def openPhotos(self, url):
       # Open Yandex Disk Photos in browser
       self.url = url
       QDesktopServices.openUrl(QUrl(url))

    def openNotif(self, url):
       # Open Notifications Yandex Disk in browser
       self.url = url
       QDesktopServices.openUrl(QUrl(url))

    def start_Stop(self):
        # Start or Stop YD deamon
        pass
    
    @pyqtSlot()
    def PreviousPosition(self):
        return self.m_previousPosition
    
    def setPreviousPosition(self, previousPosition):
        if self.m_previousPosition == previousPosition:
            return
        
        self.m_previousPosition = previousPosition

        print(self.m_previousPosition.y())
        
        self.previousPositionChanged.connect(self.PreviousPosition)
        self.previousPositionChanged.emit()
        
        
    def mousePressEvent(self, eventQMouseEvent):
        # При клике левой кнопкой мыши
        if eventQMouseEvent.button() == Qt.LeftButton:
            # Определяем, в какой области произошёл клик
            self.m_leftMouseButtonPressed = self.checkResizableField(eventQMouseEvent)
            self.setPreviousPosition(eventQMouseEvent.pos()) # и устанавливаем позицию клика

        return QWidget.mousePressEvent(self, eventQMouseEvent)

    def mouseReleaseEvent(self, eventQMouseEvent):
        # 
        if eventQMouseEvent.button()  == Qt.LeftButton:
            self.m_leftMouseButtonPressed = None;
        
        return QWidget.mouseReleaseEvent(self, eventQMouseEvent)
        
        
    def mouseMoveEvent(self, eventQMouseEvent):
        
        #При перемещении мыши, проверяем статус нажатия левой кнопки мыши    
        if self.m_leftMouseButtonPressed == 'Top':
            dy = self.event.y() - self.m_previousPosition.y()
            #self.setGeometry(self.x(), self.y() + dy, self.width(), self.height() - dy)
            self.setGeometry(x(), y() + dy, width(), height() - dy)
            
        elif self.m_leftMouseButtonPressed == 'Bottom':
            dy = self.event.y() - self.m_previousPosition.y()
            self.setGeometry(self.x(), self.y(), 309, self.height() + dy)
            self.setPreviousPosition(eventQMouseEvent)
        
        else :
            self.checkResizableField(eventQMouseEvent)

        return QWidget.mouseMoveEvent(self, eventQMouseEvent)

    def checkResizableField(self, eventQMouseEvent):
        position = eventQMouseEvent.screenPos() # Determine the position of the cursor on the screen
     
        x = self.x() # координаты окна приложения
        y = self.y() # то есть координату левого верхнего угла окна
        width = self.width()           # А также ширину
        height = self.height();        # и высоту окна
        
        # Определяем области, в которых может находиться курсор мыши
        # По ним будет определён статус клика
        rectTop = QRectF(x + 9, y, width - 18, 7)       
        rectBottom = QRectF(x + 9, y + height - 7, width - 18, 7)
        rectpepelac = QRectF(x + 9, y + 9, width - 18, height - 18)

        # Mouse on top border  
        if rectTop.contains(position):
            self.setCursor(Qt.SizeVerCursor)
            return 'Top'

        # Mouse on bottom border    
        elif rectBottom.contains(position):
            self.setCursor(Qt.SizeVerCursor)
            return 'Bottom'
        
        # Mouse on main interface
        elif rectpepelac.contains(position):
            self.setCursor(QCursor())
            return 'Interface'

        else:
            self.setCursor(QCursor())
            return None;
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False) # Do not close QApplication after closing the window
    mainWindow = PepelacWindow()
    ex=mainWindow
    signal.signal(signal.SIGINT, signal.SIG_DFL) # Ctrl + C for kill
    sys.exit(app.exec_())


        
