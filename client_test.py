import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # since the getDataPoint returns a tuple, assert that it returns a tuple containing
    # the data you expect.
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price']+quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  # write tests that cover getRatio
  def test_getRatio_normal(self):
    prices = {
      112.3: 115.7, 118.25: 111.16
    }
    for price_a in prices:
      self.assertEqual(getRatio(price_a, prices.get(price_a)), price_a / prices.get(price_a))

  def test_getRatio_price_a_zero(self):
    price_a = 0
    price_b = [120.5, 144.37, 239.3, 112.90]

    for price in price_b:
      self.assertEqual(getRatio(price_a, price), 0)

  def test_getRatio_price_b_zero(self):
    price_b = 0
    price_a = [120.5, 144.37, 239.3, 112.90]

    for price in price_a:
      self.assertEqual(getRatio(price, price_b), None)

if __name__ == '__main__':
    unittest.main()
