%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

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

Name: kf6-rpm-build
Version: 6.0.4
Release: alt2

Group: Development/KDE and QT
Summary: Development utils for KDE
Url: http://altlinux.org/KDE
License: GPL-2.0-or-later

BuildArch: noarch

Source1: macrosd
Source2: rpm-build-kf6-find-qtlang

BuildRequires: rpm-build-ubt

%description
Set of KF6 RPM macros.

%package -n rpm-build-kf6
Summary: Set of RPM macros for packaging KF6-based applications
Group: Development/Other
Requires: rpm-build-xdg rpm-macros-qt6 rpm-build-qml /usr/bin/rpmvercmp
%description -n rpm-build-kf6
Set of RPM macros for packaging KF6-based applications for ALT Linux.
Install this package if you want to create RPM packages that use KF6.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/kf6
#__if_ver_lt %ubt_id M110
#sed -i 's|^%%__kf6_altplace_default[[:space:]].*|%%__kf6_altplace_default true|' %buildroot/%_rpmmacrosdir/kf6
#sed -i 's|^%%__kf6_desktop_subdir[[:space:]].*|%%__kf6_desktop_subdir /kf6|' %buildroot/%_rpmmacrosdir/kf6
#endif
install -D -m 0755 %SOURCE2 %buildroot/%_bindir/rpm-build-kf6-find-qtlang

%files -n rpm-build-kf6
%_rpmmacrosdir/kf6
%_bindir/rpm-build-kf6-*

%changelog
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
