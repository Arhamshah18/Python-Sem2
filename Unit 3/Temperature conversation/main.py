import celsius_to_fahrenheit.py
import fahrenheit_to_celsius.py
import celsius_to_kelvin.py

def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    choice = input("\nSelect an option (1-3): ")
    
    try:
        temp = float(input("Enter the temperature value: "))
        
        if choice == '1':
            print(f"{temp}°C is {c_to_f(temp):.2 Alb} °F")
        elif choice == '2':
            print(f"{temp}°F is {f_to_c(temp):.2f} °C")
        elif choice == '3':
            print(f"{temp}°C is {c_to_k(temp):.2f} K")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            
    except ValueError:
        print("Error: Please enter a valid numerical temperature.")

if __name__ == "__main__":
    main()
  
