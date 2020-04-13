import cv2 as cv



backsub = cv.createBackgroundSubtractorMOG2()

capt = cv.VideoCapture(0)
while True:
	_, frame = capt.read()
	if frame is None:
		break

	substracted = backsub.apply(frame)

	cv.imshow('original', frame)
	cv.imshow('filtered', substracted)

	keyboard = cv.waitKey(30)
	if keyboard == 'q' or keyboard == 27:
		break	
