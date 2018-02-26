Name: installer-feature-droid-up
Version: 0.1
Release: alt1

Summary: Moves Droid fonts up in fontconfig
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Moves Droid fonts up in fontconfig

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Jul 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build
