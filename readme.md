# Bird Watching Made Easy

## What is the motivation?

I have a birdfeeder on my deck, and we get quite a lot of visitors throughout the day.
My girlfriend and I work all day, so we often miss most of the birds during the weekday.

How many birds do we miss?
How many birds even visit out deck in a day?

These questions motivated me to devise a system that would monitor the birdfeeder and tell us when we have a visitor.
This problem is quite straight forward, and it isn't at the same time.
I will obviously need a camera and some way to process the video into information about visits from our guests.
The birdfeeder is stationary, and I can position the camera in the same place such that the image is consistent.
I have some experience in computer vision, but we are going to have to go on a journey to get this to work.

## The Plan

### Step 1: Camera and Pi

This step is pretty easy. I got a standard webcam and a Raspberry Pi for computing the images.
As a bonus, I can also use it as a mini web server, so I can view the live feed when I am at home.
I am a python dev for my day job, so I am using python to power this project.

Deal with it.

*I am thinking that a Flask + HTMX web app would fit my need nicely.*

Add notes from installation here.

### Step 2: How do we detect a bird?!

So this is where my knowledge gets a bit thin.
