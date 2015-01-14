import inspect

class test_unit():
	error = ""			#Member to hold error messages and HINTS for failed test cases.
	status = ""			#Member to hold success/failure messages for failed test cases.


	def __init__(self):
		pass

	def edit_error_msg(self,test_case_id,expected,actual,hint = ""):
		"""
		Method to update error messages during execution of test cases.
		"""
		self.error += "\n\nTest case"+str(test_case_id)+ " Failure Details :\n"+"Expected Output:\n"+ str(expected) +"\n\n"+"Actual Output:\n"+ str(actual) 

		if hint != "":
			self.error+="\nHint : " + hint +"\n"

		self.status+= "Test case "+str(test_case_id)+": Failed\n"


		
	def edit_status_msg(self,query_index):
		"""
		Method to update status messages during execution of test cases.
		"""
		self.status+= "Test case "+str(query_index)+": Passed\n"



	def show_results(self):
		"""
		Method to display results of test cases ran.
		"""

		print "-------Summary of Test Cases Ran---------"
		print self.status[:-1]
		print "-----------------------------------------\n"
		if len(self.error) > 0:
			print "-----------Test Cases Failed-------------"
			print self.error
		else:
			print "Ran OK. All test cases passed."




	def assert_op(self,actual,expected,test_case_id,hint=""):
		"""
		Assert operation for the suite.
		"""

		result = actual == expected
		if result == False:
			self.edit_error_msg(test_case_id,expected,actual,hint)
		else:
			self.edit_status_msg(test_case_id)



	def run_tests(self):
		"""
		This is the method that would run all test cases of the test object.
		"""

		method_tuples = inspect.getmembers(self.__class__, predicate=inspect.ismethod)
		for method_tuple in method_tuples:
			if method_tuple[0][0:5]=="test_":
				method_tuple[1](self)
		self.show_results()

