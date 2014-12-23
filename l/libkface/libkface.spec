Name: libkface
Version: 3.5.0
Release: alt2

Summary: Libkface is a Qt/C++ wrapper around LibFace
License: GPL2
Group: System/Libraries
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Url: https://projects.kde.org/projects/kdereview/libkface
Source: %name-%version.tar

BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ kde4libs-devel libopencv-devel >= 2.4.9

%description
Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition and detection over pictures.

%package devel
Group: Development/KDE and QT
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup

%build
%K4build

%install
%K4install

%files
%_K4libdir/%name.so*
%_K4apps/%name

%files devel
%_pkgconfigdir/%name.pc
%_K4includedir/*
%_K4link/*.so
#%_K4apps/cmake/modules/FindKface.cmake
%_libdir/cmake/Kface-*/

%changelog
* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt2
- digikam 4.6.0

* Thu Dec 18 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt0.M70P.1
- built for M70P

* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt1
- new version

* Fri Oct 10 2014 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt2
- digikam 4.3.0

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt1
- new version

* Tue Jul 01 2014 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Mon May 19 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt4
- digikam 4.0.0

* Fri Feb 14 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt3
- rebuilt with new opencv

* Mon Oct 14 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1.M70P.1
- built for M70P

* Fri Oct 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt2
- digikam 3.5.0

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- digikam 3.2.0

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- digikam 3.1.0

* Wed Sep 26 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt1
- Update to latest stable

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.1
- Rebuilt with OpenCV 2.3.1

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 0.1.0-alt1
- Initial build for sysiphus

