#LoeweTag Link Communication
import ast
import serial
import serial.tools.list_ports
import ui
import logging

logging.basicConfig(format='[link.py] %(levelname)s: %(message)s', level=logging.INFO)

class SerialCommunication:
    def __init__(self):
        self.ser = serial.Serial()
        self.ports = []
        self.node_ids = []
        self.node_firmwares = []
        self.node_types = []
        self.network_change = True
        self.master_fw = ""
        self.master_id = ""
        self.device_ids = []
        self.device_types = []
        self.device_typeIcons = []
        self.device_firmwares = []
        self.device_findButtons = []
    
    def refresh_serial(self):
        p = []
        i = 0
        while i < len([comport.device for comport in serial.tools.list_ports.comports()]):
            p.append([comport.device for comport in serial.tools.list_ports.comports()][i])
            i+=1
        ui.gui.serialPorts['values'] = p
        del p

    def update_devices(self):
        for i in self.device_ids:
            i.grid_remove()
        for i in self.device_types:
            i.grid_remove()
        for i in self.device_typeIcons:
            i.grid_remove()
        for i in self.device_firmwares:
            i.grid_remove()
        self.device_ids = []
        self.device_types = []
        self.device_typeIcons = []
        self.device_firmwares = []
        if len(self.node_ids) != 0:    
            for i in range(len(self.node_ids)):
                self.device_ids.append(ui.ttk.Label(ui.gui.IdFrame,text=self.node_ids[i]))
                self.device_ids[i].grid(row=1+i,column=0,sticky="NWSE")
                self.device_typeIcons.append(ui.ttk.Label(ui.gui.deviceTypeFrame,image=ui.deviceTypeIcons[self.node_types[i]][1]))
                self.device_typeIcons[i].grid(row=1+i,column=0,sticky="NWSE")
                self.device_types.append(ui.ttk.Label(ui.gui.deviceTypeFrame,text=ui.deviceTypeIcons[self.node_types[i]][0]))
                self.device_types[i].grid(row=1+i,column=1,sticky="NWSE")
                self.device_firmwares.append(ui.ttk.Label(ui.gui.firmwareFrame,text=self.node_firmwares[i]))
                self.device_firmwares[i].grid(row=1+i,column=0,sticky="NWSE")
        else:
            pass

    def change_serial(self):
        if self.ser.is_open:
            self.ser.close()
            ui.gui.serialPorts.configure(state="normal")
            ui.gui.connectSerial['text'] = ui.lang.connect
            ui.gui.notebook.tab(0, state="disabled")
        else:
            try:
                self.ser.port = ui.gui.serialPorts.get()
                self.ser.baudrate = "115200"
                self.ser.open()
            except Exception as e:
                print(e)
            else:
                ui.gui.serialPorts.configure(state="disabled")
                ui.gui.connectSerial['text'] = ui.lang.disconnect
                ui.gui.notebook.tab(0, state="normal")
                self.ser.write(".".encode())
                self.node_firmwares = []
                self.node_types = []
                self.node_ids = []
                self.network_change = True
    
    def handle_message(self, message):
        if message['type'] == "thisNode":
            self.master_id = message['id']
            self.master_fw = message['fw']
            self.network_change = True
            ui.gui.MasterDeviceTypeImage.grid()
            ui.gui.MasterDeviceType.grid()
            ui.gui.MasterID.grid()
            ui.gui.MasterFirmware.grid()
            ui.gui.MasterID['text'] = self.master_id
            ui.gui.MasterFirmware['text'] = self.master_fw
        elif message['type'] == "connectionChange":
            self.node_ids = message['nodes']
            self.node_firmwares = []
            self.node_types = []
            for i in range(len(self.node_ids)):
                self.node_firmwares.append("?")
                self.node_types.append("unknown")
            self.network_change = True
        elif message['type'] == "deviceInfo":
            self.node_firmwares[self.node_ids.index(message['id'])] = message['fw']
            self.node_types[self.node_ids.index(message['id'])] = message['deviceType']
            self.network_change = True
        elif message['type'] == "request":
             if message['request'] == "gamestate":
                self.ser.write((message['from']+"@"+"gamestate"+ui.dev.gamestate.get()).encode())
                logging.info(message['from']+"@"+"gamestate"+ui.dev.gamestate.get())
        else:
            logging.warn("Recieved unknown type \""+message['type']+"\", Full Message: \""+str(message)+"\"")

    def readSerial(self):
        if self.ser.is_open:
            if self.ser.in_waiting > 0:
                Input = self.ser.read_until().decode()[0:-1]
                try:
                    Input = ast.literal_eval(Input)
                except Exception as e:
                    logging.error("Error while Parsing input: "+e+"String:"+Input)
                else:
                    self.handle_message(Input)
            if self.network_change == True:
                self.update_devices()
                self.network_change = False
    
    def sendSerial(self, msg):
        self.ser.write(msg.encode())

global link
link = SerialCommunication()