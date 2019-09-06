# tmessage
## This is a lightweight and low bandwidth CLI tool which can be used for group communication right from your terminal (isn't this cool ; ) )

### Installation instructions

* Clone this project using the command ```git clone https://github.com/Haider8/tmessage.git```
* Setup your python3 virtual environment using this command ```virtualenv -p python3 venv```
* Switch to your venv using ```source venv/bin/activate```
* Now install the required dependencies by running ```pip install -r requirements.txt```
* Now to run tmessage use ```python msg.py --user [YOUR USERNAME] --server [YOUR BROKER IP OR URL (OPTIONAL)]```

#### NOTE: If you don't want to create your own broker it's perfectly fine as tmessage is using a default broker ```test.mosquitto.org```. Therefore, you can then run tmessage using ```python msg.py --user [YOUR USERNAME]```

#### To test this you can open different terminal tabs of course.

### Development Instructions

* You can first fork tmessage and can then clone using command ```git clone https://github.com/[YOUR USERNAME]/tmessage.git```
* Please send PRs using new branch and not master
* Commit message should perfectly describe the code changes done by you

*Would love to hear any suggestions, feedback, feature requests or any other issue*