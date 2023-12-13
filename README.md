# Summarizer

Welcome to the Summarizer repository! This project currently features a URL and PDF summarizer, with plans for expanding the range of machine learning applications in the future.

## Overview

The existing version utilizes the Bard AI for text summarization and TKinter for the graphical user interface (GUI). Future updates will introduce more specialized models for different tasks and an improved GUI.

## Getting Started

To run the code:

1. Execute the following command:

    ```bash
    python tk_graphic.py
    ```

2. Once the application is running, you'll need to provide your Bard API key. Follow these steps to obtain the key:

    - Visit the Bard website.
    - Open the browser developer tools using `F12`.
    - Navigate to the "Application" tab.
    - Copy the value from the `_Secure-1PSID` field.

    Paste this copied value as your Bard API key when prompted by the application.

**Note:** Due to the nature of the Bard AI, there may be instances where the summarization process can result in the conflation of unrelated articles. During testing, it has been observed that a Computer Science article, for example, might be summarized into content resembling an NFL article. Please be aware of this potential behavior when using the application.