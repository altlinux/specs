Name: settime-rfc867 
Version: 0.4
Release: alt3

Summary: Set ditetime from hardcoded ldap server
License: GPL
Group: System/Configuration/Hardware
BuildArch: noarch

Source: %name.init
Source1: %name.sysconfig
Source2: %name.service

Requires: netcat

%description
Set ditetime from hardcoded ldap server via rfc867

%install
install -D -m755 %SOURCE0 %buildroot%_initdir/%name
install -D -m755 %SOURCE1 %buildroot/etc/sysconfig/%name
install -pD -m0644 %SOURCE2 %buildroot%_unitdir/%name.service


%files
%_initdir/%name
%_unitdir/%name.service
%config(noreplace) /etc/sysconfig/%name

%changelog
* Fri Oct 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.4-alt3
- add requirement of netcat

* Fri May 24 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- waiting online added

* Fri May 24 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- systemd support added

* Thu Oct 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- configuration file added
- dependence on alterator-auth removed

* Thu Jun 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- moved to start later

* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build


