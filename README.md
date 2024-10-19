Inheritance Shares Calculator

This application calculates the inheritance shares for sons, daughters, and other family members based on the total inheritance amount and family structure.
Features

    Inheritance calculation for sons, daughters, wife, mother, and father.
    Error handling for invalid input types.
    Unit testing is included to ensure correctness of the logic.

Requirements

    Python 3.x
    unittest for unit testing.

How to Run the Application

    Run the Main Application:
To execute the main inheritance calculator, follow the steps below:
python main.py

Run Unit Tests:

You can also run the unit tests to verify that the logic is functioning correctly.

To run the tests, use the following command:
    python -m unittest test_calculator.py

When you run the application, it will ask for the following inputs:

    Inheritance Amount: The total amount left by the deceased (float).
    Number of Sons: Number of sons (integer).
    Number of Daughters: Number of daughters (integer).
    Spouse Status: Whether the spouse is alive. (y for yes, n for no).
    Number of Wives: If the spouse is alive, you need to input the number of wives.
    Mother's Status: Whether the mother is alive. (y for yes, n for no).
    Father's Status: Whether the father is alive. (y for yes, n for no).
Here are snaps of Application Output..

![Screenshot from 2024-10-11 16-41-17](https://github.com/user-attachments/assets/2223d362-f0d3-4403-8b5b-8e8d4b0b5270)

![Screenshot from 2024-10-11 16-41-04](https://github.com/user-attachments/assets/fc761ca5-8348-4f5a-9957-3d2ce9606da0)


Unit Testing

Unit tests are written using Python's unittest framework to verify the correctness of the share calculation logic. The tests cover the following scenarios:

    Spouse With Sons or Daughters:
        Tests the calculation when the spouse, mother, and father are involved along with sons and daughters.

    Spouse Without Sons or Daughters:
        Tests the calculation in the absence of sons or daughters, but with the spouse, mother, and father.

    Helper Methods:
        Tests utility methods such as isFatherAlive, isMotherAlive, and isWifeAlive.

Sample Test Code

python

import unittest
import spouseOrParentShares as sp
import CheckPart as cp

class Tests(unittest.TestCase):
    def setUp(self):
        print("Setup Phase")
    
    def tearDown(self):
        print("Tear Down Phase")
    
    def testSpouseWithSonsOrDaughters(self):
        result = sp.SpouseWithSonsOrDaughters(1200, "n", "n", 1)
        self.assertEquals(result, 1000)
        result = sp.SpouseWithSonsOrDaughters(1200, "y", "n", 1)
        self.assertEquals(result, 875)
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
    
You have to write just file's name with extension to test these modules like .
        python test_Calculate.py
Here are some snaps of Unit Testing..

![image](https://github.com/user-attachments/assets/5f929c52-d4d5-4b8b-94e7-b718ed4c887d)

![image](https://github.com/user-attachments/assets/553651c2-2d34-4d20-9f9a-071e760cb3d7)

![image](https://github.com/user-attachments/assets/a9ae3dbd-ab1c-4f0c-929b-562172dac07e)



        
