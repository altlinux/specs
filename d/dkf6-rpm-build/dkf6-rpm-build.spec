%define __if_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define __if_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define __if_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define __if_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define __if_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define __if_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define __if_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define __if_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define __if_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define __if_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"

Name: dkf6-rpm-build
Version: 6.1.1
Release: alt0.dde.1

Group: Development/KDE and QT
Summary: Fork from kf6-rpm-build
Url: http://altlinux.org/KDE
License: GPL-2.0-or-later

BuildArch: noarch

Source1: macrosd
Source2: rpm-build-dkf6-find-qtlang

%description
Set of DKF6 RPM macros.

%package -n rpm-build-dkf6
Summary: Set of RPM macros for packaging DKF6-based applications
Group: Development/Other
Requires: rpm-build-xdg rpm-macros-dqt6 rpm-build-dqml6 /usr/bin/rpmvercmp rpm-build-ninja
%description -n rpm-build-dkf6
Set of RPM macros for packaging DKF6-based applications for ALT Linux.
Install this package if you want to create RPM packages that use DKF6.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/dkf6
install -D -m 0755 %SOURCE2 %buildroot/%_bindir/rpm-build-dkf6-find-qtlang

%files -n rpm-build-dkf6
%_rpmmacrosdir/dkf6
%_bindir/rpm-build-dkf6-*

%changelog
* Thu Aug 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.1-alt0.dde.1
- fork kf6 for separate deepin buildings (ALT #48138)

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- skip license test by default

* Mon Apr 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- add workaround against new cmake

* Tue Sep 03 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.4-alt3
- fix requires

* Fri Jul 12 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.4-alt2
- fix undefine KDE_INSTALL_INCLUDEDIR

* Fri Jul 12 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.4-alt1
- allow to define _K6buildsubdir

* Fri Jul 05 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.3-alt1
- return KDE_INSTALL_INCLUDEDIR undefined

* Thu Jul 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt1
- define KDE_INSTALL_INCLUDEDIR

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt1
- export LC_ALL=C.UTF-8 when build

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- initial build
