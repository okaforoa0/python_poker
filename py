from bakery import assert_equal
# do not delete the above line
def hand_to_string(hand:list[int]) -> str:
    '''
    This function consumes a list of integers and returns them as a string with a space in between.
    
    Args:
    hand (list[int): Card numbers in hand that we want to convert to a string.
    
    Returns:
    str: The corrected hand.
    '''
    return convert_hand(hand[0]) +" "+ convert_hand(hand[1]) + " " + convert_hand(hand[2])
def convert_hand(hand:int) -> str:
    '''
    This function consumes a single integer and returns it as a string.
    
    Args:
    hand (list[int]): Card numbers in hand that we want to convert to a string.
    
    Returns:
    str: The corrected hand.
    '''
    if hand == 10:
        return "X"
    elif hand == 11:
        return "J"
    elif hand == 12:
        return "Q"
    elif hand == 13:
        return "K"
    elif hand == 14:
        return "A"
    else:
        return str(hand)
    
assert_equal(hand_to_string([5,6,7]), "5 6 7")
assert_equal(hand_to_string([10,11,12]), "X J Q")
assert_equal(hand_to_string([12,13,14]), "Q K A")

from bakery import assert_equal
# do not delete the above line
def sort_hand(hand: list[int]) -> list[int]:
    '''
    This function consumes a list of integers and returns them as a list of integers from smallest to largest.
    
    Args:
    hand (list[int]): Hand of a list of integers that we want to convert from largest to smallest.
    
    Returns:
    hand (list[int]): The corrected list of integers from largest to smallest.
    '''
    a1 = hand[0]
    a2 = hand[1]
    a3 = hand[2]
    if a1 > a2> a3:
        return [a1, a2, a3]
    if a2> a3 > a1:
        return [a2, a3, a1]
    if a3> a1> a2:
        return [a3, a1, a2]
    if a2> a1> a3:
        return [a2, a1, a3]
    if a3> a2 > a1:
        return [a3, a2, a1]
    if a1 > a3 > a2:
        return [a1, a3, a2]
    return hand
 
assert_equal(sort_hand([0,1,2]), [2,1,0])
assert_equal(sort_hand([2,3,4]), [4,3,2])
assert_equal(sort_hand([4,5,6]), [6,5,4])
assert_equal(sort_hand([1,3,2]), [3,2,1])
assert_equal(sort_hand([5,3,7]), [7,5,3])
assert_equal(sort_hand([8,7,9]), [9,8,7])
assert_equal(sort_hand([6,7,2]), [7,6,2])
assert_equal(sort_hand([1,9,2]), [9,2,1])
assert_equal(sort_hand([3,2,1]), [3,2,1])
assert_equal(sort_hand([2,3,1]), [3,2,1])
assert_equal(sort_hand([8,3,2]), [8,3,2])
assert_equal(sort_hand([9,3,4]), [9,4,3])

from bakery import assert_equal
# do not delete the above line
def has_triple(hand: list[int]) -> bool:
    '''
    This function accepts a lsit of three integers and returns True if the list has the same identical numbers.
    
    Args: 
    hand list[int]: Consumes a hand that has a list of integers.
    
    Returns:
    bool: If the list of integers are the same, it returns True, otherwise False. 
    '''
    if [hand[0], hand[1], hand[2]] == [hand[0], hand[0], hand[0]]:
        return True
    elif [hand[0], hand[1], hand[2]] == [hand[0], hand[1], hand[2]]:
        return False
    
assert_equal(has_triple([1,1,1]), True)
assert_equal(has_triple([2,3,3]), False)
assert_equal(has_triple([2,2,2]), True)
assert_equal(has_triple([4,3,2]), False)
assert_equal(has_triple([6,6,6]), True)

from bakery import assert_equal
# do not delete the above line
def has_straight(hand: list[int]) -> bool:
    '''
    This function consumes a list of three integers and returns True if it is in direct consecutive order from largest to smallest.
    
    Args:
    hand(list[int]): This consumes a list from greatest to largest.
    
    Returns:
    bool: Returns True if list is in consecutive order. 
    '''
    if hand[0]-1 == hand[1] and hand[1]-1 == hand[2]:
        return True
    else:
        return False
    
assert_equal(has_straight([3,2,1]), True)
assert_equal(has_straight([5,4,3]), True)
assert_equal(has_straight([4,2,1]), False)

from bakery import assert_equal
# do not delete the above line
def has_pair(hand: list[int]) -> bool:
    '''
    This function consumes a list of integers and returns True if it has a pair.
    
    Args:
    hand(list[int]): Consumes a list of integers.
    
    Returns:
    bool: Returns True if integers has a pair.
    '''
    if hand[0] == hand[1]:
        return True
    elif hand[0] == hand[2]:
        return True
    elif hand[1] == hand[2]:
        return True
    else:
        return False
       
assert_equal(has_pair([9,3,3]), True)
assert_equal(has_pair([5,5,3]), True)
assert_equal(has_pair([3,2,1]), False)

from bakery import assert_equal
from hands import has_pair, has_triple, has_straight
# do not delete anything above this line
def score_hand(hand: list[int]) -> int:
    '''
    This function consumes a list of three integers and returns an int.
    
    Args:
    hand(list[int]): Consumes a list of integers and returns the score as an int.
    
    Returns:
    int: The score based on the list of integers.
    '''
    num = 16**3
    total_score = hand[0]*16**2 + hand[1]*16 + hand[2]
    if has_triple(hand):
        return 16*num + total_score
    if has_pair(hand):
        return hand[1]*num + total_score
    elif has_straight(hand):
        return 15*num + total_score
    return total_score
   
assert_equal(score_hand([4, 3, 2]), 62514)
assert_equal(score_hand([5, 3, 3]), 13619)
assert_equal(score_hand([5, 5, 3]), 21843)
assert_equal(score_hand([0, 0, 0]), 65536)

from bakery import assert_equal
from score import score_hand
# do not delete anything above this line

def dealer_plays(hand: list[int]) -> bool:
    '''
    This function consumes a hand which is an int list and returns a bool.
    
    Args:
    hand(list[int]): Consumes a hand and returns true if hand has a queen or higher.
    
    Returns:
    bool: Returns true or false if hand has a queen or higher or not.
    '''
    if score_hand(hand) >= score_hand([12, 3, 2]):
        return True
    else:
        return  False
                    
assert_equal(dealer_plays([11, 3, 2]), False)
assert_equal(dealer_plays([4, 3, 2]), True)
assert_equal(dealer_plays([5, 5, 3]), True)
assert_equal(dealer_plays([7, 7, 7]), True)
assert_equal(dealer_plays([3, 4, 4]), True)

from poker import deal,dealer_plays,score_hand,hand_to_string,sort_hand
# don't remove the above line. Note that "get_choice" is also already defined.
def play_round() -> int:
    player_hand = deal()
    dealer_hand = deal()
    card = hand_to_string(player_hand)
    player_score = 0
    print(card)
    if get_choice() == "f":
        return player_score - 10
    else:
        print(hand_to_string(dealer_hand))
        if dealer_plays(dealer_hand) == False:
            return player_score + 10
        if score_hand(sort_hand(player_hand)) > score_hand(sort_hand(dealer_hand)):
            return player_score + 20
        else:
            return player_score - 20
            
def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")
