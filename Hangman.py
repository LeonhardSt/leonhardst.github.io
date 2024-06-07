import random
print("Hello and welcome to the game")
from collections import Counter

someWords= '''hund katze banane apfel feuerwehr polizei fussballspieler direktor lehrer garage flugzeug lokomotive schule eisbergsalat musikalbum interpret genre bildschirm computer fruchtzwerge einkaufsladen mittagessen unterricht klausuren curriculum abschlusszeugnis autobahn Ärger Ärztin Abend Abfahrt Abflug Absender Adresse Alkohol Alter Ampel Anfang Angebot Angestellte Angst Ankunft Anmeldung Anrede Anruf Anrufbeantworter Ansage Anschluss Antwort Anzeige Anzug Apfel Apotheke Appartement Appetit April Arbeit Arbeitsplatz Arm Arzt Aufenthalt Aufgabe Aufzug Auge August Ausbildung Ausflug Ausgang Auskunft Ausländer Ausländerin Ausland Aussage Ausstellung Ausweis Auto Autobahn Automat Bäckerei Büro Baby Bad Bahn Bahnhof Bahnsteig Balkon Banane Bank Batterie Baum Beamte Beamtin Bein Beispiel Bekannte Benzin Beratung Berg Beruf Berufsschule Besuch Betrag Bett Bewerbung Bier Bild Bildschirm Birne Bitte Blatt Bleistift Blick Blume Bluse Blut Bogen Bohne Brötchen Brücke Brief Briefkasten Briefmarke Brieftasche Briefumschlag Brille Brot Bruder Buch Buchstabe Bus Butter Café CD CD-ROM Chef Computer Creme Dach Dame Dank Datum Dauer Deutsche Dezember Dienstag Ding Disco Doktor Dom Donnerstag Doppelzimmer Dorf Drucker Durchsage Durst Dusche E-Mail Ecke Ehefrau Ehemann Ei Einführung Eingang Einladung Eintritt Einwohner Einzelzimmer Eis Eltern Empfänger Empfang Ende Enkel Entschuldigung Erdgeschoss Erfahrung Ergebnis Erlaubnis Ermäßigung Erwachsene Essen Export Fähre Führerschein Führung Fabrik Fahrer Fahrkarte Fahrplan Fahrrad Familie Familienname Familienstand Farbe Fax Februar Fehler Fenster Ferien Fernsehgerät Fest Feuer Feuerwehr Feuerzeug Fieber Film Firma Fisch Flasche Fleisch Flughafen Flugzeug Flur Fluss Formular Foto Fotoapparat Frühjahr Frühling Frühstück Frage Frau Freitag Freizeit Freund Friseur Frist Fuß Fußball Fundbüro Gabel Garage Garten Gas Gast Gebühr Geburtsjahr Geburtsort Geburtstag Gegenteil Geld Geldbörse Gemüse Gepäck Gericht Gesamtschule Geschäft Geschenk Geschirr Gesicht Gespräch Gesundheit Getränk Gewicht Gewitter Glück Glückwunsch Glas Gleis Goethe-Institut Größe Die Grenze Grippe Großeltern Großmutter Großvater Gruß Grundschule Gruppe Guthaben Gymnasium Hähnchen Haar Halbpension Halle Hals Haltestelle Hand Handtuch Handy Haus Hausaufgabe Hausfrau Haushalt Hausmann Heimat Heizung Hemd Herbst Herd Herr Herz Hilfe Hobby Holz Hose Hund Hunger Idee Import Industrie Information Inhalt Internet Jacke Jahr Januar Job Jugendherberge Jugendliche Juli Junge Juni Käse Körper Küche Kühlschrank Kündigung Kaffee Kalender Kamera Kanne Karte Kartoffel Kasse Kassette Kassettenrecorder Katze Keller Kellner Kenntnisse Kennzeichen Kette Kfz Kind Kindergarten Kinderwagen Kino Kiosk Kirche Klasse Kleid Kleidung Kneipe Koffer Kollege Kollegin Konsulat Kontakt Konto Kontrolle Konzert Kopf Kosmetik Krankenkasse Krankheit Kredit Kreditkarte Kreis Kreuzung Kuchen Kugelschreiber Kunde Kundin Kurs Löffel Lösung Laden Lager Lampe Land Landschaft Leben Lebensmittel Leid Lehre Lehrer Lehrerin Leute Licht Lied Lkw Loch Lohn Lokal Luft Lust Mädchen März Möbel Müll Mülltonne Magen Mai Mal Mann Mantel Markt Maschine Material Mechaniker Medikament Meer Mehrwertsteuer Meinung Menge Mensch Messer Metall Miete Milch Minute Mittag Mitte Mitteilung Mittel Mittelschule Mittwoch Mode Moment Monat Montag Morgen Motor Mund Museum Musik Mutter Nähe Nachbar Nachbarin Nachmittag Nachrichten Nacht Name Natur Nebel Norden Notarzt Note Notfall Notiz November Nudel Nummer Ober Obst Oktober Oma Opa Operation Orange Ordnung Ort Osten Öl Päckchen Paket Panne Papier Papiere Parfüm Park Partei Partner Partnerin Party Pass Pause Pension Pkw Plan Plastik Platz Polizei Pommes frites Portion Post Postleitzahl Prüfung Praktikum Praxis Preis Problem Programm Prospekt Pullover Qualität Quittung Rücken Rabatt Radio Rathaus Raucher Raucherin Raum Realschule Rechnung Regen Reifen Reinigung Reis Reise Reisebüro Reiseführer Reparatur Restaurant Rezept Rezeption Rind Rock Rose Rundgang Süden S-Bahn Sache Saft Salat Salz Samstag Sonnabend Satz Schüler Schülerin Schalter Scheckkarte Schiff Schild Schinken Schirm Schlüssel Schloss Schluss Schmerzen Schnee Schnupfen Schokolade Schrank Schuh Schule Schwein Schwester Schwimmbad See Sehenswürdigkeit Seife Sekretärin Sekunde Sendung Senioren September Service Sessel Sofa Sohn Sommer Sonderangebot Sonne Sonntag Sorge Spülmaschine Spaß Spaziergang Speisekarte Spielplatz Sprache Sprachschule Sprechstunde Stück Stadt Standesamt Stempel Steuer Stock Stoff Straße Straßenbahn Strand Streichholz Strom Student Studentin Studium Stuhl Stunde Supermarkt Suppe Tür Tüte Tag Tankstelle Tasche Tasse Taxi Der Tee Teil Telefon Telefonbuch Teller Teppich Termin Test Text Theater Thema Ticket Tier Tipp Tisch Tochter Toilette Tomate Topf Tourist Treppe Trinkgeld Turm U-Bahn Uhr Unfall Universität Unterhaltung Unterkunft Unterricht Unterschied Unterschrift Untersuchung Urlaub Übernachtung Vater Verbindung Verein Verkäufer Verkäuferin Verkehr Vermieter Versicherung Verspätung Vertrag Video Vogel Volksschule Vormittag Vorname Vorsicht Vorwahl Wäsche Wagen Wald Wasser Weg Wein Welt Werkstatt Werkzeug Westen Wetter Wiederhören Wiedersehen Wind Winter Wirtschaft Woche Wochenende Wochentag Wohnung Wolke Wort Wunsch Wurst Zahl Zahn Zeit Zeitschrift Zeitung Zentrum Zettel Zeugnis Zigarette Zimmer Zitrone Zoll Zucker Zug.  '''

someWords = someWords.split(' ')
word = random.choice(someWords)
word = word.lower()

if __name__ == '__main__': 
    print('Finde das richtige Wort! Es könnte vieles sein!') 
  
    for i in word: 
        print('_', end=' ') 
    print() 
  
    playing = True
    letterGuessed = '' 
    chances = len(word) + 2
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0:  
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Rate einen Buchstaben: ')) 
                print("So viele Versuche hast du noch:",chances)
            except: 
                print('Schreibe einen Buchstaben') 
                continue
  
            if not guess.isalpha(): 
                print('Nur einen BUCHSTABEN') 
                continue
            elif len(guess) > 1: 
                print('Nur EINEN Buchstaben') 
                continue
            elif guess in letterGuessed: 
                print('Den buchstaben hattest du schon') 
                continue
  
            if guess in word: 
                k = word.count(guess) 
                for _ in range(k): 
                    letterGuessed += guess  
  
            for char in word: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end=' ') 
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)): 
                                                               
                    print("Das richtige Wort ist: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Du hast gewonnen!! :)') 
                    break  
                    break  
                else: 
                    print('_', end=' ') 
  
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('Du hast verloren du opp :(') 
            print('Die Lösung war: {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Versuchs nochmal!') 
        exit() 
