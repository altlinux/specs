Name: installer-feature-init-italc
Version: 0.2.1
Release: alt1

Summary: Setup iTALC-master
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setup iTALC-master

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{preinstall.d,postinstall.d}
install -pm755 preinstall.sh %buildroot%hookdir/preinstall.d/90-italc.sh
install -pm755 postinstall.sh %buildroot%hookdir/postinstall.d/90-italc.sh

%files
%hookdir/postinstall.d/*
%hookdir/preinstall.d/*

%changelog
* Fri Nov 22 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.1-alt1
- Support both iTalc and iTalc2

* Mon Sep 30 2013 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Adapt to iTalc2
- Hide normal output during key generation
- Do not require install2-init-functions

* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


