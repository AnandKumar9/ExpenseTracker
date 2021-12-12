import enum
from enum import Enum

class MerchantCategory(Enum):
    Groceries = 'Groceries'
    Meal = 'Meal'
    Coffee = 'Coffee, etc.'
    FastFood = 'Fast Food',
    Gas = 'Gas, Parking, Tolls'
    Car = 'Car'
    HouseRent = 'House Rent'
    ElectricityBill = 'Electricity Bill'
    WaterBill = 'Water Bill'
    GasBill = 'Gas Bill'
    HouseholdStuff = 'Household Stuff'
    Streaming = 'Streaming Services'
    Movies = 'Movies'
    BooksAndMagazines = 'Books, Magazines',
    ClothesAndShoes = 'Clothes And Shoes'
    Other1 = 'Other 1'
    Other2 = 'Other 2'
    AllElse = 'All Else'

merchants = {

    # Groceries
    'ADITI': ('Aditi Spice Depot', MerchantCategory.Groceries),
    'GIANT': ('Giant', MerchantCategory.Groceries),
    'HARRIS': ('Harris Teeter', MerchantCategory.Groceries),
    'INDIAN SPICES': ('Indian Spices', MerchantCategory.Groceries),
    'PATEL BROTHER': ('Patel Brothers', MerchantCategory.Groceries),
    'WHOLEFDS': ('Whole Foods', MerchantCategory.Groceries),

    # Meal
    'TST* A2B - HERNDON': ('A2B', MerchantCategory.Meal),
    'BAWARCHI': ('Bawarchi', MerchantCategory.Meal),
    'BUSBOYS AND POETS': ('Busboys and Poets', MerchantCategory.Meal),
    'BUFFALO': ('Buffalo Wild Wings', MerchantCategory.Meal),
    'CAVA PIKE 7 PLAZA': ('Cava', MerchantCategory.Meal),
    'CHINA EXPRESS': ('China Express', MerchantCategory.Meal),
    'CRUST PIZZERIA NAPOLET': ('Crust', MerchantCategory.Meal),
    'DISTRICT TACO 5723': ('District Taco', MerchantCategory.Meal),
    'DOMINO\'S': ('Domino\'s', MerchantCategory.Meal),
    'HONG KONG PALACE': ('Hong Kong Palace', MerchantCategory.Meal),
    'IHOP': ('IHOP', MerchantCategory.Meal),
    'OLIVE': ('Olive Garden', MerchantCategory.Meal),
    'NOODLES': ('Noodles & Co', MerchantCategory.Meal),
    'MCDONALDS': ('McDonald\'s', MerchantCategory.Meal),
    'MOBY': ('Moby Dick', MerchantCategory.Meal),
    'NATTA THAI CUISINE': ('Natta Thai', MerchantCategory.Meal),
    'PANERA': ('Panera Bread', MerchantCategory.Meal),
    'PASTRY CORNER': ('Pastry Corner', MerchantCategory.Meal),
    'PEKING': ('Peking Express', MerchantCategory.Meal),
    'PIND INDIAN CUISINE': ('Pind Cuisine', MerchantCategory.Meal),
    'PIZZA HUT': ('Pizza Hut', MerchantCategory.Meal),
    'QDOBA': ('QDoba', MerchantCategory.Meal),
    'TST* ROLL PLAY TYSONS': ('Roll Play', MerchantCategory.Meal),
    'PARADISE BIRYANI P': ('Paradise Pointe Biryani', MerchantCategory.Meal),
    'SideBar': ('SideBar', MerchantCategory.Meal),
    'Subway': ('Subway', MerchantCategory.Meal),
    'SWEET LEAF': ('Sweet Leaf', MerchantCategory.Meal),
    'SWEETGREEN': ('Sweet Green', MerchantCategory.Meal),
    'TARA THAI RESTAURANT': ('Tara Thai', MerchantCategory.Meal),
    'TST* TOOSSO PAKISTANI': ('Toosso', MerchantCategory.Meal),
    'WOODLANDS RESTAURANT': ('Woodlands', MerchantCategory.Meal),

    # Coffee
    'DUNKIN': ('Dunkin\' Donuts', MerchantCategory.Coffee),
    'KUNG FU TEA': ('Kung Fu Tea', MerchantCategory.Coffee),
    'SHARE TEA': ('Share Tea', MerchantCategory.Coffee),
    'STARBUCKS': ('Starbucks', MerchantCategory.Coffee),

    # Fast Food
    'BASKIN': ('Baskin Robbins', MerchantCategory.FastFood),
    'BEN & JERRY\'S': ('Ben & Jerry\'s', MerchantCategory.FastFood),
    'COLDSTONE': ('Coldstone', MerchantCategory.FastFood),
    'DUCK DONUTS HERNDON, V': ('Duck Donuts', MerchantCategory.FastFood),
    'JENI\'S SPLENDID I': ('Jeni\'s Splendid Ice Cream', MerchantCategory.FastFood),

    # House Rent
    'STATE FARM  INSURANCE': ('State Farm Insurance', MerchantCategory.HouseRent),

    # Gas
    'EXXONMOBIL': ('Exxon', MerchantCategory.Gas),
    'SHELL': ('Shell Oil', MerchantCategory.Gas),
    'SUNOCO': ('Sunoco', MerchantCategory.Gas),

    # Household Stuff
    'TARGET': ('Target', MerchantCategory.HouseholdStuff),

    # Streaming Services
    'Amazon Prime': ('Amazon Prime', MerchantCategory.Streaming),
    'APPLE.COM/BILL': ('Apple', MerchantCategory.Streaming),
    'HELP.HBOMAX.COM': ('HBO', MerchantCategory.Streaming),
    'Spotify USA': ('Spotify', MerchantCategory.Streaming),
    'SXM*SIRIUSXM.COM/ACCT': ('SiriusXM', MerchantCategory.Streaming),
    'VUDU.COM': ('Vudu', MerchantCategory.Streaming),

    # Books, Magazines
    'NYTimes*NYTimes': ('NYTimes', MerchantCategory.BooksAndMagazines),
    'RAZ*BLACKCURRANT APPS': ('Splainer', MerchantCategory.BooksAndMagazines),
    'TWP*PROMO43231056': ('Washington Post', MerchantCategory.BooksAndMagazines),

    # Clothes and Shoes
    'TEEPUBLIC': ('Tee Public', MerchantCategory.ClothesAndShoes),

    # All Else
    '7-ELEVEN': ('7-Eleven', MerchantCategory.AllElse),
    'BATH & BODY WORKS 3050': ('Bath & Body Works', MerchantCategory.AllElse),
    'CVS/PHARMACY': ('CVS', MerchantCategory.AllElse),
    'HAIR CUTTERY': ('Hair Cuttery', MerchantCategory.AllElse),
    'STAPLES': ('Staples', MerchantCategory.AllElse),
}