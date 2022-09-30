import simplekml
from polycircles import polycircles
import subprocess
import pandas as pd

p=simplekml.Kml()
p.newpoint(name='monish', coords=[(-116.995704,33.097877)])
pp= "C:\\xampp\\htdocs\\last\\test3.kml"
p.save(pp)
subprocess.call(['open', pp])