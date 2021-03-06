# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.client.enclosure import Enclosure

'''
API for the functions that affect the Mark 1 device.
NOTE: current state management is poorly implemented,
will be changed in the future.
'''


class EnclosureArduino(Enclosure):
    """
    Listens to enclosure commands for Mycroft's Arduino.

    Performs the associated command on Arduino by writing on the Serial port.
    """

    def __init__(self, ws, writer):
        super(EnclosureArduino, self).__init__(ws, "arduino")
        self.writer = writer

    def reset(self, event=None):
        self.writer.write("system.reset")

    def mute(self, event=None):
        self.writer.write("system.mute")

    def unmute(self, event=None):
        self.writer.write("system.unmute")

    def blink(self, event=None):
        times = 1
        if event and event.data:
            times = event.data.get("times", times)
        self.writer.write("system.blink=" + str(times))
