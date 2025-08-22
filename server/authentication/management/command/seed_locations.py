from django.core.management.base import BaseCommand
from server.authentication.models import Province, District, Location 

class Command(BaseCommand):
    help = 'List all property titles'

    def handle(self, *args, **kwargs):
        location_data = {
            "Koshi Province": {
                "Jhapa": ["Birtamode", "Damak", "Mechinagar"],
                "Morang": ["Biratnagar", "Rangeli", "Urlabari"],
                "Sunsari": ["Inaruwa", "Itahari", "Dharan"],
                "Ilam": ["Ilam", "Suryodaya"],
                "Dhankuta": ["Dhankuta"],
                "Bhojpur": ["Bhojpur"],
                "Udayapur": ["Gaighat"],
                "Sankhuwasabha": ["Khandbari"],
                "Taplejung": ["Taplejung"],
                "Terhathum": ["Myanglung"],
                "Panchthar": ["Phidim"],
                "Khotang": ["Diktel"],
                "Okhaldhunga": ["Okhaldhunga"],
                "Solukhumbu": ["Salleri"]
            },
            "Madhesh Province": {
                "Saptari": ["Rajbiraj", "Kanchanrup"],
                "Siraha": ["Siraha"],
                "Dhanusha": ["Janakpur"],
                "Mahottari": ["Jaleshwar"],
                "Sarlahi": ["Malangwa"],
                "Rautahat": ["Gaur"],
                "Bara": ["Kalaiya"],
                "Parsa": ["Birgunj"]
            },
            "Bagmati Province": {
                "Kathmandu": ["Kathmandu", "Kirtipur", "Tokha"],
                "Lalitpur": ["Lalitpur", "Godawari"],
                "Bhaktapur": ["Bhaktapur"],
                "Chitwan": ["Bharatpur", "Ratnanagar"],
                "Makwanpur": ["Hetauda"],
                "Dhading": ["Dhadingbesi"],
                "Nuwakot": ["Bidur"],
                "Rasuwa": ["Dhunche"],
                "Sindhupalchok": ["Chautara"],
                "Dolakha": ["Charikot"],
                "Ramechhap": ["Manthali"],
                "Sindhuli": ["Sindhulimadi"],
                "Kavrepalanchok": ["Banepa", "Panauti"]
            },
            "Gandaki Province": {
                "Kaski": ["Pokhara"],
                "Lamjung": ["Besisahar"],
                "Tanahun": ["Damauli"],
                "Gorkha": ["Gorkha"],
                "Syangja": ["Putalibazar"],
                "Parbat": ["Kushma"],
                "Baglung": ["Baglung"],
                "Myagdi": ["Beni"],
                "Mustang": ["Jomsom"],
                "Manang": ["Chame"],
                "Nawalpur": ["Kawasoti"]
            },
            "Lumbini Province": {
                "Rupandehi": ["Butwal", "Siddharthanagar"],
                "Kapilvastu": ["Taulihawa"],
                "Parasi": ["Ramgram"],
                "Palpa": ["Tansen"],
                "Arghakhanchi": ["Sandhikharka"],
                "Gulmi": ["Tamghas"],
                "Dang": ["Ghorahi", "Tulsipur"],
                "Banke": ["Nepalgunj"],
                "Bardiya": ["Gulariya"],
                "Eastern Rukum": ["Rukumkot"],
                "Rolpa": ["Liwang"],
                "Pyuthan": ["Pyuthan"]
            },
            "Karnali Province": {
                "Surkhet": ["Birendranagar"],
                "Dailekh": ["Dailekh"],
                "Jajarkot": ["Khalanga"],
                "Dolpa": ["Dunai"],
                "Jumla": ["Chandannath"],
                "Mugu": ["Gamgadhi"],
                "Humla": ["Simikot"],
                "Kalikot": ["Manma"],
                "Salyan": ["Sharada"],
                "Western Rukum": ["Musikot"]
            },
            "Sudurpashchim Province": {
                "Kailali": ["Dhangadhi", "Tikapur"],
                "Kanchanpur": ["Mahendranagar"],
                "Dadeldhura": ["Dadeldhura"],
                "Doti": ["Dipayal"],
                "Achham": ["Mangalsen"],
                "Bajura": ["Martadi"],
                "Bajhang": ["Chainpur"],
                "Baitadi": ["Dasharathchand"],
                "Darchula": ["Darchula"]
            }
        }

        for province_name, districts in location_data.items():
            province, created = Province.objects.get_or_create(name=province_name)
            for district_name, locations in districts.items():
                district_obj, created = District.objects.get_or_create(name=district_name, province=province)
                for location_name in locations:
                    Location.objects.get_or_create(name=location_name, district=district_obj)

        self.stdout.write(self.style.SUCCESS('Successfully seeded locations.'))