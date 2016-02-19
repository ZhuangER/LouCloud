#coding:utf8
import libvirt
import xml.dom.minidom
import time
import os
class VMError(Exception):
    def __init__(self,vmName):
        print vmName

class zxvm:
    def __init__(self):
        self.host=libvirt.open('qemu+ssh://vagrant@localhost/system')
    #这里通过defineXML(）/cretateXML（）创建虚拟机
    def createVM(self,vmName,cpunum,freenum,path):
        with open('louvm1.xml','r') as infile:
            defaultString=infile.read()

        dom = xml.dom.minidom.parseString(defaultString)
        root=dom.documentElement
        xmlname=dom.getElementsByTagName('vmName')[0]
        xmlname.firstChild.data=vmName
        xmlcpunum=dom.getElementsByTagName('vcpu')[0]
        xmlcpunum.firstChild.data=cpunum
        xmlname=dom.getElementsByTagName('memory')[0]
        xmlname.firstChild.data=freenum
        xmlname=dom.getElementsByTagName('source')[0]
        xmlname.attributes['file'].value=path
        with open('tmp.xml','w') as tmp:
            dom.writexml(tmp) 
        with open('tmp.xml','r') as infile:
            xmlString=infile.read()
            #self.host.defineXML(xmlString)
            self.host.createXML(xmlString,0)
        domain=self.host.lookupByName(vmName)
        #domain.create()
        print domain.state()
        tmp=os.path.join('./','tmp.xml')
        os.remove(tmp)
        print 'VM %s is ok!' %(vmName)

    def startVM(self,vmName):
        try:
             domain=self.host.lookupByName(vmName)
        except  Exception,e:
            with open('./vmfailed.log','a') as logfile:
             #   logfile.write(str(time.time()))
                logfile.write(':\n startVM %s Failed' %(vmName))
                logfile.write(str(e))
                print "VM %s Create [Failed]!" %(vmName)
            return False
        if domain.state()[0]==libvirt.VIR_DOMAIN_RUNNING:
            print 'VM %s :It\'s running!' %(vmName)
            return False
        else:
            domain.create()
            print  'VM %s :Start    [OK]' %(vmName)
            return True

    def shutdownVM(self,vmName):
        domain=self.host.lookupByName(vmName)
        if domain.state()[0]==libvirt.VIR_DOMAIN_RUNNING:
            domain.destroy()
            print 'VM %s :ShutdownVM successed!' %(vmName)
            return True
        else:
            print  'VM %s :ShutdownVM failed!' %(vmName)
            return False


    def getVNCPort(self,vmName):
        try:
             domain=self.host.lookupByName(vmName)
        except  Exception,e:
            with open('./vmfailed.log','a') as logfile:
             #   logfile.write(str(time.time()))
                logfile.write(':\n startVM %s Failed' %(vmName))
                logfile.write(str(e))
                print "VM %s Create [Failed]!" %(vmName)
            raise VMError('VM %s dose not exist！' %(vmName))
        xmlString=domain.XMLDesc()
        dom = xml.dom.minidom.parseString(xmlString)
        vncport=dom.getElementsByTagName('graphics')[0].getAttribute('port')
        print 'VM %s VNCPort is %s' %(vmName,vncport)
        return vncport

    def rebootVM(self, vmName):
    	domain = self.host.lookupByName(vmName)
    	if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
			domain.reboot()
            print 'VM %s : Reboot successed!' %(vmName)
            return True
        else:
        	print 'VM %s : Reboot failed!' %(vmName)
            return False

    def deleteVM(self, vmName):
    	domain = self.host,lookupByName(vmName)
        if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
            domain.destroy()
            domain.undefine()
            return True
        elif domain.state()[0] == libvirt.VIR_DOMAIN_SHUTOFF:
            domain.undefine()
            return True
        else:
            return False


if __name__=="__main__":
    vm=zxvm()
    vm.createVM('louvm2',2,102400,'/vagrant/data/louvm1.qcow2')
    vm.shutdownVM('louvm2')

    vm.startVM('louvm1')
    vm.getVNCPort('louvm1')
    vm.shutdownVM('louvm1')