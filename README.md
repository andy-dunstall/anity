# Anity CLI
[anity.io](https://anity.io) is an uptime monitoring tool built to enable running more complex system tests rather than the standard 'ping' requests provided by other services.

Test suites in Anity are written in Python with the `unittest` framework. This means:
* Software engineers can quickly write system tests rather than deal with with complex GUI configurations. Such as creating an account, performing some action, then deleting that account,
* Test suites can be version controlled,
* Tests can be updated via the Anity CLI as part of the systems deployment CI/CD pipeline to ensure the tests remain up to date.

## Features
* Test suites are run every 15 minutes (this will be confiurable in a future release),
* View a summary of each test suite including the current status (passing / failing), average pass rate and average runtime,
* View each individual test run and output for the failed tests,
* Create multiple monitors

### Priority Features
* Notifications when tests fail. The first interation of notifications will use [Pushover](https://pushover.net/),
* Configurable scheduling of when test suites run. This will support both a rate (such as every 5 minutes) and cron (such as Saturdays at 2am).

_Note this is still an early release so feedback is appreciated by emailing andy@anity.io_

## Setup
This section lists the setup process to create your first monitor and upload your test suite.
1. Sign in at [anity.io](https://anity.io),
2. Create a monitor and view the monitors settings to get your API key,
3. Clone the anity-cli (this repo)
```bash
   $ git clone ...
   $ cd anity-cli
```
4. Add an environment variable `ANITY_API_KEY=your_api_key`,
5. Zip up your Python `unittest` suite. See `fake_package/` for the directory
structure.
```bash
   $ zip -r fake_package.zip fake_package
```
6. Install the requirements
```bash
   $ pip3 install -r requirements.txt
```
7. Add your test suite to anity. This will start invoking your tests every 15 minutes (soon to be configurable):
```bash
   $ python3 -m anity update mysuite.zip
```
8. Optionally invoke your test suite to check its working as expected. This will print the test results to stdout
```bash
   $ python3 -m anity invoke
```
9. In [anity.io](https://anity.io) view your monitor summary and inspect test results.


![Suite summary](images/summary.png?raw=true "Summary")
![Suite test results](images/results.png?raw=true "Results")
