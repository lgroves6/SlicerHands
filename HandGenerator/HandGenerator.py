import sys 
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import numpy as np 
#
# HandGenerator
#

class HandGenerator(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "HandGenerator" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
    self.parent.helpText += self.getDefaultModuleDocumentationLink()
    self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

#
# HandGeneratorWidget
#

class HandGeneratorWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  def __init__(self, parent=None):
    ScriptedLoadableModuleWidget.__init__(self, parent)
    slicer.mymod = self
    self.connectorNode = None
    self.Node = None
    self.Node1 = None
    self.Node2 = None
    self.Node3 = None
    self.Node4 = None
    self.Node5 = None
    self.Node6 = None
    self.Node7 = None
    self.Node8 = None
    self.Node9 = None
    self.Node10 = None
    self.Node11 = None
    self.Node12 = None
    self.Node13 = None
    self.Node14 = None
    
    self.NodeX = None
    self.NodeX1 = None
    self.NodeX2 = None
    self.NodeX3 = None
    self.NodeX4 = None
    self.NodeX5 = None
    self.NodeX6 = None
    self.NodeX7 = None
    self.NodeX8 = None
    self.NodeX9 = None
    self.NodeX10 = None
    self.NodeX11 = None
    self.NodeX12 = None
    self.NodeX13 = None
    self.NodeX14 = None
    self.counterLD = 0
    self.mat = vtk.vtkMatrix4x4()   
    self.counter = 0 
    self.LPPI = None 
    self.LL = 0 
    self.RL = 0
    self.mag = []
    self.trans = []
    self.spheres = None 
    self.generated = False 
  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    l = slicer.modules.createmodels.logic()
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
    
    
    
    # self.LDP = l.CreateSphere(5)
    # self.LDP.SetName('LDP')
    # self.LDR = l.CreateSphere(5)
    # self.LDR.SetName('LDR')
    # self.LDM = l.CreateSphere(5)
    # self.LDM.SetName('LDM')
    # self.LDI = l.CreateSphere(5)
    # self.LDI.SetName('LDI')
    # self.LDT = l.CreateSphere(5)
    # self.LDT.SetName('LDT')
    
    # self.LDP.GetDisplayNode().SetColor(0,0,1)
    # self.LDR.GetDisplayNode().SetColor(0,0,1)
    # self.LDM.GetDisplayNode().SetColor(0,0,1)
    # self.LDI.GetDisplayNode().SetColor(0,0,1)
    # self.LDT.GetDisplayNode().SetColor(0,0,1)
    
    # self.LIP = l.CreateSphere(5)
    # self.LIP.SetName('LIP')
    # self.LIR = l.CreateSphere(5)
    # self.LIR.SetName('LIR')
    # self.LIM = l.CreateSphere(5)
    # self.LIM.SetName('LIM')
    # self.LII = l.CreateSphere(5)
    # self.LII.SetName('LII')
    # self.LIT = l.CreateSphere(5)
    # self.LIT.SetName('LIT')
    
    # self.LIP.GetDisplayNode().SetColor(0,1,0)
    # self.LIR.GetDisplayNode().SetColor(0,1,0)
    # self.LIM.GetDisplayNode().SetColor(0,1,0)
    # self.LII.GetDisplayNode().SetColor(0,1,0)
    # self.LIT.GetDisplayNode().SetColor(0,1,0)
    
    # self.LPP = l.CreateSphere(5)
    # self.LPP.SetName('LPP')
    # self.LPR = l.CreateSphere(5)
    # self.LPR.SetName('LPR')
    # self.LPM = l.CreateSphere(5)
    # self.LPM.SetName('LPM')
    # self.LPI = l.CreateSphere(5)
    # self.LPI.SetName('LPI')
    # self.LPT = l.CreateSphere(5)
    # self.LPT.SetName('LPT')
    # self.LPP.GetDisplayNode().SetColor(1,0,0)
    # self.LPR.GetDisplayNode().SetColor(1,0,0)
    # self.LPM.GetDisplayNode().SetColor(1,0,0)
    # self.LPI.GetDisplayNode().SetColor(1,0,0)
    # self.LPT.GetDisplayNode().SetColor(1,0,0)
    # self.RDP = l.CreateSphere(5)
    # self.RDP.SetName('RDP')
    # self.RDR = l.CreateSphere(5)
    # self.RDR.SetName('RDR')
    # self.RDM = l.CreateSphere(5)
    # self.RDM.SetName('RDM')
    # self.RDI = l.CreateSphere(5)
    # self.RDI.SetName('RDI')
    # self.RDT = l.CreateSphere(5)
    # self.RDT.SetName('RDT')
    
    # self.RDP.GetDisplayNode().SetColor(0,0,1)
    # self.RDR.GetDisplayNode().SetColor(0,0,1)
    # self.RDM.GetDisplayNode().SetColor(0,0,1)
    # self.RDI.GetDisplayNode().SetColor(0,0,1)
    # self.RDT.GetDisplayNode().SetColor(0,0,1)
    
    # self.RIP = l.CreateSphere(5)
    # self.RIP.SetName('RIP')
    # self.RIR = l.CreateSphere(5)
    # self.RIR.SetName('RIP')
    # self.RIM = l.CreateSphere(5)
    # self.RIM.SetName('RIM')
    # self.RII = l.CreateSphere(5)
    # self.RII.SetName('RII')
    # self.RIT = l.CreateSphere(5)
    # self.RIT.SetName('RIT')
    
    # self.RIP.GetDisplayNode().SetColor(0,1,0)
    # self.RIR.GetDisplayNode().SetColor(0,1,0)
    # self.RIM.GetDisplayNode().SetColor(0,1,0)
    # self.RII.GetDisplayNode().SetColor(0,1,0)
    # self.RIT.GetDisplayNode().SetColor(0,1,0)
    
    # self.RPP = l.CreateSphere(5)
    # self.RPP.SetName('RPP')
    # self.RPR = l.CreateSphere(5)
    # self.RPR.SetName('RPR')
    # self.RPM = l.CreateSphere(5)
    # self.RPM.SetName('RPM')
    # self.RPI = l.CreateSphere(5)
    # self.RPI.SetName('RPI')
    # self.RPT = l.CreateSphere(5)
    # self.RPT.SetName('RPT')
    
    # self.RPP.GetDisplayNode().SetColor(1,0,0)
    # self.RPR.GetDisplayNode().SetColor(1,0,0)
    # self.RPM.GetDisplayNode().SetColor(1,0,0)
    # self.RPI.GetDisplayNode().SetColor(1,0,0)
    # self.RPT.GetDisplayNode().SetColor(1,0,0)
    
    # self.LP = l.CreateSphere(5)
    # self.LP.GetDisplayNode().SetColor(1,1,1)
    
    # self.RP = l.CreateSphere(5)
    # self.RP.GetDisplayNode().SetColor(1,1,1)


    self.parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    self.parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(self.parametersCollapsibleButton)
    
    self.parametersFormLayout = qt.QFormLayout(self.parametersCollapsibleButton)
     
    self.connectButton = qt.QPushButton()
    self.connectButton.setDefault(False)
    self.connectButton.text = "Click to connect" 
    self.parametersFormLayout.addWidget(self.connectButton)
    
    # self.leftCheck = qt.QCheckBox()
    # self.leftCheck.text = "Check for left hand"
    # self.parametersFormLayout.addWidget(self.leftCheck)
    # self.rightCheck = qt.QCheckBox()
    # self.rightCheck.text = "Check for right hand"
    # self.parametersFormLayout.addWidget(self.rightCheck)
    
    self.pathText = qt.QLabel("Please place hands within view")
    self.parametersFormLayout.addRow(self.pathText)
    
    self.generateButton = qt.QPushButton()
    self.generateButton.setDefault(False)
    self.generateButton.text = "Generate Hands" 
    self.parametersFormLayout.addWidget(self.generateButton)
    
    
    # self.updateButton = qt.QPushButton()
    # self.updateButton.setDefault(False)
    # self.updateButton.text = "Update" 
    # self.parametersFormLayout.addWidget(self.updateButton)
    
    self.connectButton.connect('clicked(bool)', self.onConnectButtonClicked)
    self.generateButton.connect('clicked(bool)', self.generateCylinders)
    # self.updateButton.connect('clicked(bool)', self.update)
    self.layout.addStretch(1)
    # slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, self.onTransformChanged)
  def onConnectButtonClicked(self):
    if self.connectorNode is not None: 
      self.connectorNode = None
      self.connectCheck = 1
      self.connectButton.text = 'Click to connect'
    else:
      self.connectorNode = slicer.vtkMRMLIGTLConnectorNode()
      slicer.mrmlScene.AddNode(self.connectorNode) 
      self.connectorNode.SetTypeClient('localhost', 18944)
      self.connectorNode.Start() 
      self.connectCheck = 0  
      self.connectButton.text = 'Connected'

  def generateCylinders(self):
    if self.generated == False:
      self.nodes = slicer.util.getNodesByClass('vtkMRMLLinearTransformNode')
      self.n = len(self.nodes)
      l = slicer.modules.createmodels.logic()
      mat = vtk.vtkMatrix4x4()
      self.generated = True 
      # self.generated = True
      for i in range (0, self.n):
        if 'Left' in self.nodes[i].GetName() or 'Right' in self.nodes[i].GetName():
          if 'Dis' in self.nodes[i].GetName() or 'Int' in self.nodes[i].GetName() or 'Prox' in self.nodes[i].GetName() or 'Meta' in self.nodes[i].GetName():
            self.spheres = l.CreateSphere(3)
            self.spheres.SetAndObserveTransformNodeID(self.nodes[i].GetID())
            self.spheres.SetName('Sphere'+self.nodes[i].GetName())
            self.Zshift = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
            self.Zshift.SetName('Zshift')
            self.length = float(self.nodes[i].GetAttribute('lengthMm'))
            mat.SetElement(2,3,self.length/2)
            self.Zshift.SetAndObserveMatrixTransformToParent(mat)
            self.Zshift.SetAndObserveTransformNodeID(self.nodes[i].GetID())
            self.cyl = l.CreateCylinder(self.length-1.5, 1.5)
            self.cyl.SetAndObserveTransformNodeID(self.Zshift.GetID())
            self.cyl.SetName('Cyl'+self.nodes[i].GetName())
    else:
      self.nodes = slicer.util.getNodesByClass('vtkMRMLLinearTransformNode')
      self.n = len(self.nodes)
      self.models = slicer.util.getNodesByClass('vtkMRMLModelNode')
      mat = vtk.vtkMatrix4x4()
      l = slicer.modules.createmodels.logic()
      for j in range(0, len(self.models)-1): 
        if 'Cyl' in self.models[j].GetName():
          slicer.mrmlScene.RemoveNode(self.models[j])
      for i in range (0, self.n-1):
        if 'Zshift' in self.nodes[i].GetName(): 
          slicer.mrmlScene.RemoveNode(self.nodes[i])
        if 'Left' in self.nodes[i].GetName() or 'Right' in self.nodes[i].GetName():
          if 'Dis' in self.nodes[i].GetName() or 'Int' in self.nodes[i].GetName() or 'Prox' in self.nodes[i].GetName() or 'Meta' in self.nodes[i].GetName():
            self.Zshift = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
            self.Zshift.SetName('Zshift')
            self.length = float(self.nodes[i].GetAttribute('lengthMm'))
            mat.SetElement(2,3,self.length/2)
            self.Zshift.SetAndObserveMatrixTransformToParent(mat)
            self.Zshift.SetAndObserveTransformNodeID(self.nodes[i].GetID())
            self.cyl = l.CreateCylinder(self.length-1.5, 1.5)
            self.cyl.SetAndObserveTransformNodeID(self.Zshift.GetID())
  