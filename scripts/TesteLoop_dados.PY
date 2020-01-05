import unittest
from ddt import ddt, data, idata, file_data, unpack


@ddt
class TESTE(unittest.TestCase):

    @data(1, -2, 3, 4, -5)
    def test_with_ddt_data(self, x):
        self.assertGreater(x, 0)
@ddt
class FooTestCase(unittest.TestCase):
    @data('it is a test!', 'it is a test!', 'something else')
    def test_lines(self, Y):
        self.assertEqual(Y, 'it is a test!')


if __name__=="__main__":
     unittest.main()