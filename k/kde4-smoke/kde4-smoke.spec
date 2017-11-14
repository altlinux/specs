%add_findpackage_path %_kde4_bindir

%def_disable okular

%define rname smokekde
Name: kde4-smoke
Version: 4.11.1
Release: alt5

Group: Development/KDE and QT
Summary: Bindings for KDE libraries
Url: http://www.kde.org
License: LGPLv2+

#Conflicts: kde4bindings < %version

Source: %rname-%version.tar
Source2: FindAkonadi.cmake
Source3: FindOkular.cmake
Patch1: smokekde-4.7.1-alt-find-okular.patch

BuildRequires: cmake gcc-c++ phonon-devel smokegen-devel smokeqt-devel kde4base-workspace-devel
BuildRequires: kde4pimlibs-devel kde4-kate-devel akonadi-devel libqimageblitz-devel attica-devel
#BuildRequires: libsoprano-devel soprano soprano-backend-redland
BuildRequires: libqscintilla2-qt4-devel shared-desktop-ontologies-devel
BuildRequires: kde-common-devel
%if_enabled okular
BuildRequires: kde4-okular-devel
%endif
#BuildRequires: kde4sdk-devel


%description
This package includes bindings for KDE libraries.

%package devel
Group: Development/KDE and QT
Summary: Development files for smokekde
Requires: smokeqt-devel
Provides: smoke4-devel = %version-%release
Obsoletes: smoke4-devel < %version-%release
#Requires: lib%name = %version-%release
#Conflicts: kde4bindings-devel < %version
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

%package -n libsmokekate4
Summary: Qt generic bindings library
Group: System/Libraries
%description -n libsmokekate4
Qt generic bindings library.

%prep
%setup -qn %rname-%version
%patch1 -p1
mkdir -p cmake/modules/
cp -ar %SOURCE2 cmake/modules/
%if_enabled okular
cp -ar %SOURCE3 cmake/modules/
%endif


%build
%add_optflags -std=c++98
%K4cmake
NPROCS=1 %K4make


%install
%K4install


#%files
#%_libdir/libsmoke*.so.*

%files devel
%_K4link/lib*.so
%_includedir/smoke/*
%_datadir/smokegen/*

%files -n libsmokeakonadi4
%_libdir/libsmokeakonadi.so.*
%files -n libsmokeattica4
%_libdir/libsmokeattica.so.*
%files -n libsmokekate4
%_libdir/libsmokekate.so.*
%files -n libsmokekdecore4
%_libdir/libsmokekdecore.so.*
%files -n libsmokekdeui4
%_libdir/libsmokekdeui.so.*
%files -n libsmokekfile4
%_libdir/libsmokekfile.so.*
%files -n libsmokekhtml4
%_libdir/libsmokekhtml.so.*
%files -n libsmokekio4
%_libdir/libsmokekio.so.*
%files -n libsmokeknewstuff24
%_libdir/libsmokeknewstuff2.so.*
%files -n libsmokeknewstuff34
%_libdir/libsmokeknewstuff3.so.*
%files -n libsmokekparts4
%_libdir/libsmokekparts.so.*
%files -n libsmokektexteditor4
%_libdir/libsmokektexteditor.so.*
%files -n libsmokekutils4
%_libdir/libsmokekutils.so.*
#%files -n libsmokenepomuk4
#%_libdir/libsmokenepomuk.so.*
#%files -n libsmokenepomukquery4
#%_libdir/libsmokenepomukquery.so.*
#%files -n libsmokeokular4
#%_libdir/libsmokeokular.so.*
%files -n libsmokeplasma4
%_libdir/libsmokeplasma.so.*
%files -n libsmokesolid4
%_libdir/libsmokesolid.so.*
#%files -n libsmokesoprano4
#%_libdir/libsmokesoprano.so.*
#%files -n libsmokesopranoclient4
#%_libdir/libsmokesopranoclient.so.*
#%files -n libsmokesopranoserver4
#%_libdir/libsmokesopranoserver.so.*


%changelog
* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 4.11.1-alt5
- fix build

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt4
- rebuild with gcc5

* Wed Aug 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt3
- rebuild

* Tue Nov 19 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- rebuild

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Tue Jan 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- fix build requires

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- rebuilt

* Fri Dec 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Fri Dec 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt2
- rebuilt with new okular

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- rebuilt with new soprano

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- rebuilt with new soprano

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Thu Jan 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Thu Sep 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build

