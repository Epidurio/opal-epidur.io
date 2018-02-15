class BaseApi(object):
    def demographics(self, hospital_number):
        """ get me all demographics information for this patient
        """
        raise NotImplementedError('Please implement a demographics query')
