""" Alternativa
wmp11 (Fixes missing logo videos and problems with working videos)
hangs on logo without override
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.set_environment('WINEDLLOVERRIDES', 'libvkd3d-1=n')
    util.protontricks('wmp11')