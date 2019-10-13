# tmessage
[![Build Status](https://travis-ci.com/Haider8/tmessage.svg?branch=master)](https://travis-ci.com/Haider8/tmessage)
## This is a lightweight and low bandwidth CLI tool which can be used for group communication right from your terminal (isn't this cool ; ) )


![Hacktoberfest 2019 presented by DigitalOcean and DEV](https://hacktoberfest.digitalocean.com/assets/logo-hf19-header-8245176fe235ab5d942c7580778a914110fa06a23c3d55bf40e2d061809d8785.svg)
### Contributions are welcome for [Hacktoberfest 2019](https://hacktoberfest.digitalocean.com/) (Presented by DigitalOcean and DEV). Search for issues labeled [`Hacktoberfest`](https://github.com/Haider8/tmessage/issues?q=is%3Aopen+is%3Aissue+label%3AHacktoberfest).

* [Our Contributing Guidelines](https://github.com/Haider8/tmessage/blob/master/CONTRIBUTING.md)
* [Our Code of Conduct](https://github.com/Haider8/tmessage/blob/master/CODE_OF_CONDUCT.md)

### Installation instructions

* Clone this project using the command ```git clone https://github.com/Haider8/tmessage.git```
* Setup your python3 virtual environment using this command ```virtualenv -p python3 venv```
* Switch to your venv using ```source venv/bin/activate```
* Now install the required dependencies by running ```pip install .```
* Now to run tmessage use ```tmessage --user [YOUR USERNAME] --port [PORT (optional)] --server [YOUR BROKER IP OR URL (optional)] --dont-store (optional)```
* By default, messages are stored in a SQLite database. To turn this feature off, simply use the `--dont-store` argument.
* To test this you can open different terminal tabs.

### Some optional instructions for PROs ;)
* If you don't want to create your own broker it's perfectly fine as tmessage is using a default broker ```test.mosquitto.org```. Therefore, you can then run tmessage using ```python msg.py --user [YOUR USERNAME]```.

* If you happen to use this on a different port, it can be specified as - 
```tmessage --user [USERNAME] --port [PORT]```. If omitted, it defaults to 1883.

* This project uses an [API](https://github.com/Haider8/tmessage-api) for the authentication of users. Default API Url is [this](https://peaceful-waters-15584.herokuapp.com). If you want to use your own authentication API you can deploy our [tmessage-api](https://github.com/Haider8/tmessage-api) locally(for testing) or on some cloud (the default API is hosted on Heroku). Then, you can set that Url in `.env` file like this `TMESSAGE_API_URL=http://localhost:8080` or `TMESSAGE_API_URL=<your-api-url>`.


### Development Instructions

* You can first fork tmessage and can then clone using command ```git clone https://github.com/[YOUR USERNAME]/tmessage.git```
* Please send PRs using new branch and not master
* Commit message should perfectly describe the code changes done by you

*Would love to hear any suggestions, feedback, feature requests or any other issue*