
%define hookdir %_datadir/install2/postinstall.d

Name: installer-feature-samba-automount
Version: 0.1.1
Release: alt2

Summary: Installer stage3 for Samba automounting
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
This package contains installer stage3 hook for
enabling Samba automounting.

%package stage2
Summary: Installer stage2 hook for Samba automounting
Group: System/Configuration/Other
%description stage2
This package contains installer stage2 hook for
enabling Samba automounting.

%prep
%setup

%install
mkdir -p %buildroot/%hookdir
install -pm755 *.sh %buildroot/%hookdir/

%files stage2
%hookdir/*

%changelog
* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt2
- dont use ubt macro

* Tue Jun 20 2017 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- check for files first

* Tue May 16 2017 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial build
