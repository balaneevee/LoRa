import RPi.GPIO as GPIO
import serial
import sys
from time import sleep
GPIO.setwarnings(False)


class SerialPass:
    
    def __init__(self,portname='/dev/ttyUSB1',baudrate = 9600):
        self.portname=portname
        self.baudrate=baudrate
        self.ser=serial.Serial(port = portname,baudrate = baudrate,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
      
    def serial_write(self,data):
        self.ser.write(data)
        
    def serial_read(self):
        rx_data = self.ser.read()
        sleep(0.3)
        data_left = self.ser.inWaiting()
        if data_left > 0:
            rx_data += self.ser.read(data_left)
        return rx_data
        

class AT_COMMAND(SerialPass):
    
    def at(self):
        try:
            atcommand.serial_write(b'AT')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+AT')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e    
        
    def version(self):
        try:
            atcommand.serial_write(b'AT+VER')
            res1=atcommand.serial_read()
            rec = ("+VER: 4.0.11")
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+VER')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
    def reset(self):
        try:
            atcommand.serial_write(b'AT+RESET')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RESET')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def port(self):
        try:
            atcommand.serial_write(b'AT+PORT=?')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+PORT')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def port_set(self,data):
        try:
            atcommand.serial_write(b'AT+PORT=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+PORT')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def adr(self,data):
        try:
            atcommand.serial_write(b'AT+ADR=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ADR')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
        
    def dr(self):
        try:
            atcommand.serial_write(b'AT+DR')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DR')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def dr_set(self,data):
        try:
            atcommand.serial_write(b'AT+DR=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DR')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
        
    def ch(self):
        try:
            atcommand.serial_write(b'AT+CH')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CH')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def ch_set(self,data):
        try:
            atcommand.serial_write(b'AT+CH=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CH')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def power(self):
        try:
            atcommand.serial_write(b'AT+POWER')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+POWER')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def power_set(self,data):
        try:
            atcommand.serial_write(b'AT+POWER=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+POWER')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def rept_set(self,data):
        try:
            atcommand.serial_write(b'AT+REPT=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+REPT')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def retry_set(self,data):
        try:
            atcommand.serial_write(b'AT+RETRY=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RETRY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def rxwin2(self):
        try:
            atcommand.serial_write(b'AT+RXWIN2')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RXWIN2')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def rxwin2_set(self,data):
        try:
            atcommand.serial_write(b'AT+RXWIN2=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RXWIN2')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def rxwin1(self):
        try:
            atcommand.serial_write(b'AT+RXWIN1')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RXWIN1')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def rxwin1_set(self,data):
        try:
            atcommand.serial_write(b'AT+RXWIN1=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RXWIN1')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def key(self):
        try:
            atcommand.serial_write(b'AT+KEY')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+KEY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
        
    def key_set(self,data):
        try:
            atcommand.serial_write(b'AT+KEY=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+KEY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def app_key_set(self,data):
        try:
            atcommand.serial_write(b'AT+KEY=APPKEY,' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+KEY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def fdefault(self):
        try:
            atcommand.serial_write(b'AT+FDEFAULT')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+FDEFAULT')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def fdefault_set(self,data):
        try:
            atcommand.serial_write(b'AT+FDEFAULT=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+FDEFAULT')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def dfu(self):
        try:
            atcommand.serial_write(b'AT+DFU')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DFU')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def dfu_set(self,data):
        try:
            atcommand.serial_write(b'AT+DFU=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DFU')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def mode_set(self,data):
        try:
            atcommand.serial_write(b'AT+MODE=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+MODE')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def join(self):
        try:
            atcommand.serial_write(b'AT+JOIN')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+JOIN')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def join_set(self,data):
        try:
            atcommand.serial_write(b'AT+JOIN=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+JOIN')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def beacon(self):
        try:
            atcommand.serial_write(b'AT+BEACON')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+BEACON')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def beacon_set(self,data):
        try:
            atcommand.serial_write(b'AT+BEACON=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+BEACON')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def class_forced(self):
        try:
            atcommand.serial_write(b'AT+CLASS=B')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+BEACON')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def OTAA(self):
        try:
            atcommand.serial_write(b'AT+MODE=LWOTAA')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            #index_res1 = str_res1.find('+BEACON')
            #cmp = str_res1[index_res1 : -2]
            return str_res1
        
        except Exception as e:
            return e
        
    def delay(self):
        try:
            atcommand.serial_write(b'AT+DELAY')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DELAY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def delay_set(self,data):
        try:
            atcommand.serial_write(b'AT+DELAY=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+DELAY')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def wdt(self):
        try:
            atcommand.serial_write(b'AT+WDT')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+WDT')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def wdt_set(self,data):
        try:
            atcommand.serial_write(b'AT+WDT=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+WDT')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def lowpower(self):
        try:
            atcommand.serial_write(b'AT+LOWPOWER')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LOWPOWER')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def lowpower_set(self,data):
        try:
            atcommand.serial_write(b'AT+LOWPOWER=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LOWPOWER')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def vdd(self):
        try:
            atcommand.serial_write(b'AT+VDD')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+VDD')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def vdd_req(self,data):
        try:
            atcommand.serial_write(b'AT+VDD=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+VDD')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def temp(self):
        try:
            atcommand.serial_write(b'AT+TEMP')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+TEMP')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def temp_set(self,data):
        try:
            atcommand.serial_write(b'AT+TEMP=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+TEMP')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def eeprom_set(self,data):
        try:
            atcommand.serial_write(b'AT+TEMP=' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+EEPROM')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def timeout(self):
        try:
            atcommand.serial_write(b'AT+UART=TIMEOUT,' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            #index_res1 = str_res1.find('+TIMEOUT')
            #cmp = str_res1[index_res1 : -2]
            return str_res1
            
        except Exception as e:
             return e
            
    def timeout_disable(self,data):
        try:
            atcommand.serial_write(b'AT+UART=TIMEOUT,0')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            #index_res1 = str_res1.find('+TIMEOUT')
            #cmp = str_res1[index_res1 : -2]
            return str_res1
            
        except Exception as e:
             return e
            
    def timeout_set(self,data):
        try:
            atcommand.serial_write(b'AT+UART=TIMEOUT,1000')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            #index_res1 = str_res1.find('+TIMEOUT')
            #cmp = str_res1[index_res1 : -2]
            return str_res1
            
        except Exception as e:
             return e
            
    def br(self):
        try:
            atcommand.serial_write(b'AT+UART=BR')
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+UART')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def br_set(self,data):
        try:
            atcommand.serial_write(b'AT+UART=BR,' + bytes(data, 'UTF-8'))
            res1=atcommand.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+UART')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
        
        
class DEV_ID(SerialPass):
    
    
    def ID(self):
        try:
            dev.serial_write(b'AT+ID')
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
             print("error") 
             return e
            
            
    def ID_DevAddr(self):
        try:
            dev.serial_write(b'AT+ID=DevAddr')
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
            
            
    def ID_DevEui(self):
        try:
            dev.serial_write(b'AT+ID=DevEui')
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
    
    def ID_AppEui(self):
        try:
            dev.serial_write(b'AT+ID=AppEui')
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
        
    def ID_DevAddr_set(self,data):
        try:
            
            dev.serial_write(b'AT+ID=DevAddr,'+ bytes(data, 'UTF-8'))
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
            
            
    def ID_DevEui_set(self,data):
        try:
            dev.serial_write(b'AT+ID=DevEui,'+ bytes(data, 'UTF-8'))
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
    
    def ID_AppEui_set(self,data):
        try:
            dev.serial_write(b'AT+ID=AppEui,'+ bytes(data, 'UTF-8'))
            res1=dev.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+ID')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             print("error") 
             return e
            
    

class MSG(SerialPass):
        
    def mesg(self,data):
        try:
            msg.serial_write(b'AT+MSG=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+MSG')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
        
    def cmsg(self,data):
        try:
            msg.serial_write(b'AT+CMSG=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CMSG')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def msghex(self,data):
        try:
            msg.serial_write(b'AT+MSGHEX=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+MSG')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def cmsghex(self,data):
        try:
            msg.serial_write(b'AT+CMSGHEX=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CMSG')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def pmsg(self,data):
        try:
            msg.serial_write(b'AT+PMSG=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+PMSG')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
    def pmsghex(self,data):
        try:
            msg.serial_write(b'AT+PMSGHEX=' + bytes(data, 'UTF-8'))
            res1=msg.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+PMSGHEX')
            cmp = str_res1[index_res1 : -2]
            return cmp
        
        except Exception as e:
            return e
        
            
            
class AT_CLASS(SerialPass):
    
    def cur_class(self):
        try:
            atclass.serial_write(b'AT+CLASS')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e

    def class_set_a(self):
        try:
            atclass.serial_write(b'AT+CLASS=A')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def class_set_b(self):
        try:
            atclass.serial_write(b'AT+CLASS=B')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def class_set_c(self):
        try:
            atclass.serial_write(b'AT+CLASS=C')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def class_save_a(self):
        try:
            atclass.serial_write(b'AT+CLASS=A,SAVE')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def class_save_b(self):
        try:
            atclass.serial_write(b'AT+CLASS=B,SAVE')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def class_save_c(self):
        try:
            atclass.serial_write(b'AT+CLASS=C,SAVE')
            res1=atclass.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+CLASS')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            

class LW(SerialPass):
    
    def cdr(self):
        try:
            lw.serial_write(b'AT+LW=CDR')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def uldl(self):
        try:
            lw.serial_write(b'AT+LW=ULDL')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def uldl_set(self,data):
        try:
            lw.serial_write(b'AT+LW=ULDL,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def dc(self):
        try:
            lw.serial_write(b'AT+LW=DC')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def dc_set(self,data):
        try:
            lw.serial_write(b'AT+LW=DC,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
            
    def net_set(self,data):
        try:
            lw.serial_write(b'AT+LW=DC,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def mc(self):
        try:
            lw.serial_write(b'AT+LW=MC')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
            
    def mc_set(self,data):
        try:
            lw.serial_write(b'AT+LW=DC,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def thld(self):
        try:
            lw.serial_write(b'AT+LW=THLD')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def thld_set(self,data):
        try:
            lw.serial_write(b'AT+LW=THLD,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def bat(self):
        try:
            lw.serial_write(b'AT+LW=BAT')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def bat_set(self,data):
        try:
            lw.serial_write(b'AT+LW=BAT,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def tps(self):
        try:
            lw.serial_write(b'AT+LW=TPS')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def tps_set(self,data):
        try:
            lw.serial_write(b'AT+LW=TPS,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def scr(self):
        try:
            lw.serial_write(b'AT+LW=SCR')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def scr_set(self,data):
        try:
            lw.serial_write(b'AT+LW=SCR,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def jdc(self):
        try:
            lw.serial_write(b'AT+LW=JDC')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def jdc_set(self,data):
        try:
            lw.serial_write(b'AT+LW=JDC,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def ct(self):
        try:
            lw.serial_write(b'AT+LW=CT')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def ct_set(self,data):
        try:
            lw.serial_write(b'AT+LW=CT,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def len_payload(self):
        try:
            lw.serial_write(b'AT+LW=LEN')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def len_payload_set(self,data):
        try:
            lw.serial_write(b'AT+LW=LEN,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def prot_ver(self):
        try:
            lw.serial_write(b'AT+LW=VER')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def prot_ver_set(self,data):
        try:
            lw.serial_write(b'AT+LW=VER,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
            
    def dtr(self):
        try:
            lw.serial_write(b'AT+LW=DTR')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def lcr(self):
        try:
            lw.serial_write(b'AT+LW=LCR')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def ldro(self):                # use in TEST_MODE
        try:
            lw.serial_write(b'AT+LW=LDRO')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def ldro_set(self,data):          # use in TEST_MODE
        try:
            lw.serial_write(b'AT+LW=LDRO,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
            
    def dcmrx(self):
        try:
            lw.serial_write(b'AT+LW=DCMRX')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def dcmrx_set(self,data):
        try:
            lw.serial_write(b'AT+LW=DCMRX,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
        
    def dumrx(self):
        try:
            lw.serial_write(b'AT+LW=DUMRX')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def dumrx_set(self,data):
        try:
            lw.serial_write(b'AT+LW=DUMRX,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def afpack(self):
        try:
            lw.serial_write(b'AT+LW=AFPACK')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def afpack_set(self,data):
        try:
            lw.serial_write(b'AT+LW=AFPACK,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def chrb(self):
        try:
            lw.serial_write(b'AT+LW=CHRB')
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def chrb_set(self,data):
        try:
            lw.serial_write(b'AT+LW=CHRB,' + bytes(data, 'UTF-8'))
            res1=lw.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LW')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
class RTC(SerialPass):
    
    def rtc_cur_time(self):
        try:
            rtc.serial_write(b'AT+RTC')
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_set_time(self,data):
        try:
            rtc.serial_write(b'AT+RTC=' + bytes(data, 'UTF-8'))
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_time_zone(self):
        try:
            rtc.serial_write(b'AT+RTC=ZONE')
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_time_zoneset(self,data):
        try:
            rtc.serial_write(b'AT+RTC=ZONE,' + bytes(data, 'UTF-8'))
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_verbose(self):
        try:
            rtc.serial_write(b'AT+RTC=FULL')
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_leapsec(self):
        try:
            rtc.serial_write(b'AT+RTC=LEAPSEC')
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_leapsec_set(self,data):
        try:
            rtc.serial_write(b'AT+RTC=LEAPSEC,' + bytes(data, 'UTF-8'))
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def rtc_utcms(self):
        try:
            rtc.serial_write(b'AT+RTC=UTCMS')
            res1=rtc.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+RTC')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
            
class TEST(SerialPass):
    
    def test_mode(self):
        try:
            test.serial_write(b'AT+MODE=TEST')
            res1=test.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+MODE')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
             return e
            
    def test_query(self):
        try:
            test.serial_write(b'AT+TEST=?')
            res1=test.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+TEST')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
    def test_set(self,data):
        try:
            test.serial_write(b'AT+TEST=' + bytes(data, 'UTF-8'))
            res1=test.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+TEST')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
    def test_beacon_sniffer(self):
        try:
            test.serial_write(b'AT+TEST=BEACON')
            res1=test.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+TEST')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
        
        
class LOG(SerialPass):
    
    def log_level(self):
        try:
            log.serial_write(b'AT+LOG=LEVEL')
            res1=log.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LOG')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
    def log_debug(self):
        try:
            log.serial_write(b'AT+LOG=DEBUG')
            res1=log.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LOG')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e

    def log_quiet(self):
        try:
            log.serial_write(b'AT+LOG=QUIET')
            res1=log.serial_read()
            str_res1 = str(res1, 'UTF-8')
            index_res1 = str_res1.find('+LOG')
            cmp = str_res1[index_res1 : -2]
            return cmp
            
        except Exception as e:
            return e
        
if __name__ == "__main__":
    
    atcommand = AT_COMMAND()
    dev = DEV_ID()
    msg = MSG()
    atclass = AT_CLASS()
    lw = LW()
    rtc = RTC()
    test = TEST()
    log = LOG()
    print("HELLO")
    '''res=atcommand.at()
    print(res)
    res=dev.ID_DevEui_set("70B3D57ED0043FEE")
    print(res)
    res=atcommand.app_key_set("FBD285BDBCD1D1DE906A860B622E6DFB")
    print(res)
    res=dev.ID_AppEui_set("0101010101010101")
    print(res)
    res=dev.ID()
    print(res)
    res=atcommand.dr_set("EU868")
    print(res)
    res=atcommand.ch_set("NUM,0-2")
    print(res)
    res=atcommand.mode_set("LWOTAA")
    print(res)
    res=atcommand.port_set("8")
    print(res)
    res=atcommand.rept_set("10")
    print(res)
    res=atcommand.dr_set("DR5")
    print(res)
    res=atcommand.join_set("DR5")
    print(res)
    sleep(10)'''
    while True:
        print("loop before msg")
        res=atcommand.rept_set("10")
        print(res)
        res=msg.msghex("0102")
        print(res)
        print("loop after msg")
        sleep(130)
    '''res=atcommand.reset()
    print(res)'''
    
    
    