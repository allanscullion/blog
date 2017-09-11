Title: Fixing Windows Updates
Date: 2017-08-31 11:54
Author: Allan Scullion
Category: Tech
Tags: Windows, Updates, Shavlik
Slug: fixing-windows-updates

# Fixing Windows Updates
![Seriously Microsoft... wtf!](/images/2400.jpg "Head in Hands")
I have no idea what travesty I committed in a past life to deserve the pain I have recently experienced with Windows Updates[^1]. However, I do know that my punishment is to know way more about the Windows Update module than any sane IT Manager has the right to know.

By way of atonement for my past sins, I offer the following in the hope that it helps some other poor bugger out there who might be in a similar situation.

## What happened?
Our IT Estate has roughly 40 workstations. We use Shavlik to push out Windows patches. I noticed one month that Shavlik was pushing out patches but in many cases could not confirm that they had been installed properly. After a bit of digging around, we decided to have a go at patching those machines manually. That is when things went south.

The machines in question refused to push out updates using Windows Update (seriously… Microsoft… WTF!) 

We Googled every single error code and tried every single internet “fix” that we could find. Nothing was working. It was time to admit defeat and do the unthinkable… the last resort… we had no choice… we had to get on the phone to Microsoft support.

## What Microsoft found
On the first pass, even Microsoft gave up and recommended an OS re-install. Of course, we all laughed heartily at that suggestion (seriously… Microsoft… WTF!) 

After the required amount of pushback, Microsoft relented and escalated internally.

For several more days, Microsoft worked remotely on one of our affected PCs and discovered that a number of patches had been “Staged”, but never installed. They were stuck in this “Staged” state and this was preventing all other patches from installing.

## How did we get into this mess
This is our working theory. One word. McAfee.

It turns out that one of our EPO policies was actively preventing some Windows Updates from installing. If you have landed on this page because you have the same problem, you have to disable the following option:

## How we got out of this mess
This is where it gets “interesting”. The solution on paper sounds simple:

* Reset Windows Update:
	* Stop all Windows Update related services
	* Rename the SoftwareDistribution folder
	* Rename the catroot folder
* Extract a list of all installed/staged packages to a text file using `dsim`
* Restart Windows Update services
* Parse the file containing the installed packages, extract any module name in the “Staged” state, and use `dsim` to remove those packages.

The problem is that the list of Staged packages was different on every single machine - not the sort of task you want to be doing by hand on that many machines.

The good news is that is is scriptable, but has to be done in phases.

### Phase One
Run the following Powershell script on every affected machine (it can be run in a remote Powershell session without disturbing the target machine user):

	$res = "\\<yourservershare>\WindowsUpdates\StagedResult." + $env:COMPUTERNAME + ".txt"
	
	"Stopping BACKGROUND INTELLIGENT TRANSFER SERVICE..."
	net stop BITS
	"Stopping CRYPTOGRAPHIC SERVICES..."
	net stop Cryptsvc
	"Stopping WINDOWS MODULES INSTALLER..."
	net stop trustedinstaller
	"Stopping WINDOWS UPDATE..."
	net stop wuauserv
	 
	"Renaming Windows Update Folders..."
	ren $env:systemroot\SoftwareDistribution SoftwareDistribution.old
	ren $env:WINDIR\system32\catroot2 catroot2.old
	 
	"Getting packages..."
	dism /online /get-packages | out-file -encoding ascii $res
	 
	"Starting BACKGROUND INTELLIGENT TRANSFER SERVICE..."
	net start BITS
	"Starting CRYPTOGRAPHIC SERVICES..."
	net start Cryptsvc
	"Starting WINDOWS MODULES INSTALLER..."
	net start trustedinstaller
	"Starting WINDOWS UPDATE..."
	net start wuauserv
	"Complete."

Note that this script outputs the installed packages for that machine to a file called:

	StagedResult.<COMPUTERNAME>.txt

In our case, we output this file to a shared folder on a server so that we could collate all the files in preparation for phase two.

Here is an example of the `dsim` output file:

	Deployment Image Servicing and Management tool
	Version: 6.1.7600.16385
	 
	Image Version: 6.1.7601.18489
	 
	Packages listing:
	 
	Package Identity : Package_for_KB272945231bf3856ad364e35amd646.1.1.0
	State : Staged
	Release Type : Security Update
	Install Time : 17/02/2017 23:04

### Phase Two
I have a bit of background in Linux system admin, so I chose to use `Cygwin` bash scripts for this phase. The principle is pretty simple, so if you are not comfortable with `bash`, `grep` or `sed`, feel free to script in a language of your choice.

The following `bash` script: `stagedupdateremoval.sh` takes a generated package list file from phase one as a parameter, then uses `grep` to extract the list of “Staged” package names, and pipes that output to `sed` to create a Powershell script that can be run on the source machine to remove all of the Staged packages:

	#!/bin/bash
	cat $1 | grep -Pzo '(?<=^Package Identity \: )(.*)(?=\n^State : Staged$)' | sed 's/^/dism \/online \/remove-package \/packagename:/' > $1.remove.ps1

As we had collated all of the files from the affected machines in a shared folder, I used the following script to process them all in the one go:

	#!/bin/bash
	for f in ./StagedResult*.txt; do
	 
	    if [ -e "$f" ]; then
	        ./stagedupdateremoval.sh "$f"
	    fi
	 
	done

This is an example of the output script for a single machine:

	dism /online /remove-package /packagename:Package_for_KB272945231bf3856ad364e35amd646.1.1.0
	dism /online /remove-package /packagename:Package_for_KB300374331bf3856ad364e35amd646.1.1.1
	dism /online /remove-package /packagename:Package_for_KB302038731bf3856ad364e35amd646.1.1.2

The output filename of the new script is: `StagedResult.<COMPUTERNAME>.txt.removal.ps1`

### Phase Three
We now have to run the targeted output scripts from Phase Two on each of the affected machines. Again, this can be done using a remote Powershell session without disturbing the machine user.

When this phase has been completed, Windows Updates will work again.



[^1]:	The post was composed on a nice, clean, virus free (and Anti Virus free) Mac. A world where OS updates magically work every time. As if by magic.