Name: etersoft-admin-essential
Version: 0.6
Release: alt1

Summary: Virtual package for packages required by Etersoft's vision

Group: System/Servers
License: GPLv3

Source: %name-%version.tar

BuildArch: noarch


%description
Virtual package for host system requires in Etersoft's vision.
Install it in host system.

###############################
%package container
Group: System/Servers
Summary: Virtual package for container's requires in Etersoft's vision

# Debug
Requires: strace

# System
Requires: openssh-blacklist openssh-server

# Administration
Requires: etckeeper apt-conf-etersoft-common

# Network
Requires: tcpdump traceroute tcptraceroute bind-utils hostinfo net-tools netcat whois

# File utils
Requires: wget unzip vim-console eepm erc

# Monitoring
Requires: nagios-nrpe monit


%description container
Virtual package for container's requires in Etersoft's vision.


###############################
%package host
Group: System/Servers
Summary: Virtual package for host system's requires in Etersoft's vision

# Debug
Requires: strace

# System
Requires: openssh-blacklist openssh-server

# Hardware
Requires: fdisk ntpdate smartmontools hdparm sysstat ptmax

# Administration
Requires: etckeeper apt-conf-etersoft-common apt-conf-etersoft-hold

# Network
Requires: tcpdump traceroute tcptraceroute bind-utils hostinfo net-tools netcat whois iftop nmap

# File utils
Requires: wget unzip vim-console eepm erc

# Monitoring
Requires: nagios-nrpe monit hddtemp collectd collectd-sensors

# Backup
Requires: backupninja rdiff-backup

%description host
Virtual package for host system's requires in Etersoft's vision.

###############################
%package webhost
Group: System/Servers
Summary: Virtual package for web host system's requires in Etersoft's vision

Requires: %name-host

# Monitoring
Requires: collectd-openvz collectd-sensors
Requires: nginx-etersoft collectd-nginx

# OpenVZ
Requires: vzctl openvz-etersoft

# nginx
Requires: nginx nginx-etersoft collectd-nginx

%description webhost
Virtual package for web host system's requires in Etersoft's vision.
OpenVZ based.

%files host

%files webhost

%files container

%changelog
* Sat Sep 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- add clone_vz.sh (eterbug #9281)
- add some ddos script
- add mail check script, add broken web hosts to access list
- add hdd utils
- add get_userpass_for_nginx
- add starthttpd2
- add dns utils
- add nic_domains.sh for get domains info
- commit check_git_activity.sh
- improve gluster fixing scripts
- add glusterupdate.sh
- update rsync_all
- add nginx_le.sh for letsencrypt using

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- add vz utils: load_svg, move_vz
- add common scripts and ddos
- add web url stat
- add script for check hosted sites
- add refresh_site_conf script replaced rewrite_httpd_conf.sh
- improve to save aliases for sites
- merge dir perms and owners code, add refresh_dirs.sh script
- commit shareinet script
- add load_avg_vz

* Mon Mar 05 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- add some utils
- add admin scripts

* Fri Nov 04 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- add some utils

* Sat Oct 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add webhost subpackage

* Wed Sep 21 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
