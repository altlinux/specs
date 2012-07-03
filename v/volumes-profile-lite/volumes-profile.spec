Name: volumes-profile-lite
Version: 0.2
Release: alt1

Summary: Volumes description for School Lite distribution
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org> 
Source: %name-%version.tar

%description
Volumes description for School Lite distribution

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Dec 17 2010 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Reduce total installation to 8 Gb

* Thu Dec 09 2010 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- initial build (derived from volumes-profile-master)

