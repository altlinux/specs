Name: installer-feature-start-avahi
Version: 0.2
Release: alt1

Summary: Installer stage3 avahi starter
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar
Requires: avahi-daemon iproute2

%description
This package contains Avahi start and enable multicast hook for installer stage3.

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Apr 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added starting messagebus before avahi 

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build 
