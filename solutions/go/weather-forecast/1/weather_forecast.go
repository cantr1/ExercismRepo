// Package weather takes current conditions with current location
// to produce a weather forcast.
package weather

var (
    // CurrentCondition represents current weather state.
	CurrentCondition string
    // CurrentLocation represents the current location.
	CurrentLocation  string
)

// Forecast returns a string of the current weather forcast.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
