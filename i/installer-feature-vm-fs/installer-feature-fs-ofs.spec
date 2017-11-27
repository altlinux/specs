Name: installer-feature-vm-fs
Version: 0.3
Release: alt2
Summary: Installer alterator-vm profile tuning and filesystem layout hooks and other stuff for special needs
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains alterator-vm profile tuning and
filesystem layout hooks for Office Server.

%package stage2
Summary: Installer stage2 alterator-vm profile tuning hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
This package contains alterator-vm profile tuning hook for
custom installer stage2.

%package stage3
Summary: Installer stage3 filesystem layout hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage3

%description stage3
This package contains filesystem layout hooks for
custom installer stage3.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall}.d
install -pm755 05-* %buildroot%hookdir/initinstall.d/
install -pm755 01-* %buildroot%hookdir/preinstall.d/

%files stage2
%hookdir/initinstall.d/*

%files stage3
%hookdir/preinstall.d/*

%changelog
* Mon Nov 27 2017 Denis Medvedev <nbr@altlinux.org> 0.3-alt2
- fix typo.

* Mon Nov 27 2017 Denis Medvedev <nbr@altlinux.org> 0.3-alt1
- Initial Sisyphus release
