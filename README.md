# edit-movie

Edit-movie is a Python script that allows you to perform various video editing tasks, including converting between horizontal and vertical videos, maintaining aspect ratios, stretching, and more. It utilizes the MoviePy library for video editing.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [TODO](#todo)

## Overview

Edit-movie simplifies the video editing process, providing a set of functions to manipulate video and audio clips. 
Whether you need to convert video orientations, maintain aspect ratios, or automate uploads to various platforms, edit-movie has you covered.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Axlfc/edit-movie
   cd edit-movie
   ```

2. Install required dependencies:
   ```bash
   pip install moviepy
   ```

## Usage

1. Import the script in your Python code:
   ```python
   from edit_movie import *
   ```

2. Utilize the provided functions based on your editing needs. Example:
   ```python
   # Convert vertical videos to horizontal
   video_clips = import_videos("video1.mp4", "video2.mp4")
   convert_vertical_to_horizontal(video_clips)
   ```

3. Run your Python script.

## TODO

1. **[Prove consistent horizontal-to-vertical video and vertical-to-horizontal logic](https://github.com/Axlfc/edit-movie/issues/1)**
   - **Description:** Validate and ensure consistent functionality for converting between horizontal and vertical videos.

2. **[Prove music video short based on images or video input can be edited and exported correctly](https://github.com/Axlfc/edit-movie/issues/2)**
   - **Description:** Test data will come from [afaces-reel repo](https://github.com/afaces/afaces-reel) output.

3. **[Functions to automate upload videos to YouTube (or YT shorts) to TikTok and IG reels automatically after being exported](https://github.com/Axlfc/edit-movie/issues/3)**
   - **Description:** Implement functions to automate video uploads to various platforms.

4. **[Keep aspect ratio](https://github.com/Axlfc/edit-movie/issues/4)**
   - **Description:** Ensure that the aspect ratio is maintained during video editing.

5. **[Stretch if needed](https://github.com/Axlfc/edit-movie/issues/5)**
   - **Description:** Implement stretching functionality if required.

6. **[Do not upscale](https://github.com/Axlfc/edit-movie/issues/6)**
   - **Description:** Restrict upscaling of videos during editing.

7. **[Add black bars if needed](https://github.com/Axlfc/edit-movie/issues/7)**
   - **Description:** Implement the addition of black bars to maintain the aspect ratio.

8. **[Add white bars if needed](https://github.com/Axlfc/edit-movie/issues/8)**
   - **Description:** Implement the addition of white bars to maintain the aspect ratio.

9. **[Add blurred image if needed](https://github.com/Axlfc/edit-movie/issues/9)**
   - **Description:** Implement the addition of a blurred image if required.

10. **[Crop image if needed](https://github.com/Axlfc/edit-movie/issues/10)**
    - **Description:** Implement image cropping functionality if required.

11. **[`change_image_proportions` function](https://github.com/Axlfc/edit-movie/issues/11)**
    - **Description:** Implement the `change_image_proportions` function.

