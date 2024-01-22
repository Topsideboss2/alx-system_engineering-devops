# **Title: Postmortem - Learning from a Critical Outage**

![Birdbox image](./_docs/Birdbox.png)

**Issue Summary:**
- **Duration:** 
  - Start Time: 2024-01-22 15:30 UTC
  - End Time: 2024-01-22 16:45 UTC
- **Impact:**
  - The user authentication service was completely down for 45% of our users.
  - Users experienced inability to log in, leading to a halt in accessing critical features.
  
**Timeline:**
- **15:30 UTC:**
  - Issue Detected through a surge in customer support tickets reporting login failures.
- **15:30 UTC:**
  - Monitoring alerts failed to trigger; the issue was initially noticed by the customer support team inundated with user complaints.
- **15:40 UTC:**
  - Investigated the authentication service logs to identify any recent changes or errors.
  - Assumed it might be a database issue and began inspecting database connection logs.
- **15:45 UTC:**
  - Initially suspected a database failure due to recent updates; spent significant time investigating database configurations and connections.
- **15:50 UTC:**
  - Escalated the incident to the DevOps team after preliminary investigations failed to pinpoint the root cause.
- **16:10 UTC:**
  - Identified a misconfiguration in the authentication service that caused the failure.
- **16:30 UTC:**
  - Rolled back changes related to the service configuration.
- **16:45 UTC:**
  - Functionality restored.

**Root Cause and Resolution:**
- **Root Cause:**
  - A configuration change in the authentication service introduced an error, causing a failure in user authentication.
  - The change was related to an update in the service's token generation mechanism.
- **Resolution:**
  - Rolled back the configuration changes to revert to the previous, stable state.
  - Deployed a hotfix to address the token generation issue, ensuring proper authentication.

**Corrective and Preventative Measures:**
- **Improvements/Fixes:**
  - Implement a more robust monitoring system to detect anomalies in user authentication promptly.
  - Conduct regular code reviews for configuration changes to catch potential issues early.
- **Tasks to Address the Issue:**
  1. Implement additional monitoring alerts specifically for user authentication service health.
  2. Enhance documentation for configuration changes to prevent misconfigurations.
  3. Schedule regular team training on the importance of monitoring and quick issue detection.
  4. Conduct a comprehensive review of recent changes to identify any other potential hidden issues.