import  unittest
import  spouseOrParentShares as sp
import CheckPart as cp

class Tests(unittest.TestCase):
    def setUp(self):
        print("Setup Phase")
    def tearDown(self):
        print("Tear Dowm Phase")
    def testSpouseWithSonsOrDaughters(self):
        result = sp.SpouseWithSonsOrDaughters(1200,"n","n",1)
        self.assertEquals(result,1000)
        result = sp.SpouseWithSonsOrDaughters(1200,"y","n",1)
        self.assertEquals(result,875)
        result = sp.SpouseWithSonsOrDaughters(1200,"n","y",1)
        self.assertEquals(result,875)

    def testSpouseWithoutSonsOrDaughters(self):
        result = sp.SpouseWithSonsOrDaughters(1200,"n","n",1)
        self.assertEquals(result,1000)
        result = sp.SpouseWithSonsOrDaughters(1200,"y","n",1)
        self.assertEquals(result,875)
        result = sp.SpouseWithSonsOrDaughters(1200,"n","y",1)
        self.assertEquals(result,875)

        # with self.assertRaises(ValueError):
        #     result = sp.SpouseWithSonsOrDaughters(1200, "n", "y", 1)
        #     self.assertEquals(result, 850)

    def testFatherAlive(self):
        self.assertEqual(cp.isFatherAlive("y"),True)
        self.assertEquals(cp.isWifeAlive(2),True)
        self.assertEquals(cp.isMotherAlive("n"),False)

if __name__ == '__main__':
    unittest.main()