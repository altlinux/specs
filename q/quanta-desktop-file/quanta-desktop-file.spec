Name: quanta-desktop-file
Version: 0.1
Release: alt1

Summary: Desktop file for run quanta not from kde3
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar
Requires: kdewebdev-quanta

%description
Desktop file for run quanta not from kde3

%prep
%setup

%install
%define appdir %_datadir/applications
mkdir -p %buildroot%appdir
install -pm640 *.desktop %buildroot%appdir/

%files
%appdir/*

%changelog
* Thu May 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


