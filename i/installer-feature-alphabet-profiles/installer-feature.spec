Name: installer-feature-alphabet-profiles
Version: 1.0
Release: alt2

Summary: Setups package groups from selected vm-profile
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setups package groups from selected vm-profile

%prep
%setup

%install
%define hookdir %_datadir/install2/prepkg.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Feb 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt2
- 'double-path' fixed

* Tue Feb 28 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt1
- alphabet based selection

* Tue Nov 29 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.0-alt1
- error with absent groups fixed

* Wed May 08 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- profile-based selection used (see http://www.altlinux.org/Alterator-pkg)

* Thu Feb 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2
- check domain-server on server 

* Tue Feb 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- sysvinit and systemd groups added

* Fri Jan 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- add sysvinit in server cases

* Wed Dec 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- use centaurus-mate instead of centaurus-gnome
- remove kernel setup

* Fri Feb 11 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- kernel setup added: el-smp for server, std-def for desktop
  and both for custom

* Thu Feb 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- server: kvm enabled, bacula disabled

* Wed Feb 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- added bacula-server setting

* Tue Feb 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added bacula setting

* Thu Jan 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


