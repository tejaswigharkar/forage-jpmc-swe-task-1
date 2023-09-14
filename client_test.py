import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for i in quotes:
      self.assertEqual(getDataPoint(i),i['stock'],i[bid_price], i['ask_price'], (i['bid_price']+i['ask_price']/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
   for i in quotes:
      self.assertEqual(getDataPoint(i), (i['stock'], i['top_bid']['price'], i['top_ask']['price'], (i['top_bid']['price'] + i['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceWithNoBids(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {}, 'id': '0.109974697771', 'stock': 'XYZ'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {}, 'id': '0.109974697771', 'stock': 'PQR'}
    ]
    for i in quotes:
      self.assertEqual(getDataPoint(i), (i['stock'], None, i['top_ask']['price'], None))

  def test_getDataPoint_calculatePriceWithNoAsks(self):
    quotes = [
      {'top_ask': {}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'LMN'},
      {'top_ask': {}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'QRS'}
    ]
    for i in quotes:
      self.assertEqual(getDataPoint(i), (i['stock'], i['top_bid']['price'], None, None))



if __name__ == '__main__':
    unittest.main()
