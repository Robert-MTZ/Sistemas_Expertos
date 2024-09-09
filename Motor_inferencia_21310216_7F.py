# Motor_inferencia
# Roberto_Martinez_Bailon_21310216
# Sistemas_expertos
# Ingeniria en Mecatronica

class CarRecommendationEngine:
    def __init__(self):
        # Base de datos de carros
        self.cars = [
            {"name": "Toyota Corolla", "type": "sedan", "price": 20000, "fuel_efficiency": 30, "brand": "Toyota"},
            {"name": "Ford Mustang", "type": "sports", "price": 45000, "fuel_efficiency": 20, "brand": "Ford"},
            {"name": "Honda CR-V", "type": "SUV", "price": 30000, "fuel_efficiency": 25, "brand": "Honda"},
            {"name": "Chevrolet Silverado", "type": "truck", "price": 35000, "fuel_efficiency": 18, "brand": "Chevrolet"},
            {"name": "Tesla Model 3", "type": "sedan", "price": 50000, "fuel_efficiency": 120, "brand": "Tesla"}
        ]

    def recommend_car(self, budget, preferred_type, min_fuel_efficiency, preferred_brand):
        recommendations = []
       
        for car in self.cars:
            if car["price"] <= budget and car["type"] == preferred_type and car["fuel_efficiency"] >= min_fuel_efficiency and (car["brand"] == preferred_brand or preferred_brand == "any"):
                recommendations.append(car)

        return recommendations

def get_user_input():
    print("Bienvenido al motor de recomendación de carros.")
    budget = float(input("Ingrese su presupuesto máximo ($): "))
    preferred_type = input("Ingrese el tipo de carro preferido (sedan, sports, SUV, truck): ").strip().lower()
    min_fuel_efficiency = float(input("Ingrese la eficiencia mínima de combustible deseada (millas por galón): "))
    preferred_brand = input("Ingrese la marca preferida (o 'any' para cualquier marca): ").strip().capitalize()
   
    return budget, preferred_type, min_fuel_efficiency, preferred_brand

def main():
    engine = CarRecommendationEngine()
    budget, preferred_type, min_fuel_efficiency, preferred_brand = get_user_input()
   
    recommendations = engine.recommend_car(budget, preferred_type, min_fuel_efficiency, preferred_brand)
   
    if recommendations:
        print("\nCarros recomendados para ti:")
        for car in recommendations:
            print(f"- {car['name']}, Tipo: {car['type'].capitalize()}, Precio: ${car['price']}, Eficiencia: {car['fuel_efficiency']} mpg, Marca: {car['brand']}")
    else:
        print("No se encontraron carros que cumplan con los criterios.")

if __name__ == "__main__":
    main()
