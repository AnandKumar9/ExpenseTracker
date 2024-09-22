from enum import Enum

class Expense:
    rawMerchantName = None
    merchantName = None
    category = None
    transactionDate = None
    transactionAmount = None
    isShared = None

    def __init__(self, rawMerchantName, merchantName, category, transactionDate, transactionAmount, isShared):
        self.rawMerchantName = rawMerchantName
        self.merchantName = merchantName
        self.category = category
        self.transactionDate = transactionDate
        self.transactionAmount = transactionAmount
        self.isShared = isShared

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
    'HELLO 2 INDIA': ('Hello 2 India', ExpenseCategory.Groceries),
    'INDIAN SPICES': ('Indian Spices', ExpenseCategory.Groceries),
    'MORE GROCERIES': ('More Groceries', ExpenseCategory.Groceries),
    'PATEL BROTHER': ('Patel Brothers', ExpenseCategory.Groceries),
    'PATEL BROTHERS ASHBURN': ('Patel Brothers', ExpenseCategory.Groceries),
    'WHOLEFDS': ('Whole Foods', ExpenseCategory.Groceries),

    # Meal
    'A2B - HERNDON': ('A2B', ExpenseCategory.Meal),
    'AMK CAPITAL ONE C1': ('Office cafeteria', ExpenseCategory.Meal),
    'AMKCAPITAL ONE C2': ('Office cafeteria', ExpenseCategory.Meal),
    'BAWARCHI': ('Bawarchi', ExpenseCategory.Meal),
    'BAGEL CAFE': ('Bagel Cafe', ExpenseCategory.Meal),
    'BAR LOUIE - ASHBU': ('Bar Louie', ExpenseCategory.Meal),
    'BOMBAY CAFE': ('Bombay Cafe', ExpenseCategory.Meal),
    'BUSBOYS AND POETS': ('Busboys and Poets', ExpenseCategory.Meal),
    'BUFFALO': ('Buffalo Wild Wings', ExpenseCategory.Meal),
    'CAFEIN.': ('Cafein', ExpenseCategory.Meal),
    'CAFEIN CENTREVILLE': ('Cafein', ExpenseCategory.Meal),
    'CAVA': ('Cava', ExpenseCategory.Meal),
    '10010D CAVA BELMONT': ('Cava', ExpenseCategory.Meal),
    'CAFE HYDERABAD CHU': ('Cafe Hyderabad Chutney\'s', ExpenseCategory.Meal),
    'CHICK-FIL-A': ('Chick-Fil-A', ExpenseCategory.Meal),
    'CHINA EXPRESS': ('China Express', ExpenseCategory.Meal),
    'CHOPT CREATIVE SALAD C': ('Chopt', ExpenseCategory.Meal),
    'CHIPOTLE': ('Chipotle', ExpenseCategory.Meal),
    'CHINA EXPRESS': ('China Express', ExpenseCategory.Meal),
    'COUNTRY OVEN': ('Country Oven', ExpenseCategory.Meal),
    'CRUST PIZZERIA NAPOLET': ('Crust', ExpenseCategory.Meal),
    'CRUST PIZZERIA VIE': ('Crust', ExpenseCategory.Meal),
    'DECLIEU COFFEE & SANDW': ('DeClieu Coffee & Sandwich', ExpenseCategory.Meal),
    'DISTRICT TACO 5723': ('District Taco', ExpenseCategory.Meal),
    'COOKNSOLO - DIZEN': ('Dizengoff', ExpenseCategory.Meal),
    'DOMINO\'S': ('Domino\'s', ExpenseCategory.Meal),
    'DWARAKAS BAWARCHI': ('Bawarchi Centreville', ExpenseCategory.Meal),
    'FIRST WATCH': ('First Watch', ExpenseCategory.Meal),
    'HONG KONG PALACE': ('Hong Kong Palace', ExpenseCategory.Meal),
    'IHOP': ('IHOP', ExpenseCategory.Meal),
    'COOKNSOLO - K\'FAR': ('K\'Far', ExpenseCategory.Meal),
    'McDonalds': ('McDonalds', ExpenseCategory.Meal),
    'MCDONALDS': ('McDonald\'s', ExpenseCategory.Meal),
    'MEHRAN': ('Mehran', ExpenseCategory.Meal),
    'MOBY': ('Moby Dick', ExpenseCategory.Meal),
    'MOBYDICKHOUSEOFKABOB': ('Moby Dick', ExpenseCategory.Meal),
    'MOD PIZZA': ('Mod Pizza', ExpenseCategory.Meal),
    'MOE\'S # 457': ('Moe\'s Southwest Grill', ExpenseCategory.Meal),
    'NANDO\'S PERI PERI #017': ('Nando\'s Peri Peri', ExpenseCategory.Meal),
    'NOODLES': ('Noodles & Co', ExpenseCategory.Meal),
    'ORDER.NOODLES.COM': ('Noodles & Co', ExpenseCategory.Meal),
    'NATTA THAI CUISINE': ('Natta Thai', ExpenseCategory.Meal),
    'Northside Social': ('Northside Social', ExpenseCategory.Meal),
    'OLIVE': ('Olive Garden', ExpenseCategory.Meal),
    'PANERA': ('Panera Bread', ExpenseCategory.Meal),
    'PASTRY CORNER': ('Pastry Corner', ExpenseCategory.Meal),
    'PARIS BAGUETTE -': ('Paris Baguette', ExpenseCategory.Meal),
    'PEKING': ('Peking Express', ExpenseCategory.Meal),
    'POTBELLY': ('Potbelly', ExpenseCategory.Meal),
    'PIND INDIAN CUISINE': ('Pind Cuisine', ExpenseCategory.Meal),
    'PIZZA HUT': ('Pizza Hut', ExpenseCategory.Meal),
    'PUNJABI JUNCTION': ('Punjabi Junction', ExpenseCategory.Meal),
    'QDOBA': ('QDoba', ExpenseCategory.Meal),
    'RAUNAQ MELA (MARKE': ('Raunaq Mela', ExpenseCategory.Meal),
    'RICE & MIX': ('Rice & Mix', ExpenseCategory.Meal),
    'ROLL PLAY TYSONS': ('Roll Play', ExpenseCategory.Meal),
    'PARADISE BIRYANI P': ('Paradise Pointe Biryani', ExpenseCategory.Meal),
    'SideBar': ('SideBar', ExpenseCategory.Meal),
    'Store': ('Subway', ExpenseCategory.Meal),
    'Subway': ('Subway', ExpenseCategory.Meal),
    'Sweet Leaf': ('Sweet Leaf', ExpenseCategory.Meal),
    'SWEET LEAF': ('Sweet Leaf', ExpenseCategory.Meal),
    'SWEETLEAF': ('Sweet Leaf', ExpenseCategory.Meal),
    'SWEETGREEN': ('Sweet Green', ExpenseCategory.Meal),
    'WWW.SWEETGREEN.COM': ('Sweet Green', ExpenseCategory.Meal),
    'TARA THAI RESTAURANT': ('Tara Thai', ExpenseCategory.Meal),
    'TATTE BAKERY - BE': ('Tatte Bakery', ExpenseCategory.Meal),
    'TATTE BAKERY - CL': ('Tatte Bakery', ExpenseCategory.Meal),
    'TATTE BAKERY - RE': ('Tatte Bakery', ExpenseCategory.Meal),
    'TEDS BULLETIN ONE': ('Ted\'s Bulletin', ExpenseCategory.Meal),
    'THE SANDWICH SHOP': ('The Sandwich Shop', ExpenseCategory.Meal),
    'TACO BAMBA': ('Taco Bamba', ExpenseCategory.Meal),
    'Taco Rock Falls C': ('Taco Rock', ExpenseCategory.Meal),
    'TOOSSO PAKISTANI': ('Toosso', ExpenseCategory.Meal),
    'WOODLANDS RESTAURANT': ('Woodlands', ExpenseCategory.Meal),

    # Coffee
    'BASECAMP COFFEE': ('Basecamp Coffee', ExpenseCategory.Coffee),
    'DUNKIN': ('Dunkin\' Donuts', ExpenseCategory.Coffee),
    'THE HUMAN BEAN -': ('The Human Bean', ExpenseCategory.Coffee),
    'KUNG FU TEA': ('Kung Fu Tea', ExpenseCategory.Coffee),
    'SHARE TEA': ('Share Tea', ExpenseCategory.Coffee),
    'STARBUCKS': ('Starbucks', ExpenseCategory.Coffee),
    'TEADM FAIRFAX': ('Starbucks', ExpenseCategory.Coffee),

    # Fast Food
    'BASKIN': ('Baskin Robbins', ExpenseCategory.FastFood),
    'BEN & JERRY\'S': ('Ben & Jerry\'s', ExpenseCategory.FastFood),
    'COLDSTONE': ('Coldstone', ExpenseCategory.FastFood),
    'DUCK DONUTS HERNDON, V': ('Duck Donuts', ExpenseCategory.FastFood),
    'DUCK DONUTS #14 HERNDO': ('Duck Donuts', ExpenseCategory.FastFood),
    'JENI\'S SPLENDID I': ('Jeni\'s Splendid Ice Cream', ExpenseCategory.FastFood),
    'LIL CITY CREAMERY': ('Lil City Creamery', ExpenseCategory.Meal),
    'WOODY`S ICE CREAM': ('Woody\'s Ice Cream', ExpenseCategory.FastFood),

    # House Rent
    'AVALON': ('Avalon Tysons Corner', ExpenseCategory.HouseRent),
    'STATE FARM INSURANCE': ('State Farm Insurance', ExpenseCategory.HouseRent),
    'STATE FARM  INSURANCE': ('State Farm Insurance', ExpenseCategory.HouseRent),

    # Electricity Bill
    'DOMINION': ('Dominion Energy', ExpenseCategory.ElectricityBill),

    # Gas Bill
    'WASHINGTON GAS': ('Washington Gas', ExpenseCategory.GasBill),

    # Water Bill
    'AVALON WATER': ('Water Bill, Conservice', ExpenseCategory.WaterBill),

    # Gas
    'COSTCO GAS': ('Costco Gas', ExpenseCategory.Gas),
    'EXXON': ('Exxon', ExpenseCategory.Gas),
    'EXXON A-PLUS #71': ('Exxon', ExpenseCategory.Gas),
    'EXXONMOBIL': ('Exxon', ExpenseCategory.Gas),
    'E Z PASS VA WEB': ('EZ Pass', ExpenseCategory.Gas),
    'SHELL': ('Shell Oil', ExpenseCategory.Gas),
    'SUNOCO': ('Sunoco', ExpenseCategory.Gas),

    # Car
    'BMW OF FAIRFAX': ('BMW', ExpenseCategory.Car),
    'FLAGSHIP CAR WASH VIEN': ('Car Wash, Flagship Car Wash', ExpenseCategory.Car),
    'PROGRESSIVE': ('Progressive Car Insurance', ExpenseCategory.Car),
    'PROG ADVANCED': ('Progressive Car Insurance', ExpenseCategory.Car),

    # Healthcare
    'CVS/SPECIALTY': ('CVS/SPECIALTY', ExpenseCategory.Healthcare),
    'SGF': ('SGF', ExpenseCategory.Healthcare),

    # Household Stuff
    'IKEA': ('Ikea', ExpenseCategory.HouseholdStuff),
    'TARGET': ('Target', ExpenseCategory.HouseholdStuff),

    # Streaming Services
    'Amazon Prime': ('Amazon Prime', ExpenseCategory.Streaming),
    # 'APPLE.COM/BILL': ('Apple TV', ExpenseCategory.Streaming),
    'Audible': ('Audible', ExpenseCategory.Streaming),
    'GOOGLE *YouTubePremium': ('YouTube Premium', ExpenseCategory.Streaming),
    'HELP.HBOMAX.COM': ('HBO', ExpenseCategory.Streaming),
    'Prime Video': ('Prime Video Rental', ExpenseCategory.Streaming),
    'Spotify USA': ('Spotify', ExpenseCategory.Streaming),
    'SXM*SIRIUSXM.COM/ACCT': ('SiriusXM', ExpenseCategory.Streaming),
    'VUDU.COM': ('Vudu', ExpenseCategory.Streaming),
    'WILLOW TV': ('Willow TV', ExpenseCategory.Streaming),

    # Movies
    'ICON @ TYSONS CORNER': ('Icon Cinemas', ExpenseCategory.Movies),

    # Books, Magazines
    'NYTimes*NYTimes': ('NYTimes', ExpenseCategory.BooksAndMagazines),
    'RAZ*BLACKCURRANT APPS': ('Splainer', ExpenseCategory.BooksAndMagazines),
    'TWPSUB43231056': ('Washington Post', ExpenseCategory.BooksAndMagazines),
    'Washington Post': ('Washington Post', ExpenseCategory.BooksAndMagazines),

    # Clothes and Shoes
    'BANANA REPUBLIC': ('Banana Republic', ExpenseCategory.ClothesAndShoes),
    'TEEPUBLIC': ('Tee Public', ExpenseCategory.ClothesAndShoes),

    # All Else
    '7-ELEVEN': ('7-Eleven', ExpenseCategory.AllElse),
    'BATH & BODY WORKS 3050': ('Bath & Body Works', ExpenseCategory.AllElse),
    'CVS/PHARMACY': ('CVS', ExpenseCategory.AllElse),
    'HAIR CUTTERY': ('Hair Cuttery', ExpenseCategory.AllElse),
    'METRO 124-ASHBURN': ('WMATA', ExpenseCategory.AllElse),
    'STAPLES': ('Staples', ExpenseCategory.AllElse),
}