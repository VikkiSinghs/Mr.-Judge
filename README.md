<img src="https://github.com/VikkiSinghs/oj/assets/68416943/4cfefc57-0594-4ef0-890e-ba7c70e54009" alt="System components for Online Judge">
<h1>💡Mr Judge - Product Spec</h1>
🤔 <b>A coding challenge is a competitive event in which a group of participants solve a set of coding questions within a specified timeframe, typically ranging from a few hours to a few days. Participants who have registered beforehand compete by submitting their solutions, which are
evaluated against concealed test cases. Based on the test results, participants are assigned scores.</b>

<h1>👀 Areas of concern</h1>
<li>Scalabiliity</li>
<li>Malicious code execution</li>
<li>Network congestion</li>

<h1>💭 Proposal</h1>
<img src="https://github.com/VikkiSinghs/oj/assets/68416943/4cfefc57-0594-4ef0-890e-ba7c70e54009" alt="System components for Online Judge">

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Technology</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Front-end</td>
      <td>React / Django User Interface</td>
      <td>Provides the user interface for interacting with the platform.</td>
    </tr>
    <tr>
      <td>User Registration and Authentication</td>
      <td>AWS Cognito</td>
      <td>Manages user registration, login, and authentication processes securely.</td>
    </tr>
    <tr>
      <td>Coding Questions and Submissions</td>
      <td  >Amazon S3</td>
      <td>Stores coding problems, user submissions, and related resources.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon DynamoDB</td>
      <td>Stores metadata for coding problems, user profiles, submission history, and verdicts.</td>
    </tr>
    <tr>
      <td>Code Evaluation Backend Servers</td>
      <td  >Amazon ECS</td>
      <td>Runs the code evaluation service, securely executing user-submitted code against test cases.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon EC2 (Worker)</td>
      <td>Handles compute-intensive tasks related to code evaluation.</td>
    </tr>
    <tr>
      <td>Test Case Management</td>
      <td>Amazon S3</td>
      <td>Stores test cases and expected results.</td>
    </tr>
    <tr>
      <td>Code Evaluation Service</td>
      <td>ECS Task</td>
      <td>Retrieves test cases from S3, runs code, and compares output to expected results.</td>
    </tr>
    <tr>
      <td>Returning Verdicts</td>
      <td  >Backend Servers (Amazon ECS)</td>
      <td>Processes the results of code execution and returns the verdict to the user.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon DynamoDB</td>
      <td>Stores verdicts and execution logs for user submissions.</td>
    </tr>
    <tr>
      <td>Visualizing User Interaction</td>
      <td >AWS AppSync</td>
      <td>Provides a GraphQL API for real-time updates and data synchronization between frontend and backend.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon Timestream</td>
      <td>Stores time-series data such as user interactions, problem views, and submission times.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon API Gateway</td>
      <td>Exposes APIs for fetching user interaction data.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon S3 (DataLake)</td>
      <td>Stores raw interaction data for further analysis and visualization.</td>
    </tr>
    <tr>
      <td>Scalability and High Availability</td>
      <td>Elastic Load Balancer</td>
      <td>Distributes incoming traffic across multiple backend servers.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon ECS</td>
      <td>Manages containerized backend services for scalability and reliability.</td>
    </tr>
    <tr>
      <td> </td>
      <td>AWS Amplify</td>
      <td>Provides scalable hosting for the frontend application with built-in CDN for fast content delivery.</td>
    </tr>
    <tr>
      <td>Asynchronous Processing and Event Management</td>
      <td  >Amazon SQS</td>
      <td>Queues user submissions and other asynchronous tasks to ensure reliable processing.</td>
    </tr>
    <tr>
      <td> </td>
      <td>Amazon EventBridge</td>
      <td>Facilitates event-driven architecture, triggering actions based on user submissions and system events.</td>
    </tr>
    <tr>
      <td>Data Transfer and Synchronization</td>
      <td>AWS DataSync</td>
      <td>Ensures data consistency and efficient transfer between on-premises storage (if needed) and AWS storage services.</td>
    </tr>
    <tr>
      <td>Data Transfer and Synchronization</td>
      <td>Amazon SES</td>
      <td>Sends email notifications to users regarding submission status, results, and other updates.</td>
    </tr>
  </tbody>
</table>

<h1>🛫 Plan</h1>
