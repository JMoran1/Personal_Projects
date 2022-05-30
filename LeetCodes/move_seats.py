# 2037. Minimum Number of Moves to Seat Everyone
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

def minMovesToSeats(seats, students):
    seats = seats
    students = students
    seats.sort()
    students.sort()
    moves = 0
    for i in range(len(students)):
        if students[i] != seats[i]:
            moves += abs(students[i] - seats[i])
    return moves


seat = [4,1,5,9]
student = [1,3,2,6]
print(minMovesToSeats(seat, student))