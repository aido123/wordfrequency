from wordfrequency.workdayfactory import WorkdayFactory

class FactoryProducer:
    def get_factory(self, factory_type):
        if factory_type == "workday":
            return WorkdayFactory()