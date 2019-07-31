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
    self.trans = []
    self.spheres = None 
    self.generated = False 
  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    l = slicer.modules.createmodels.logic()
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)

    self.parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    self.parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(self.parametersCollapsibleButton)
    
    self.parametersFormLayout = qt.QFormLayout(self.parametersCollapsibleButton)
     
    self.connectButton = qt.QPushButton()
    self.connectButton.setDefault(False)
    self.connectButton.text = "Click to connect" 
    self.parametersFormLayout.addWidget(self.connectButton)
    
    self.pathText = qt.QLabel("Please place hands within view")
    self.parametersFormLayout.addRow(self.pathText)
    
    self.generateButton = qt.QPushButton()
    self.generateButton.setDefault(False)
    self.generateButton.text = "Generate Hands" 
    self.parametersFormLayout.addWidget(self.generateButton)
    
    
    self.connectButton.connect('clicked(bool)', self.onConnectButtonClicked)
    self.generateButton.connect('clicked(bool)', self.generateCylinders)
    self.layout.addStretch(1)
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
      for j in range(0, len(self.models)): 
        if 'Cyl' in self.models[j].GetName():
          slicer.mrmlScene.RemoveNode(self.models[j])
      for i in range (0, self.n):
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
