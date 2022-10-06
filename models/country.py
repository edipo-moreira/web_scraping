class Country:
    def __init__(self, name: str, capital: str, population: str, area: float):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area

    def to_dict(self):
        return {
            "name": self.name if self.name.lower() != "none" else None,
            "capital": self.capital if self.capital.lower() != "none" else None,
            "population": self.population,
            "area": self.area,
        }
