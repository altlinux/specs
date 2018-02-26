Name: installer-feature-vm-server-light
Version: 0.2
Release: alt1

Summary: Installer alterator-vm profile tuning and filesystem layout hooks
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager:  Anton Farygin <rider@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains alterator-vm profile tuning and
filesystem layout hooks for Server Light.

%package stage2
Summary: Installer stage2 alterator-vm profile tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
This package contains alterator-vm profile tuning hook for
Server Light installer stage2.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall}.d
install -pm755 05-* %buildroot%hookdir/initinstall.d/

%files stage2
%hookdir/initinstall.d/*

%changelog
* Mon Nov 08 2010 Anton Farygin <rider@altlinux.ru> 0.2-alt1
- 2Gb for root

* Fri Jun 19 2009 Anton Farygin <rider@altlinux.ru> 0.1-alt1
- Initial revision based on installer-feature-vm-ofs hooks
