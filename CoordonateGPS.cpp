#include<iostream>

using namespace std;

struct CoordonateGPS {
	int latitudine;
	int longitudine;
	float altitudine;
	string locatie;
 };

void afisareCoordonateGPS(CoordonateGPS l) {
	cout << "Latitudinea:" << l.latitudine << endl;
	cout << "Longitudine:" << l.longitudine << endl;
	cout << "Altitudine:" << l.altitudine<< endl;
	cout << "Locatie:" << l.locatie << endl;
}

void modificaAltitudine(CoordonateGPS* l, float nouaAltitudine)
{
	l->altitudine = nouaAltitudine;
}

void modificaAltitudineRef(CoordonateGPS& l, float nouaAltitudine)
{
	l.altitudine = nouaAltitudine;
}

CoordonateGPS initializareCoordonate(int latitudine, int longitudine, float altitudine, string locatie)
{
	CoordonateGPS l;
	l.latitudine = latitudine;
	l.longitudine = longitudine;
	l. altitudine = altitudine;
	l.locatie = locatie;

	return l;
}

int main()
{
	CoordonateGPS l;
	l.latitudine = 46;
	l.longitudine = 22;
	l.altitudine = 1010;
	l.locatie = "Predeal";

	afisareCoordonateGPS(l);

	CoordonateGPS(l2);

	cout << "Introduceti Latitudinea:";
	cin >> l2.latitudine;
	cout << "Introduceti Longitudinea:";
	cin >> l2.longitudine;
	cout << "Introduceti Altitudinea:";
	cin >> l2.altitudine;
	cout << "Introduceti Locatia:";
	cin >> l2.locatie;


	afisareCoordonateGPS(l2);

	modificaAltitudine(&l2, 2000);

	modificaAltitudineRef(l2, 3000);

	afisareCoordonateGPS(l2);

	return 0;


}
