Name: installer-feature-load-tun
Version: 0.1
Release: alt1

Summary: Loads tun kernel module by default
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Loads tun kernel module by default

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Feb 04 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- load tun by default 


