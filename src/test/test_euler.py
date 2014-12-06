import unittest
import numpy as np

from use_generator import Generator
from template import Template
from molecules import Water, Atom, Property

class WaterTest( unittest.TestCase ):

    def setUp(self):
        self.ut_alpha = np.random.random( (6, ) )
        self.ut_beat = np.random.random(  (10, ) )

        self.g = Generator()
        self.w = self.g.get_mol( center = np.random.uniform( -10, 10, [3] ), mol = "water" )

        self.t1 = np.random.uniform( 0, np.pi/2 )
        self.t2 = np.random.uniform( 0, np.pi   )
        self.t3 = np.random.uniform( 0, np.pi/2 )

    def test_inv_rotation(self):
        """rotate two water molecules by random angles,
        translate them in random space, one by oxygen other by center of mass
        rotate them to standard orientation and center by mass"""
        w1 = self.g.get_mol( center = [0,0,0], mol = "water" )
        w2 = self.g.get_mol( center = [0,0,0], mol = "water" )

        t1, t2, t3 = np.random.uniform( -np.pi, np.pi, [3] )
        d1, d2, d3 = np.random.uniform( -np.pi, np.pi, [3] )

        r1, r2 = np.random.uniform( -100, 100, [2,3] )

        w1.translate_o( r1 )
        w2.translate( r1 )

        w1.rotate( t1, t2, t3 )
        w2.rotate( d1, d2, d3 )

        w1.inv_rotate( )
        w2.inv_rotate( )

        w1.center()
        w2.center()

        self.eq ( w1.com, w2.com )

        
    def test_center_get_euler(self):
        w = self.g.get_mol( center = [0,0,0], mol = "water" )

        t1, t2, t3 = w.get_euler()
        self.eq( [t1, t2, t3] , np.zeros(3) )

    def test_moved_get_euler(self):
        w = self.g.get_mol( center = [0,0,0], mol = "water" )
        w.translate([5,5,5])
        t1, t2 ,t3 =  w.get_euler()
        w.center()

        self.eq( [t1, t2, t3] , np.zeros(3) )

        t1, t2 ,t3 =  w.get_euler()
        w.center()

        self.eq( [t1, t2, t3] , np.zeros(3) )

    def test_negative_x_get_euler(self):
        w = self.g.get_mol( center = [0,0,0], mol = "water" )

        x1 = -0.5
        x2 = -0.5
        y1 =  0.5
        y2 = -0.5
        z1 = 0
        z2 = 0

        w.h1.x = x1 
        w.h2.x = x2 
        w.h1.y = y1
        w.h2.y = y2
        w.h1.z = z1
        w.h2.z = z2

        #self.eq ( w.get_euler(), [ np.pi/2 , np.pi/2, 0 ] )

    def test_negative_y_get_euler(self):
        w = self.g.get_mol( center = [0,0,0], mol = "water" )
        
        x1 =  0.5
        x2 = -0.5
        y1 = -0.5
        y2 = -0.5
        z1 = 0
        z2 = 0

        w.h1.x = x1 
        w.h2.x = x2 

        w.h1.y = y1
        w.h2.y = y2

        w.h1.z = z1
        w.h2.z = z2
        print w.p

        #self.eq ( w.get_euler(), [ np.pi/2 , np.pi/2, np.pi/2]  )


    def eq(self, a, b):
        np.testing.assert_almost_equal( a, b, decimal = 3)



if __name__ == '__main__':
    unittest.main()