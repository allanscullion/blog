Title: Cygwin, Crontab and Shared Windows Drives
Date: 2014-10-27 15:30
Author: Allan Scullion
Category: Tech
Tags: Cygwin,cron,mount,Windows,Shares
Slug: cygwin-crontab-shares

If you have ever tried to setup `crontab` in [Cygwin][cygwin], you might also have struggled to schedule scripts that reside or read/write data on shared network drives.

When you run an interactive bash shell in Cygwin, by default, your shared network drives are mounted in `/cygdrive`. So, for example, drive S: in Windows is available as `/cygdrive/S` in `bash`.

The trouble is, even if you configure the `cron` service to run as a specific user, it will not have automatic access to these `/cygdrive` mount points. The service can see local disks, but not network disks.

To get around this, you have to create a new mount point that mounts the Windows share name directly, *not* the mounted drive letter. The command to do this is as follows (obviously substituting your own share and mount point):

    mkdir /mnt
    mount "//[server]/[sharename]" /mnt/[whatever]

Don't try to create a new mount point under `/cygdrive`... that does not work (by design).

You can then change your `crontab` entry and/or script to reference the new mount point and everything should work as expected.

[cygwin]: https://www.cygwin.com