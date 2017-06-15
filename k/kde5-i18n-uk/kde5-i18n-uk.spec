
%define lng uk
%define lngg Ukrainian

Name: kde5-i18n-%lng
Version: 17.04.0
Release: alt1%ubt

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE Applications
License: GPL
Url: http://www.kde.org/

Conflicts: kf5-i18n-uk <= 5.6.3-alt1
Requires: kf5-filesystem
BuildArch: noarch

Source: .gear-rules

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt

%description
%lngg language support for KDE Applications.


%prep
%setup -qcT

%files

%changelog
* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- remove all translations

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.2-alt1
- new version

* Thu Sep 29 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- initial build
