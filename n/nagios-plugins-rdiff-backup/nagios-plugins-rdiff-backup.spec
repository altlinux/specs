Name: nagios-plugins-rdiff-backup
Version: 0.2
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

%prep
%setup

%install
mkdir -p %buildroot%plugindir
install -m755 check_rdiff-backup %buildroot%plugindir/

%files
%plugindir/check_rdiff-backup

%changelog
* Fri Aug 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
