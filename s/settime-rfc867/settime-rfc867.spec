Name: settime-rfc867 
Version: 0.3
Release: alt1

Summary: Set ditetime from hardcoded ldap server
License: GPL
Group: System/Configuration/Hardware
BuildArch: noarch

Source: %name.init
Source1: %name.sysconfig


%description
Set ditetime from hardcoded ldap server via rfc867

%install
install -D -m755 %SOURCE0 %buildroot%_initdir/%name
install -D -m755 %SOURCE1 %buildroot/etc/sysconfig/%name


%files
%_initdir/%name
%config(noreplace) /etc/sysconfig/%name

%changelog
* Thu Oct 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- configuration file added
- dependence on alterator-auth removed

* Thu Jun 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- moved to start later

* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build


