# Seagate BlackArmor SSH enabling

This script enables ssh access and sets a new password for root user so you could log in the NAS. After that, dropbear is enabled to start at NAS boot up.

This script is based upon the exploit released by JDiel in https://www.nerdbox.it/blackarmor-rooter-windows-released/ although in his exploit the dropbear process is only alive until the NAS is rebooted. My script improves this by enabling ssh in inetd configuration.

I don't have a NAS 1xx or 2xx to check it but on 4xx it works. If you have one of the former, provide feedback, please.
