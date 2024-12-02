class MatchingCandidate:
    def __init__(self, numValue, lineString):
        self.numValue = numValue
        self.lineString = lineString.strip()
        self.matchIndex = 0
    
    # Attempt to match the next char in lineString.
    # If matched, advance matchIndex by 1, return True
    # If not matched, return False
    def match(self, c):
        if self.lineString[self.matchIndex] == c:
            self.matchIndex += 1
            return True
        else:
            return False
    
    def hasCompletedMatch(self):
        return self.matchIndex == len(self.lineString)

    def resetIndex(self):
        self.matchIndex = 0



def find_number(line):
    found_nums = []
    candidates = [
        MatchingCandidate(1, '1'),
        MatchingCandidate(2, '2'),
        MatchingCandidate(3, '3'),
        MatchingCandidate(4, '4'),
        MatchingCandidate(5, '5'),
        MatchingCandidate(6, '6'),
        MatchingCandidate(7, '7'),
        MatchingCandidate(8, '8'),
        MatchingCandidate(9, '9'),
        MatchingCandidate(1, 'one'),
        MatchingCandidate(2, 'two'),
        MatchingCandidate(3, 'three'),
        MatchingCandidate(4, 'four'),
        MatchingCandidate(5, 'five'),
        MatchingCandidate(6, 'six'),
        MatchingCandidate(7, 'seven'),
        MatchingCandidate(8, 'eight'),
        MatchingCandidate(9, 'nine')
    ]

    for c in line:
        for candidate in candidates:
            result = candidate.match(c)
            if result:
                if candidate.hasCompletedMatch():
                    found_nums.append(candidate.numValue)
                    candidate.resetIndex()
            else:
                # If we cannot keep matching, reset
                if candidate.matchIndex > 0:
                    candidate.resetIndex()
                    # Must attemp to match the char after reset in case the char
                    # is the first char of this candidate
                    candidate.match(c)
    
    return found_nums


def compute_score(line):
    nums = find_number(line)
    return nums[0] * 10 + nums[-1]


total = 0
with open('2023/d01_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        total += compute_score(line)

print(total)
