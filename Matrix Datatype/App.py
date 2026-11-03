class Matrix():
    def __init__(self,lst=[]):
        self.elements=lst

    def isMatrix(self):
        """This method returns True or False on the basis of
          the given object

        Requirements to consider the list a matrix
        1) There must be a trailing 'n' at the end of the list
        2) All rows (between 'n' separators) must have equal length
        3) The matrix must not be empty (at least one row and one column)"""
        
        # Basic checks
        if not self.elements:
            return False
        if self.elements[-1] != 'n':
            return False
        if not all(isinstance(x, (int, str)) for x in self.elements):
            return False

        # Parse rows
        rows = []
        current = []
        for element in self.elements:
            if element == 'n':
                if not current:  # empty row
                    return False
                rows.append(current)
                current = []
            else:
                current.append(element)

        if not rows:
            return False

        # All rows must have the same number of elements
        row_len = len(rows[0])
        if row_len == 0:
            return False
        for r in rows:
            if len(r) != row_len:
                return False

        return True

    def _parse_rows(self):
        rows = []
        current = []
        for element in self.elements:
            if element == 'n':
                if not current:
                    return []
                rows.append(current)
                current = []
            else:
                current.append(element)
        return rows

    def Order(self):
        """"This method returns the order of the matrix in a form of a string and
            Hits none when the given object is not a matrix"""
        if self.isMatrix():
            return None

        rows = self._parse_rows()
        if not rows:
            return None

        return f"{len(rows)}x{len(rows[0])}"
    def isNull(self):
        """This function will tells you if the matrix
            is null matrix or not"""
        if self.isMatrix():
            count=''
            for element in self.elements:
                if element==0 or element=='n':
                    count+='Y'
                else:
                    count+='N'
                    break
            if 'N' not in count:
                return True
            else:
                return False
        else:
            return False
    
    def isColumn(self):
        """Return True if the represented matrix is a single-column matrix.

        The list uses the string 'n' to separate rows. This method requires
        the entire matrix list to end with 'n'. It parses rows by splitting
        at each 'n' and verifies every row contains exactly one element.
        
        # Require trailing 'n' as the matrix terminator
        if not self.elements or self.elements[-1] != 'n'
            return False"""

        rows = []
        current = []
        for element in self.elements:
            if element == 'n':
                # empty rows (consecutive 'n' or leading 'n') are invalid
                if not current:
                    return False
                rows.append(current)
                current = []
            else:
                current.append(element)

        if not rows:
            return False

        for r in rows:
            if len(r) != 1:
                return False
        return True

    def isRow(self):
        """Return True if the represented matrix is a single-row matrix."""
        
        if self.isMatrix():
            count=0
            for element in self.elements:
                if element == 'n':
                    count+=1

            if count==1:
                return True
            else:
                return False
        else:
            return False 
        
    def isSquare(self):
        """Return True if the represented matrix has the same number of rows and columns."""
        order = self.Order()
        if not order:
            return False

        rows, cols = order.split('x')
        return rows == cols

    def isDiagonal(self):
        """Returns True if the given matrix has the elements in a diagonal form
            but it should be a square matrix first"""
        if not self.isMatrix() or not self.isSquare():
            return False

        rows = self._parse_rows()
        n = len(rows)

        # Check if all non-diagonal elements are 0
        for i in range(n):
            for j in range(n):
                if i != j : # Non-diagonal elements
                    if rows[i][j] != 0:
                        return False

        return True
    def Determinant(self):
        """Returns a integer which tells the Determinant of the given Matrix,
            returns None if the given object is not Matrix"""
        if not self.isMatrix() or not self.isSquare():
                    return None
        mat=self._parse_rows()
        order=self.Order()
        for l in range(len(order[0])):
            if l%2==0:
                self[l]+mat
            elif l%2!=0:
                self[l]-mat 
        
"""-== Test Objects ============================================-"""
matrix1 = Matrix([29,23,'n',23,53,'n',34,64,'n'])
matrix2 = Matrix([0,0,0,'n',0,0,0,'n',0,0,0,'n'])
matrix3 = Matrix([12,'n',13,'n',14,'n'])
matrix4 = Matrix([12,10,9,8,'n'])
matrix5 = Matrix([0,0,'n',0,0,'n'])
matrix6 = Matrix([21,0,0,'n',0,22,0,'n',0,0,23])
matrix7 = Matrix([1,0,4,-6,'n',
                  2,5,0,3,'n',
                  -1,2,3,5,'n',
                  2,1,-2,3,'n'])

"""-== Test Operations ==========================================-"""
# order=matrix1.Order()
# print('matrix1 isMatrix -', matrix1.isMatrix(), 'isColumn -', matrix1.isColumn())
# print('matrix2 isMatrix -', matrix2.isMatrix(), 'isColumn -', matrix2.isColumn())
# print('matrix3 isMatrix -', matrix3.isMatrix(), 'isColumn -', matrix3.isColumn())
# print(matrix4.isRow())
# print(matrix5.isSquare())
# print(matrix6.isDiagonal())
# print(Order of the matrix is ,order)
print(matrix7.Order())
print(matrix7._parse_rows())