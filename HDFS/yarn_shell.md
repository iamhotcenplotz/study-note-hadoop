# YARN shell commands
- check application lsit
    ```shell
    yarn application -list
    ```
- check logs
  ```shell
  yarn logs -applicationId application_1648019508270_0004
  yarn logs -applicationId application_1648019508270_0004 -containerId container_1648019508270_0004_01_000001
  ```
- check container logs
  ```shell
  yarn logs -applicationId <ApplicationId> -containerId <ContainerId>
  yarn logs -applicationId application_1648019508270_0004 -containerId container_1648019508270_0004_01_000001
  ```
- check attempt logs
  ```shell
  yarn applicationattempt -list <ApplicationId>
  yarn applicationattempt -list application_1648019508270_0004
  ```
- check application attempt status
  ```shell
  yarn applicationattempt -status <ApplicationAttemptId>
  ```
- check node status
  ```shell
  yarn node -list -all
  ```
- refresh yarn queue 
  ```shell
  yarn rmadmin -refreshQueues
  ```
- check yarn queue status
  ```shell
  yarn queue -status <QUeueName>
  yarn queue -status default
  ```