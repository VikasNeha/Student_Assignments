
################################################################################
## Class Triangle
################################################################################

import math


class Triangle(object):

    def __init__( self, sideA=0.0, sideB=0.0, sideC=0.0 ):
        """
        Initialize an object of type Triangle.
        """

        self.__sideA = 0.0
        self.__sideB = 0.0
        self.__sideC = 0.0
        self.__valid = False

        try:
            self.__sideA = float(sideA)
            self.__sideB = float(sideB)
            self.__sideC = float(sideC)
        except ValueError:
            self.__sideA = 0.0
            self.__sideB = 0.0
            self.__sideC = 0.0
        self.__valid = self.__validate()

    def __validate( self ):
        #
        # Check the three sides to determine if a Triangle is valid.
        #

        if self.__sideA <= 0.0 or self.__sideB <= 0.0 or self.__sideC <= 0.0:
            return False

        if self.__sideA >= self.__sideB and self.__sideA >= self.__sideC:
            if self.__sideB + self.__sideC > self.__sideA:
                return True
            else:
                return False
        elif self.__sideB >= self.__sideA and self.__sideB >= self.__sideC:
            if self.__sideA + self.__sideC > self.__sideB:
                return True
            else:
                return False
        elif self.__sideC >= self.__sideA and self.__sideC >= self.__sideA:
            if self.__sideA + self.__sideB > self.__sideC:
                return True
            else:
                return False

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """

        return "( " + "%.1f" % self.__sideA + ", " + "%.1f" % self.__sideB + ", " + "%.1f" % self.__sideC + " )"

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """

        return self.__valid

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """

        if self.__sideA == self.__sideB == self.__sideC:
            return True
        else:
            return False

    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """

        if self.__sideA == self.__sideB or self.__sideB == self.__sideC or self.__sideC == self.__sideA:
            return True
        else:
            return False

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """

        if not self.is_isosceles():
            return True
        else:
            return False

    def sides(self):
        """
        Return a tuple containing the Triangle's three sides.
        """

        return self.__sideA, self.__sideB, self.__sideC

    def angles( self ):
        """
        Return a tuple containing the Triangle's three angles (in degrees)
        """

        if self.is_valid():
            a = self.__sideA
            b = self.__sideB
            c = self.__sideC

            cos_C = ((a**2) + (b**2) - (c**2)) / (2*a*b)
            angle_C = math.acos(cos_C)
            angle_C = math.degrees(angle_C)

            cos_B = ((c**2) + (a**2) - (b**2)) / (2*c*a)
            angle_B = math.acos(cos_B)
            angle_B = math.degrees(angle_B)

            angle_A = 180 - (angle_B + angle_C)

            return round(angle_A, 1), round(angle_B, 1), round(angle_C, 1)

        else:
            return None, None, None

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """

        if self.is_valid():
            return self.__sideA + self.__sideB + self.__sideC
        else:
            return 0

    def area( self ):
        """
        Return a float representing the Triangle's area.
        """

        if self.is_valid():
            S = self.perimeter() / 2
            T = S * (S - self.__sideA) * (S - self.__sideB) * (S - self.__sideC)
            return round(math.sqrt(T), 1)
        else:
            return 0

    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """

        if self.is_valid() and factor > 0:
            self.__sideA = self.__sideA * factor
            self.__sideB = self.__sideB * factor
            self.__sideC = self.__sideC * factor

