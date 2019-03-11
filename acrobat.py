from pypresence import Presence as ps, Activity
from time import sleep as sp, time as tm
import win32gui
import win32process
import sys
import psutil
def get_process():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd):
            if 'Adobe' in win32gui.GetWindowText(hwnd):
                print(win32gui.GetWindowText(hwnd))
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    try:
        if ('- Adobe Acrobat Reader DC' in win32gui.GetWindowText(hwnds[0])):
            return win32gui.GetWindowText(hwnds[0]).replace('- Adobe Acrobat Reader DC', '')
        else:
            return 'Seaching...'
    except:
        for proc in psutil.process_iter():
            if 'acrobat.exe' in proc.name():
                proc.kill()
rp = ps('553048619440275486')
rp.connect()
a = int(tm())
while True:
    rp.update(details=get_process(), start=a, large_text="peep main lee desd season 0.1", large_image="acrobat2", state='Ҳуҷҷати интиқоли ҳуҷҷат')
    sp(5)
