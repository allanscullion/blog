Title: Exchange 2010 - How to Monitor Mailbox Sizes
Date: 2014-03-12 12:19
Author: Allan Scullion
Category: Technology
Tags: PowerShell, Exchange
Slug: exchange-2010-monitor-mailbox-sizes

How to schedule a PowerShell script to automatically email a report listing user mailbox sizes.

## Required Powershell Scripts {#requiredpowershellscripts}

The following PowerShell script will list all mailboxes sorting by size (descending):

### ExchGetMailboxSizes.ps1 {#exchgetmailboxsizesps1}

```ps1
Get-Mailbox -ResultSize Unlimited |
    Get-MailboxStatistics |
    Select DisplayName,StorageLimitStatus, `
        @{name="TotalItemSize (MB)"; `
            expression={[math]::Round(($_.TotalItemSize.ToString().Split("(")[1].Split(" ")[0].Replace(",","") / 1MB) ,2)} `
        }, `
       ItemCount |
    Sort "TotalItemSize (MB)" -Descending
```

### Example Output {#exampleoutput}

```
DisplayName  StorageLimitStatus  TotalItemSize (MB)  ItemCount
-----------  ------------------  ------------------  ---------
User 1               NoChecking            10942.95     123888
User 2               NoChecking            10307.82     122734
User 3               NoChecking            10105.58      86925
User 4               NoChecking             9746.91     162055
```
  
### MailboxAlerts.ps1 {#mailboxalertsps1}

This next script will send the output of the above script as an email:

```ps1
$messageParameters = @{
    Subject = "[Exchange Report] Mailbox Sizes"
    Body = (.\ExchGetMailboxSizes.ps1 | Out-String)
    From = "your@yourdomain.com"
    To = "alerts@yourdomain.com"
    SmtpServer = "smtp.yourdomain.com"
}
Send-MailMessage @messageParameters
```
  
Now you can setup a scheduled task to run this script from your Exchange Server.

## Creating a Scheduled Task {#creatingascheduledtask}

First up, copy both of the above scripts to a folder on a local disk of the Exchange Server. In the examples below I am assuming `C:\Scripts`.

Next, create a new Task from the Windows 2008 Task Scheduler. You should configure this task as a user who has Exchange Admin privileges.

### Task Settings {#tasksettings}

#### General - Security Options {#generalsecurityoptions}

*   Name the task: e.g.: *Weekly Mailbox Size Alerts*
*   Select *Run whether user is logged in or not* (will require the user's password to save the task)
*   Leave *Do not store password* unchecked
*   Check *Run with highest privileges*

#### Action Settings {#actionsettings}

*   Go to the Action tab and click *New...*

[Mike Pfeiffer does a great job][mikepfeiffer] of explaining how to set up scheduled tasks for Exchange 2010 PowerShell Scripts. In summary, use the following settings:

**Program/Script**

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```

**Add Arguments (optional)**

```text
-version 2.0 -NonInteractive -WindowStyle Hidden -command ". 'C:\Program Files\Microsoft\Exchange Server\V14\bin\RemoteExchange.ps1'; Connect-ExchangeServer -auto;c:\Scripts\MailboxAlerts.ps1"
```

**Start in (optional)**

```text
C:\Scripts
```

**Triggers**

*   Setup a sensible schedule that works for you, e.g.: *Weekly - Monday at 9am*
*   Save the Task be clicking *OK*.
*   You will be prompted for your password at this stage - this is required so that the task can run when the user is logged off.

[mikepfeiffer]: http://www.mikepfeiffer.net/2010/02/creating-scheduled-tasks-for-exchange-2010-powershell-scripts/
