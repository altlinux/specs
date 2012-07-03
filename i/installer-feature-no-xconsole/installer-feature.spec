Name: installer-feature-no-xconsole
Version: 0.1
Release: alt1

Summary: no xconsole in XDM by default
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
Set no xconsole in XDM by default

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


