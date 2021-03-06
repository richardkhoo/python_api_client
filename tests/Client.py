'''
Created on Dec 7, 2015

@author: Andrew
'''
import unittest
from tests import get_test_session
import calcbench as cb


class NormalizedClient(unittest.TestCase):


    def setUp(self):
        get_test_session()


    def tearDown(self):
        pass


    def testNormalizedRaw(self):
        data = cb.normalized_raw(company_identifiers=['msft', 'orcl'], 
                                 metrics=['revenue', 'taxespayable'],
                                start_year=2014, 
                                start_period=1, 
                                end_year=2014, 
                                end_period=4, 
                                entire_universe=False, 
                                filing_accession_number=None)
        expected_data = [
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 1,
        "metric": "Revenue",
        "value": 20403000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 2,
        "metric": "Revenue",
        "value": 23382000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 3,
        "metric": "Revenue",
        "value": 23201000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 4,
        "metric": "Revenue",
        "value": 26470000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 1,
        "metric": "Revenue",
        "value": 9307000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 2,
        "metric": "Revenue",
        "value": 11320000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 3,
        "metric": "Revenue",
        "value": 8596000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 4,
        "metric": "Revenue",
        "value": 9598000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 4,
        "metric": "TaxesPayable",
        "value": 4671000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 3,
        "metric": "TaxesPayable",
        "value": 4573000000
    },
    {
        "ticker": "ORCL",
        "calendar_year": 2014,
        "calendar_period": 1,
        "metric": "TaxesPayable",
        "value": 4493000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 3,
        "metric": "TaxesPayable",
        "value": 11603000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 1,
        "metric": "TaxesPayable",
        "value": 10094000000
    },
    {
        "ticker": "MSFT",
        "calendar_year": 2014,
        "calendar_period": 4,
        "metric": "TaxesPayable",
        "value": 12011000000
    }
]
        self.assertListEqual(data, expected_data, "Data did not match")

    def testBreakoutsRaw(self):
        data = cb.breakouts_raw(company_identifiers=['msft', 'orcl'], 
                                metrics=['operatingSegmentRevenue'], 
                                start_year=2014, start_period=1, 
                                end_year=2014, end_period=4)
        expected_data = [{'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Consulting and product support services',
  'operatingSegmentRevenue': '$5,090,000,000',
  'operatingSegmentRevenue_effvalue': '5090000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Windows PC operating system',
  'operatingSegmentRevenue': '$14,826,000,000',
  'operatingSegmentRevenue_effvalue': '14826000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Server products and tools',
  'operatingSegmentRevenue': '$18,612,000,000',
  'operatingSegmentRevenue_effvalue': '18612000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Advertising',
  'operatingSegmentRevenue': '$4,557,000,000',
  'operatingSegmentRevenue_effvalue': '4557000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Microsoft Office system',
  'operatingSegmentRevenue': '$23,538,000,000',
  'operatingSegmentRevenue_effvalue': '23538000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Surface',
  'operatingSegmentRevenue': '$3,900,000,000',
  'operatingSegmentRevenue_effvalue': '3900000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Other products and services',
  'operatingSegmentRevenue': '$6,234,000,000',
  'operatingSegmentRevenue_effvalue': '6234000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Xbox',
  'operatingSegmentRevenue': '$9,121,000,000',
  'operatingSegmentRevenue_effvalue': '9121000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Phone',
  'operatingSegmentRevenue': '$7,702,000,000',
  'operatingSegmentRevenue_effvalue': '7702000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Commercial Licensing - Commercial',
  'operatingSegmentRevenue': '$41,039,000,000',
  'operatingSegmentRevenue_effvalue': '41039000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Commercial - Commercial Other',
  'operatingSegmentRevenue': '$10,836,000,000',
  'operatingSegmentRevenue_effvalue': '10836000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Operating Segments - Productivity And Business Processes',
  'operatingSegmentRevenue': '$26,431,000,000',
  'operatingSegmentRevenue_effvalue': '26431000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Devices and Consumer Licensing - Devices and Consumer',
  'operatingSegmentRevenue': '$14,969,000,000',
  'operatingSegmentRevenue_effvalue': '14969000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Devices and Consumer - Devices and Consumer Other',
  'operatingSegmentRevenue': '$8,825,000,000',
  'operatingSegmentRevenue_effvalue': '8825000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'More Personal Computing - Operating Segments',
  'operatingSegmentRevenue': '$42,953,000,000',
  'operatingSegmentRevenue_effvalue': '42953000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Intelligent Cloud - Operating Segments',
  'operatingSegmentRevenue': '$23,715,000,000',
  'operatingSegmentRevenue_effvalue': '23715000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Computing and Gaming Hardware - Hardware - Devices and Consumer',
  'operatingSegmentRevenue': '$10,183,000,000',
  'operatingSegmentRevenue_effvalue': '10183000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 136461,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Hardware - Devices and Consumer - Phone Hardware',
  'operatingSegmentRevenue': '$7,524,000,000',
  'operatingSegmentRevenue_effvalue': '7524000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515272806/0001193125-15-272806-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0000789019',
  'Company': 'Microsoft Corp',
  'accession_id': 143120,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-06-30',
  'entity_id': 5716,
  'fast_index_dim': 5716150,
  'is_subtotal': False,
  'label': 'Revenue',
  'operatingSegmentRevenue': '$93,580,000,000',
  'operatingSegmentRevenue_effvalue': '93580000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/789019/000119312515353706/0001193125-15-353706-index.htm',
  'sic_code': 7372,
  'ticker': 'MSFT'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'New Software Licenses And Cloud Software Subscriptions',
  'operatingSegmentRevenue': '$10,025,000,000',
  'operatingSegmentRevenue_effvalue': '10025000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Hardware Systems Support',
  'operatingSegmentRevenue': '$2,384,000,000',
  'operatingSegmentRevenue_effvalue': '2384000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Software And Cloud Business',
  'operatingSegmentRevenue': '$29,491,000,000',
  'operatingSegmentRevenue_effvalue': '29491000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Hardware Systems Products',
  'operatingSegmentRevenue': '$2,825,000,000',
  'operatingSegmentRevenue_effvalue': '2825000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Services',
  'operatingSegmentRevenue': '$3,553,000,000',
  'operatingSegmentRevenue_effvalue': '3553000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Software License Updates Product Support',
  'operatingSegmentRevenue': '$18,858,000,000',
  'operatingSegmentRevenue_effvalue': '18858000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Hardware Systems Business',
  'operatingSegmentRevenue': '$5,209,000,000',
  'operatingSegmentRevenue_effvalue': '5209000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Cloud Infrastructure As A Service',
  'operatingSegmentRevenue': '$608,000,000',
  'operatingSegmentRevenue_effvalue': '608000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Total for operating segments',
  'operatingSegmentRevenue': '$38,253,000,000',
  'operatingSegmentRevenue_effvalue': '38253000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'},
 {'CIK': '0001341439',
  'Company': 'Oracle Corp',
  'accession_id': 134892,
  'calendar_period': 0,
  'calendar_year': 2014,
  'disclosure_type': '66',
  'end_date': '2015-05-31',
  'entity_id': 2606,
  'fast_index_dim': 2606150,
  'is_subtotal': False,
  'label': 'Revenues',
  'operatingSegmentRevenue': '$38,226,000,000',
  'operatingSegmentRevenue_effvalue': '38226000000.00000000',
  'sec_html_url': 'http://www.sec.gov/Archives/edgar/data/1341439/000119312515235239/0001193125-15-235239-index.htm',
  'sic_code': 7372,
  'ticker': 'ORCL'}]
        self.assertListEqual(data, expected_data, "Breakouts did not match")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()