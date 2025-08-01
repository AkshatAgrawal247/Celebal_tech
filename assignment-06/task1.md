# Configure Self-hosted integration runtime to Extract the data from your local server and load it into azure DB

To configure a self hosted Integration runtime **first we need to create it.**

[ref : https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime?tabs=data-factory]


## Step 1 : Creating and configuring self hosted IR
  

![](task.1.jpg)
![](task..1.jpg)
![](linked_ser.jpg)
![](task...1.jpg)


### Configuring steps

1. Enter a name for your IR, and select Create.

On the Integration runtime setup page, select the link under Option 1 to open the express setup on your computer. Or follow the steps under Option 2 to set up manually. The following instructions are based on manual setup:

    i. Copy and paste the authentication key. Select Download and install integration runtime.

    ii. Download the self-hosted integration runtime on a local Windows machine. Run the installer.

    iii. On the Register Integration Runtime (Self-hosted) page, paste the key you saved earlier, and select Register.

![](https://learn.microsoft.com/en-us/azure/data-factory/media/create-self-hosted-integration-runtime/integration-runtime-setting-up.png)

![](https://learn.microsoft.com/en-us/azure/data-factory/media/create-self-hosted-integration-runtime/register-integration-runtime.png)

2. On the New Integration Runtime (Self-hosted) Node page, select Finish.

After the self-hosted integration runtime is registered successfully, you see the following window:

![](https://learn.microsoft.com/en-us/azure/data-factory/media/create-self-hosted-integration-runtime/registered-successfully.png)

## Step 2 : Migrating data from SQL server local to Azure DB

[ref : https://stackoverflow.com/questions/30649105/copy-local-sql-database-onto-azure]
 
 option to deploy db to azure from sql management studio

![](https://i.sstatic.net/7IQwH.png)