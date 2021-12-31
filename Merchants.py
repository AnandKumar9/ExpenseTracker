from enum import Enum

class Expense:
    rawMerchantName = None
    merchantName = None
    category = None
    transactionDate = None
    transactionAmount = None

    def __init__(self, rawMerchantName, merchantName, category, transactionDate, transactionAmount):
        self.rawMerchantName = rawMerchantName
        self.merchantName = merchantName
        self.category = category
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount

class ExpenseCategory(Enum):
    Groceries = 'Groceries'
    Meal = 'Meal'
    Coffee = 'Coffee, etc.'
    FastFood = 'Fast Food'
    Gas = 'Gas, Parking, Tolls'
    Car = 'Car'
    HouseRent = 'House Rent'
    ElectricityBill = 'Electricity Bill'
    WaterBill = 'Water Bill'
    GasBill = 'Gas Bill'
    Healthcare = 'Healthcare'
    HouseholdStuff = 'Household Stuff'
    Streaming = 'Streaming Services'
    Movies = 'Movies'
    BooksAndMagazines = 'Books, Magazines'
    ClothesAndShoes = 'Clothes And Shoes'
    Other1 = 'Other 1'
    Other2 = 'Other 2'
    AllElse = 'All Else'
    Unknown = 'Unknown'

merchants = {

    # Groceries
    'ADITI': ('Aditi Spice Depot', ExpenseCategory.Groceries),
    'COSTCO': ('Costco', ExpenseCategory.Groceries),
    'GIANT': ('Giant', ExpenseCategory.Groceries),
    'HARRIS': ('Harris Teeter', ExpenseCategory.Groceries),
    'INDIAN SPICES': ('Indian Spices', ExpenseCategory.Groceries),
    'PATEL BROTHER': ('Patel Brothers', ExpenseCategory.Groceries),
    'WHOLEFDS': ('Whole Foods', ExpenseCategory.Groceries),

    # Meal
    'A2B - HERNDON': ('A2B', ExpenseCategory.Meal),
    'BAWARCHI': ('Bawarchi', ExpenseCategory.Meal),
    'BAGEL CAFE': ('Bagel Cafe', ExpenseCategory.Meal),
    'BUSBOYS AND POETS': ('Busboys and Poets', ExpenseCategory.Meal),
    'BUFFALO': ('Buffalo Wild Wings', ExpenseCategory.Meal),
    'CAVA PIKE 7 PLAZA': ('Cava', ExpenseCategory.Meal),
    'CHINA EXPRESS': ('China Express', ExpenseCategory.Meal),
    'CRUST PIZZERIA NAPOLET': ('Crust', ExpenseCategory.Meal),
    'DISTRICT TACO 5723': ('District Taco', ExpenseCategory.Meal),
    'DOMINO\'S': ('Domino\'s', ExpenseCategory.Meal),
    'FIRST WATCH': ('First Watch', ExpenseCategory.Meal),
    'HONG KONG PALACE': ('Hong Kong Palace', ExpenseCategory.Meal),
    'IHOP': ('IHOP', ExpenseCategory.Meal),
    'NOODLES': ('Noodles & Co', ExpenseCategory.Meal),
    'MCDONALDS': ('McDonald\'s', ExpenseCategory.Meal),
    'MOBY': ('Moby Dick', ExpenseCategory.Meal),
    'NATTA THAI CUISINE': ('Natta Thai', ExpenseCategory.Meal),
    'OLIVE': ('Olive Garden', ExpenseCategory.Meal),
    'PANERA': ('Panera Bread', ExpenseCategory.Meal),
    'PASTRY CORNER': ('Pastry Corner', ExpenseCategory.Meal),
    'PEKING': ('Peking Express', ExpenseCategory.Meal),
    'PIND INDIAN CUISINE': ('Pind Cuisine', ExpenseCategory.Meal),
    'PIZZA HUT': ('Pizza Hut', ExpenseCategory.Meal),
    'QDOBA': ('QDoba', ExpenseCategory.Meal),
    'ROLL PLAY TYSONS': ('Roll Play', ExpenseCategory.Meal),
    'PARADISE BIRYANI P': ('Paradise Pointe Biryani', ExpenseCategory.Meal),
    'SideBar': ('SideBar', ExpenseCategory.Meal),
    'Subway': ('Subway', ExpenseCategory.Meal),
    'SWEET LEAF': ('Sweet Leaf', ExpenseCategory.Meal),
    'SWEETLEAF': ('Sweet Leaf', ExpenseCategory.Meal),
    'SWEETGREEN': ('Sweet Green', ExpenseCategory.Meal),
    'TARA THAI RESTAURANT': ('Tara Thai', ExpenseCategory.Meal),
    'TOOSSO PAKISTANI': ('Toosso', ExpenseCategory.Meal),
    'WOODLANDS RESTAURANT': ('Woodlands', ExpenseCategory.Meal),

    # Coffee
    'DUNKIN': ('Dunkin\' Donuts', ExpenseCategory.Coffee),
    'KUNG FU TEA': ('Kung Fu Tea', ExpenseCategory.Coffee),
    'SHARE TEA': ('Share Tea', ExpenseCategory.Coffee),
    'STARBUCKS': ('Starbucks', ExpenseCategory.Coffee),

    # Fast Food
    'BASKIN': ('Baskin Robbins', ExpenseCategory.FastFood),
    'BEN & JERRY\'S': ('Ben & Jerry\'s', ExpenseCategory.FastFood),
    'COLDSTONE': ('Coldstone', ExpenseCategory.FastFood),
    'DUCK DONUTS HERNDON, V': ('Duck Donuts', ExpenseCategory.FastFood),
    'JENI\'S SPLENDID I': ('Jeni\'s Splendid Ice Cream', ExpenseCategory.FastFood),

    # House Rent
    'AVALON': ('Avalon Tysons Corner', ExpenseCategory.HouseRent),
    'STATE FARM INSURANCE': ('State Farm Insurance', ExpenseCategory.HouseRent),

    # Electricity Bill
    'DOMINION': ('Dominion Energy', ExpenseCategory.ElectricityBill),

    # Gas Bill
    'WASHINGTON GAS': ('Washington Gas', ExpenseCategory.GasBill),

    # Water Bill
    'AVALON WATER': ('Water Bill, Conservice', ExpenseCategory.WaterBill),

    # Gas
    'COSTCO GAS': ('Costco Gas', ExpenseCategory.Gas),
    'EXXONMOBIL': ('Exxon', ExpenseCategory.Gas),
    'E Z PASS VA WEB': ('EZ Pass', ExpenseCategory.Gas),
    'SHELL': ('Shell Oil', ExpenseCategory.Gas),
    'SUNOCO': ('Sunoco', ExpenseCategory.Gas),

    # Car
    'BMW OF FAIRFAX': ('BMW', ExpenseCategory.Car),
    'PROGRESSIVE': ('Progressive Car Insurance', ExpenseCategory.Car),

    # Healthcare
    'CVS/SPECIALTY': ('CVS/SPECIALTY', ExpenseCategory.Healthcare),
    'SGF': ('SGF', ExpenseCategory.Healthcare),

    # Household Stuff
    'IKEA': ('Ikea', ExpenseCategory.HouseholdStuff),
    'TARGET': ('Target', ExpenseCategory.HouseholdStuff),

    # Streaming Services
    'Amazon Prime': ('Amazon Prime', ExpenseCategory.Streaming),
    'APPLE.COM/BILL': ('Apple TV', ExpenseCategory.Streaming),
    'Audible': ('Audible', ExpenseCategory.Streaming),
    'HELP.HBOMAX.COM': ('HBO', ExpenseCategory.Streaming),
    'Prime Video': ('Prime Video Rental', ExpenseCategory.Streaming),
    'Spotify USA': ('Spotify', ExpenseCategory.Streaming),
    'SXM*SIRIUSXM.COM/ACCT': ('SiriusXM', ExpenseCategory.Streaming),
    'VUDU.COM': ('Vudu', ExpenseCategory.Streaming),

    # Books, Magazines
    'NYTimes*NYTimes': ('NYTimes', ExpenseCategory.BooksAndMagazines),
    'RAZ*BLACKCURRANT APPS': ('Splainer', ExpenseCategory.BooksAndMagazines),
    'Washington Post': ('Washington Post', ExpenseCategory.BooksAndMagazines),

    # Clothes and Shoes
    'BANANA REPUBLIC': ('Banana Republic', ExpenseCategory.ClothesAndShoes),
    'TEEPUBLIC': ('Tee Public', ExpenseCategory.ClothesAndShoes),

    # All Else
    '7-ELEVEN': ('7-Eleven', ExpenseCategory.AllElse),
    'BATH & BODY WORKS 3050': ('Bath & Body Works', ExpenseCategory.AllElse),
    'CVS/PHARMACY': ('CVS', ExpenseCategory.AllElse),
    'HAIR CUTTERY': ('Hair Cuttery', ExpenseCategory.AllElse),
    'STAPLES': ('Staples', ExpenseCategory.AllElse),
}