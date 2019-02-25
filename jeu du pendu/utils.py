#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utils.py
#
#  Copyright 2019 Master Dell Universo <tux@master-desktop>
#

def removeAccent(lettre):
	try:
		"""Enlève l'accent sur les caractères accentués"""
		import unicodedata
		decomp = unicodedata.decomposition(lettre)

		if decomp:
			car = decomp.split(" ")[0]
			return chr(int(car, 16))
		return lettre
	except:
		return lettre
