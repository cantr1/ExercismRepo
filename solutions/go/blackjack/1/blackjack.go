package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
    case "ace":
        return 11
    case "two":
        return 2
    case "three":
        return 3
    case "four":
        return 4
    case "five":
        return 5
    case "six":
        return 6
    case "seven":
        return 7
    case "eight":
        return 8
    case "nine":
        return 9
    case "ten":
        return 10
    case "jack":
        return 10
    case "queen":
        return 10
    case "king":
        return 10
    default:
        return 0
    }
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
    c1 := ParseCard(card1)
    c2 := ParseCard(card2)
    hand := c1 + c2
    dc := ParseCard(dealerCard)
    
	if card1 == "ace" && card2 == "ace" {
        return "P"
    }

    if hand == 21 {
        if dc == 10 || dc == 11 {
        	return "S"
    	}
        return "W"
    }
    
    if hand >= 17 && hand <= 20 {
        return "S"
    }

    if hand <= 11 {
        return "H"
    }

    if hand >= 12 && hand <= 16 {
        if dc >= 7 {
            return "H"
        }
        return "S"
    }

    return ""
}
