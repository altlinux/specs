%define rname gpgmepp

Name: kde5-%rname
Version: 16.08.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: C++ wrapper for gpgme
Url: http://www.kde.org
License: LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Aug 03 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libgpg-error libgpg-error-devel libqt5-core libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ glibc-devel-static libdb4-devel libgpgme-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: boost-devel libgpgme-devel

%description
GpgME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's
gpgme (GnuPG Made Easy) library.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libgpgme-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5gpgmepp
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gpgmepp
KF5 library

%package -n libkf5gpgmepp-pthread
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5gpgmepp-pthread
KF5 library

%package -n libkf5qgpgme
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5qgpgme
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*

%files devel
%_K5inc/gpgmepp_version.h
%_K5inc/gpgme++/
%_K5inc/qgpgme/
%_K5link/lib*.so
%_K5lib/cmake/KF5Gpgmepp/
%_K5archdata/mkspecs/modules/qt_QGpgme.pri

%files -n libkf5gpgmepp
%_K5lib/libKF5Gpgmepp.so.*
%files -n libkf5gpgmepp-pthread
%_K5lib/libKF5Gpgmepp-pthread.so.*
%files -n libkf5qgpgme
%_K5lib/libKF5QGpgme.so.*

%changelog
* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- initial build
