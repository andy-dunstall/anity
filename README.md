# Anity CLI
[anity.io](https://anity.io) is an uptime monitoring tool that enables developers to monitor their APIs using system tests written in Python rather than traditional ‘ping’ tests.

![Suite summary](images/summary.png?raw=true "Summary")

Each monitor has an associated test suite written in Python with the `unittest` framework. The monitor will then run your test suite on a configured schedule. All results from the test suite are recorded and can be configured to configure an alerts when tests fail. Each test case run can be inspected which will include the tests output, runtime and status.

Writing your system tests in Python enables:
* Develop complex system tests quickly,
* Deploy your tests alongside your application code via CI/CD,
* Store your tests in version control alongside the application code their testing.

_Note this is still an early release so questions and feedback are appreciated by emailing andy@anity.io_

## Setup
This section describes the setup process to create your first monitor and upload your test suite.
1. Sign in at [anity.io](https://anity.io),
2. Select 'New Monitor' and give a monitor name and optionally provide a pushover user key to configure alerts when tests fail,
3. Once your monitor is created you'll be redirected to your API key,
4. Clone the anity-cli (this repo)
```bash
   $ git clone https://github.com/andy-dunstall/anity-cli.git
```
5. Add an environment variable `ANITY_API_KEY=your_api_key`,
6. Zip up your Python `unittest` suite. See `fake_package/` for the directory
structure.
```bash
   $ zip -r fake_package.zip fake_package
```
7. Add your test suite to anity. This will start invoking your tests on your configured schedule:
```bash
   $ python3 -m anity update mysuite.zip
```
8. Optionally invoke your test suite to check its working as expected. This will print the test results to stdout
```bash
   $ python3 -m anity invoke
```
9. In [anity.io](https://anity.io) view your monitor summary and inspect test results.

![Suite test results](images/results.png?raw=true "Results")
