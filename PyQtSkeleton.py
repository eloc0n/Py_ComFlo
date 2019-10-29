import sys
import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow
from mygui import Ui_MainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
import sqlite3
import floatRange
from math import sqrt , acos , atan , degrees , cos , radians , tan , sin , asin, log
from scipy.optimize import bisect, fsolve
import matplotlib.pyplot as plt
from matplotlib import style
style.use('classic')
import math



class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self, mainwindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainwindow)

        
        self.QuitBtn.clicked.connect(self.exit_app)
        self.actionExit.triggered.connect(self.exit_app)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.actionPrint.triggered.connect(self.file_print)
        self.actionDatabase.triggered.connect(self.dbrowser)
        self.actionInfo.triggered.connect(self.txt_info)
        self.helpBtn.clicked.connect(self.help_Btn)

        
        self.machPMradioButton.toggled.connect(self.RBtnCheckMachPM)
        self.pressurePMradioButton.toggled.connect(self.RBtnCheckPressurePM)
        self.machAnglePMradioButton.toggled.connect(self.RBtnCheckMachAnglePM)
        self.PMangleRadioButton.toggled.connect(self.RbtnCheckPMangle)
        
        self.machIsentropicRadioButton.toggled.connect(self.RBtnCheckMachIsentropic)
        self.tempIsentropicRadioButton.toggled.connect(self.RBtnCheckTempIsentropic)
        self.pressIsentropicRadioButton.toggled.connect(self.RBtnCheckPressureIsentropic)
        self.densityIsentropicRadioButton.toggled.connect(self.RBtnCheckDensityIsentropic)
        self.dynamicIsentropicRadioButton.toggled.connect(self.RBtnCheckDynamicIsentropic)
        self.lowerDynIsentropicRadioButton.toggled.connect(self.RBtnCheckLowerDynIsentropic)
        self.greaterDynIsentropicRadioButton.toggled.connect(self.RBtnCheckGreaterDynIsentropic)
        self.cssIsentropicRadioButton.toggled.connect(self.RBtnCheckCrtSoundIsentropic)
        self.subAcaIsentropicRadioButton.toggled.connect(self.RBtnCheckSubCrtAreaIsentropic)
        self.supAcaIsentropicRadioButton.toggled.connect(self.RBtnCheckSupCrtAreaIsentropic)
        
        self.mach1NormalShockRadioButton.toggled.connect(self.RBtnCheckmach1NormalShock)
        self.mach2NormalShockRadioButton.toggled.connect(self.RBtnCheckmach2NormalShock)
        self.P2P1NormalShockRadioButton.toggled.connect(self.RBtnCheckP2P1NormalShock)
        self.densityNormalShockRadioButton.toggled.connect(self.RBtnCheckDensityNormalShock)
        self.temperatureNormalShockRadioButton.toggled.connect(self.RBtnCheckTemperatureNormalShock)
        self.p2pt1LowerNormalShockRadioButton.toggled.connect(self.RBtnCheckP2Pt1LowerNormalShock)
        self.p2pt1GreaterNormalShockRadioButton.toggled.connect(self.RBtnCheckP2Pt1GreaterNormalShock)
        self.p2pt2NormalShockRadioButton.toggled.connect(self.RBtnCheckP2Pt2NormalShock)
        self.pt2pt1NormalShockRadioButton.toggled.connect(self.RBtnCheckPt2Pt1NormalShock)
        self.p1pt2NormalShockRadioButton.toggled.connect(self.RBtnCheckP1Pt2NormalShock)
        
        self.ShowObliqueShockGraph.clicked.connect(self.ObliqueShockGraph)
        self.MxObliqueShockRadioButton.toggled.connect(self.RBtnCheckMxObliqueShock)
        self.saObliqueShockRadioButton.toggled.connect(self.RBtnCheckSAObliqueShock)
        self.wraObliqueShockRadioButton.toggled.connect(self.RBtnCheckWRAObliqueShock)
        self.sraObliqueShockRadioButton.toggled.connect(self.RBtnCheckSRAObliqueShock)
        
        self.machFannoRadioButton.toggled.connect(self.RBtnCheckMachFanno)
        self.tempFannoRadioButton.toggled.connect(self.RBtnCheckTempFanno)
        self.staticpFannoRadioButton.toggled.connect(self.RBtnCheckStaticpFanno)
        self.totalLowerFannoRadioButton.toggled.connect(self.RBtnCheckTotalLowerFanno)
        self.totalGreaterFannoRadioButton.toggled.connect(self.RBtnCheckTotalGreaterFanno)
        self.speedFannoRadioButton.toggled.connect(self.RBtnCheckspeedFanno)
        self.fldLowerFannoRadioButton.toggled.connect(self.RBtnCheckfldLowerFanno)
        self.fldGreaterFannoRadioButton.toggled.connect(self.RBtnCheckfldGreaterFanno)
        
        self.machRayleighRadioButton.toggled.connect(self.RBtnCheckmachRayleigh)
        self.totalLowerTempRayleighRadioButton.toggled.connect(self.RBtnCheckTotalLowerTempRayleigh)
        self.totalGreaterTempRayleighRadioButton.toggled.connect(self.RBtnCheckTotalGreaterTempRayleigh)
        self.lowerTempRayleighRadioButton.toggled.connect(self.RBtnCheckLowerTempRayleigh)
        self.greaterTempRayleighRadioButton.toggled.connect(self.RBtnCheckGreaterTempRayleigh)
        self.pressureRayleighRadioButton.toggled.connect(self.RBtnCheckPressureRayleigh)
        self.lowerTotalPressureRayleighRadioButton.toggled.connect(self.RBtnCheckTotalLowerPressureRayleigh)
        self.greaterTotalPessureRayleighRadioButton.toggled.connect(self.RBtnCheckTotalGreaterPressureRayleigh)
        self.speedRayleighRadioButton.toggled.connect(self.RBtnCheckSpeedRayleigh)
        
            
    def file_open(self):
        
        fname = QFileDialog.getOpenFileName(None, 'Open file', '/.txt')

        if fname[0]:
            f = open(fname[0], 'r')
                
            with f:
                data = f.read()
                self.ShowPM.setText(data)
                
    def file_save(self):
        
        name, _ = QFileDialog.getSaveFileName(None,'Save File', '/.txt')
        if name:
            
            file = open(name, 'w')
            text = self.ShowPM.toPlainText()
            file.write(text)
            file.close()
        
        
    def file_print(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, None)
        preview.paintRequested.connect(self.printPreviewPM)
        preview.exec_()
  
    def printPreviewPM(self, printer):
        self.ShowPM.print_(printer)
        

    def dbrowser(self):
        
        os.chdir(r'C:\Program Files (x86)\DB Browser for SQLite')   
        os.startfile("DB Browser for SQLite.exe") 
        
    
    def txt_info(self):
        #opens a text with information about Py_ComFlo
        QMessageBox.information(None, 'Information',
                                     "Py_ComFlo is an academic aid towards the students of Piraeus University of Applied Sciences Department of Mechanical Engineering to making calculations in compressible fluid dynamics, such as isentropic flow ,Rayleigh ,Fanno etc.                                                                         One in order to fully utilize this program should be able to understand the basics of compressible fluid mechanics."
                                     , QMessageBox.Ok)
        
    def help_Btn(self):
        
        QMessageBox.information(None, 'Help',
                                          "STEP 1 : Select the flow and the parameter you want to calculate.                           STEP 2 : Enter the proper input values.                                                                                                 STEP 3 : Press Calculate.                                                                                            STEP 4 : Press Show Graph."
                                          ,QMessageBox.Ok)
        
        
                    
    def exit_app(self):
        choice = QMessageBox.question(None, 'Message',
                                     "Are you sure you want to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass
           
    


###############################################################################
################## Prandtl - Meyer RadioButton ################################
###############################################################################

    def RBtnCheckMachPM(self, Checked=True):
        if not Checked:
            return
        else:
            self.PMBtn.clicked.connect(self.machPM)
            
    def RBtnCheckPressurePM(self, Checked=True):
        if not Checked:
            return
        else:
            self.PMBtn.clicked.connect(self.pressurePM)
            
    def RBtnCheckMachAnglePM(self, Checked=True):
        if not Checked:
            return
        else:
            self.PMBtn.clicked.connect(self.machAnglePM)
            
    def RbtnCheckPMangle(self, Checked=True):
        if not Checked:
            return
        else:
            self.PMBtn.clicked.connect(self.PMangle)

###############################################################################
################# Isentropic RadioButton ######################################
###############################################################################
            
    def RBtnCheckMachIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.machISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckTempIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.tempISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
    
                
    def RBtnCheckPressureIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.pressureISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckDensityIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.densityISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckDynamicIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.dynamicISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckLowerDynIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.lowerTotDynISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckGreaterDynIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.greaterTotDynISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckCrtSoundIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.criticalSoundISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckSubCrtAreaIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.subCriticalAreaISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
            
                
    def RBtnCheckSupCrtAreaIsentropic(self, Checked=True):
        if not Checked:
            return
        else:
            self.IsentropicBtn.clicked.connect(self.supCriticalAreaISENTROPIC)
            self.ShowIsentropicGraph.clicked.connect(self.ISENTROPICgraph)
    

###############################################################################
###################### Normal Shock RadioButton ############################### 
###############################################################################
                    
    def RBtnCheckmach1NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.mach1NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)  

                        
    def RBtnCheckmach2NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.mach2NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
                            
    def RBtnCheckP2P1NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.P2P1NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
            
                                
    def RBtnCheckDensityNormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.densityNormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
                                    
    def RBtnCheckTemperatureNormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.temperatureNormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
            
                                     
    def RBtnCheckP2Pt1LowerNormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.p2pt1LowerNormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
            
                                       
    def RBtnCheckP2Pt1GreaterNormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.p2pt1GreaterNormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
                                           
    def RBtnCheckP2Pt2NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.p2pt2NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
            
                                            
    def RBtnCheckPt2Pt1NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.pt2pt1NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)
            
            
                                             
    def RBtnCheckP1Pt2NormalShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.NormalShockBtn.clicked.connect(self.p1pt2NormalShock)
            self.ShowNormalShockGraph.clicked.connect(self.NormalShockGraph)

###############################################################################
#################### Oblique Shock RadioButton ################################
###############################################################################

    def RBtnCheckMxObliqueShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.ObliqueShockBtn.clicked.connect(self.MxObliqueShock)
            
            
    
    def RBtnCheckSAObliqueShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.ObliqueShockBtn.clicked.connect(self.saObliqueShock)
            
            
    def RBtnCheckWRAObliqueShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.ObliqueShockBtn.clicked.connect(self.wraObliqueShock)
            
            
    def RBtnCheckSRAObliqueShock(self, Checked=True):
        if not Checked:
            return
        else:
            self.ObliqueShockBtn.clicked.connect(self.sraObliqueShock)
    
###############################################################################    
####################### Fanno RadioButton #####################################
###############################################################################


    def RBtnCheckMachFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.machFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
    
    def RBtnCheckTempFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.temperatureFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
        
    def RBtnCheckStaticpFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.staticpFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
            
    def RBtnCheckTotalLowerFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.totalLowerFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
     
    def RBtnCheckTotalGreaterFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.totalGreaterFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
         
    def RBtnCheckspeedFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.speedFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
          
    def RBtnCheckfldLowerFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.fldLowerFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
            
          
    def RBtnCheckfldGreaterFanno(self, Checked=True):
        if not Checked:
            return
        else:
            self.FannoBtn.clicked.connect(self.fldGreaterFANNO)
            self.ShowFannoGraph.clicked.connect(self.FANNOgraph)
    
###############################################################################
######################## Rayleigh RadioButton #################################
###############################################################################


    def RBtnCheckmachRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.machRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
    
    def RBtnCheckTotalLowerTempRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.totalLowerTempRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
        
    def RBtnCheckTotalGreaterTempRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.totalGreaterTempRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
             
    def RBtnCheckLowerTempRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.lowerTempRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
        
    def RBtnCheckGreaterTempRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.greaterTempRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
            
    def RBtnCheckPressureRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.pressureRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
            
    def RBtnCheckTotalLowerPressureRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.totalLowerPressureRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
               
    def RBtnCheckTotalGreaterPressureRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.totalGreaterPressureRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)
            
            
               
    def RBtnCheckSpeedRayleigh(self, Checked=True):
        if not Checked:
            return
        else:
            self.RayleighBtn.clicked.connect(self.speedRAYLEIGH)
            self.ShowRayleighGraph.clicked.connect(self.RAYLEIGHgraph)

###############################################################################                
###############################################################################
###############################################################################

        
    def floatFunction(self):
        
        global start, end, inc, gam
        
        start = float(self.startBox.text())
        end = float(self.endBox.text())
        inc = float(self.incBox.text()) 
        end+=inc
        gam = float(self.gammaBox.text())
                          
###############################################################################        
#########  PRANDTL - MEYER Functions ##########################################
###############################################################################

        
    def machPM(self):
        
        conn = sqlite3.connect('PMeyer.db')
        c = conn.cursor()
        
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS PMeyer(mach REAL , pressure REAL , anglem REAL , anglev REAL)")

    
        def delete_previous_values():
            c.execute("DELETE FROM PMeyer")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
               
        showFirst =  "___________________________________________"+"\n"+"     M                  p/pt                    μ                    ν         " + "\n"+"___________________________________________" + "\n"

        self.ShowPM.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            ma = float(m)
            if ma < 1 or ma > 10 :
                self.ShowPM.setText("  ")
                showError="Mach input has to be 1 <= M <= 10"
                self.ShowPM.setText(showError)
                break
            else:
                v = "{0:.3f}".format(float(sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1))))))-((degrees(acos(1/ma))))))
                mang = "{0:.3f}".format(float( float(v) + 90 - (sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1)))))))))
                pspt = "{0:.7f}".format(((1/(gam+1))*(1+cos(radians(2*sqrt((gam-1)/(gam+1))*(float(v) + 90 - float(mang))))))**(gam/(gam-1)))
        
                c.execute("INSERT INTO PMeyer (mach , pressure , anglem , anglev) VALUES(? , ? , ? , ?)",(ma , pspt , mang , v ))
            
                showSecond = '%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), pspt, mang, v)
                self.ShowPM.append(showSecond)
                conn.commit()
        create_table()
        
    def pressurePM(self):
        
        conn = sqlite3.connect('PMeyer.db')
        c = conn.cursor()
        
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS PMeyer(mach REAL , pressure REAL , anglem REAL , anglev REAL)")

    
        def delete_previous_values():
            c.execute("DELETE FROM PMeyer")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst =  "___________________________________________"+"\n"+"     M                  p/pt                    μ                    ν         " + "\n"+"___________________________________________" + "\n"

        self.ShowPM.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
    
            pspt = float(m)
            if pspt < 0.0000236 or pspt > 0.5282818:
                self.ShowPM.setText("  ")
                showError="Pressure input has to be 0.0000236 <= p/pt <= 0.5282818"
                self.ShowPM.setText(showError)
                break
            else:
                
                def f(ma):
                      return pspt -(((1/(gam+1))*(1+cos(radians(2*sqrt((gam-1)/(gam+1))*(sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1)))))))))))**(gam/(gam-1)))
                ma = float (bisect(f , 1 , 100 , xtol=1e-4))
                v = "{0:.3f}".format(float(sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1))))))-((degrees(acos(1/ma))))))
                mang = "{0:.3f}".format(float( float(v) + 90 - (sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1)))))))))
        
                c.execute("INSERT INTO PMeyer (mach , pressure , anglem , anglev) VALUES(? , ? , ? , ?)",(ma , pspt , mang , v ))
            
                showSecond = '%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), "{0:.7f}".format(pspt), mang, v)
                
                self.ShowPM.append(showSecond)
    
    
                conn.commit()
        create_table()
    
        
    def machAnglePM(self):
        
        
        conn = sqlite3.connect('PMeyer.db')
        c = conn.cursor()
        
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS PMeyer(mach REAL , pressure REAL , anglem REAL , anglev REAL)")

    
        def delete_previous_values():
            c.execute("DELETE FROM PMeyer")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________"+"\n"+"     M                  p/pt                    μ                    ν         " + "\n"+"___________________________________________" + "\n"

        self.ShowPM.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
        
            mang = float(m)
            if mang > 90 or mang < 5.739:
                self.ShowPM.setText("  ")
                showError="Mach angle input has to be 5.739 <= μ <= 90"
                self.ShowPM.setText(showError)
                break
            else:
                def f(ma):
                    return mang - 90 + degrees(acos(1/ma))
                ma = float (bisect(f , 1 , 100 , xtol=1e-4))
                v = "{0:.3f}".format(float(sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1))))))-((degrees(acos(1/ma))))))
                pspt = "{0:.7f}".format(((1/(gam+1))*(1+cos(radians(2*sqrt((gam-1)/(gam+1))*(float(v) + 90 - float(mang))))))**(gam/(gam-1)))
    
                c.execute("INSERT INTO PMeyer (mach , pressure , anglem , anglev) VALUES(? , ? , ? , ?)",(ma , pspt , mang , v ))
         
                showSecond = '%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), pspt, "{0:.3f}".format(mang), v)
                
                self.ShowPM.append(showSecond)
    
                conn.commit()
        create_table()

        
        
    def PMangle(self):
        
        conn = sqlite3.connect('PMeyer.db')
        c = conn.cursor()
        
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS PMeyer(mach REAL , pressure REAL , anglem REAL , anglev REAL)")

    
        def delete_previous_values():
            c.execute("DELETE FROM PMeyer")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________"+"\n"+"     M                  p/pt                    μ                    ν         " + "\n"+"___________________________________________" + "\n"


        self.ShowPM.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
        
            v = float(m)
            if v > 102.317 or v < 0:
                self.ShowPM.setText("  ")
                showError="Prandtl Meyer angle input has to be 0 <= v <= 102.317"
                self.ShowPM.setText(showError)
                break
            else:
                
                def f(ma):
                    return v - (sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1))))))-((degrees(acos(1/ma)))))
                ma = float (bisect(f , 1 , 100 , xtol=1e-4))
                mang = "{0:.3f}".format(float( float(v) + 90 - (sqrt((gam+1)/(gam-1))*((degrees(atan(sqrt(((gam-1)/(gam+1))*((ma**2)-1)))))))))
                pspt = "{0:.7f}".format(((1/(gam+1))*(1+cos(radians(2*sqrt((gam-1)/(gam+1))*(float(v) + 90 - float(mang))))))**(gam/(gam-1)))
    
                c.execute("INSERT INTO PMeyer (mach , pressure , anglem , anglev) VALUES(? , ? , ? , ?)",(ma , pspt , mang , v ))
         
                showSecond = '%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), pspt, mang, "{0:.3f}".format(v))
                
                self.ShowPM.append(showSecond)
    
                conn.commit()
        create_table()

        
###############################################################################        
##################### ISENTROPIC Functions ####################################
###############################################################################


    def machISENTROPIC(self):
        
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            ma = float(m)
            if ma > 10 or ma < 0:
                self.ShowIsentropic.setText("  ")
                showError="Mach input has to be 0 <= M <= 10"
                self.ShowIsentropic.setText(showError)
                break
            else:
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, qpt, vcss, aca)
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        

    
    def tempISENTROPIC(self):
        
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            tstt = float(m)
            if tstt > 1 or tstt < 0.047618:
                self.ShowIsentropic.setText("  ")
                showError="Temperature input has to be 0.047618 <= T/Tt <= 1"
                self.ShowIsentropic.setText(showError)
                break
            else:
                
                ma = float(math.sqrt((2*(1-m))/(m*(gam-1))))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), "{0:.5f}".format(tstt), pspt, rsrt, pdps, qpt, vcss, aca)
            
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
    def pressureISENTROPIC(self):
        
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            pspt = float(m)
            if pspt > 1 or pspt < 0.00002536:
                self.ShowIsentropic.setText("  ")
                showError="Pressure input has to be 0.00002536 <= p/pt <= 1"
                self.ShowIsentropic.setText(showError)
                break
            else:
                           
                ma = float(math.sqrt((1-m**((gam-1)/gam))/((m**((gam-1)/gam))*((gam-1)/2))))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, "{0:.5f}".format(pspt), rsrt, pdps, qpt, vcss, aca)
            
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
        
    def densityISENTROPIC(self):
        
                
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
                
            rsrt = float(m)
            if rsrt > 1 or rsrt < 0.000495:
                self.ShowIsentropic.setText("  ")
                showError="Density input has to be 0.000495 <= ρ/ρt <= 1"
                self.ShowIsentropic.setText(showError)
                break
            else:
                          
                ma = float(math.sqrt((1-m**(gam-1))/((m**((gam-1)))*((gam-1)/2))))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, "{0:.5f}".format(rsrt), pdps, qpt, vcss, aca)
            
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
        
    def dynamicISENTROPIC(self):
        
                       
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
                
            pdps = float(m)
            if pdps > 70 or pdps < 0:
                self.ShowIsentropic.setText("  ")
                showError="Dynamic pressure input has to be 0 <= q/p <= 70"
                self.ShowIsentropic.setText(showError)
                break
            else:
                               
                ma = float(math.sqrt(2*m/gam))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, "{0:.2f}".format(pdps), qpt, vcss, aca)
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()

        
    
        
    
    def lowerTotDynISENTROPIC(self):
        
                               
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
                
            qpt = float(m)
            if qpt > 0.431138 or qpt < 0:
                self.ShowIsentropic.setText("  ")
                showError="Total dynamic pressure (for M < 1.4) input has to be 0 <= q/pt <= 0.431138"
                self.ShowIsentropic.setText(showError)
                break
            else:
                        
                def f(ma):
                    return qpt-((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                ma = float( bisect(f , 0 , 1.4 , xtol = 1e-6))            
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, "{0:.5f}".format(qpt), vcss, aca)
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
        
    def greaterTotDynISENTROPIC(self):
        
                               
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
                
            qpt = float(m)
            if qpt > 0.431138 or qpt < 0.00165:
                self.ShowIsentropic.setText("  ")
                showError="Total dynamic pressure (for M > 1.4) input has to be 0.00165 <= q/pt <= 0.431138"
                self.ShowIsentropic.setText(showError)
                break
            else:
                   
                def f(ma):
                    return qpt-((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                ma = float( bisect(f , 1.4 , 100 , xtol = 1e-6))            
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, "{0:.5f}".format(qpt), vcss, aca)
                
                self.ShowIsentropic.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
        
        
    def criticalSoundISENTROPIC(self):
        
        
                                       
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            vcss = float(m)
            if vcss > 2.3905 or vcss < 0:
                self.ShowIsentropic.setText("  ")
                showError="Speed of sound input has to be 0 <= u/a* <= 2.3905"
                self.ShowIsentropic.setText(showError)
                break
            else:
                
                def f(ma):
                   return vcss-math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1)
                ma = float( bisect(f , 0 , 100 , xtol = 1e-6))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                aca = "{0:.5f}".format((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))    
    
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, qpt, "{0:.4f}".format(vcss), aca)
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
    
        
        
    def subCriticalAreaISENTROPIC(self):
        
        
                                               
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            aca = float(m)
            if aca > 1 or aca < 0:
                self.ShowIsentropic.setText("  ")
                showError="Critical area subsonic input has to be 0 <= A*/A <= 1"
                self.ShowIsentropic.setText(showError)
                break
            else:
                
                def f(ma):
                    return aca-((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
                ma = float( bisect(f , 0 , 1 , xtol = 1e-6))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
    
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, qpt, vcss, "{0:.5f}".format(aca))
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
    def supCriticalAreaISENTROPIC(self):
        
        
                                               
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
    
    
        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Isentropic(mach REAL , temperature_ratio REAL , pressure_ratio REAL , density_ratio REAL , dynamic_pressure_ratio REAL , tot_dynamic_pressure_ratio REAL , critical_speed_of_sound REAL , critical_area REAL)")
        
        
        def delete_previous_values():
            c.execute("DELETE FROM Isentropic")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________________________"+"\n"+"     M                  T/Tt                    p/pt                 ρ/ρt               q/p                q/pt                V/a*                 A*/A            " + "\n"+"____________________________________________________________________________________________" + "\n"

        self.ShowIsentropic.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
        
            aca = float(m)
            if aca > 1 or aca < 0.00187:
                self.ShowIsentropic.setText("  ")
                showError="Critical area supersonic input has to be 0.00187 <= A*/A <= 1"
                self.ShowIsentropic.setText(showError)
                break
            else:
                    
                def f(ma):
                    return aca-((((gam+1)/2)**((gam+1)/(2*(gam-1))))*ma*(1+((gam-1)/2)*(ma**2))**(-(gam+1)/(2*(gam-1))))
                ma = float( bisect(f , 1 , 100 , xtol = 1e-6))
                tstt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**-1)
                rsrt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-1/(gam-1)))
                pspt = "{0:.5f}".format((1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                pdps = "{0:.2f}".format((gam/2)*(ma**2))
                qpt = "{0:.5f}".format((gam/2)*(ma**2)*(1+(((gam-1)/2)*(ma**2)))**(-gam/(gam-1)))
                vcss = "{0:.4f}".format(math.sqrt((((gam+1)/2)*(ma**2))*(1+((gam-1)/2)*(ma**2))**-1))
    
        
                c.execute("INSERT INTO Isentropic (mach , temperature_ratio , pressure_ratio , density_ratio , dynamic_pressure_ratio , tot_dynamic_pressure_ratio , critical_speed_of_sound , critical_area ) VALUES(? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma , tstt , pspt , rsrt , pdps , qpt , vcss , aca))
                
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstt, pspt, rsrt, pdps, qpt, vcss, "{0:.5f}".format(aca))
                
                self.ShowIsentropic.append(showSecond)
            
                conn.commit()
            
        create_table()
        
        
        
    def ISENTROPICgraph(self):
        
        conn = sqlite3.connect('Isentropic.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Isentropic")
        data = c.fetchall()

        plt.close()
    
        mach = []
        temperature_ratio = []
        pressure_ratio = []
        density_ratio = []
        tot_dynamic_pressure_ratio = []
        critical_area = []

        for row in data:
            mach.append(row[0])
            temperature_ratio.append(row[1])
            pressure_ratio.append(row[2])
            density_ratio.append(row[3])
            tot_dynamic_pressure_ratio.append(row[5])
            critical_area.append(row[7])
        
        plt.figure()
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True) 
    
        plt.plot(mach,temperature_ratio,label="T/Tt")
        plt.plot(mach,pressure_ratio,label="P/Pt")
        plt.plot(mach,density_ratio,label="p/pt")
        plt.plot(mach,tot_dynamic_pressure_ratio,label="q/Pt")
        plt.plot(mach,critical_area,label="A*/A")
    
        plt.grid(True, linestyle='-')
    
        plt.xlabel("Mach Number")
        plt.ylabel("Ratio")
        plt.title("Isentropic Flow")
        plt.legend()
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
        plt.show()
        
    
        
###############################################################################        
###################### Normal Shock Function ##################################
###############################################################################

    
    def mach1NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            ma1 = float(m)
            if ma1 > 10 or ma1 < 1:
                self.ShowNormalShock.setText("  ")
                showError="Upstream mach input has to be 1 <= M1 <= 10"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, p2pt1, p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
            
    

             
        
    def mach2NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            ma2 = float(m)
            if ma2 > 1 or ma2 < 0.3876:
                self.ShowNormalShock.setText("  ")
                showError="Downstream mach input has to be 0.3876 <= M2 <= 1"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return  (ma2**2) - (((gam - 1) * (ma1 ** 2) + 2) / (2 * gam * (ma1 ** 2) - (gam - 1)))
                ma1 = float( bisect(f , 1 , 10 , xtol = 1e-4)) 
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), "{0:.4f}".format(ma2), p2p1, r2r1, t2t1, p2pt1, p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
        
           
    def P2P1NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            p2p1 = float(m)
            if p2p1 > 116.503 or p2p1 < 1:
                self.ShowNormalShock.setText("  ")
                showError="Pressure input has to be 1 <= p2/p1 <= 116.503"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                ma1 = float(math.sqrt((m*(gam+1)+(gam-1))/(2*gam)))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, "{0:.4f}".format(p2p1), r2r1, t2t1, p2pt1, p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
        
    
    
    def densityNormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            r2r1 = float(m)
            if r2r1 > 5.7143 or r2r1 < 1:
                self.ShowNormalShock.setText("  ")
                showError="Density input has to be 1 <= ρ2/ρ1 <= 5.7143"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return r2r1 - (((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                ma1 = float( bisect(f , 1 , 10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, "{0:.4f}".format(r2r1), t2t1, p2pt1, p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
       
    def temperatureNormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
   
            t2t1 = float(m)
            if t2t1 > 20.388 or t2t1 < 1:
                self.ShowNormalShock.setText("  ")
                showError="Temperature input has to be 1 <= T2/T1 <= 20.388"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return t2t1 - (((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                ma1 = float( bisect(f , 1 , 10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, "{0:.4f}".format(t2t1), p2pt1, p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
        
           
    def p2pt1LowerNormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
   
             
            p2pt1 = float(m)
            if p2pt1 < 0.5283 or p2pt1 > 0.6697:
                self.ShowNormalShock.setText("  ")
                showError="Total pressure p2/pt1 input has to be 0.5283 <= p2/pt1 <= 0.6697"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return p2pt1 - (((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                ma1 = float( bisect(f , 1 , 1.5 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, "{0:.4f}".format(p2pt1), p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
               
    def p2pt1GreaterNormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
   
             
            p2pt1 = float(m)
            if p2pt1 > 0.6697 or p2pt1 < 0.00274:
                self.ShowNormalShock.setText("  ")
                showError="Total pressure p2/pt1 input has to be 0.00274 <= p2/pt1 <= 0.6697"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return p2pt1 - (((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                ma1 = float( bisect(f , 1.5 , 10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, "{0:.4f}".format(p2pt1), p2pt2, pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
                  
    def p2pt2NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
   
             
            
            p2pt2 = float(m)
            if p2pt2 > 0.9016 or p2pt2 < 0.5283:
                self.ShowNormalShock.setText("  ")
                showError="Total pressure p2/pt2 input has to be 0.5283 <= p2/pt2 <= 0.9016"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return p2pt2 - ((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                ma1 = float( bisect(f , 1 ,10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, p2pt1, "{0:.4f}".format(p2pt2), pt2pt1, p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
                      
    def pt2pt1NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
              
            pt2pt1 = float(m)
            if pt2pt1 > 1 or pt2pt1 < 0.00304:
                self.ShowNormalShock.setText("  ")
                showError="Total pressure pt2/pt1 input has to be 0.00304 <= pt2/pt1 <= 1"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                   return pt2pt1 - (((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
                ma1 = float( bisect(f , 1 , 10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                p1pt2 = "{0:.4f}".format(1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, p2pt1, p2pt2, "{0:.4f}".format(pt2pt1), p1pt2 )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        
                          
    def p1pt2NormalShock(self):
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()


        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS NormalShock(mach1 REAL , mach2 REAL, P2P1 REAL , r2r1 REAL , T2T1 REAL , P2Pt1 REAL , P2Pt2 REAL , Pt2Pt1 REAL , P1Pt2 REAL)")
    
        def delete_previous_values():
            c.execute("DELETE FROM NormalShock")
            conn.commit()
        delete_previous_values()
        
        self.floatFunction()
        
        showFirst = "___________________________________________________________________________________________________________"+"\n"+"     M1                M2                 p2/p1               ρ2/ρ1             T2/T1              p2/pt1            p2/pt2            pt2/pt1            p1/pt2            " + "\n"+"___________________________________________________________________________________________________________" + "\n"

        self.ShowNormalShock.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
              
             
            p1pt2 = float(m)
            if p1pt2 > 0.5283 or p1pt2 < 0.00774:
                self.ShowNormalShock.setText("  ")
                showError="Total pressure pt2/pt1 input has to be 0.00304 <= p1/pt2 <= 1"
                self.ShowNormalShock.setText(showError)
                break
            else:
                
                def f(ma1):
                    return p1pt2 - (1/(((((gam+1)*(ma1**2))/2)**(gam/(gam-1)))*(((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))))
                ma1 = float( bisect(f , 1 , 10 , xtol = 1e-4))
                ma2 = "{0:.4f}".format(math.sqrt(((gam-1)*(ma1**2)+2)/(2*gam*(ma1**2)-(gam-1))))
                p2p1 = "{0:.4f}".format((2*gam*(ma1**2)-(gam-1))/(gam+1))
                r2r1 = "{0:.4f}".format(((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))
                t2t1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))*((gam-1)*(ma1**2)+2))/(((gam+1)**2)*(ma1**2)))
                p2pt1 = "{0:.4f}".format(((2*gam*(ma1**2)-(gam-1))/(gam+1))*(2/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))
                p2pt2 = "{0:.4f}".format((((4*gam*(ma1**2)-2*(gam-1))/(((gam+1)**2)*(ma1**2))))**(gam/(gam-1)))
                pt2pt1 = "{0:.4f}".format(((((gam+1)*(ma1**2))/((gam-1)*(ma1**2)+2))**(gam/(gam-1)))*((gam+1)/(2*gam*(ma1**2)-(gam-1)))**(1/(gam-1)))
        
                c.execute("INSERT INTO NormalShock (mach1  , mach2 , P2P1 , r2r1 , T2T1 , P2Pt1 , P2Pt2  , Pt2Pt1  , P1Pt2 ) VALUES(? , ? , ? , ? , ? , ? , ? , ? , ?)",
                  (ma1 , ma2 , p2p1 , r2r1 , t2t1  , p2pt1 , p2pt2 , pt2pt1 , p1pt2))
                
                            
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), ma2, p2p1, r2r1, t2t1, p2pt1, p2pt2, pt2pt1, "{0:.4f}".format(p1pt2) )
                
                self.ShowNormalShock.append(showSecond)
                
                conn.commit()
            
        create_table()
        
        

    def NormalShockGraph(self):
        
        
        conn = sqlite3.connect('NormalShock.db')
        c = conn.cursor()
        c.execute("SELECT * FROM NormalShock")
        data = c.fetchall()

        plt.close("all")
    
        mach1 = []
        mach2 = []
        P2Pt2 = []
        Pt2Pt1 = []
        P2Pt1 = []
        P1Pt2 = []
        P2P1 = []
        p2p1 = []
        T2T1 = []
   
        for row in data:
            mach1.append(row[0])
            mach2.append(row[1])
            P2Pt2.append(row[6])
            Pt2Pt1.append(row[7])
            P2Pt1.append(row[5])
            P1Pt2.append(row[8])
            P2P1.append(row[2])
            p2p1.append(row[3])
            T2T1.append(row[4])
        
    
        plt.figure(1)
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True) 
    
        plt.plot(mach1,mach2,label="M2")
        plt.plot(mach1,P2Pt2,label="P2/Pt2")
        plt.plot(mach1,Pt2Pt1,label="Pt2/Pt1")
        plt.plot(mach1,P2Pt1,label="P2/Pt1")
        plt.plot(mach1,P1Pt2,label="P1/Pt2")
    
        plt.grid(True, linestyle='-')
    
        plt.xlabel("Mach Number , M1")
        #plt.ylabel("Ratio")
        plt.title("Normal Wave Shock")
        plt.legend()
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
    
        plt.figure(2)
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True)
    
        plt.plot(mach1,P2P1,label="P2/P1")
        plt.plot(mach1,p2p1,label="p2/p1")
        plt.plot(mach1,T2T1,label="T2/T1")
    
        plt.grid(True, linestyle='-')
     
        plt.xlabel("Mach Number , M1")
        #plt.ylabel("Ratio")
        plt.title("Normal Wave Shock")
        plt.legend()
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
        plt.show()

###############################################################################
################## Oblique Shock Function #####################################
###############################################################################


    def MxObliqueShock(self):
        
        ma1 = float(self.upstreamObliqueBox.text())
        gam = float(self.gammaObliqueBox.text())
        mx = float(self.obliqueBox.text())
        
        if mx >= ma1:
            
            showError="Mx input has to be 1 <= Mx <= M1"
            self.ShowObliqueShock.setText(showError)
                
        else:

            sa = float("{0:.5f}".format(degrees(asin(mx/ma1))))
            my = float("{0:.5f}".format(sqrt((((gam-1)*(mx**2))+2)/(2*gam*(mx**2)-(gam-1)))))
            ra = float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(sa)))*((ma1**2)*((sin(radians(sa)))**2)-1)/(2+(ma1**2)*(gam+1-2*((sin(radians(sa)))**2)))))))
            ma2 = my/sin(radians(sa-ra))
            
            showFirst = "______________________________________________________________________"+"\n"+"     M1                M2                  Mx                   My                      θ                      β            " + "\n"+"______________________________________________________________________" + "\n"
    
            self.ShowObliqueShock.setText(showFirst)
            
            showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), "{0:.3f}".format(ma2), "{0:.3f}".format(mx), my, ra, sa )
                
            self.ShowObliqueShock.append(showSecond)
        
    
        
    def saObliqueShock(self):
        
        ma1 = float(self.upstreamObliqueBox.text())
        gam = float(self.gammaObliqueBox.text()) 

        sa =  float(self.obliqueBox.text())
        mx = float("{0:.5f}".format(ma1*sin(radians(sa))))
        my = float("{0:.5f}".format(sqrt((((gam-1)*(mx**2))+2)/(2*gam*(mx**2)-(gam-1)))))
        ra = float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(sa)))*((ma1**2)*((sin(radians(sa)))**2)-1)/(2+(ma1**2)*(gam+1-2*((sin(radians(sa)))**2)))))))
        ma2 = my/sin(radians(sa-ra))
              
        if ra < 0:
                  
           showError="Wave angle input has to be greater than Mach angle"
           self.ShowObliqueShock.setText(showError)
           
        else:
                  
             showFirst = "______________________________________________________________________"+"\n"+"     M1                M2                  Mx                   My                      θ                      β            " + "\n"+"______________________________________________________________________" + "\n"
        
             self.ShowObliqueShock.setText(showFirst)
                
             showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), "{0:.3f}".format(ma2), mx, my, ra, "{0:.3f}".format(sa) )
                    
             self.ShowObliqueShock.append(showSecond)
                  
                
                
    
    
    def wraObliqueShock(self):
        
        
        ma1 = float(self.upstreamObliqueBox.text())
        gam = float(self.gammaObliqueBox.text())
            
        ra = float(self.obliqueBox.text())
        def f(sa):
            return ra - degrees(atan(2*(1/tan(radians(sa)))*((ma1**2)*((sin(radians(sa)))**2)-1)/(2+(ma1**2)*(gam+1-2*((sin(radians(sa)))**2)))))
        sa = float(fsolve(f,1))
        mx = float("{0:.5f}".format(ma1*sin(radians(sa))))
        my = float("{0:.5f}".format(sqrt((((gam-1)*(mx**2))+2)/(2*gam*(mx**2)-(gam-1)))))
        ma2 = my/sin(radians(sa-ra))
        if ma2 < 1:
            showError="Ramp angle too large"
            self.ShowObliqueShock.setText(showError)
        else:
            showFirst = "______________________________________________________________________"+"\n"+"     M1                M2                  Mx                   My                      θ                      β            " + "\n"+"______________________________________________________________________" + "\n"

            self.ShowObliqueShock.setText(showFirst)
            
            showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), "{0:.3f}".format(ma2), mx, my, "{0:.5f}".format(ra), "{0:.5f}".format(sa) )
                
            self.ShowObliqueShock.append(showSecond)

            
    def sraObliqueShock(self):
        
        
        ma1 = float(self.upstreamObliqueBox.text())
        gam = float(self.gammaObliqueBox.text())
            
        ra = float(self.obliqueBox.text())
        def f(sa):
            return ra - degrees(atan(2*(1/tan(radians(sa)))*((ma1**2)*((sin(radians(sa)))**2)-1)/(2+(ma1**2)*(gam+1-2*((sin(radians(sa)))**2)))))
        sa = float(fsolve(f,90))
        mx = float("{0:.5f}".format(ma1*sin(radians(sa))))
        my = float("{0:.5f}".format(sqrt((((gam-1)*(mx**2))+2)/(2*gam*(mx**2)-(gam-1)))))
        ma2 = my/sin(radians(sa-ra))
        if ma2 > 1:
            showError="Ramp angle too large"
            self.ShowObliqueShock.setText(showError)
        else:
            showFirst = "______________________________________________________________________"+"\n"+"     M1                M2                  Mx                   My                      θ                      β            " + "\n"+"______________________________________________________________________" + "\n"

            self.ShowObliqueShock.setText(showFirst)
            
            showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma1), "{0:.3f}".format(ma2), mx, my, "{0:.5f}".format(ra), "{0:.5f}".format(sa) )
                
            self.ShowObliqueShock.append(showSecond)
            
                        
        
            

    

    def ObliqueShockGraph(self):
        
        gam = float(self.gammaObliqueBox.text())
    
        plt.close()
    
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        x6 = []
        x7 = []
        x8 = []
        x9 = []
        x10 = []

        y1 = []
        y2 = []
        y3 = []
        y4 = []
        y5 = []
        y6 = []
        y7 = []
        y8 = []
        y9 = []
        y10 = []
    

        for m in floatRange.frange(56.5,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((1.2**2)*((sin(radians(m)))**2)-1)/(2+(1.2**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x1.append(ra)
            y1.append(m)
    
        for m in floatRange.frange(45.6,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((1.4**2)*((sin(radians(m)))**2)-1)/(2+(1.4**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x2.append(ra)
            y2.append(m)   
        
        for m in floatRange.frange(38.7,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((1.6**2)*((sin(radians(m)))**2)-1)/(2+(1.6**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x3.append(ra)
            y3.append(m)
        
        for m in floatRange.frange(33.8,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((1.8**2)*((sin(radians(m)))**2)-1)/(2+(1.8**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x4.append(ra)
            y4.append(m)
  
        for m in floatRange.frange(30,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((2**2)*((sin(radians(m)))**2)-1)/(2+(2**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x5.append(ra)
            y5.append(m)  
        
        for m in floatRange.frange(23.6,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((2.5**2)*((sin(radians(m)))**2)-1)/(2+(2.5**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x6.append(ra)
            y6.append(m) 
        
        for m in floatRange.frange(19.5,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((3**2)*((sin(radians(m)))**2)-1)/(2+(3**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x7.append(ra)
            y7.append(m) 
        
        for m in floatRange.frange(14.5,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((4**2)*((sin(radians(m)))**2)-1)/(2+(4**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x8.append(ra)
            y8.append(m) 
        
        for m in floatRange.frange(11.6,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((5**2)*((sin(radians(m)))**2)-1)/(2+(5**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x9.append(ra)
            y9.append(m) 
        
        for m in floatRange.frange(5.8,90,0.1):
            ra =float("{0:.5f}".format(degrees(atan(2*(1/tan(radians(m)))*((10**2)*((sin(radians(m)))**2)-1)/(2+(10**2)*(gam+1-2*((sin(radians(m)))**2)))))))
            x10.append(ra)
            y10.append(m) 
        
        plt.figure()
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True)
    
        plt.plot(y1,x1)    
        plt.plot(y2,x2) 
        plt.plot(y3,x3)
        plt.plot(y4,x4)
        plt.plot(y5,x5)
        plt.plot(y6,x6)
        plt.plot(y7,x7)
        plt.plot(y8,x8)
        plt.plot(y9,x9)
        plt.plot(y10,x10)
    
        plt.text(64, 5, '1.2')
        plt.text(64, 10, '1.4')
        plt.text(64, 15, '1.6')
        plt.text(64, 20, '1.8')
        plt.text(64, 24, '2')
        plt.text(64, 31, '2.5')
        plt.text(65, 35, '3')
        plt.text(65, 39, '4')
        plt.text(65, 42, '5')
        plt.text(65, 46, '10')
     
        plt.grid(True, linestyle='-')
    
        plt.xlabel("Shock angle")
        plt.ylabel("Ramp angle")
    
    
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
        plt.show()

###############################################################################
########################### Fanno Function  ###################################
###############################################################################


    def machFANNO(self):
        
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            ma = float(m)
            if ma < 0.1 or ma > 10:
                self.ShowFanno.setText("  ")
                showError="Mach input has to be 0.1 <= pt2/pt1 <= 10"
                self.ShowFanno.setText(showError)
                break
            else:
                
                tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
                pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
                fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
        
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, ptptc, uuc, fld)
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
    def temperatureFANNO(self):
        
                
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
                
            tstc = float(m)
            if tstc > 1.19760 or tstc < 0.05714:
                self.ShowFanno.setText("  ")
                showError="Temperature input has to be 0.05714 <= T/T* <= 1.19760"
                self.ShowFanno.setText(showError)
                break
            else:
                
                def f(ma):
                    return tstc - ((gam + 1)/(2+(gam-1)*(ma**2)))
                ma = float (bisect(f , 0.1 , 10 , xtol= 1e-5))
                pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
                fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
        
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), "{0:.5f}".format(tstc), pspsc, ptptc, uuc, fld)
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        
      
    def staticpFANNO(self):
        
               
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
             
            pspsc = float(m)
            if pspsc > 10.94351 or pspsc < 0.02390:
                self.ShowFanno.setText("  ")
                showError="Static pressure input has to be 0.02390 <= p/p* <= 10.94351"
                self.ShowFanno.setText(showError)
                break
            else:
                
                def f(ma):
                    return pspsc - ((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                ma =  float (bisect(f , 0.1 , 10 , xtol= 1e-5))
                tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
                ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
                fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
        
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, "{0:.5f}".format(pspsc), ptptc, uuc, fld)
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        
    
    def totalLowerFANNO(self):
        
        
                      
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
                
            ptptc = float(m)
            if ptptc > 5.833 or ptptc < 1:
                self.ShowFanno.setText("  ")
                showError="Total pressure (for M < 1) input has to be 1 <= pt/pt* <= 5.833"
                self.ShowFanno.setText(showError)
                break
            else:
                
                def f(ma):
                    return ptptc - ((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                ma = float (bisect(f , 0.1 , 1 , xtol= 1e-5))
                tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
                pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
                fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
        
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, "{0:.5f}".format(ptptc), uuc, fld)
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        

        
    def totalGreaterFANNO(self):
        
        
                      
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
                
            ptptc = float(m)
            if ptptc > 535.938 or ptptc < 1:
                self.ShowFanno.setText("  ")
                showError="Total pressure (for M > 1) input has to be 1 <= pt/pt* <= 535.938"
                self.ShowFanno.setText(showError)
                break
            def f(ma):
                return ptptc - ((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
            ma = float (bisect(f , 1 , 10 , xtol= 1e-5))
            tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
            pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
            uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
            fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
    
    
            c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
              (ma , tstc , pspsc , ptptc , uuc , fld ))
     
            showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, "{0:.5f}".format(ptptc), uuc, fld)
            
            self.ShowFanno.append(showSecond)
    
            conn.commit()
            
        create_table()
        
    
            
    def speedFANNO(self):
        
        
                      
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            uuc = float(m)
            if uuc > 2.39046 or uuc < 0.10944:
                self.ShowFanno.setText("  ")
                showError="Speed input has to be 0.10944 <= u/u* <= 2.39046"
                self.ShowFanno.setText(showError)
                break
            def f(ma):
                 return uuc - (ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
            ma = float (bisect(f , 0.1 , 10 , xtol= 1e-5))    
            tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
            pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
            ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
            fld ="{0:.5f}".format((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
    
    
            c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
              (ma , tstc , pspsc , ptptc , uuc , fld ))
     
            showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, ptptc, "{0:.5f}".format(uuc), fld)
            
            self.ShowFanno.append(showSecond)
    
            conn.commit()
            
        create_table()
        
        
               
    def fldLowerFANNO(self):
        
        
                      
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
             
            fld = float(m)
            if fld > 66.92158 or fld < 0:
                self.ShowFanno.setText("  ")
                showError="f (Lcr / D)  (for M < 1) input has to be 0 <= f (Lcr / D) <= 66.92158"
                self.ShowFanno.setText(showError)
                break
            else:
                
                def f(ma):
                    return fld - ((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
                ma = float (bisect(f , 0.1 , 1 , xtol=1e-5 )) 
                tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
                pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, ptptc, uuc, "{0:.5f}".format(fld))
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
                   
    def fldGreaterFANNO(self):
        
        
                      
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Fanno (mach REAL , temperature REAL , static_pressure REAL , total_pressure REAL , speed REAL , fLcrD REAL )")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Fanno")
            conn.commit()
        delete_previous_values()
        
                
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  T/T*                 p/p*               pt/pt*              u/u*               f(Lcr/D)         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowFanno.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
             
            fld = float(m)
            if fld > 0.78683 or fld < 0:
                self.ShowFanno.setText("  ")
                showError="f (Lcr / D)  (for M > 1) input has to be 0 <= f (Lcr / D) <= 0.78683"
                self.ShowFanno.setText(showError)
                break
            else:
                
                def f(ma):
                    return fld - ((1/gam)*((1/(ma**2))-1) + ((gam+1)/(2*gam))*log((((gam+1)/2)*(ma**2))/(1+((gam-1)/2)*(ma**2))))
                ma = float (bisect(f , 1 , 10 , xtol=1e-5 )) 
                tstc ="{0:.5f}".format((gam + 1)/(2+(gam-1)*(ma**2)))
                pspsc ="{0:.5f}".format((((sqrt((gam+1)/(2+(gam-1)*(ma**2))))))/ma)
                ptptc ="{0:.3f}".format((((2+((gam-1)*(ma**2)))/(gam+1))**((gam+1)/(2*(gam-1))))/ma)
                uuc ="{0:.5f}".format(ma*(sqrt((gam + 1)/(2+(gam-1)*(ma**2)))))
        
                c.execute("INSERT INTO Fanno ( mach , temperature , static_pressure , total_pressure , speed , fLcrD  ) VALUES( ? , ? , ? , ? , ? , ? )",
                  (ma , tstc , pspsc , ptptc , uuc , fld ))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), tstc, pspsc, ptptc, uuc, "{0:.5f}".format(fld))
                
                self.ShowFanno.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
        
        
        
    def FANNOgraph(self):
               
        conn = sqlite3.connect('Fanno.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM Fanno")
        data = c.fetchall()

        plt.close()
        mach = []
        temperature = []
        static_pressure = []
        total_pressure = []
        speed = []
        fLcrD = []

        for row in data:
            mach.append(row[0])
            temperature.append(row[1])
            static_pressure.append(row[2])
            total_pressure.append(row[3])
            speed.append(row[4])
            fLcrD.append(row[5])
        
        plt.figure()
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True)
    
        ax1 = fig.add_subplot(111) 
    
        ax1.plot(mach,temperature,label="T/T*")
        ax1.plot(mach,static_pressure,label="p/p*")
        ax1.plot(mach,total_pressure,label="pt/pt*")
        ax1.plot(mach,speed,label="u/u*")
        
        ax1.grid(True, linestyle='-')

        plt.legend()
    
        ax2 = ax1.twinx()
        ax2.grid(False)
        ax2.plot(mach,fLcrD,label="4fLcr/D",color = 'm')
#        ax2.text(1, 0.5, '4fLcr/D')
    
        ax1.set_xlabel("Mach Number")
        ax1.set_ylabel("Ratio")
        ax2.set_ylabel("Ratio")
    
        plt.title("Fanno Flow")
    
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
    
        plt.show()
        
###############################################################################    
######################## Rayleigh Function ####################################
###############################################################################

    
    def machRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
             
            ma = float(m)
            if ma > 10 or ma < 0:
                self.ShowRayleigh.setText("  ")
                showError="Mach input has to be 0 <= M <= 10"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, tstc, pspsc, ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
     
    def totalLowerTempRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            ttc = float(m)
            if ttc > 1 or ttc < 0:
                self.ShowRayleigh.setText("  ")
                showError="Total temperature (for M < 1) input has to be 0 <= Tt/Tt* <= 1"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                   return ttc - (2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                ma =  float (bisect(f , 0 , 1 , xtol= 1e-5))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), "{0:.5f}".format(ttc), tstc, pspsc, ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
    def totalGreaterTempRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            ttc = float(m)
            if ttc > 1 or ttc < 0.50702:
                self.ShowRayleigh.setText("  ")
                showError="Total temperature (for M > 1) input has to be 0 <= Tt/Tt* <= 1"
                self.ShowRayleigh.setText(showError)
                break
            else:

                def f(ma):
                   return ttc - (2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                ma =  float (bisect(f , 1 , 10 , xtol= 1e-5))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), "{0:.5f}".format(ttc), tstc, pspsc, ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
         
    def lowerTempRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            tstc = float(m)
            if tstc > 1.02854 or tstc < 0:
                self.ShowRayleigh.setText("  ")
                showError="Temperature (for M < 1) input has to be 0 <= T/T* <= 1.02854"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                    return tstc - (((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2)
                ma =  float (bisect(f , 0 , 1 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, "{0:.5f}".format(tstc), pspsc, ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
          
    def greaterTempRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            tstc = float(m)
            if tstc > 1 or tstc < 0.02897:
                self.ShowRayleigh.setText("  ")
                showError="Temperature (for M > 1) input has to be 0.02897 <= T/T* <= 1"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                    return tstc - (((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2)
                ma =  float (bisect(f , 1 , 10 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, "{0:.5f}".format(tstc), pspsc, ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
              
    def pressureRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            pspsc = float(m)
            if pspsc > 2.4 or pspsc < 0.10702:
                self.ShowRayleigh.setText("  ")
                showError="Pressure input has to be 0.10702 <= p/p* <=  2.4"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                    return pspsc - ((gam+1)/(1+gam*(ma**2)))
                ma =  float (bisect(f , 0 , 10 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, tstc, "{0:.5f}".format(pspsc), ptptc, uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
                  
    def totalLowerPressureRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            ptptc = float(m)
            if ptptc > 1.268 or ptptc < 1:
                self.ShowRayleigh.setText("  ")
                showError="Total pressure (for M < 1) input has to be 1 <= pt/pt* <=  1.268"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                    return ptptc - (((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                ma =  float (bisect(f , 0 , 1 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, tstc, pspsc, "{0:.3f}".format(ptptc), uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
                      
    def totalGreaterPressureRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            ptptc = float(m)
            if ptptc > 381.615 or ptptc < 1:
                self.ShowRayleigh.setText("  ")
                showError="Total pressure (for M > 1) input has to be 1 <= pt/pt* <=  381.615"
                self.ShowRayleigh.setText(showError)
                break
            else:
                
                def f(ma):
                    return ptptc - (((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
                ma =  float (bisect(f , 1 , 10 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                uuc = "{0:.5f}".format(((gam+1)*(ma**2))/(1+(gam*(ma**2))))
        
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, tstc, pspsc, "{0:.3f}".format(ptptc), uuc)
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
                      
    def speedRAYLEIGH(self):
        
        
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()

        def create_table():
            c.execute("CREATE TABLE IF NOT EXISTS Rayleigh (mach REAL , total_temperature REAL , temperature REAL , pressure REAL , total_pressure REAL , speed REAL)")
    
    
        def delete_previous_values():
            c.execute("DELETE FROM Rayleigh")
            conn.commit()
        delete_previous_values()
        
                 
        self.floatFunction()
        
        showFirst = "____________________________________________________________________________"+"\n"+"     M                  Tt/Tt*                 T/T*               p/p*              pt/pt*               u/u*         " + "\n"+"____________________________________________________________________________" + "\n"


        self.ShowRayleigh.setText(showFirst)
        
        for m in floatRange.frange(start,end,inc):
            
            
            uuc = float(m)
            if uuc > 1.70213 or uuc < 0:
                self.ShowRayleigh.setText("  ")
                showError="Speed input has to be 0 <= u/u* <=  1.70213"
                self.ShowRayleigh.setText(showError)
                break
            else:
                    
                def f(ma):
                    return uuc - (((gam+1)*(ma**2))/(1+(gam*(ma**2))))
                ma =  float (bisect(f , 0 , 10 , xtol= 1e-5))
                ttc = "{0:.5f}".format(2*(gam+1)*(1+((gam-1)/2)*(ma**2))*(ma**2)*((1+(gam*(ma**2)))**(-2)))
                tstc = "{0:.5f}".format((((gam+1)**2)*(ma**2))/((1+(gam*(ma**2)))**2))
                pspsc = "{0:.5f}".format((gam+1)/(1+gam*(ma**2)))
                ptptc = "{0:.3f}".format(((gam+1)/(1+(gam*(ma**2))))*(((1+((gam-1)/2)*(ma**2))/((gam+1)/2))**(gam/(gam-1))))
        
        
                c.execute("INSERT INTO Rayleigh ( mach , total_temperature , temperature , pressure , total_pressure , speed) VALUES ( ? , ? , ? , ? , ? , ?)", 
                  (ma , ttc , tstc , pspsc , ptptc , uuc))
         
                showSecond = '%-18s%-18s%-18s%-18s%-18s%-18s' % ("{0:.3f}".format(ma), ttc, tstc, pspsc, ptptc, "{0:.5f}".format(uuc))
                
                self.ShowRayleigh.append(showSecond)
        
                conn.commit()
            
        create_table()
        
        
        
    def RAYLEIGHgraph(self):
        
         
        conn = sqlite3.connect('Rayleigh.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM Rayleigh")
        data = c.fetchall()

        plt.close()
    
        mach = []
        total_temperature = []
        temperature = []
        pressure = []
        total_pressure = []
    

        for row in data:
            mach.append(row[0])
            total_temperature.append(row[1])
            temperature.append(row[2])
            pressure.append(row[3])
            total_pressure.append(row[4])
        
        plt.figure()
    
        fig = plt.gcf()
        fig.set_size_inches(12, 9, forward=True)    
        
        plt.plot(mach,total_temperature,label="Tt/Tt*")
        plt.plot(mach,temperature,label="T/T*")
        plt.plot(mach,pressure,label="p/p*")
        plt.plot(mach,total_pressure,label="pt/pt*")

    
        plt.grid(True, linestyle='-')
    
        plt.xlabel("Mach Number")
        plt.ylabel("Ratio")
        plt.title("Rayleigh Flow")
        plt.legend()
        plt.subplots_adjust(top=0.90 ,bottom=0.10 ,left=0.10 , right=0.95 )
        plt.show()
        
###############################################################################
###############################################################################
###############################################################################        
        
        
if __name__ == '__main__':
    
    
	app = QApplication(sys.argv)
	mainwindow = QMainWindow()
 
	PyQtSkeleton = MyFirstGuiProgram(mainwindow)
 
	mainwindow.show()
	sys.exit(app.exec_())      