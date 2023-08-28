#country information using countryinfo module

from countryinfo import CountryInfo
country = input("Enter country: ")

i = CountryInfo(country).info()
for _ in i:
    print(_ + ": " + str(i[_]))


