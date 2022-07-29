# Import module



from nudenet import NudeClassifier

# initialize classifier (downloads the checkpoint file automatically the first time)
classifier = NudeClassifier()


def image_checker(path_to_image_1):

				#path_to_image_1='nude.jpg'
				# Classify single image
				result=classifier.classify(path_to_image_1)



				print(result[path_to_image_1]['unsafe'])

				result_1=result[path_to_image_1]['unsafe']

				if result_1 >= 0.50:
					print("image is not good")
					result_3="blocked"

				else:
					print("image is good")
					result_3="verified"
				return result_3

#image_checker('nude.jpg')
