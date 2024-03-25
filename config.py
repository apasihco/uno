#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os
from os import getenv

TOKEN = "6993345701:AAHLw4mF2FbssqjEMieFIba-PKcWa1vKi0c"
WORKERS = int(os.getenv("WORKERS", 32))
ADMIN_LIST = os.getenv("ADMIN_LIST", "")

if isinstance(ADMIN_LIST, str):
    ADMIN_LIST = set(int(x) for x in ADMIN_LIST.split())

OPEN_LOBBY = os.getenv("OPEN_LOBBY","")
ENABLE_TRANSLATIONS = os.getenv("ENABLE_TRANSLATIONS", "")

if isinstance(OPEN_LOBBY, str):
    OPEN_LOBBY = OPEN_LOBBY.lower() in ("yes", "true", "t", "1")

if isinstance(ENABLE_TRANSLATIONS, str):
    ENABLE_TRANSLATIONS = ENABLE_TRANSLATIONS.lower() in ("yes", "true", "t", "1")

DEFAULT_GAMEMODE = os.getenv("DEFAULT_GAMEMODE", "fast")
WAITING_TIME = int(os.getenv("WAITING_TIME", 120))
TIME_REMOVAL_AFTER_SKIP = int(os.getenv("TIME_REMOVAL_AFTER_SKIP", 20))
MIN_FAST_TURN_TIME = int(os.getenv("MIN_FAST_TURN_TIME", 15))
MIN_PLAYERS = int(os.getenv("MIN_PLAYERS", 2))
