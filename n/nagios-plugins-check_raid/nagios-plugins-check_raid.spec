Name: nagios-plugins-check_raid
Version: 2.1
Release: alt2

Summary: Nagios(R) plug-in for checking raid status
License: GPL
Group: Monitoring

Url: http://exchange.nagios.org/directory/Plugins/Hardware/Storage-Systems/RAID-Controllers/check_raid/details

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe

# nagios uses /usr/lib for plugins in any arch
%define pluginsdir %_prefix/lib/nagios/plugins

%description
Nagios plugin for checking all RAID volumes (hardware and software) that can be identified.

%prep
%setup

%install
mkdir -p %buildroot%pluginsdir/
install -m755 check_raid %buildroot%pluginsdir/

%files
%pluginsdir/check_raid
%doc check_raid.cfg

%changelog
* Fri Jun 10 2011 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- small cleanup, rebuild

* Tue Sep 21 2010 Dmitriy Shestakov <mid@etersoft.ru> 2.1-alt1
- initial build for ALT Linux Sisyphus
