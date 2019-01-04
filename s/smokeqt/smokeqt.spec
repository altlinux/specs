%add_findpackage_path %_kde4_bindir

%def_disable qwt

Name: smokeqt
Version: 4.14.0
Release: alt6%ubt

Group: Development/KDE and QT
Summary: Bindings for Qt libraries
Url: http://www.kde.org
License: LGPLv2+

#Conflicts: kde4bindings < 4.7

Source: %name-%version.tar

# Automatically added by buildreq on Wed Sep 14 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig libGL-devel libGLU-devel libqscintilla2-6-qt4 libqt4-clucene libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-help libqt4-multimedia libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel pkg-config
#BuildRequires: cmake gcc-c++ libqimageblitz-devel libqscintilla2-qt4-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel smokegen-devel
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake gcc-c++ libqimageblitz-devel libqscintilla2-qt4-devel libqt4-devel phonon-devel smokegen-devel
#BuildRequires: kde-common-devel libsoprano-devel kde4libs-devel
BuildRequires: kde-common-devel kde4libs-devel
%if_enabled qwt
BuildRequires: libqwt-devel
%endif

%description
This package includes Bindings for Qt libraries.

%package devel
Group: Development/KDE and QT
Summary: Development files for smokeqt
#Requires: %name = %version-%release
Requires: smokegen-devel
Conflicts: smoke4-devel < 4.7
%description devel
This package includes the header files.

%package -n   libsmokekde4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokekde4
KDE generic bindings library.

%package -n libsmokeqimageblitz4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokeqimageblitz4
KDE generic bindings library.

%package -n   libsmokephonon4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokephonon4
KDE generic bindings library.

%package -n   libsmokekhtml4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokekhtml4
KDE generic bindings library.

%package -n   libsmokektexteditor4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokektexteditor4
KDE generic bindings library.

%package -n   libsmokeqtuitools4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokeqtuitools4
KDE generic bindings library.

%package -n   libsmokeqtwebkit4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokeqtwebkit4
KDE generic bindings library.

%package -n   libsmokesolid4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokesolid4
KDE generic bindings library.

%package -n libsmokeokular4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokeokular4
KDE generic bindings library.

%package -n   libsmokeqsci4
Summary: KDE generic bindings library
Group: System/Libraries
%description -n libsmokeqsci4
KDE generic bindings library.

%package -n libsmokesoprano4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokesoprano4
Qt generic bindings library.

%package -n libsmokeqtscript4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtscript4
Qt generic bindings library.

%package -n libsmokenepomuk4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokenepomuk4
Qt generic bindings library.

%package -n libsmokeqt4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqt4
Qt generic bindings library.

%package -n libsmokeqttest4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqttest4
Qt generic bindings library.

%package -n libsmokeakonadi4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeakonadi4
Qt generic bindings library.

%package -n libsmokeplasma4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeplasma4
Qt generic bindings library.

%package -n libqyoto4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libqyoto4
Qt generic bindings library.

%package -n libsmokeattica4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeattica4
Qt generic bindings library.

%package -n libsmokekdecore4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekdecore4
Qt generic bindings library.

%package -n libsmokekdeui4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekdeui4
Qt generic bindings library.

%package -n libsmokekfile4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekfile4
Qt generic bindings library.

%package -n libsmokekio4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekio4
Qt generic bindings library.

%package -n libsmokeknewstuff24
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeknewstuff24
Qt generic bindings library.

%package -n libsmokeknewstuff34
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeknewstuff34
Qt generic bindings library.

%package -n libsmokekparts4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekparts4
Qt generic bindings library.

%package -n libsmokekutils4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekutils4
Qt generic bindings library.

%package -n libsmokenepomukquery4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokenepomukquery4
Qt generic bindings library.

%package -n libsmokeqtcore4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtcore4
Qt generic bindings library.

%package -n libsmokeqtdbus4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtdbus4
Qt generic bindings library.

%package -n libsmokeqtgui4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtgui4
Qt generic bindings library.

%package -n libsmokeqtmultimedia4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtmultimedia4
Qt generic bindings library.

%package -n libsmokeqtnetwork4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtnetwork4
Qt generic bindings library.

%package -n libsmokeqtopengl4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtopengl4
Qt generic bindings library.

%package -n libsmokeqtsql4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtsql4
Qt generic bindings library.

%package -n libsmokeqtsvg4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtsvg4
Qt generic bindings library.

%package -n libsmokeqtxml4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtxml4
Qt generic bindings library.

%package -n libsmokeqtxmlpatterns4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtxmlpatterns4
Qt generic bindings library.

%package -n libsmokesopranoserver4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokesopranoserver4
Qt generic bindings library.

%package -n libsmokesopranoclient4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokesopranoclient4
Qt generic bindings library.

%package -n libsmokebase4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokebase4
Qt generic bindings library.

%package -n libsmokeqt3support4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqt3support4
Qt generic bindings library.

%package -n libsmokeqthelp4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqthelp4
Qt generic bindings library.

%package -n libsmokeqtdeclarative4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqtdeclarative4
Qt generic bindings library.

%package -n libsmokeqwt4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokeqwt4
Qt generic bindings library.

%prep
%setup

%build
%add_optflags -std=c++98
%Kcmake \
	-DQSCINTILLA_NAMES=qscintilla2_qt4
%Kmake VERBOSE=1

%install
%Kinstall


%files devel
%_libdir/libsmoke*.so
%_includedir/smoke/*
%_datadir/smokegen/*
%_datadir/smoke/*

%files -n libsmokephonon4
%_libdir/libsmokephonon.so.*
%files -n libsmokeqimageblitz4
%_libdir/libsmokeqimageblitz.so.*
%files -n libsmokeqsci4
%_libdir/libsmokeqsci.so.*
%files -n libsmokeqt3support4
%_libdir/libsmokeqt3support.so.*
%files -n libsmokeqtcore4
%_libdir/libsmokeqtcore.so.*
%files -n libsmokeqtdbus4
%_libdir/libsmokeqtdbus.so.*
%files -n libsmokeqtdeclarative4
%_libdir/libsmokeqtdeclarative.so.*
%files -n libsmokeqtgui4
%_libdir/libsmokeqtgui.so.*
%files -n libsmokeqthelp4
%_libdir/libsmokeqthelp.so.*
%files -n libsmokeqtmultimedia4
%_libdir/libsmokeqtmultimedia.so.*
%files -n libsmokeqtnetwork4
%_libdir/libsmokeqtnetwork.so.*
%files -n libsmokeqtopengl4
%_libdir/libsmokeqtopengl.so.*
%files -n libsmokeqtscript4
%_libdir/libsmokeqtscript.so.*
%files -n libsmokeqtsql4
%_libdir/libsmokeqtsql.so.*
%files -n libsmokeqtsvg4
%_libdir/libsmokeqtsvg.so.*
%files -n libsmokeqttest4
%_libdir/libsmokeqttest.so.*
%files -n libsmokeqtuitools4
%_libdir/libsmokeqtuitools.so.*
%files -n libsmokeqtwebkit4
%_libdir/libsmokeqtwebkit.so.*
%files -n libsmokeqtxmlpatterns4
%_libdir/libsmokeqtxmlpatterns.so.*
%files -n libsmokeqtxml4
%_libdir/libsmokeqtxml.so.*
%if_enabled qwt
%files -n libsmokeqwt4
%_libdir/libsmokeqwt.so.*
%endif


%changelog
* Fri Jan 04 2019 Vitaly Lipatov <lav@altlinux.ru> 4.14.0-alt6
- NMU: build without libqwt

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.14.0-alt5%ubt
- Rebuilt with qscintilla2 2.10.1.

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt4
- rebuild with gcc5

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt3
- rebuild with new qscintilla

* Wed Aug 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- build with qwt

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Mon Nov 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- rebuilt with new libqscintilla2

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Fri Dec 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- rebuilt with new qscintilla

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
