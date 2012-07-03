Name: java-service
Version: 0.1
Release: alt2

Summary: Java service tools
License: GPL
Group: System/Servers
Packager: Eugene Prokopiev <enp@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: jakarta-commons-daemon jakarta-commons-daemon-jsvc java-1.6.0-sun

%description
Java service tools

%prep
%setup -c

%install
cp -a * %buildroot/

%files
%_sbindir/*
%_initdir/java-template
%_localstatedir/%name

%changelog
* Fri Oct 29 2010 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt2
- add requires and update service template

* Wed Apr 14 2010 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build

