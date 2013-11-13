from mrjob.job import MRJob


class MRMatrixMultiply(MRJob):
	def mapper(self, _, line):
		colsInB = 4
		rowsInA = 3
		colsInA = 2

		matrix, row, column, value = line.split()	
		print matrix + " " + str(row) +" " + str(column) +" "+ str(value)
		if matrix is "A":
			for i in range(1,colsInB+1):
				yield (int(row), i), (column,float(value))
		else:
			for i in range(1, rowsInA+1):
				yield (i, int(column)), (row,float(value))

	def reducer(self, key, values):
		firstMultipliers = {}
		product = 0

		for valueTuple in values:
			index, value = valueTuple
			if index in firstMultipliers:
				product += firstMultipliers[index] * value
			else:
				firstMultipliers[index] = value
		yield key, product

if __name__ == '__main__':
	MRMatrixMultiply.run()
