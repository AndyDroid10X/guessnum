def mass(f, obj):
	mg = {
		"earth" : f,
		"moon" : (f / 9.81) *  1.62,
		"venus" : (f / 9.81) *  8.88,
		"mercury" : (f / 9.81) *  3.71,
		"mars" : (f / 9.81) *  3.86,
		"saturn" : (f / 9.81) *  10.44,
		"sun" : (f / 9.81) *  273.1,
		"jupiter" : (f / 9.81) *  23.95,
		"uranus" : (f / 9.81) *  8.86,
		"neptune" : (f / 9.81) *  11.09
	}
	print(round(mg[obj], 3))

mass(int(input("Введите вес на Земле:")), input("Введите название обьекта на английском:").lower())