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

Name: kf5-rpm-build
Version: 5.101.0
Release: alt1

Group: Development/KDE and QT
Summary: Development utils for KDE
Url: http://altlinux.org/KDE
License: GPL-2.0-or-later

BuildArch: noarch

Source1: macrosd
Source2: rpm-build-kf5-find-qtlang

BuildRequires: rpm-build-ubt

%description
Set of KF5 RPM macros.

%package -n rpm-build-kf5
Summary: Set of RPM macros for packaging KF5-based applications
Group: Development/Other
Requires: rpm-build-xdg rpm-macros-qt5 rpm-build-qml /usr/bin/rpmvercmp
%description -n rpm-build-kf5
Set of RPM macros for packaging KF5-based applications for ALT Linux.
Install this package if you want to create RPM packages that use KF5.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/kf5
%__if_ver_lt %ubt_id M110
sed -i 's|^%%__kf5_altplace_default[[:space:]].*|%%__kf5_altplace_default true|' %buildroot/%_rpmmacrosdir/kf5
sed -i 's|^%%__kf5_desktop_subdir[[:space:]].*|%%__kf5_desktop_subdir /kf5|' %buildroot/%_rpmmacrosdir/kf5
%endif
install -D -m 0755 %SOURCE2 %buildroot/%_bindir/rpm-build-kf5-find-qtlang

%files -n rpm-build-kf5
%_rpmmacrosdir/kf5
%_bindir/rpm-build-kf5-*

%changelog
* Thu Dec 21 2023 Sergey V Turchin <zerg@altlinux.org> 5.101.0-alt1
- allow to redefine _K5link

* Thu Nov 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.100.2-alt1
- fix install files

* Mon Oct 30 2023 Sergey V Turchin <zerg@altlinux.org> 5.100.1-alt1
- don't move desktop-files upper for old branches

* Tue Oct 24 2023 Sergey V Turchin <zerg@altlinux.org> 5.100.0-alt1
- move all to standart placement by default(only for new branches)
- move desktop-files up from subdirectory by default

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- fix removing metainfo

* Tue Apr 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt2
- fix requires, description
- drop %%ubt macro

* Wed Aug 08 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- don't remove appdata by default

* Thu Nov 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- add new macros:
  _K5if_ver_eq _K5if_ver_not_gt _K5if_ver_not_gteq _K5if_ver_not_lt _K5if_ver_not_lteq _K5if_ver_not_eq

* Wed Oct 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- require rpm-build-qml

* Wed Sep 07 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- fix removing metainfo appdata

* Fri Sep 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- more clean from appdata

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- use kde own dbus services dir

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- remove manpages and appdata by default

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- fix html docs install dir

* Wed Sep 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- add _K5conf_up and _K5conf_bin macros
- fix paths in cmake files during install
- move akonadi data to /usr/share/akonadi5 during install

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- move dbus *5*.service to standard place

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- move k*5 dirs to _datadir

* Wed Apr 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- update macros

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- update macros

* Thu Mar 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.7
- update macros

* Thu Mar 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.5
- update macros

* Wed Feb 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.4
- update macros

* Wed Feb 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.3
- update macros

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.2
- update paths

* Wed Dec 24 2014 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.1
- initial build
