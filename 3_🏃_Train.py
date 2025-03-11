import streamlit as st
import json
import requests 
import cv2
from cvzone.PoseModule import PoseDetector
import math
import numpy as np
import plotly.graph_objects as go
import tempfile

# Fine-tuned angle calculation for better accuracy
class angleFinder:
    def __init__(self, lmlist, p1, p2, p3, drawPoints):
        self.lmlist = lmlist
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.drawPoints = drawPoints

    def angle(self):
        if len(self.lmlist) != 0:
            try:
                point1 = self.lmlist[self.p1] if len(self.lmlist) > self.p1 else None
                point2 = self.lmlist[self.p2] if len(self.lmlist) > self.p2 else None
                point3 = self.lmlist[self.p3] if len(self.lmlist) > self.p3 else None

                if point1 and point2 and point3 and len(point1) >= 3 and len(point2) >= 3 and len(point3) >= 3:
                    x1, y1 = point1[1], point1[2]
                    x2, y2 = point2[1], point2[2]
                    x3, y3 = point3[1], point3[2]
                else:
                    return None

                raw_angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                         math.atan2(y1 - y2, x1 - x2))
                adjusted_angle = max(0, min(100, int(np.interp(raw_angle, [30, 150], [100, 0]))))
                return adjusted_angle

            except Exception as e:
                print("Error in angle calculation:", e)
                return None

# Streamlit UI
st.markdown("## Fitness Trainer")
app_mode = st.sidebar.selectbox("Choose the exercise", ["About", "Left Dumbbell", "Right Dumbbell", "Squats", "Pushups", "Shoulder press"], key="exercise_select")

if app_mode != "About":
    weight = st.slider('What is your weight?', 20, 130, 40)
    goal_calorie = st.slider('Set a goal calorie to burn', 10, 200, 15)
    st.write("Click on the Start button to start the live video feed.")
    
    if 'type' not in st.session_state:
        st.session_state.type = None

    def handle_click_start():
        st.session_state.type = "Start"
        st.session_state.counter = 0

    def handle_click_stop():
        st.write(st.session_state.counter)
        st.session_state.type = "Stop"
    
    st.button('Start', on_click=handle_click_start)
    st.button('Stop',  on_click=handle_click_stop)
    
    counter = 0
    direction = 0
    frame_placeholder = st.empty()
    detector = PoseDetector(detectionCon=0.7, trackCon=0.7)

    if st.session_state['type'] == 'Start':
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, img = cap.read()
            if not ret:
                break
            img = cv2.resize(img, (640, 480))
            detector.findPose(img, draw=0)
            lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0, draw=False)

            angle1 = angleFinder(lmList, 11, 13, 15, drawPoints=True)
            left = angle1.angle()
            if left is None:
                left = 0

            if left >= 85:
                if direction == 0:
                    counter += 0.5
                    st.session_state.counter = counter
                    direction = 1
            if left <= 65:
                if direction == 1:
                    counter += 0.5
                    st.session_state.counter = counter
                    direction = 0

            st.write(f"Detected angle: {left}")  # Debugging for motion tracking
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(img, "RGB")
            cv2.waitKey(1)

    elif st.session_state['type'] == 'Stop':
        st.write("The video capture has ended")
        st.write("You did ", st.session_state.counter, " reps")
        calories = 3.8 * weight / max(1, st.session_state.counter)
        st.write("You have burned ", round(calories, 2), "kcal of calories")
        fig = go.Figure(data=[go.Bar(x=['Exercise'], y=[calories], name='Calories Burned')])
        fig.add_trace(go.Bar(x=['Exercise'], y=[goal_calorie], name='Goal Calorie'))
        fig.update_layout(title='Calories Burned', xaxis_title='Exercise', yaxis_title='Calories Burned')
        st.plotly_chart(fig)