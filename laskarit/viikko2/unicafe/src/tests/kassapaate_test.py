import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(1000)
    
    def test_luodun_paatteen_raha_ja_myynntien_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_maukkaiden_osalta(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)

    def test_kateisosto_toimii_edullisten_osalta(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300),60)
    
    def test_kateisosto_toimii_maukkaiden_osalta_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300),300)

    def test_kateisosto_toimii_edullisten_osalta_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(150),150)

    def test_korttiosto_toimii_edullisen_osalta_rahat_riittavat(self):
        
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,760)    
        
    def test_korttiosto_toimii_maukkaan_osalta_rahat_riittavat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,600)   


    def test_korttiosto_toimii_edullisen_osalta_rahat_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(2))
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(2)),False)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)  
    
    def test_korttiosto_toimii_maukkaan_osalta_rahat_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(10))
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(10)),False)

        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kortin_lataaminen_kasvattaa_kassapaatetta(self):
        kortti=Maksukortti(10000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,105000)
        self.assertEqual(kortti.saldo,15000)

    def test_kortin_lataaminen_kasvattaa_kassapaatetta_negatiivinen(self):
        kortti=Maksukortti(10000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(kortti.saldo,10000)