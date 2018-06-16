#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        """
         Changed the below from False to True
        """
        self.assertTrue(True) # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(True, "This should be True -- Please fix this. Fixed!")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values

        Seems i have to add a 2 as an arg to assertEqual, that would be to the second arg 1+1
        """
        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.

        Expected value should be equal to 2.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.

        Will setting the expected_value=2 fix make this test pass. Yeup!!
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.

        Seems this test was testing the syntax of writting an assertTrue
        statement.
        """

        # This throws an AssertionError exception
        self.assertTrue(True)

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:
        """
            __class__ attribute tells us the class type for a given
            object.
            For example say:
                num = 77 
                num.__class__ -->  <type 'int'>
                num.__class__ == int --> True
                
                dec = 77 
                dec.__class__ -->  <type 'float'>
                dec.__class__ == float --> True

                string = 'navel' 
                string.__class__ -->  <type 'str'>
                string.__class__ == str --> True

                Note: the comparison is without the quotation marks.

                For python3.x we can now get the class type for
                exceptions.
                Whereas in python2 we had to chain __class__ with
                __name__ to get to the type of an exception.
                
                Check out:
                https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
                for more info
        """
        self.assertEqual(str, "navel".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__

