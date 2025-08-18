database = [("Relapse: refill edition", 2009, "29 tracks"),
            ("Encore: deluxe", 2004, "23 tracks"),
            ("Eminem show: expanded edition", 2022 , "32 tracks"),
            ("revival", 2017, "17 tracks")]
year, tracks = lambda release: release[1], lambda tracks_count: tracks_count[2]
user = input("welcome to eminem discography! tell me which order you want to go with:" \
"tracks, name, or the year? ")
if user == 'tracks':
    database.sort(key = tracks)
    for i in database:
        print(f"{i[0]} it has {i[2][:2]} tracks!")
elif user == 'year':
        database.sort(key = year)
        for i in database:
             print(f"{i[0]} was released on {i[1]}...")
else: 
         database.sort()
         for i in database:
               print(i[0])
relapse_tracklist = (("must be the ganja", 14),
                     ('Dr.west', 1),
                     ('3 a.m', 2))
#if you have a tuple of tuples:
#sorted_eminem = sorted(relapse_tracklist)
#for i in sorted_eminem: print(i)