Name: installer-feature-selinux
Version: 0.4
Release: alt1

Summary: Installer selinux hooks
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains selinux hooks for installer.

%package stage2
Summary: Installer stage2 selinux hook
License: GPL
Group: System/Configuration/Other

%description stage2
This package contains selinux hook for installer stage2.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall,postinstall}.d
install -pm755 preinstall.sh %buildroot%hookdir/preinstall.d/90-selinux.sh
install -pm755 postinstall.sh %buildroot%hookdir/postinstall.d/90-selinux.sh

%files stage2
%hookdir/preinstall.d/*
%hookdir/postinstall.d/*

%changelog
* Wed Apr 02 2014 Timur Aitov <timonbl4@altlinux.org> 0.4-alt1
- [0.4]

* Wed Dec 11 2013 Timur Aitov <timonbl4@altlinux.org> 0.3-alt1
- [0.3]

* Tue Aug 06 2013 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- [0.2]

* Tue Jun 25 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- first build

