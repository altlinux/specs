Name: installer-feature-xdm-hack
Version: 0.2
Release: alt1

Summary: Hack xdm-config for OO.o
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Hacks xdm-config for OO.o, see #23108

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Mar 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- file corruption fixed :D

* Wed Mar 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


