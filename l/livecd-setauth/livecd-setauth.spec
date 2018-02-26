Name: livecd-setauth
Version: 0.4
Release: alt2

Summary: Setup krb5 and cifs homes in livecd
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig
Requires: alterator-auth alterator-net-shares netcat

%description
Setup krb5 auth and cifs homes if there is 'krb5' in /proc/cmdline

%prep
%setup -c


%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 livecd-setauth/livecd-setauth %buildroot%_initdir/livecd-setauth 


%files 
%_initdir/livecd-setauth


%changelog
* Wed Jun 20 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt2
- force set /etc/localtime

* Tue Jun 19 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- set time zone from kernel command line

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- set time from server via datetime protocol

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- run after network

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- autologin disabling added

* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build

