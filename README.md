# Anity CLI
[anity.io](https://anity.io) is an uptime monitoring tool built around the Python `unittest` framework. This was built with the aim of making uptime monitoring simpler for software engineers rather than trying to configure monitoring tools with complicated GUIs enabling:
* Writing tests with Python,
* Adding your monitoring tests to version control,
* Updating your monitoring tests and running as part of your CI/CD pipelines.

_Note this is still an early release so there are a number of planned features not yet available such as configuring how often your tests run, alerts when tests fail, monitoring response times, etc... Feedback is appreciated emailing andy@anity.io._

## Setup
1. Sign in at [anity.io](https://anity.io),
2. Find your API key in the top right,
3. Clone the anity-cli (this repo)
```bash
   $ git clone ...
   $ cd anity-cli
```
4. Add an environment variable `ANITY_API_KEY=your_api_key`,
5. Zip up your Python `unittest` suite
```bash
   $ zip -r mysuite.zip mysuite/
```
6. Install the requirements
```bash
   $ pip3 install -r requirements.txt
```
7. Add your test suite to anity. This will start invoking your tests every 15 minutes (soon to be configurable):
```bash
   $ python3 -m anity update mysuite.zip
```
8. Optionally manually invoke anity to run your suite with
```bash
   $ python3 -m anity invoke
```
9. Login to [anity.io](https://anity.io) to view your test results where your can inspect each suite and the results of each test ran. Results provide whether the test passed of failed, the tests average runtime, and average pass rate (over a configurable range of time)


![Suite summary](images/summary.png?raw=true "Summary")
![Suite test results](images/test_results.png?raw=true "Results")
