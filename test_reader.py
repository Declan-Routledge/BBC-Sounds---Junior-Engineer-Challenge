import unittest
import reader
import csv

class testreader(unittest.TestCase):
    def test_Add(self):
        value = ["737533d8-576d-41e6-a302-0492e029a2c8", "Dreamland","Glass Animals", "2020"]
        self.assertIn(value, reader.Add("737533d8-576d-41e6-a302-0492e029a2c8", "Dreamland","Glass Animals", "2020"))
    def test_Get_id(self):
        self.assertEqual(reader.Get("f337fd51-7bf5-44bf-9553-5826162bc83a"),["Pink Noise"])
    def test_Get_artist(self):
        self.assertEqual(reader.Get("Gorillaz"),['Demon Days', 'Plastic Beach', 'Demon Days'])
    def test_Update(self):
        value= ["c2263b8c-6718-4494-8218-1e739cf04e0a", "Melodrama","Lorde", "2017"]
        notUpdateValue = ["c2263b8c-6718-4494-8218-1e739cf04e0a", "Melodrama","Lorde", "1917"]
        self.assertIn(value, reader.Update("c2263b8c-6718-4494-8218-1e739cf04e0a", "year released", "2017"))
        self.assertNotIn(notUpdateValue, reader.Update("c2263b8c-6718-4494-8218-1e739cf04e0a", "year released", "2017"))
    def test_Delete(self):
        valueToDelete= ["17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd","Nightcall", "Kavinsky","2011"]
        self.assertNotIn(valueToDelete, reader.Delete("17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd"))
    def test_values_Add(self):
        #make sure value errors are raised when necessary
        self.assertRaises(ValueError,reader.Add,"22", "Dreamland","Glass Animals", "2020")
        self.assertRaises(ValueError,reader.Add,22, "Dreamland","Glass Animals", "2020")
        #check for updateValue wrongful year
        self.assertRaises(ValueError,reader.Add,"17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd", "Dreamland","Glass Animals", -1)
        self.assertRaises(ValueError,reader.Add,22, "Dreamland","Glass Animals", "-1")
        
    def test_values_Update(self):
        #make sure value errors are raised when necessary
        #check for wrong ID
        self.assertRaises(ValueError,reader.Update,"22", "year released", "2020")
        self.assertRaises(ValueError,reader.Update,22,"year released", "2020")
        #check for updateValue wrongful year
        self.assertRaises(ValueError,reader.Update,"17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd", "year released", "-1")
        self.assertRaises(ValueError,reader.Update,"17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd","year released", -1)
        #check for incorrect headerToUpdate field
        self.assertRaises(ValueError,reader.Update,"17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd","album", "2020")
        self.assertRaises(ValueError,reader.Update,"17cd04a4-ef0a-468f-9f47-5d9dbb1c0dbd",-1, "2020")        
    
    def test_values_Delete(self):
        self.assertRaises(ValueError,reader.Delete,"22")
        self.assertRaises(ValueError,reader.Delete,22)


        

