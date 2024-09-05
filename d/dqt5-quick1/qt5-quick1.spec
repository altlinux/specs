
%global qt_module dqtquick1
%def_disable qtwebkit

Name: dqt5-quick1
Version: 5.9.4
Release: alt2.dde.1

Group: System/Libraries
Summary: A declarative language for describing user interfaces in Qt5
License: LGPLv2 / GPLv3
Url: http://qt.io/

BuildRequires(pre): rpm-build-ubt

%description
Qt Quick is a collection of technologies that are designed to help
developers create the kind of intuitive, modern, fluid user interfaces
that are increasingly used on mobile phones, media players, set-top
boxes and other portable devices.

Qt Quick consists of a rich set of user interface elements, a declarative
language for describing user interfaces and a language runtime. A
collection of C++ APIs is used to integrate these high level features
with classic Qt applications.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
BuildArch: noarch
Requires: %name-common = %EVR
Requires: dqt5-base-devel
%description devel
%summary.

%package -n libdqt5-declarative
Summary: Qt5 library
Group: System/Libraries
BuildArch: noarch
Requires: %name-common = %EVR
%description -n libdqt5-declarative
%summary

%prep

%files common
%files -n libdqt5-declarative
%files devel

%changelog
* Thu Jul 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.9.4-alt2.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Thu Nov 22 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt3
- rebuild

* Mon Apr 02 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt2%ubt
- make empty package to system update

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Aug 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2%ubt
- build without qtwebkit

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Nov 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- clean build requires

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Mon Feb 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Tue Oct 29 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
