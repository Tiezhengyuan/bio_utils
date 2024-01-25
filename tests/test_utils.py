'''
Test class Utils
'''
from .helper import *
from src.biosequtils import Utils

@ddt
class TestUtils(TestCase):

    @data(
        [
            ['chrY', 'chr8', 'chrX', 'chr2', 'chr1', 'chr10'],
            ['chr1', 'chr2', 'chr8', 'chr10', 'chrX', 'chrY'],
        ],
    )
    @unpack
    def test_sort_array(self, input, expect):
        res = Utils.sort_array(input)
        assert res == expect

    @data(
        ['a', [10,]],
        # ['b', ['ab']],
        # ['c', [{'a':1}]],
        # ['wrong', []],
    )
    @unpack
    def test_search_series(self, key, expect):
        s = pd.Series([10, 'ab', {'a':1}, [2,3,4],20,],
            index=['a','b','c','d','e'])
        res = Utils.search_series(s, key)
        assert res == expect

    # @data(
    #     ['A0A1J0MUK8', ''],
    #     # ['Q96678', ''],
    # )
    # @unpack
    # def test_parse_ncbi_acc(self, key, expect):
    #     infile = os.path.join(DIR_DATA, 'gene_refseq_uniprotkb_collab.txt')
    #     res = Utils.parse_ncbi_acc(infile)
    #     assert res.get(key[:2]) == expect