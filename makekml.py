import simplekml
import sqldata
from sqldata import listt


sqldata.main()
k=sqldata.listt
print(k)
kml = simplekml.Kml() 
for point in k: 
    kml.newpoint (coords=[(point [0], point [1])])
kml.save ("theee.kml")