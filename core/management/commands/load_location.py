from django.core.management.base import BaseCommand
from core.models import Continent, Country

class Command(BaseCommand):
    help = 'Select Country based on chosen Continent'

    def handle(self, *args, **kwargs):
        Country.objects.all().delete()
        continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania/Australia']
        if not Continent.objects.count():
            for continent in continents:
                Continent.objects.create(continent=continent)

        #AFRICA
        africa = Continent.objects.get(continent='Africa')
        african_countries = [
           ' Algeria',
            'Angola',
            'Benin',
            'Botswana',
            'Burkina Faso',
            'Burundi',
            'Cabo Verde/Cape Verde',
            'Cameroon',
            'Central African Republic',
            'Chad',
            'Comoros',
            'Congo/Republic of the Congo',
            'Democratic Republic of the Congo',
            'Djibouti',
            'Egypt',
            'Equatorial Guinea',
            'Eritrea',
            'Eswatini (formerly Swaziland)',
            'Ethiopia',
            'Gabon',
            'Gambia',
            'Ghana',
            'Guinea',
            'Guinea-Bissau',
            "Ivory Coast/Republic of Côte d'Ivoire",
            'Kenya',
            'Lesotho',
            'Liberia',
            'Libya',
            'Madagascar',
            'Malawi',
            'Mali',
            'Mauritania',
            'Mauritius',
            'Morocco',
            'Mozambique',
            'Namibia',
            'Niger',
            'Nigeria',
            'Rwanda',
            'Sao Tome and Principe',
            'Senegal',
            'Seychelles',
            'Sierra Leone',
            'Somalia',
            'South Africa',
            'South Sudan',
            'Sudan',
            'Tanzania',
            'Togo',
            'Tunisia',
            'Uganda',
            'Zambia',
            'Zimbabwe'
        ]
        for african_country in african_countries:
            Country.objects.create(country=african_country, continent=africa)


        #ASIA
        asia = Continent.objects.get(continent='Asia')
        asian_countries = [
            'Afghanistan',
            'Armenia',
            'Azerbaijan',
            'Bahrain',
            'Bangladesh',
            'Bhutan',
            'Brunei',
            'Cambodia',
            'China',
            'Cyprus',
            'Georgia',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Israel',
            'Japan',
            'Jordan',
            'Kazakhstan',
            'Kuwait',
            'Kyrgyzstan',
            'Laos',
            'Lebanon',
            'Macau',
            'Malaysia',
            'Maldives',
            'Mongolia',
            'Myanmar',
            'Nepal',
            'North Korea',
            'Oman',
            'Pakistan',
            'Palestine',
            'Philippines',
            'Qatar',
            'Saudi Arabia',
            'Singapore',
            'South Korea(Republic of Korea)',
            'Sri Lanka',
            'Syria',
            'Taiwan',
            'Tajikistan',
            'Thailand',
            'Timor-Leste/East Timor',
            'Turkmenistan',
            'United Arab Emirates',
            'Uzbekistan',
            'Vietnam',
            'Yemen',
        ]
        for asian_country in asian_countries:
            Country.objects.create(continent=asia, country=asian_country)


        #EUROPE
        europe = Continent.objects.get(continent='Europe')
        european_countries = [
            'Albania',
            'Andorra',
            'Austria',
            'Belarus',
            'Belgium',
            'Bosnia and Herzegovina',
            'Bulgaria',
            'Croatia',
            'Cyprus',
            'Czechia/Czech Republic',
            'Denmark',
            'Estonia',
            'Finland',
            'France',
            'Germany',
            'Greece',
            'Hungary',
            'Iceland',
            'Ireland',
            'Italy',
            'Latvia',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Malta',
            'Moldova',
            'Monaco',
            'Montenegro',
            'Netherlands',
            'North Macedonia',
            'Norway',
            'Poland',
            'Portugal',
            'Romania',
            'Russia',
            'San Marino',
            'Serbia',
            'Slovakia',
            'Slovenia',
            'Spain',
            'Sweden',
            'Switzerland',
            'Turkey',
            'Ukraine',
            'United Kingdom',
            'Vatican City (Holy See)'
        ]
        for european_country in european_countries:
            Country.objects.create(continent = europe, country=european_country)


        #NORTH AMERICA
        north_america = Continent.objects.get(continent = 'North America')
        north_american_countries = [
            'Antigua and Barbuda',
            'Bahamas',
            'Barbados',
            'Belize',
            'Canada',
            'Costa Rica',
            'Cuba',
            'Dominica',
            'Dominican Republic',
            'El Salvador',
            'Grenada',
            'Guatemala',
            'Haiti',
            'Honduras',
            'Jamaica',
            'Mexico',
            'Nicaragua',
            'Panama',
            'Saint Kitts and Nevis',
            'Saint Lucia',
            'Saint Vincent and the Grenadines',
            'Trinidad and Tobago',
            'United States of America'
        ]
        for north_american_country in north_american_countries:
            Country.objects.create(continent=north_america,country=north_american_country)


        #OCEANIA
        oceania = Continent.objects.get(continent = 'Oceania/Australia')
        oceanian_countries = [
            'Australia',
            'Fiji',
            'Kiribati',
            'Marshall Islands',
            'Micronesia (The Federated States of)',
            'Nauru',
            'New Zealand',
            'Palau',
            'Papua New Guinea',
            'Samoa',
            'Solomon Islands',
            'Tonga',
            'Tuvalu',
            'Vanuatu'
        ]
        for oceanian_country in oceanian_countries:
            Country.objects.create(continent=oceania,country = oceanian_country)


        #SOUTH AMERICA
        south_america = Continent.objects.get(continent='South America')
        south_american_countries = [
            'Argentina',
            'Bolivia',
            'Brazil',
            'Chile',
            'Colombia',
            'Ecuador',
            'Guyana',
            'Paraguay',
            'Peru',
            'Suriname',
            'Uruguay',
            'Venezuela'
        ]
        for south_american_country in south_american_countries:
            Country.objects.create(continent=south_america,country=south_american_country)

        return