## Shutdown EC2 periodically to save cost
Many a times you might forget to shutdown ec2 after late night learning and forget to turn off your ec2 instances. This article focuses on to `Shutdown EC2 periodically to save cost`  

#### Task
Create a Lambda function that shutdowns ec2 instances periodically using AWS CloudWatch Events.

This task is achieved using two ways
1. Manually (Recommended for first time practise)
2. Automated using CloudFormation (Recommended for saving time)

#### 2. Automated using CloudFormation IaaC Template
I like automating things. So here is the how to achieve this

1. Create an IAM Role for CloudFormation to deploy stacks and create resources. Skip if you already have a role.
2. GoTo AWS Console. Goto ClouFormation and Create a Stack.
3. Pass Params to CloudFormation
4. Select IAM Role for CloudFormation to create stacks.
5. Checkbox CAPABILITY IAM as Ticked
6. Deploy Stack. Wait for Stack to deploy.
7. Check for ec2 instances if they are running or stopped.
