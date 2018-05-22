
# Without "path" paths do not work
path = "./icons/"

def getWindowStyleSheet():
	return """QWidget { background-color: #ffffff;
			border: 1px solid black;
			}"""

# Open Folder
def getOpenFolderBtnleSheet():
	return """QToolButton { image: url(./icons/folder.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}

			QToolButton:hover {
			image: url(./icons/folder-hover.png);
			} """

# Open Browser
def getOpenBrowserBtnleSheet():
	return """QToolButton { image: url(./icons/browser.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}

			QToolButton:hover {
			image: url(./icons/browser-hover.png);
			} """

# Open Photos
def getOpenPhotosBtnleSheet():
	return """QToolButton { image: url(./icons/photos.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}

			QToolButton:hover {
			image: url(./icons/photos-hover.png);
			} """

# Open Notificaton
def getOpenNotifBtnleSheet():
	return """QToolButton { image: url(./icons/notifications.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}

			QToolButton:hover {
			image: url(./icons/notifications-hover.png);
			} """


# Open Settings
def getOpenSettingBtnleSheet():
	return """QToolButton { image: url(./icons/setting.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}

			QToolButton:hover {
			image: url(./icons/setting-hover.png);
			} """

# Status button
def getStatusBtnSyncleSheet():
	return """QToolButton { image: url(./icons/status.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}"""

def getStatusBtnStopedSyncleSheet():
	return """QToolButton { image: url(./icons/status-start.png); 
			icon-size:24px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			}"""


# Sputnik icon 
def getSputnikIconeSheet():
	return """QToolButton { image: url(./icons/sputnik.png); 
			icon-size:32px;
			padding: 2px;
			margin: 2px;
			border: 0px;
			} """

# Screnshot text button
def getScreenShotSheet():
	return """QLabel {
			border: 0px;
			}"""

# Status text button
def getStatusSheet():
	return """QLabel {
			border: 0px;
			}"""

# Synclist
def getSynclistSheet():
	return # """QListView {
			#border: 0px;
			#} """  