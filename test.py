months = ["jan", "feb", "mar","apirl","may","june","july","Aug","sep","oct","nov","dec"]
endings = ['st','nd','rd'] + 17*['th']+['st']+['nd']+['rd']+7*['th']+['st']
year = input('year is:')
month = input ('month is:')
day = input ('day is :')
months_ned = month-1


if len(months) < months_ned:
    print "Range is out of months listed"
    quit()
print (str(day)+(endings[day-1]), months_ned,months[months_ned])
