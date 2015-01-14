from test_unit_module import test_unit

class Usage(test_unit):
	def __init__(self):
		pass
	def test_case_0(self):
		"""
		Example of a passing test case.
		"""
		actual = 8 # 3+5
		expected = 8

		self.assert_op(actual,expected,0) # Actual result, Expected result, test case id or identifier(not optional), HINT (Optional)

	def test_case_1(self):
		"""
		Example of a failing test case without a hint.
		"""
		actual = 9 # 3+5 !=9
		expected = 8
		
		self.assert_op(actual,expected,1)	
		


	def test_case_2(self):
		"""
		Example of a failing test case with a hint
		"""
		actual = 9 # 3+5 !=9
		expected = 8
		
		self.assert_op(actual,expected, 2,"Addition is not done right.")	
		# NOTE : There is a third parameter. It is an optional parameter and will be used a hint ONLY IF the test case FAILS.


def main():
	suite = Usage()
	suite.run_tests()

if __name__ == "__main__":
	main()
