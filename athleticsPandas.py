import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

bball = pd.read_csv('./Rosters - Bball.csv', header=0)
crew = pd.read_csv('./Rosters - crew.csv', header=0)
crosscountry = pd.read_csv('./Rosters - crosscountry.csv', header=0)
fencing = pd.read_csv('./Rosters - Fencing.csv', header=0)
fhockey = pd.read_csv('./Rosters - Field Hockey.csv', header=0)
golf = pd.read_csv('./Rosters - golf.csv', header=0)
lax = pd.read_csv('./Rosters - Lax.csv', header=0)
soccer = pd.read_csv('./Rosters - Soccer.csv', header=0)
sball = pd.read_csv('./Rosters - Softball.csv', header=0)
swive = pd.read_csv('./Rosters - Swive.csv', header=0)
tennis = pd.read_csv('./Rosters - tennis.csv', header=0)
track = pd.read_csv('./Rosters - Track&Field.csv', header=0)
vball = pd.read_csv('./Rosters - volleyball.csv', header=0)

listofAllRosters = [bball,crew,crosscountry,fencing,fhockey,golf,lax,soccer,sball,swive,tennis,track,vball]
# the header = 0 parameter indicates that the column
# names are in the first row

print(bball.head()) # useful for looking at the top few rows
print(bball.columns)

bballTeamSize = bball.groupby(['Year']).count()
bballTeamSize = bballTeamSize[['Name']]
print(bballTeamSize)

xcTeamSize = crosscountry.groupby(['Year']).count()
xcTeamSize = xcTeamSize[['Name']]
print(xcTeamSize)

fenTeamSize = fencing.groupby(['Year']).count()
fenTeamSize = fenTeamSize[['Name']]
print(fenTeamSize)

fhTeamSize = fhockey.groupby(['Year']).count()
fhTeamSize = fhTeamSize[['Name']]
print(fhTeamSize)

gTeamSize = golf.groupby(['Year']).count()
gTeamSize = gTeamSize[['Name']]
print(gTeamSize)

laxTeamSize = lax.groupby(['Year']).count()
laxTeamSize = laxTeamSize[['Name']]
print(laxTeamSize)

socTeamSize = soccer.groupby(['Year']).count()
socTeamSize = socTeamSize[['Name']]
print(socTeamSize)

sbTeamSize = sball.groupby(['Year']).count()
sbTeamSize = sbTeamSize[['Name']]
print(sbTeamSize)

tenTeamSize = tennis.groupby(['Year']).count()
tenTeamSize = tenTeamSize[['Name']]
print(tenTeamSize)

tfTeamSize = track.groupby(['Year']).count()
tfTeamSize = tfTeamSize[['Name']]
print(tfTeamSize)

vbTeamSize = vball.groupby(['Year']).count()
vbTeamSize = vbTeamSize[['Name']]
print(vbTeamSize)

swiveTeamSize = swive.groupby(['Year']).count()
swiveTeamSize = swiveTeamSize[['Name']]
print(swiveTeamSize)

crewTeamSize = crew.groupby(['Year']).count()
crewTeamSize = crewTeamSize[['Name']]
print(crewTeamSize)

years = list(['(2010-2011)',
'(2011-2012)',
'(2012-2013)',
'(2013-2014)',
'(2014-2015)',
'(2015-2016)',
'(2016-2017)',
'(2017-2018)',
'(2018-2019)',
'(2019-2020)',
'(2020-2021)'])
print(years)

fig, ax = plt.subplots()
ax.plot(years, crewTeamSize, label="crew")
ax.plot(years, swiveTeamSize, label="swive")
ax.plot(years, bballTeamSize, label="bball")
ax.plot(years, xcTeamSize, label="cross country")
ax.plot(years, fenTeamSize, label="fencing")
ax.plot(years, fhTeamSize, label="field hockey")
ax.plot(years, gTeamSize, label="golf")
ax.plot(years, laxTeamSize, label="Lacrosse")
ax.plot(years, socTeamSize, label="soccer")
ax.plot(years, sbTeamSize, label="softball")
ax.plot(years, tenTeamSize, label="tennis")
ax.plot(years, tfTeamSize, label="track & field")
ax.plot(years, vbTeamSize, label="volleyball")

ax.legend()
plt.title('Wellesley Varsity Athletics Team Size over the last 10 years')
plt.xlabel('Seasons')
plt.ylabel('Number of Team members')


print(plt.show())

