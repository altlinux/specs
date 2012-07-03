Name: appliance-service-nagios
Summary: Virtual package that require all Nagios plugins
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: nagios
Requires: nagios-www
Requires: nagios-plugins-extra
Requires: nagios-plugins-snmp
Requires: nagios-plugins
Requires: nagios-plugins-network
Requires: nagios-plugins-ldap
Requires: nagios-plugins-samba
Requires: nagios-plugins-pgsql
Requires: nagios-plugins-mysql
Requires: nagios-plugins-common
Requires: nagios-plugins-nrpe
Requires: nagios-plugins-perl
Requires: nagios-plugins-local

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

