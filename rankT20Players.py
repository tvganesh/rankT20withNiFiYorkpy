import yorkpy.analytics as yka
rank=yka.rankIPLT20Batting("/Users/tvganesh/backup/software/nifi/ipldata")
print(rank.head(15))
