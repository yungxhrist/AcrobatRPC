from pypresence import Presence as ps, Activity
from process import sktup as sk
from time import sleep as sp, time as tm
rp = ps('553048619440275486')
rp.connect()
a = int(tm())
while True:
    rp.update(details=sk(), start=a, large_text="peep main lee desd season 0.1", large_image="acrobat2", state='Ҳуҷҷати интиқоли ҳуҷҷат')
    sp(15)
