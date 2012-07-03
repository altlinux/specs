Name: installer-feature-default-xfce4
Version: 0.1
Release: alt1

Summary: Sets Xfce4 default window manager
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Sets Xfce4 default window manager

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu May 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


