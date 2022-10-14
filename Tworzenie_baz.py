import sqlite3
conn = sqlite3.connect('film.db')
cur = conn.cursor()
cur.execute("create table movie(film_id var, tytul var, gatunek var, rok_produkcji var, rodzaj var, ilość_czesc var)")
cur.execute(" insert into movie values ('1','Tie Me Up! Tie Me Down!','Comedy','1990','Cat A','1');")
cur.execute(" insert into movie values ('2','High Heels','Comedy','1991','Cat B','1');")
cur.execute(" insert into movie values ('3','Dead Zone  The','Horror','1983','Cat C','1');")
cur.execute(" insert into movie values ('4','Cuba','Action','1979','Cat A','1');")
cur.execute(" insert into movie values ('5','Days of Heaven','Drama','1978','Cat B','1');")
cur.execute(" insert into movie values ('6','Octopussy','Action','1983','Cat C','1');")
cur.execute(" insert into movie values ('7','Target Eagle','Action','1984','Cat A','1');")
cur.execute(" insert into movie values ('8','American Angels: Baptism of Blood  The','Drama','1989','Cat B','1');")
cur.execute(" insert into movie values ('9','Subway','Drama','1985','Cat C','1');")
cur.execute(" insert into movie values ('10','Camille Claudel','Drama','1990','Cat A','1');")
cur.execute(" insert into movie values ('11','Fanny and Alexander','Drama','1982','Cat B','1');")
cur.execute(" insert into movie values ('1628','Duke  The Films of John Wayne','Western','1993','Cat B','1');")
cur.execute(" insert into movie values ('1629','Frontier Horizon','Western','1939','Cat C','1');")
cur.execute(" insert into movie values ('1630','Hell Town','Western','1934','Cat A','1');")
cur.execute(" insert into movie values ('1631','Hurricane Express','Western','1932','Cat B','1');")
cur.execute(" insert into movie values ('1632','Hurricane Express  The','Action','1932','Cat C','1');")
cur.execute(" insert into movie values ('1633','In Harm s Way','War','1965','Cat A','1');")
cur.execute(" insert into movie values ('1634','John Wayne Collection  Red River  The','War','1991','Cat B','1');")
cur.execute(" insert into movie values ('1648','Neath Arizona Skies','Western','1993','Cat A','1');")
cur.execute(" insert into movie values ('1649','Neath the Arizona Skies','Western','1991','Cat B','1');")
cur.execute(" insert into movie values ('1650','Randy Rides Alone','Western','1991','Cat C','1');")
cur.execute(" insert into movie values ('1651','Range Feud','Western','1993','Cat A','1');")
cur.execute(" insert into movie values ('1652','Red River','Western','1992','Cat B','1');")
cur.execute(" insert into movie values ('1653','Riders of Destiny','Western','1991','Cat C','1');")
cur.execute(" insert into movie values ('1654','Sagebrush Trail','Western','1990','Cat A','1');")
cur.execute(" insert into movie values ('1655','Shadow of the Eagle  The','Action','1932','Cat B','1');")
cur.execute(" insert into movie values ('1656','Blood & Guns','Action','1989','Cat C','1');")
cur.execute(" insert into movie values ('1657','Hot Money','Drama','1988','Cat A','1');")
cur.execute(" insert into movie values ('1658','Comedy Tonight','Comedy','1977','Cat B','1');")
cur.execute(" insert into movie values ('1659','Robin Williams','Comedy','1991','Cat A','1');")
conn.commit()
cur.execute('select * from movie order by film_id desc limit 5')
print(cur.fetchall())
print()
cur.execute("update movie set rodzaj = 'Cat Z' where rodzaj = 'Cat A'")
conn.commit()
cur.execute('select * from movie order by film_id desc limit 5')
print(cur.fetchall())
print('\n\n')
z_lp = input('A teraz wprowadzimy wartości do bazy sami. Najpierw, liczba porządkowa (LP):\n')
print('Wybrales: ',z_lp)
z_tytul = input('Teraz tytuł filmu:\n')
print('Wybrales: ',z_tytul)
z_gatunek = input('Gatunek filmu:\n')
print('Wybrales: ',z_gatunek)
z_rok = input('Rok wydania:\n')
print('Wybrales: ',z_rok)
z_rodzaj = input('Jak myślisz, Cat A, Cat B czy Cat C? A może Cat Z?:\n')
print('Wybrales: ',z_rodzaj)
z_ilosc = input('Ilość odcinków / części:\n')
print('Wybrales: ',z_ilosc)

cur.execute(" insert into movie values ('%s','%s','%s','%s','%s','%s');" % (z_lp, z_tytul, z_gatunek, z_rok,z_rodzaj, z_ilosc))
conn.commit()
cur.execute('select * from movie order by film_id desc limit 5')
print('\nDo bazy filmów dodano nowy wiersz, dostępny pod ID: %s'%(z_lp))
conn.commit()
cur.execute('select * from movie where film_id = %s' %(z_lp))
print(cur.fetchall())
