# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import json
import os
import shutil
import sys

###########################################################################
## Class mainWindow
###########################################################################

class mainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fast Server v1.1", pos = wx.DefaultPosition, size = wx.Size( 533,457 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Location" ), wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		sbSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.directoryInput = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer1.Add( self.directoryInput, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.BrowseFolder = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.BrowseFolder, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		sbSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.createHTMLcheckbox = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add an app.html for my server", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.createHTMLcheckbox, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Choose a server template", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

		template_choiceChoices = [ u"Do not use any template", u"Vue" ]
		self.template_choice = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, template_choiceChoices, 0 )
		self.template_choice.SetSelection( 0 )
		bSizer3.Add( self.template_choice, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		sbSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Port Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.PortInput = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.PortInput, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Bootup Notification", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.bootupInput = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.bootupInput, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( bSizer1, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.create = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Create Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.create, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.start_server_btn = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Start the server", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.start_server_btn, 1, wx.ALL|wx.EXPAND, 5 )

		self.stop_server_btn = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Stop the server", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.stop_server_btn, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( sbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.BrowseFolder.Bind( wx.EVT_BUTTON, self.openFolderBrowser )
		self.create.Bind( wx.EVT_BUTTON, self.createServer )
		self.start_server_btn.Bind( wx.EVT_BUTTON, self.start_server )
		self.stop_server_btn.Bind( wx.EVT_BUTTON, self.stop_server )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def openFolderBrowser( self, event ):
		event.Skip()

	def createServer( self, event ):
		event.Skip()

	def start_server( self, event ):
		event.Skip()

	def stop_server( self, event ):
		event.Skip()

            


class pageEvent(mainWindow):
    
    def __init__(self, parent):
        mainWindow.__init__(self, parent)
        self.location = ""
        self.port_number = ""
        self.bootup_notification = ""
        self.needHomepage = False
        self.serverTemplate = ""
        
    def openFolderBrowser(self, event):
        self.location = filedialog.askdirectory()
        # Try to open the configuration file
        self.directoryInput.SetValue(self.location)
        try:
            with open(self.location + "/serverConfig.json", "r") as config_json_file:
                config_info = json.load(config_json_file)
                self.port_number = config_info["port_number"]
                self.bootup_notification = config_info["bootup_notification"]
                self.needHomepage = config_info["needHomepage"]
                self.serverTemplate = config_info["serverTemplate"]
                
            # Setup the values
            self.createHTMLcheckbox.SetValue(self.needHomepage)
            self.template_choice.SetLabelText(self.serverTemplate)
            self.PortInput.SetValue(self.port_number)
            self.bootupInput.SetValue(self.bootup_notification)
            pass
        except:
            pass
        
    def createServer(self, event):
        try:
            # Gather all information
            self.location = self.directoryInput.GetValue()
            self.port_number = self.PortInput.GetValue()
            self.bootup_notification = self.bootupInput.GetValue()
            self.needHomepage = self.createHTMLcheckbox.GetValue()
            self.serverTemplate = self.template_choice.GetStringSelection()
            # Check validation
            if (self.location == "" or self.port_number == "" or self.bootup_notification == "" or self.needHomepage == "" or self.serverTemplate == ""):
                messagebox.showerror("Error", "You didn\'t fill out the essential information. Fill them out before progress.")
                pass
            else:
                # Try to create server
                with open(self.location + "/server.js", "w") as server_source_file:
                    # Edit the server file
                    if (self.needHomepage == True):
                        server_content = f"""
const express = require('express')
const cors = require('cors')
const path = require('path')

const server = express()

server.use(cors())
server.get('/', (req,resp)=>{{
    resp.sendFile(path.join(__dirname, '/Static/app.html'), (err)=>{{
        if (err) resp.send('404')
    }})
}})


server.listen({self.port_number})
console.log('{self.bootup_notification}')
"""
                        # Write the source code
                        server_source_file.write(server_content)
                        # Try to create the template
                        os.mkdir(self.location+"/Static")
                        if (self.serverTemplate == "Vue"):
                            # Copy the file
                            shutil.copy("./app-vue.html", self.location+"/Static/app.html")
                        else:
                            shutil.copy("./app.html", self.location+"/Static/app.html")
                            
                        
                        pass
                    else:
                        server_content = f"""
const express = require('express')
const cors = require('cors')
const path = require('path')

const server = express()

server.use(cors())
server.use(express.static('./Static'))
server.get('/', (req,resp)=>{{
    resp.sendFile(path.join(__dirname, '/Static/app.html'), (err)=>{{
        if (err) resp.send('404')
    }})
}})


server.listen({self.port_number})
console.log('{self.bootup_notification}')
"""
                        # Write out the source file
                        server_source_file.write(server_content)
                # Create config file
                target_config = {
                    "port_number": self.port_number,
                    "bootup_notification": self.bootup_notification,
                    "needHomepage": self.needHomepage,
                    "serverTemplate": self.serverTemplate
                }
                with open(self.location+"/serverConfig.json", "w") as target_json_file:
                    json.dump(target_config, target_json_file)
                messagebox.showinfo("Success", "Server created successfully!")
                pass
        except:
            messagebox.showerror("Error", "An error occured while processing the progress...")
            pass
        
    
    def start_server(self, event):
        command = "node "+self.directoryInput.GetValue()+"/server.js"
        messagebox.showinfo("Working", "Server started successfully!")

root = Tk()
root.withdraw()
app = wx.App(False)
page = pageEvent(None)
page.Show(True)
app.MainLoop()