"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from wordfrequency.workdayfactory import WorkdayFactory

class FactoryProducer:
    """
    Producer Class which will return our concrete Factory Implementation.
    """
    def get_factory(self, factory_type):
        """
        Get our AbstractFactory Concrete Implementation.
        : param: type of factory to create str
        """
        if factory_type == "workday":
            return WorkdayFactory()