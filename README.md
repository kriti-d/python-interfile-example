# Python Example to show inter-file findings of Snyk Code

A simple example to show differences between Snyk Code findings and Bandit findings

## How to

Make sure you install [Snyk](https://support.snyk.io/hc/en-us/articles/360003812538-Install-the-Snyk-CLI) and [Bandit](https://pypi.org/project/bandit/) installed
```bash
brew install snyk
pip install bandit
```

From the directory, to test for SAST vulns, run
```bash
# using Snyk
snyk code test

# using Bandit
bandit -r .
```

### Interesting Test

On `execer.py` if we change `foo` to String `'foo'` on line 5, then the Snyk Code results are much different. 

Bandit has a medium severity finding of `Use of exec` with high confidence. Even though we use `exec()`, if the input from the request does not reach that function, then this is not a true Code Injection vulnerability. 

If the unsanitized input does not flow to a sink, Snyk does not call it out as a vulnerability. Snyk is actually looking for an entire source to sink flow flow, which results in a lot less false positives.

Further, Snyk can do this analysis over separate files, which other static analysis tools have had limitations with. 