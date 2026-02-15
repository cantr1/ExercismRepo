package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, avgLayerTime int) int {
    if avgLayerTime == 0 {
        return len(layers) * 2
    }
    return len(layers) * avgLayerTime
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
    noodleCount := 0
    sauceCount := 0
    for _, layer := range(layers) {
        if layer == "noodles" {
            noodleCount++
        } else if layer == "sauce" {
            sauceCount++
        }
    }
    return noodleCount * 50, float64(sauceCount) * 0.2
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendList, selfList []string) {
    selfList[len(selfList) - 1] = friendList[len(friendList) - 1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(twoPersons []float64, portions int) []float64 {
    var scaledRecipe []float64
    for _, value := range(twoPersons) {
        scaledRecipe = append(scaledRecipe, (value / 2.0) * float64(portions))
    }
    return scaledRecipe
}
