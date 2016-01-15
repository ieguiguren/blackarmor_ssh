# Seagate BlackArmor SSH enabling

This script enables ssh access and sets a new password for root user so you could log in the NAS. After that, dropbear is enabled to start at NAS boot up.

This script is based upon the exploit released by JDiel in https://www.nerdbox.it/blackarmor-rooter-windows-released/ although in his exploit the dropbear process is only alive until the NAS is rebooted. This script improves this by enabling ssh in inetd configuration.

On NAS 4xx this script works. It should on 1xx or 2xx but I don't have access to one of them to check it. If you have one of the former, provide feedback, please.

My firmware version: 4000.1101 Built on Fri, 01 Oct 2010

If you have your NAS listening on port 443 (https), you must change it to http before trying to execute the script or it'll fail.

# Disclaimer
This script may just fail or may broken something unexpected, maybe because it hasn't been tested in the hardware/software/firmware version you own or maybe for some other cause. Use it at your own risk. I've tested it on my own 4xx and it has worked correctly.
