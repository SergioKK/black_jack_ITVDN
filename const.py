SUITS = ['heart', 'diamond', 'club', 'spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
PRINTED = {
    'ace':
        """*********
*   ^   *
*  / \  *
* /___\ *
*/     \*
*********""",
    'king':
"""*********
* |  /  *
* | /   *
* | \   *
* |  \  *
*********""",
    'queen':
    """*********
* ----- *
* |   | *
* |   | *
* |___|b*
*********""",
    'jack':
    """*********
*    -| *
*     | *
* |   / *
* ---/  *
*********""",
    '10':
    """*********
* | |--|*
* | |  |*
* | |  |*
* | |--|*
*********""",
    '9':
    """*********
* ----- *
* |   | *
* ----| *
* ----| *
*********""",
    '8':
    """*********
* |---| *
* |---| *
* |---| *
*       *
*********""",
    '7':
    """*********
* ----- *
* |   | *
*     | *
*     | *
*********""",
    '6':
    """*********
*       *
* |---- *
* |---| *
* |---| *
*********""",
    '5':
    """*********
*       *
* |---- *
* |---| *
* ----| *
*********""",
    '4':
    """*********
* |   | *
* |___| *
*     | *
*     | *
*********""",
    '3':
    """*********
*       *
* ----| *
* ----| *
* ----| *
*********""",
    '2':
    """*********
*       *
* ----| *
* |---| *
* |---- *
*********"""
}

MESSAGES = {
    'ask_start': 'Want to play?(y/n) ',
    'ask_card': 'Want new card?(y/n)',

}

NAMES = ['John', 'Jack', 'Vasya', 'Ivan']