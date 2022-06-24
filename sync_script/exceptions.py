class CantWriteDatabase(Exception):
    """Write DB error"""
    pass

class CantGetData(Exception):
    """Error getting data from Google Sheets"""
    pass

class CantParseCourse(Exception):
    """Error getting data from Central Bank of Russia"""
    pass
