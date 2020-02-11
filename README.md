- TO DO: update set up instructions

# Chipotle Survey Hack
Does your manager tell you to fill out the feedback surveys during your 30's? Are you tired of wasting away valuable minutes clicking dots and entering numbers? Fear not, for this script when fed any number of codes will automatically fill out Chipotle feedback surveys for you.

## Set up
Make sure an `input.txt` file exists in the same folder as the python script. The 20-digit survey code numbers must be seperated on different lines and can be of any formatting, ie seperated by spaces or dashes or whatever.

The variable `path_to_chromedriver_exe` must be set to wherever `chromedriver.exe` is stored on your machine. The default path is:
```
C:\Windows\chromedriver.exe
```

On the survey, the text box for giving more feedback is optional and thus skipped. An option is to provide a `feedback.txt` file which the program will randomly select a line from and paste that into the feedback text box. Without this file, the text box is left blank

**_Enjoy!_**

![Burrito pic](https://www.pymnts.com/wp-content/uploads/2019/08/mobile-order-ahead-Chipotle-rewards-AI.jpg)