from GUI.configfiles.log_execution import logTestExecution
from GUI.configfiles.screenshots import screenshotIt


class SoftAssertion:
    """
    Soft assertions let you make a few assertions in one test case.
    So that if one of them fails the others will be accomplished too.
    Use the method <assert_it> to evaluate the results in the middle of a test case
    For the last assertion use <assert_last>
    """
    log = logTestExecution()

    def __init__(self, driver):
        self.assertResults = []
        self.driver = driver

    def setResult(self, result, message):
        """
        :param result: a bool expression to evaluate (f.e. result = 'www.google.com' in current_url)
        :param message: description of the evaluation (f. e. "expected text 'www.google.com' FOUND in URL")
        :return:
        """
        try:
            if result:
                self.assertResults.append('PASS')
                self.log.info('{}: assertion passed'.format(message))
            else:
                self.assertResults.append('FAIL')
                self.log.error('{}: assertion failed'.format(message))
                screenshotIt(self.driver)  # if assertion failed take a screenshot
        except:
            self.assertResults.append('FAIL')
            self.log.error('Exception: assertion failed')
            screenshotIt(self.driver)  # if assertion failed take a screenshot

    def assert_it(self, result, message):
        # Append FAIL or PASS in the list of the results of the test case
        self.setResult(result, message)

    def assert_last(self, result, message):
        # Append last FAIL or PASS in the list of the results of the test case
        self.setResult(result, message)
        self.log.info([i for i in self.assertResults])
        # Then check if there is at least one FAIL in a results list
        # If so fail the test case
        if 'FAIL' in self.assertResults:
            self.log.error('Some assertions failed: Test failed')
            self.assertResults.clear()
            assert True == False
        else:
            self.log.info('All the assertions passed: Test successful')
            self.assertResults.clear()
            assert True == True