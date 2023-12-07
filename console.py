#!/user/bin/python3
"""Different modules for entry point of cmd interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

"""class definition for this file is:"""
class HBNBCommand(cmd.Cmd):

prompt = "(hbnb)"


