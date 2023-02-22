class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Flight:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def get_passengers(self):
        return self.passengers

if __name__ == "__main__":
    # Criando instâncias de Passageiro
    p1 = Passenger("João", 30)
    p2 = Passenger("Maria", 25)
    p3 = Passenger("Pedro", 40)

    # Criando instâncias de Voo
    f1 = Flight("1234", "São Paulo", "10:00")
    f2 = Flight("5678", "Rio de Janeiro", "12:00")

    # Adicionando passageiros aos voos
    f1.add_passenger(p1)
    f1.add_passenger(p2)
    f2.add_passenger(p3)

    # Exibindo passageiros de cada voo
    print("Passageiros do voo", f1.flight_number)
    for passenger in f1.get_passengers():
        print(passenger.name)

    print("Passageiros do voo", f2.flight_number)
    for passenger in f2.get_passengers():
        print(passenger.name)
