# Chipotle Survey Hack
Does your manager tell you to fill out the feedback surveys during your 30's? Are you tired of wasting away valuable minutes clicking dots and entering numbers? Fear not, for this script when fed any number of codes will automatically fill out Chipotle feedback surveys for you.

## Set up
1. **Download and install Python:** [www.python.org/downloads](https://www.python.org/downloads/).

2. **Download Selenium package:** in Command Prompt, type `py -m pip install -U selenium` and wait for download to finish.

3. **Download ChromeDriver:** [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) Make sure the version downloaded corresponds to your version of Chrome.

4. **Download that thang:** click the *Clone and download* button on and download the `.zip` file. Drag the contents of this into a new folder

5. **Configure:** open `config.txt` and change *`chromedriver_path`* to the file path of `chromedriver.exe`. By default, the bot is configured to assume you dragged `chromedriver.exe` into the folder `C:\Windows\`. In `config.txt` change `delay` to a decimal number representing the delay in seconds between each attempt (delay will be longer or shorter by a random factor between `0.8` and `1.2`)
- TO DO: update set up instructions

# Chipotle Survey Hack
Does your manager tell you to fill out the feedback surveys during your 30's? Are you tired of wasting away valuable minutes clicking dots and entering numbers? Fear not, for this script when fed any number of codes will automatically fill out Chipotle feedback surveys for you.

## Set up
1. **Download and install Python:** [www.python.org/downloads](https://www.python.org/downloads/).

2. **Download Selenium package:** in Command Prompt, type `py -m pip install -U selenium` and wait for download to finish.

3. **Download ChromeDriver:** [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) Make sure the version downloaded corresponds to your version of Chrome.

4. **Download that thang:** click the *Clone and download* button on and download the `.zip` file. Drag the contents of this into a new folder

5. **Configure:** open `config.txt` and change *`chromedriver_path`* to the file path of `chromedriver.exe`. By default, the bot is configured to assume you dragged `chromedriver.exe` into the folder `C:\Windows\`. In `config.txt` change `delay` to a decimal number representing the delay in seconds between each attempt (delay will be longer or shorter by a random factor between `0.8` and `1.2`)

6. **Input survey codes:** to feed new codes into the bot, enter each code on a separate line in `input.txt`. As long as there are 20 digits per line, the bot can understand the survey code so any format could work, i.e. `123-123-123-123-123-12` or `123 123 123 123 123 12`.

7. **Run the bot:** double click the `.py` file to run the bot


 **_NOTE:_** On the survey, the text box for giving more feedback is optional and thus skipped. An option is to provide a `feedback.txt` file which the program will randomly select a line from and paste that into the feedback text box. Without this file, the text box is left blank


![Burrito pic](https://www.pymnts.com/wp-content/uploads/2019/08/mobile-order-ahead-Chipotle-rewards-AI.jpg)
6. **Input survey codes:** to feed new codes into the bot, enter each code on a separate line in `input.txt`. As long as there are 20 digits per line, the bot can understand the survey code so any format could work, i.e. `123-123-123-123-123-12` or `123 123 123 123 123 12`.

7. **Run the bot:** double click the `.py` file to run the bot


 **_NOTE:_** On the survey, the text box for giving more feedback is optional and thus skipped. An option is to provide a `feedback.txt` file which the program will randomly select a line from and paste that into the feedback text box. Without this file, the text box is left blank


![Burrito pic](https://www.pymnts.com/wp-content/uploads/2019/08/mobile-order-ahead-Chipotle-rewards-AI.jpg)