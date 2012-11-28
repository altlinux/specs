Name: nagios-plugins-rdiff-backup
Version: 0.3
Release: alt1

Summary: Nagios(R) plug-in for checking rdiff-backup logs
License: GPL
Group: Monitoring

#Url: http://altlinux.org/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe

# nagios uses /usr/lib for plugins in any arch
%define plugindir %_prefix/lib/nagios/plugins

%description
Nagios plugin for checking rdiff-backup results at hard drives written in python.

Example:
On backup server in /etc/nagios/nrpe.cfg:
command[check_backup]=sudo /usr/lib/nagios/plugins/check_rdiff-backup /var/local $ARG1$

On nagios server:
check_command check_nrpe_arg!check_backup!backup/cellar

for check backup in /var/local/backup/cellar dir

%prep
%setup

%install
mkdir -p %buildroot%plugindir
install -m755 check_rdiff-backup %buildroot%plugindir/

%files
%plugindir/check_rdiff-backup

%changelog
* Wed Nov 28 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- check_rdiff-backup: add backup base dir as first arg

* Fri Aug 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
