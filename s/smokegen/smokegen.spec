%add_findpackage_path %_kde4_bindir

Name: smokegen
Version: 4.8.3
Release: alt1

Group: Graphical desktop/Other
Summary: Smoke Generator
Url: http://www.kde.org
License: LGPLv2 and GPLv2+

#Obsoletes: kde4bindings < %version
#Provides: kde4bindings = %version

Source: %name-%version.tar
# ALT
Patch1000: smokegen-4.7.1-fix-compile-smokekde.patch

# Automatically added by buildreq on Wed Sep 14 2011 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-xml libstdc++-devel python-base ruby
#BuildRequires: cmake gcc-c++ libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel rpm-build-ruby
BuildRequires: cmake gcc-c++ libqt4-devel kde-common-devel

%description
This package includes Smoke Generator.

%package -n libsmokebase4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokebase4
Qt generic bindings library.

%package devel
Group: Development/KDE and QT
Summary: Header files for Smoke Generator
Conflicts: smoke4-devel < 4.7
Requires: libqt4-devel
Requires: libsmokebase4 = %version-%release
%description devel
This package includes the header files you will need to compile
applications for KDE 4.

%prep
%setup
%patch1000 -p1 -b .fix-compile-smokekde

%build
%Kcmake
%Kmake

%install
%Kinstall
mkdir -p %buildroot/%_includedir/smoke/

%files -n libsmokebase4
%_K4libdir/libsmokebase.so.*

%files devel
%doc README
%_bindir/*
%_libdir/lib*.so
%_libdir/smokegen/
%_includedir/smoke.h
%_includedir/smoke/
%_includedir/smokegen/
%_datadir/smoke/
%_datadir/smokegen/

%changelog
* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
