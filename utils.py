#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import BytesIO

from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile
# from gtts import gTTS
from io import BytesIO
import numpy as np


def _display_detected_frames(conf, model, st_frame, image):
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Predict the objects in the image using YOLOv8 model
    res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()

    names = model.names
    text = 'incorrect pose'

    predictedClass = res[0].boxes.cls
    # print("predictedClass.numel() -", predictedClass.numel())
    red_tint = np.full_like(res_plotted, (0, 0, 255), dtype=np.uint8)
    res_plotted = cv2.addWeighted(res_plotted, 0.7, red_tint, 0.3, 0)
    if predictedClass.numel() != 0:
        predictedClassName = names[int(predictedClass)]
        print("predictedClassName -", predictedClassName)
        text = 'Correct pose'


        green_tint = np.full_like(res_plotted, (0, 255, 0), dtype=np.uint8)
        res_plotted = cv2.addWeighted(res_plotted, 0.7, green_tint, 0.3, 0)
    cv2.putText(res_plotted, text, (50, 50,),
    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA, )
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
         )
    # return predictedClassName


@st.cache_resource
def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model


# def textToSpeech(yogaName):
#     text = "You are performing {}".format(yogaName)
#     sound_file = BytesIO()
#     tts = gTTS(text, lang='en')
#     tts.write_to_fp(sound_file)
#     st.audio(sound_file.read(), format="audio/mp3", start_time=0)


def infer_uploaded_image(conf, model):
    """
    Execute inference for uploaded image
    :param conf: Confidence of YOLOv8 model
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    source_img = st.sidebar.file_uploader(
        label="Choose an image...",
        type=("jpg", "jpeg", "png", 'bmp', 'webp')
    )

    col1, col2 = st.columns(2)
    yogaPose = ""
    with col1:
        if source_img:
            # source_img = cv2.resize(source_img, (720, int(720 * (9 / 16))))
            uploaded_image = Image.open(source_img)
            # adding the uploaded image to the page with caption
            st.image(
                image=source_img,
                caption="Uploaded Image",
                use_column_width=True
            )

    if source_img:
        if st.button("Execution"):
            with st.spinner("Running..."):
                res = model.predict(uploaded_image,
                                    conf=conf)
                names = model.names
                boxes = res[0].boxes
                predictedClass = res[0].boxes.cls
                predictedClassName = names[int(predictedClass)]
                yogaPose = predictedClassName
                # print("names -", names)
                # print("boxes -", boxes)
                # print("predictedClass -", predictedClass)
                # print("predictedClassName -", predictedClassName)
                # if predictedClassName:
                    # textToSpeech(predictedClassName)

                res_plotted = res[0].plot()[:, :, ::-1]

                with col2:
                    st.image(res_plotted,
                             caption="Detected Image",
                             use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(box.xywh)
                    except Exception as ex:
                        st.write("No image is uploaded yet!")
                        st.write(ex)
    if len(yogaPose) > 0:
        with st.container(border=True):
            st.header("Detected Yoga pose : {}".format(yogaPose))


def infer_uploaded_video(conf, model):
    """
    Execute inference for uploaded video
    :param conf: Confidence of YOLOv8 model
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    yogaPose = ""
    source_video = st.sidebar.file_uploader(
        label="Choose a video..."
    )

    if source_video:
        st.video(source_video)

    if source_video:
        if st.button("Execution"):
            with st.spinner("Running..."):
                try:
                    tfile = tempfile.NamedTemporaryFile()
                    tfile.write(source_video.read())
                    vid_cap = cv2.VideoCapture(
                        tfile.name)
                    st_frame = st.empty()
                    while vid_cap.isOpened():
                        success, image = vid_cap.read()
                        if success:
                            _display_detected_frames(conf,
                                                     model,
                                                     st_frame,
                                                     image
                                                     )
                            # yogaPose = predictedClassName

                        else:
                            vid_cap.release()
                            break
                except Exception as e:
                    st.error(f"Error loading video: {e}")
    # if len(yogaPose) > 0:
    #     with st.container(border=True):
    #         st.header("Detected Yoga pose : {}".format(yogaPose))


def infer_uploaded_webcam(conf, model):
    """
    Execute inference for webcam.
    :param conf: Confidence of YOLOv8 model
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    yogaPose = ""
    try:
        flag = st.button(
            label="Stop running"
        )
        vid_cap = cv2.VideoCapture(0)  # local camera
        st_frame = st.empty()
        while not flag:
            success, image = vid_cap.read()
            if success:
                _display_detected_frames(
                    conf,
                    model,
                    st_frame,
                    image
                )

            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Error loading video: {str(e)}")
    if len(yogaPose) > 0:
        with st.container(border=True):
            st.header("Detected Yoga pose : {}".format(yogaPose))