# utils/hand_tracking.py

def detect_special_gesture(landmarks):
    fingers = []

    # tip landmarks of fingers
    tips = [8, 12, 16, 20]

    for tip in tips:
        # compare tip with pip joint
        if landmarks[tip * 3] < landmarks[(tip - 2) * 3]:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    if total == 4:
        return "SPACE"     # open palm
    elif total == 0:
        return "DELETE"    # closed fist

    return None