// Package weather contains variables and function to predict the weather.
package weather

var (
    // CurrentCondition is current weather.
	CurrentCondition string 
    // CurrentLocation is where we are.
	CurrentLocation  string 
)

// Forecast predicts the weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
