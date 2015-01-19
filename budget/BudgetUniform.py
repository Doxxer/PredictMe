__author__ = 'kate'
import MySQLdb
import pickle
import re

valuta = {'usd': 1, 'euro': 1.1564, 'cad': 0.835247, 'aud': 0.82305, 'pound': 1.51295, 'nlg': 0.5244, 'grd': 0.0034,
          'sek': 0.123548, 'isk': 0.007576, 'frf': 0.176322, 'inr': 0.016228, 'dem': 0.591322, 'thb': 0.030713,
          'ltl': 0.340832, 'jpy': 0.008518, 'sgd': 0.799808, 'chf': 1.161643, 'pln': 0.268159, 'myr': 0.280994,
          'ils': 0.253695,
          'brl': 0.381527, 'krw': 0.000926, 'rur': 0.015313, 'eek': 0.085249, 'mxn': 0.068704, 'nok': 0.132267,
          'nzd': 0.779185, 'zar': 0.086594,
          'egp': 0.139886, 'trl': 4.29914 * 0.0000001, 'cny': 0.161067, 'itl': 0.000597239, 'dkk': 0.155606,
          'bdt': 0.0128617,
          'hkd': 0.128982, 'huf': 0.003631, 'plz': 0.268159, 'php': 0.022404, 'ars': 0.116191, 'esp': 0.00694951,
          'pte': 0.0058, 'sar': 0.266379,
          'fim': 0.194434, 'irr': 0.0000365604, 'lkr': 0.007608, 'rol': 0.00000256987, 'cop': 0.000422, 'bhd': 2.652595,
          'aed': 0.272246,
          'lvl': 1.645956, 'mad': 0.106441, 'mtl': 2.70, 'pkr': 0.009932, 'ffr': 1, 'mmk': 0.000971817, 'veb': 0.000466,
          'yum': 0.59,
          'kzt': 0.005431, 'bgl': 0.000596, 'czk': 0.041494, 'hrk': 0.150277, 'npr': 0.01008, 'tmm': 0.0000571429,
          'bef': 0.0286554,
          'gel': 0.51, 'cup': 0.0377358, 'ron': 0.256987, 'pen': 0.331565, 'iep': 1.47, 'twd': 0.03178, 'dop': 0.022507,
          'clp': 0.001593, 'mvr': 0.065, 'vnd': 0.0000047, 'sit': 0.000484, 'mnt': 0.000516669, 'uah': 0.063102,
          'pyg': 0.000211,
          'lbp': 0.000662, 'jmd': 0.008696, 'ngn': 0.005407, 'byr': 0.00007, "luf": 0.0286688, 'ats': 0.0840475,
          'irn': 0.016228,
          'pzl': 0.268159, 'ttd': 0.156775, 'xau': 1.27762, 'amd': 0.0000218, 'jod': 1.411732, 'gtq': 0.130728,
          'xaf': 0.00176307,
          'cyp': 1.97586, 'qar': 0.274654, 'bnd': 0.753636, 'skk': 0.044968, 'kes': 0.010931, 'kwd': 3.39906,
          'nad': 0.08649, 'frr': 1,
          'bob': 0.144725, 'ang': 0.558659, 'all': 0.0083}


def convert_value(in_currency, in_value):
    mult = 1
    if len(in_currency) <= 1:
        return in_value
    if in_currency[0] == '$':
        return valuta['usd'] * in_value
    if len(in_currency) == 2:
        if in_currency[0] == '\xc2' and in_currency[1] == '\xa3':
            return valuta['pound'] * in_value
    if len(in_currency) >= 3:
        if in_currency[0] == '\xe2' and in_currency[1] == '\x82' and in_currency[2] == '\xac':
            return valuta['euro'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'A' and in_currency[2] == 'D':
            return valuta['cad'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'U' and in_currency[2] == 'D':
            return valuta['aud'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'L' and in_currency[2] == 'G':
            return valuta['nlg'] * in_value
        if in_currency[0] == 'G' and in_currency[1] == 'R' and in_currency[2] == 'D':
            return valuta['grd'] * in_value
        if in_currency[0] == 'S' and in_currency[1] == 'E' and in_currency[2] == 'K':
            return valuta['sek'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'S' and in_currency[2] == 'K':
            return valuta['isk'] * in_value
        if in_currency[0] == 'F' and in_currency[1] == 'R' and in_currency[2] == 'F':
            return valuta['frf'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'N' and in_currency[2] == 'R':
            return valuta['inr'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'D' and in_currency[2] == 'R':
            return valuta['inr'] * in_value
        if in_currency[0] == 'D' and in_currency[1] == 'E' and in_currency[2] == 'M':
            return valuta['dem'] * in_value
        if in_currency[0] == 'T' and in_currency[1] == 'H' and in_currency[2] == 'B':
            return valuta['thb'] * in_value
        if in_currency[0] == 'L' and in_currency[1] == 'T' and in_currency[2] == 'L':
            return valuta['ltl'] * in_value
        if in_currency[0] == 'J' and in_currency[1] == 'P' and in_currency[2] == 'Y':
            return valuta['jpy'] * in_value
        if in_currency[0] == 'S' and in_currency[1] == 'G' and in_currency[2] == 'D':
            return valuta['sgd'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'H' and in_currency[2] == 'F':
            return valuta['chf'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'L' and in_currency[2] == 'N':
            return valuta['pln'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'Y' and in_currency[2] == 'R':
            return valuta['myr'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'L' and in_currency[2] == 'S':
            return valuta['ils'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'R' and in_currency[2] == 'L':
            return valuta['brl'] * in_value
        if in_currency[0] == 'K' and in_currency[1] == 'R' and in_currency[2] == 'W':
            return valuta['krw'] * in_value
        if in_currency[0] == 'R' and in_currency[1] == 'U' and in_currency[2] == 'R':
            return valuta['rur'] * in_value
        if in_currency[0] == 'E' and in_currency[1] == 'E' and in_currency[2] == 'K':
            return valuta['eek'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'X' and in_currency[2] == 'N':
            return valuta['mxn'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'O' and in_currency[2] == 'K':
            return valuta['nok'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'Z' and in_currency[2] == 'D':
            return valuta['nzd'] * in_value
        if in_currency[0] == 'Z' and in_currency[1] == 'A' and in_currency[2] == 'R':
            return valuta['zar'] * in_value
        if in_currency[0] == 'E' and in_currency[1] == 'G' and in_currency[2] == 'P':
            return valuta['egp'] * in_value
        if in_currency[0] == 'T' and in_currency[1] == 'R' and in_currency[2] == 'L':
            return valuta['trl'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'N' and in_currency[2] == 'Y':
            return valuta['cny'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'T' and in_currency[2] == 'L':
            return valuta['itl'] * in_value
        if in_currency[0] == 'D' and in_currency[1] == 'K' and in_currency[2] == 'K':
            return valuta['dkk'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'D' and in_currency[2] == 'T':
            return valuta['bdt'] * in_value
        if in_currency[0] == 'H' and in_currency[1] == 'K' and in_currency[2] == 'D':
            return valuta['hkd'] * in_value
        if in_currency[0] == 'H' and in_currency[1] == 'U' and in_currency[2] == 'F':
            return valuta['huf'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'L' and in_currency[2] == 'Z':
            return valuta['plz'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'H' and in_currency[2] == 'P':
            return valuta['php'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'R' and in_currency[2] == 'S':
            return valuta['ars'] * in_value
        if in_currency[0] == 'E' and in_currency[1] == 'S' and in_currency[2] == 'P':
            return valuta['esp'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'T' and in_currency[2] == 'E':
            return valuta['pte'] * in_value
        if in_currency[0] == 'S' and in_currency[1] == 'A' and in_currency[2] == 'R':
            return valuta['sar'] * in_value
        if in_currency[0] == 'F' and in_currency[1] == 'I' and in_currency[2] == 'M':
            return valuta['fim'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'R' and in_currency[2] == 'R':
            return valuta['irr'] * in_value
        if in_currency[0] == 'L' and in_currency[1] == 'K' and in_currency[2] == 'R':
            return valuta['lkr'] * in_value
        if in_currency[0] == 'R' and in_currency[1] == 'O' and in_currency[2] == 'L':
            return valuta['rol'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'H' and in_currency[2] == 'D':
            return valuta['bhd'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'O' and in_currency[2] == 'P':
            return valuta['cop'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'E' and in_currency[2] == 'D':
            return valuta['aed'] * in_value
        if in_currency[0] == 'L' and in_currency[1] == 'V' and in_currency[2] == 'L':
            return valuta['lvl'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'A' and in_currency[2] == 'D':
            return valuta['mad'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'T' and in_currency[2] == 'L':
            return valuta['mtl'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'K' and in_currency[2] == 'R':
            return valuta['pkr'] * in_value
        if in_currency[0] == 'F' and in_currency[1] == 'F' and in_currency[2] == 'R':
            return valuta['ffr'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'M' and in_currency[2] == 'K':
            return valuta['mmk'] * in_value
        if in_currency[0] == 'V' and in_currency[1] == 'E' and in_currency[2] == 'B':
            return valuta['veb'] * in_value
        if in_currency[0] == 'Y' and in_currency[1] == 'U' and in_currency[2] == 'M':
            return valuta['yum'] * in_value
        if in_currency[0] == 'K' and in_currency[1] == 'Z' and in_currency[2] == 'T':
            return valuta['kzt'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'G' and in_currency[2] == 'L':
            return valuta['bgl'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'Z' and in_currency[2] == 'K':
            return valuta['czk'] * in_value
        if in_currency[0] == 'H' and in_currency[1] == 'R' and in_currency[2] == 'K':
            return valuta['hrk'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'P' and in_currency[2] == 'R':
            return valuta['npr'] * in_value
        if in_currency[0] == 'T' and in_currency[1] == 'M' and in_currency[2] == 'M':
            return valuta['tmm'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'E' and in_currency[2] == 'F':
            return valuta['bef'] * in_value
        if in_currency[0] == 'G' and in_currency[1] == 'E' and in_currency[2] == 'L':
            return valuta['gel'] * in_value
        if in_currency[0] == 'R' and in_currency[1] == 'O' and in_currency[2] == 'N':
            return valuta['ron'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'U' and in_currency[2] == 'P':
            return valuta['cup'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'E' and in_currency[2] == 'N':
            return valuta['pen'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'E' and in_currency[2] == 'P':
            return valuta['iep'] * in_value
        if in_currency[0] == 'T' and in_currency[1] == 'W' and in_currency[2] == 'D':
            return valuta['twd'] * in_value
        if in_currency[0] == 'D' and in_currency[1] == 'O' and in_currency[2] == 'P':
            return valuta['dop'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'L' and in_currency[2] == 'P':
            return valuta['clp'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'V' and in_currency[2] == 'R':
            return valuta['mvr'] * in_value
        if in_currency[0] == 'V' and in_currency[1] == 'N' and in_currency[2] == 'D':
            return valuta['vnd'] * in_value
        if in_currency[0] == 'M' and in_currency[1] == 'N' and in_currency[2] == 'T':
            return valuta['mnt'] * in_value
        if in_currency[0] == 'S' and in_currency[1] == 'I' and in_currency[2] == 'T':
            return valuta['sit'] * in_value
        if in_currency[0] == 'U' and in_currency[1] == 'A' and in_currency[2] == 'H':
            return valuta['uah'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'Y' and in_currency[2] == 'G':
            return valuta['pyg'] * in_value
        if in_currency[0] == 'L' and in_currency[1] == 'B' and in_currency[2] == 'P':
            return valuta['lbp'] * in_value
        if in_currency[0] == 'J' and in_currency[1] == 'M' and in_currency[2] == 'D':
            return valuta['jmd'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'G' and in_currency[2] == 'N':
            return valuta['ngn'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'Y' and in_currency[2] == 'R':
            return valuta['byr'] * in_value
        if in_currency[0] == 'L' and in_currency[1] == 'U' and in_currency[2] == 'F':
            return valuta['luf'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'T' and in_currency[2] == 'S':
            return valuta['ats'] * in_value
        if in_currency[0] == 'I' and in_currency[1] == 'R' and in_currency[2] == 'N':
            return valuta['irn'] * in_value
        if in_currency[0] == 'P' and in_currency[1] == 'Z' and in_currency[2] == 'L':
            return valuta['pzl'] * in_value
        if in_currency[0] == 'T' and in_currency[1] == 'T' and in_currency[2] == 'D':
            return valuta['ttd'] * in_value
        if in_currency[0] == 'X' and in_currency[1] == 'A' and in_currency[2] == 'U':
            return valuta['xau'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'M' and in_currency[2] == 'D':
            return valuta['amd'] * in_value
        if in_currency[0] == 'J' and in_currency[1] == 'O' and in_currency[2] == 'D':
            return valuta['jod'] * in_value
        if in_currency[0] == 'G' and in_currency[1] == 'T' and in_currency[2] == 'Q':
            return valuta['gtq'] * in_value
        if in_currency[0] == 'X' and in_currency[1] == 'A' and in_currency[2] == 'F':
            return valuta['xaf'] * in_value
        if in_currency[0] == 'C' and in_currency[1] == 'Y' and in_currency[2] == 'P':
            return valuta['cyp'] * in_value
        if in_currency[0] == 'R' and in_currency[1] == 'U' and in_currency[2] == 'B':
            return valuta['rur'] * in_value
        if in_currency[0] == 'Q' and in_currency[1] == 'A' and in_currency[2] == 'R':
            return valuta['qar'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'N' and in_currency[2] == 'D':
            return valuta['bnd'] * in_value
        if in_currency[0] == 'S' and in_currency[1] == 'K' and in_currency[2] == 'K':
            return valuta['skk'] * in_value
        if in_currency[0] == 'K' and in_currency[1] == 'E' and in_currency[2] == 'S':
            return valuta['kes'] * in_value
        if in_currency[0] == 'K' and in_currency[1] == 'W' and in_currency[2] == 'D':
            return valuta['kwd'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'A' and in_currency[2] == 'D':
            return valuta['nad'] * in_value
        if in_currency[0] == 'F' and in_currency[1] == 'R' and in_currency[2] == 'R':
            return valuta['frr'] * in_value
        if in_currency[0] == 'E' and in_currency[1] == 'U' and in_currency[2] == 'D':
            return valuta['euro'] * in_value
        if in_currency[0] == 'N' and in_currency[1] == 'K' and in_currency[2] == 'R':
            return valuta['nok'] * in_value
        if in_currency[0] == 'B' and in_currency[1] == 'O' and in_currency[2] == 'B':
            return valuta['bob'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'N' and in_currency[2] == 'G':
            return valuta['ang'] * in_value
        if in_currency[0] == 'A' and in_currency[1] == 'L' and in_currency[2] == 'L':
            return valuta['all'] * in_value
    return in_value


db = MySQLdb.connect(host="localhost"
                     , user="root"
#                     , passwd="imdb"
                     , db="imdb")

movies_cur = db.cursor()

movies_cur.execute("""select * from Movies""")

update_cursor = db.cursor()

for el in movies_cur:
    row = movies_cur.fetchone()
    title_id, cur_budget = row[1], row[5]

    currency = re.findall(r'[^\d+, ^,, ^' ']', cur_budget)
    float_value = re.findall(r'\d+.*', cur_budget)[0].replace(",", "").replace(".", "")
    cv = convert_value(currency, float(re.findall(r"\d+", float_value)[0]))
    # print(currency,float_value, cv)
    if cv == None:
        print("here", currency, float_value, cur_budget)
        continue
    # print(cv, int(title_id))
    update_cursor.execute("""UPDATE Movies SET budget = %s WHERE title_id = %s""" % (cv, int(title_id)))

db.commit()
db.close()
# movies_cur.execute("""UPDATE allMovies SET budget = 354 WHERE title_id = 2018307""")