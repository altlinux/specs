Name: ve-postgresql
Summary: PostgreSQL virtual appliance for OpenVZ
BuildArch: noarch
Version: 4.0.1
Release: alt2
License: GPL
Group: System/Base

#basic packages
Requires: basesystem
Requires: sysklogd
Requires: appliance-base-interactivesystem

#service packages
Requires: postgresql9.4-server
Requires: postgresql9.4-contrib
Requires: postgresql9.4-perl
Requires: pgpool-II

#additional packages
Requires: monit

%description
Virtual package for PostgreSQL database server

%files

%changelog
* Wed Oct 07 2015 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- postgresql 9.4

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

