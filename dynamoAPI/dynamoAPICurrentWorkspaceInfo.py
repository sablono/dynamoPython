"""
DYNAMOAPI: GET CURRENT WORKSPACE PATH AND FILE NAME FOR DYNAMO ON ALL HOST VERSIONS
"""
__author__ = 'Brendan cassidy'
__twitter__ = '@brencass86'
__version__ = '1.0.0'
"""
"""
# we need to import the common language runtime to be able to interact with Dynamo & Revit

# Importing Reference Modules
# CLR ( Common Language Runtime Module )
import clr
# Adding the DynamoServices.dll module to work with the Dynamo API
clr.AddReference('DynamoServices')
from Dynamo.Events import *

# Access to the current Dynamo workspace path(eg location of the opened dynamo file)
currentWorkspacePath = ExecutionEvents.ActiveSession.CurrentWorkspacePath

# Gets the File Name with file type
fileName = currentWorkspacePath.split("\\")[-1]

# Removes the dyn File type from the end of the file name
FileNameWithoutFileType = fileName.replace(".dyn","")

# Outputs the full file path, file name with file type and just file name
OUT = currentWorkspacePath, fileName, FileNameWithoutFileType