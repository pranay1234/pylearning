months = ["jan", "feb", "mar","apirl","may","june","july","Aug","sep","oct","nov","dec"]
endings = ['st','nd','rd'] + 17*['th']+['st']+['nd']+['rd']+7*['th']+['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
month_name = months[month_number-1]
ordinal = str(day_number) +  endings[day_number-1]
print (month_name + ' ' + ordinal + ', ' + str(year))
print "Test"

