Name: installer-feature-autoxorg
Version: 0.1
Release: alt1

Summary: Sets default runlevel to 5 if there Xorg server exists
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Sets default runlevel to 5 if there Xorg server exists

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Feb 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


