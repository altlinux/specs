Name: installer-feature-centaurus-profiles
Version: 0.5
Release: alt1

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


