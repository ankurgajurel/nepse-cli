import unittest
import all_data

class TestAllData(unittest.TestCase):

    def test_basic(self):
        self.assertIsInstance(all_data.send_req_basic('adbl'), dict)

    def test_nepse(self):
        self.assertIsInstance(float(all_data.send_req_nepse('live')), float)
        self.assertIsInstance(float(all_data.send_req_nepse('percent_change')), float)
        self.assertIsInstance(all_data.send_req_nepse('status'), dict)

    def test_news(self):
        self.assertIsInstance(all_data.send_req_news(), list)

    def test_scrip_data(self):
        scrip_data = all_data.send_req_scrip_data('adbl')
        self.assertIsInstance(scrip_data, tuple)
        for val in scrip_data:
            self.assertIsInstance(val, float)

    def test_top_stocks(self):
        n = 5
        field = 'gainer'
        for i in range(n):
            self.assertIsInstance(all_data.send_req_top_stocks(i, field), list)

    def test_indices(self):
        self.assertIsInstance(all_data.send_req_indices('devbank'), dict)

if __name__ == '__main__':
    unittest.main()