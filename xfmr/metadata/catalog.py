"""
Core classes used to manage all metadata 
"""



class Catalog:
    """Wrapper to hold metadata DataObject instances when working with multiple
    data objects or a project where all metadata for data objects is centrally
    tracked
    
    Attributes
    ----------
    objects : list
        Data object names list for 
    base : dict dict of dicts
        Dictionary with all 
    columns : dict
        
    misc : dict

    """

    def __init__(self):
        self.objects = []
        self.base = {} 
        self.columns = {} 
        self.misc = {}

