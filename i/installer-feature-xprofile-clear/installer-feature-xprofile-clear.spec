Name: installer-feature-xprofile-clear
Version: 0.4
Release: alt1

Summary: Clear xprofile
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Clear /etc/skel/.xprofile for new users.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon May 15 2023 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- fix fill .xprofile

* Mon May 15 2023 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- don't do empty .xprofile

* Fri Mar 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix run to late

* Fri Mar 25 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
