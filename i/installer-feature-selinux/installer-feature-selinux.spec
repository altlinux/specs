Name: installer-feature-selinux
Version: 0.8
Release: alt1

Summary: Installer selinux hooks
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Provides: %name-stage2

%description
This package contains selinux hooks for installer.


%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall,postinstall}.d
install -pm755 preinstall.sh %buildroot%hookdir/preinstall.d/90-selinux.sh
install -pm755 postinstall.sh %buildroot%hookdir/postinstall.d/90-selinux.sh

%files
%hookdir/preinstall.d/*
%hookdir/postinstall.d/*

%changelog
* Tue Feb 14 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt1
- disable users listing in lightdm

* Mon Feb 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.7-alt1
- disable non-root logins in console

* Fri Feb 06 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- typo fixed

* Mon Apr 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- adding pam_permit into pam.d/newrole added

* Thu Apr 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- make stage indifferent

* Wed Apr 02 2014 Timur Aitov <timonbl4@altlinux.org> 0.4-alt1
- [0.4]

* Wed Dec 11 2013 Timur Aitov <timonbl4@altlinux.org> 0.3-alt1
- [0.3]

* Tue Aug 06 2013 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- [0.2]

* Tue Jun 25 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- first build

