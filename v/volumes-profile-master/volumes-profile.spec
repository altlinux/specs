Name: volumes-profile-master
Version: 0.2
Release: alt1

Summary: Volumes description for School Master distribution
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
Volumes description for School Master distribution

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- / partition increased

* Wed Sep 02 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build



