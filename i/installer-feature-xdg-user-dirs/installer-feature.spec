Name: installer-feature-xdg-user-dirs
Version: 0.1
Release: alt1

Summary: Enables xdg-user-dirs
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar
Requires: xdg-user-dirs xdg-user-dirs-gtk

%description
Enables xdg-user-dirs

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Feb 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build
