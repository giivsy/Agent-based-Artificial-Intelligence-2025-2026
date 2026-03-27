import math

CORATO = 'Corato'
RUVO = 'Ruvo'
TRANI = 'Trani'
MOLFETTA = 'Molfetta'
ANDRIA = 'Andria'
BARLETTA = 'Barletta'
MINERVINO = 'Minervino'
ALTAMURA = 'Altamura'
BISCEGLIE = 'Bisceglie'
MODUGNO = 'Modugno'
BARI = 'Bari'

coords = {
    CORATO: (41.1536, 16.4114),
    RUVO: (41.1177, 16.4850),
    TRANI: (41.2762, 16.4186),
    MOLFETTA: (41.2006, 16.5984),
    ANDRIA: (41.2316, 16.2900),
    BARLETTA: (41.3187, 16.2830),
    MINERVINO: (41.0839, 16.0817),
    ALTAMURA: (40.8260, 16.5520),
    BISCEGLIE: (41.2426, 16.5017),
    MODUGNO: (41.0820, 16.7800),
    BARI: (41.1171, 16.8719),
}

streets = [(CORATO, TRANI, 14), (CORATO, BISCEGLIE, 13), (CORATO, RUVO, 10), (CORATO, ALTAMURA, 40),
           (CORATO, ANDRIA, 15), (BARLETTA, TRANI, 13), (BARLETTA, ANDRIA, 10), (BARLETTA, MINERVINO, 35),
           (ANDRIA, MINERVINO, 24), (MINERVINO, ALTAMURA, 50), (TRANI, BISCEGLIE, 8), (BISCEGLIE, MOLFETTA, 10),
           (MOLFETTA, RUVO, 14), (MOLFETTA, MODUGNO, 22), (MOLFETTA, BARI, 25), (RUVO, MODUGNO, 26),
           (RUVO, ALTAMURA, 34), (ALTAMURA, MODUGNO, 36), (ALTAMURA, BARI, 45), (RUVO, ALTAMURA, 34),
           (MODUGNO, BARI, 22)]

def haversine(coord1, coord2):
    R = 6371  # raggio Terra in km

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def cities_distance(city1, city2):
    return haversine(coords[city1], coords[city2])

def find_adjacent_cities(city):
    adjs = {}
    for street in streets:
        c1, c2, cost = street
        if city == c1:
            adjs[c2] = cost
        if city == c2:
            adjs[c1] = cost
    return adjs