def select_Activity(activities):
  k=0
  out=set()
  if len(activities):
    out.add(0)
  activities.sort(key=lambda x:x[1])
  for i in range(1,len(activities)):
    if activities[i][0]>=activities[k][1]:
      out.add(i)
      k=i
   return out
activities=[(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
                (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
result=select_Activity(activities)
print(activities[i] for i in result)
