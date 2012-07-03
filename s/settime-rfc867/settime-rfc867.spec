Name: settime-rfc867 
Version: 0.2
Release: alt1

Summary: Set ditetime from hardcoded ldap server
License: GPL
Group: System/Configuration/Hardware
BuildArch: noarch

Source: %name.init


%description
Set ditetime from hardcoded ldap server via rfc867

%install
install -D -m755 %SOURCE0 %buildroot%_initdir/%name


%files
%_initdir/%name

%changelog
* Thu Jun 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- moved to start later

* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build


