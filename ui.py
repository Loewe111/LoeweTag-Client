import ttkbootstrap as ttk
import tkinter as tk
from tkinter import *
from tkinter import ttk as ttk2
from PIL import Image, ImageTk

from locales.language_de import lang_de
from locales.language_en import lang_en
from gamemodes.demo import gameMode
import files
import link

global gui
global dev
class gui:
    def update_design():
        files.file.saveFile()
        style = ttk.Style(files.file.getSetting(2))


class dev:
    def broadcastVars():
        buf = "@vars"+ dev.HP.get() + "#" + dev.MHP.get() + "#" + dev.SP.get() + "#" + dev.MSP.get() + "#" + dev.ATK.get() + "#" + dev.RT.get() + "#" + dev.PTS.get() + "#" + dev.KILL.get() + "\n"
        link.link.sendSerial(buf)
        buf = "@color"+ dev.RED.get() + "#" + dev.GREEN.get() + "#" + dev.BLUE.get() + "\n"
        link.link.sendSerial(buf)
    def sendVars():
        buf = dev.address.get() + "@vars"+ dev.HP.get() + "#" + dev.MHP.get() + "#" + dev.SP.get() + "#" + dev.MSP.get() + "#" + dev.ATK.get() + "#" + dev.RT.get() + "#" + dev.PTS.get() + "#" + dev.KILL.get() + "\n"
        link.link.sendSerial(buf)
        buf = dev.address.get() + "@color"+ dev.RED.get() + "#" + dev.GREEN.get() + "#" + dev.BLUE.get() + "\n"
        link.link.sendSerial(buf)
    def SendGamestate():
        link.link.sendSerial("@"+"gamestate"+dev.gamestate.get())
    

def init():
    global lang
    global root
    global deviceTypeIcons
    global style

    root = tk.Tk()
    style = ttk.Style("darkly")
    root.title("LoeweTag PC Software")

    gamemode = gameMode()

    files.file = files.settingsFile()

    files.file.loadFile()
    if files.file.getSetting(0) == "de":
        lang = lang_de()
    if files.file.getSetting(0) == "en":
        lang = lang_en()
    
    gui.design = files.file.getSetting(1)
    gui.design_outline = files.file.getSetting(1)+"-outline"
    
    style = ttk.Style(files.file.getSetting(2))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    dev.HP = StringVar()
    dev.MHP = StringVar()
    dev.SP = StringVar()
    dev.MSP = StringVar()
    dev.ATK = StringVar()
    dev.RT = StringVar()
    dev.PTS = StringVar()
    dev.KILL = StringVar()
    dev.address = StringVar()
    dev.RED = StringVar()
    dev.GREEN = StringVar()
    dev.BLUE = StringVar()
    dev.gamestate = StringVar()

    dev.gamestate.set("0")

    gui.icon_devices = ImageTk.PhotoImage(Image.open('images/icon_devices.png'))
    gui.icon_modes = ImageTk.PhotoImage(Image.open('images/icon_mode.png'))
    gui.icon_link = ImageTk.PhotoImage(Image.open('images/icon_link.png'))
    gui.icon_settings = ImageTk.PhotoImage(Image.open('images/icon_settings.png'))
    gui.icon_dev = ImageTk.PhotoImage(Image.open("images/icon_dev.png"))
    gui.icon_router = ImageTk.PhotoImage(Image.open('images/icon_router.png'))
    gui.icon_person = ImageTk.PhotoImage(Image.open('images/icon_person.png'))
    gui.icon_repeater = ImageTk.PhotoImage(Image.open('images/icon_repeater.png'))
    gui.icon_unknown = ImageTk.PhotoImage(Image.open('images/icon_unknown.png'))

    deviceTypeIcons = {'repeater':[lang.repeater,gui.icon_repeater],'gun':[lang.gun,gui.icon_person],'unknown':[lang.unknown,gui.icon_unknown]}

    gui.notebook = ttk2.Notebook(root,bootstyle=gui.design)

    gui.deviceFrame = ttk.Frame(root)
    gui.gameFrame = ttk.Frame(root)
    gui.linkFrame = ttk.Frame(root)
    gui.devFrame = ttk.Frame(root)
    gui.settingsFrame = ttk.Frame(root)

    gui.notebook.add(gui.deviceFrame, text=lang.devices, image = gui.icon_devices, compound = "left",sticky="NSWE", state = "disabled")
    gui.notebook.add(gui.linkFrame, text=lang.link, image = gui.icon_link, compound = "left",sticky="NSWE")
    gui.notebook.add(gui.gameFrame, text=lang.gamemodes, image = gui.icon_modes, compound = "left",sticky="NSWE")
    gui.notebook.add(gui.devFrame, text=lang.developer, image = gui.icon_dev, compound= "left", sticky="NSWE")
    gui.notebook.add(gui.settingsFrame, text=lang.settings, image = gui.icon_settings, compound = "left",sticky="NSWE")
    gui.notebook.grid(row=0,column=0,sticky="NSWE")
    
    #settings
    gui.languageFrame = ttk.LabelFrame(gui.settingsFrame, text=lang.language, bootstyle=gui.design)
    gui.languageFrame.grid(row=0,column=0,sticky="NSWE")

    gui.designFrame = ttk.LabelFrame(gui.settingsFrame, text=lang.design, bootstyle=gui.design)
    gui.designFrame.grid(row=1,column=0,sticky="NSWE")

    gui.setting_color_text = ttk.Label(gui.designFrame, text = lang.color).grid(row=0,column=0,sticky="NSWE")
    gui.setting_color_primary = ttk.Radiobutton(gui.designFrame, text="\"Primary\"", variable=files.file.settings[1], value="primary", bootstyle="primary-outline-toolbutton", command = files.file.saveFile).grid(row=1,column=0,sticky="NSWE")
    gui.setting_color_secondary = ttk.Radiobutton(gui.designFrame, text="\"Secondary\"", variable=files.file.settings[1], value="secondary", bootstyle="secondary-outline-toolbutton", command = files.file.saveFile).grid(row=2,column=0,sticky="NSWE")
    gui.setting_color_success = ttk.Radiobutton(gui.designFrame, text="\"Success\"", variable=files.file.settings[1], value="success", bootstyle="success-outline-toolbutton", command = files.file.saveFile).grid(row=3,column=0,sticky="NSWE")
    gui.setting_color_info = ttk.Radiobutton(gui.designFrame, text="\"Info\"", variable=files.file.settings[1], value="info", bootstyle="info-outline-toolbutton", command = files.file.saveFile).grid(row=4,column=0,sticky="NSWE")
    gui.setting_color_warning = ttk.Radiobutton(gui.designFrame, text="\"Warning\"", variable=files.file.settings[1], value="warning", bootstyle="warning-outline-toolbutton", command = files.file.saveFile).grid(row=5,column=0,sticky="NSWE")
    gui.setting_color_danger = ttk.Radiobutton(gui.designFrame, text="\"Danger\"", variable=files.file.settings[1], value="danger", bootstyle="danger-outline-toolbutton", command = files.file.saveFile).grid(row=6,column=0,sticky="NSWE")
    gui.setting_color_light = ttk.Radiobutton(gui.designFrame, text="\"Light\"", variable=files.file.settings[1], value="light", bootstyle="light-outline-toolbutton", command = files.file.saveFile).grid(row=7,column=0,sticky="NSWE")
    
    gui.setting_design_seperator = ttk.Label(gui.designFrame).grid(row=0,column=1,rowspan=9)
    gui.setting_design_text = ttk.Label(gui.designFrame, text = lang.design).grid(row=0,column=2,sticky="NSWE")
    gui.setting_design_morph = ttk.Radiobutton(gui.designFrame, text="\"Morph\"", variable=files.file.settings[2], value="morph", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=1,column=2,sticky="NSWE")
    gui.setting_design_solar = ttk.Radiobutton(gui.designFrame, text="\"Solar\"", variable=files.file.settings[2], value="solar", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=2,column=2,sticky="NSWE")
    gui.setting_design_superhero = ttk.Radiobutton(gui.designFrame, text="\"Superhero\"", variable=files.file.settings[2], value="superhero", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=3,column=2,sticky="NSWE")
    gui.setting_design_darkly = ttk.Radiobutton(gui.designFrame, text="\"Darkly\"", variable=files.file.settings[2], value="darkly", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=4,column=2,sticky="NSWE")
    gui.setting_design_cyborg = ttk.Radiobutton(gui.designFrame, text="\"Cyborg\"", variable=files.file.settings[2], value="cyborg", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=5,column=2,sticky="NSWE")
    gui.setting_design_vapor = ttk.Radiobutton(gui.designFrame, text="\"Vapor\"", variable=files.file.settings[2], value="vapor", bootstyle=gui.design_outline+"-toolbutton", command = gui.update_design).grid(row=6,column=2,sticky="NSWE")
    
    gui.setting_language_de = ttk.Radiobutton(gui.languageFrame, text="Deutsch", variable=files.file.settings[0], value="de", bootstyle=gui.design, command = files.file.saveFile).grid(row=0,column=0,sticky="NSWE")
    gui.setting_language_en = ttk.Radiobutton(gui.languageFrame, text="English", variable=files.file.settings[0], value="en", bootstyle=gui.design, command = files.file.saveFile).grid(row=1,column=0,sticky="NSWE")
    gui.setting_info = ttk.Label(gui.settingsFrame, text=lang.settings_info).grid(row=99,column=0,sticky="SWE")

    #devices
    gui.deviceTypeFrame = ttk.LabelFrame(gui.deviceFrame, text=lang.device_type, bootstyle=gui.design)
    gui.deviceTypeFrame.grid(row=0,column=0,sticky="NSWE")
    gui.IdFrame = ttk.LabelFrame(gui.deviceFrame, text=lang.node_id, bootstyle=gui.design)
    gui.IdFrame.grid(row=0,column=1,sticky="NSWE")
    gui.firmwareFrame = ttk.LabelFrame(gui.deviceFrame, text=lang.firmware, bootstyle=gui.design)
    gui.firmwareFrame.grid(row=0,column=2,sticky="NSWE")

    gui.MasterDeviceTypeImage = ttk.Label(gui.deviceTypeFrame, image = gui.icon_router)
    gui.MasterDeviceTypeImage.grid(row=0,column=0)
    gui.MasterDeviceType = ttk.Label(gui.deviceTypeFrame, text = "LoeweTag Master Bridge")
    gui.MasterDeviceType.grid(row=0,column=1)
    gui.MasterID = ttk.Label(gui.IdFrame, text = "?")
    gui.MasterID.grid(row=0,column=0)
    gui.MasterFirmware = ttk.Label(gui.firmwareFrame, text = "?")
    gui.MasterFirmware.grid(row=0,column=0)

    gui.MasterDeviceTypeImage.grid_remove()
    gui.MasterDeviceType.grid_remove()
    gui.MasterID.grid_remove()
    gui.MasterFirmware.grid_remove()

    gui.seperator1 = ttk.Separator(gui.deviceFrame,bootstyle="dark").grid(row=1,column=0,columnspan=3,sticky="NSWE")

    #link
    gui.serialPorts = ttk.Combobox(gui.linkFrame,bootstyle=gui.design)
    gui.serialPorts.grid(row=1,column=0,columnspan=2,sticky="NSWE")

    gui.refreshSerial = ttk.Button(gui.linkFrame, text=lang.refresh, bootstyle=gui.design_outline,command=link.link.refresh_serial)
    gui.refreshSerial.grid(row=2,column=0,sticky="NSWE")
    gui.connectSerial = ttk.Button(gui.linkFrame, text=lang.connect, bootstyle=gui.design_outline,command=link.link.change_serial)
    gui.connectSerial.grid(row=2,column=1,sticky="NSWE")

    #gamemodes

    gui.gamemodeDemoStart = ttk.Button(gui.gameFrame, text="Start Demo", bootstyle=gui.design_outline,command=gamemode.startGame)
    gui.gamemodeDemoStart.grid(row=0, column=0, sticky="NSWE")

    #dev

    gui.devVarFrame = ttk.LabelFrame(gui.devFrame, text=lang.variables)
    gui.devVarFrame.grid(row=0,column=0,sticky="NSWE",columnspan=2)

    gui.devColorFrame = ttk.LabelFrame(gui.devFrame, text=lang.colors)
    gui.devColorFrame.grid(row=1,column=0,sticky="NSWE",columnspan=2)

    gui.devGamestateFrame = ttk.LabelFrame(gui.devFrame, text=lang.gamestate)
    gui.devGamestateFrame.grid(row=4,column=0,sticky="NSWE",columnspan=2)

    gui.devHP = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.HP).grid(row=1,column=0)
    gui.devMHP = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.MHP).grid(row=1,column=1)
    gui.devSP = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.SP).grid(row=1,column=2)
    gui.devMSP = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.MSP).grid(row=1,column=3)
    gui.devATK = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.ATK).grid(row=1,column=4)
    gui.devRT = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.RT).grid(row=1,column=5)
    gui.devPTS = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.PTS).grid(row=1,column=6)
    gui.devKILL = ttk.Entry(gui.devVarFrame, bootstyle=gui.design, textvariable = dev.KILL).grid(row=1,column=7)

    gui.devRed = ttk.Entry(gui.devColorFrame, bootstyle=gui.design, textvariable = dev.RED).grid(row=1,column=0)
    gui.devGreen = ttk.Entry(gui.devColorFrame, bootstyle=gui.design, textvariable = dev.GREEN).grid(row=1,column=1)
    gui.devBlue = ttk.Entry(gui.devColorFrame, bootstyle=gui.design, textvariable = dev.BLUE).grid(row=1,column=2)

    gui.devLabelHP = ttk.Label(gui.devVarFrame, text="HP").grid(row=0,column=0)
    gui.devLabelMHP = ttk.Label(gui.devVarFrame, text="MHP").grid(row=0,column=1)
    gui.devLabelSP = ttk.Label(gui.devVarFrame, text="SP").grid(row=0,column=2)
    gui.devLabelMSP = ttk.Label(gui.devVarFrame, text="MSP").grid(row=0,column=3)
    gui.devLabelATK = ttk.Label(gui.devVarFrame, text="ATK").grid(row=0,column=4)
    gui.devLabelRT = ttk.Label(gui.devVarFrame, text="RT").grid(row=0,column=5)
    gui.devLabelPTS = ttk.Label(gui.devVarFrame, text="PTS").grid(row=0,column=6)
    gui.devLabelKILL = ttk.Label(gui.devVarFrame, text="KILL").grid(row=0,column=7)

    gui.devLabelRed = ttk.Label(gui.devColorFrame, text=lang.red).grid(row=0,column=0)
    gui.devLabelGreen = ttk.Label(gui.devColorFrame, text=lang.green).grid(row=0,column=1)
    gui.devLabelBlue = ttk.Label(gui.devColorFrame, text=lang.blue).grid(row=0,column=2)

    gui.devBroadcastVars = ttk.Button(gui.devFrame, text = lang.broadcast, bootstyle=gui.design_outline, command=dev.broadcastVars).grid(row=2,column=0,columnspan=2,sticky="NSWE")
    gui.devSendAddress = ttk.Entry(gui.devFrame, bootstyle=gui.design, textvariable=dev.address).grid(row=3,column=1,sticky="NSWE")
    gui.devSendVars = ttk.Button(gui.devFrame, text = lang.send_to_address, bootstyle=gui.design_outline, command=dev.sendVars).grid(row=3,column=0,sticky="NSWE")
    
    gui.devGamestate = ttk.Entry(gui.devGamestateFrame, bootstyle=gui.design, textvariable = dev.gamestate).grid(row=0,column=0,sticky="NSWE",columnspan=4)
    gui.devSendGamestate = ttk.Button(gui.devGamestateFrame, text = lang.send, bootstyle=gui.design_outline, command=dev.SendGamestate).grid(row=0,column=4,sticky="NSWE",columnspan=4)