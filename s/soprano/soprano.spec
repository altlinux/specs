%define beta %nil

Summary: Qt wrapper API to different RDF storage solutions
Name: soprano
Version: 2.8.0
Release: alt1

Group: Text tools
License: LGPLv2+
Url: http://sourceforge.net/projects/soprano

Requires: %name-backend = %version
Requires: strigi

Source0: http://downloads.sf.net/soprano/soprano-%version%{?beta}.tar.bz2
Patch1: soprano-2.3.1-alt-cmake-install.patch
Patch2: soprano-2.3.1-alt-sort-plugins.patch
Patch3: soprano-2.3.1-alt-def-backend.patch
Patch4: soprano-2.3.1-alt-onto2vocabularyclass-backend.patch
Patch5: soprano-2.7.6-alt-use-aio.patch

BuildRequires(pre): libqt4-devel >= 4.4
BuildRequires: cmake doxygen gcc-c++ glibc-devel graphviz
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXtst-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
BuildRequires: libclucene-core-devel libiodbc-devel libredland-devel phonon-devel
BuildRequires: cmake gcc-c++ doxygen graphviz libredland-devel libiodbc-devel
BuildRequires: raptor2-devel rasqal-devel kde-common-devel

%description
Soprano (formally known as QRDF) is a library which provides a nice Qt
interface to RDF storage solutions. It has a modular structure which
allows to  replace the actual RDF storage implementation used.


%package common
Summary: %name comon package
Group: System/Configuration/Other
Conflicts: soprano <= 2.3.0-alt1
%description common
Common package for %name.

%package backend-redland
Summary: Soprano redland backend
Group: Text tools
Requires: %name-common = %version-%release
Provides: %name-backend = %version
%description backend-redland
Soprano (formally known as QRDF) is a library which provides a nice Qt
interface to RDF storage solutions. It has a modular structure which
allows to  replace the actual RDF storage implementation used.

%package backend-virtuoso
Summary: Soprano virtuoso backend
Group: Text tools
Requires: %name-common = %version-%release
Requires: virtuoso-opensource
Provides: %name-backend = %version
%description backend-virtuoso
Soprano (formally known as QRDF) is a library which provides a nice Qt
interface to RDF storage solutions. It has a modular structure which
allows to  replace the actual RDF storage implementation used.

%package -n lib%name
Summary: Soprano libraries
Group: System/Libraries
Requires: libqt4-core >= %{get_version libqt4-core}
Requires: %name-common = %version-%release
%description -n lib%name
Soprano (formally known as QRDF) is a library which provides a nice Qt
interface to RDF storage solutions. It has a modular structure which
allows to  replace the actual RDF storage implementation used.

%package -n lib%name-devel
Summary: Developer files for %name
Group: Development/KDE and QT
Requires: libqt4-devel
%description  -n lib%name-devel
Development files for the lib%name

%prep
%setup -q -n %name-%version%{?beta}
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1

%build
%add_optflags -DNDEBUG -DQT_NO_DEBUG_OUTPUT
%Kcmake \
    -DSOPRANO_BUILD_API_DOCS:BOOL=ON \
    -DSOPRANO_DISABLE_SESAME2_BACKEND:BOOL=ON
%Kmake


%install
%Kinstall


%files common
%dir %_libdir/soprano/
%dir %_datadir/soprano/
%dir %_datadir/soprano/plugins

%files
%doc AUTHORS README TODO
%_bindir/sopranocmd
%_bindir/sopranod
%_bindir/onto2vocabularyclass
%_libdir/soprano/libsoprano_nquadparser.so
%_libdir/soprano/libsoprano_nquadserializer.so
%_libdir/soprano/libsoprano_raptorparser.so
%_libdir/soprano/libsoprano_raptorserializer.so
%_datadir/soprano/plugins/nquadparser.desktop
%_datadir/soprano/plugins/nquadserializer.desktop
%_datadir/soprano/plugins/raptorparser.desktop
%_datadir/soprano/plugins/raptorserializer.desktop
%_datadir/soprano/rules

%files backend-redland
%_libdir/soprano/libsoprano_redlandbackend.so
%_datadir/soprano/plugins/redlandbackend.desktop
#%_libdir/soprano/plugins/libsoprano_sesame2backend.so
#%_datadir/soprano/plugins/sesame2backend.desktop
#%_datadir/soprano/sesame2

%files backend-virtuoso
%_libdir/soprano/libsoprano_virtuosobackend.so
%_datadir/soprano/plugins/virtuosobackend.desktop

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/soprano*.pc
%_datadir/CMake/Modules/SopranoAddOntology.cmake
%_includedir/soprano/
%_includedir/Soprano/
%_datadir/dbus-1/interfaces/*

%changelog
* Tue Jul 03 2012 Sergey V Turchin <zerg@altlinux.org> 2.8.0-alt1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.57-alt0.M60P.1
- built for M60P

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.57-alt1
- new version

* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.56-alt1
- new version

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt3.M60P.1
- built for M60P

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt4
- turn on virtuoso aio support

* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt3
- fix requires

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt2
- rebuilt with clucene-core

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt0.M60P.1
- build for M60P

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.6-alt1
- new version

* Thu Apr 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.5-alt2
- fix build requires

* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.5-alt0.M60P.2
- built for M60P

* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.5-alt1
- new version

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.4-alt0.M60P.1
- built for M60P

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 2.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt0.M60T.1
- built for M60T

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt2
- fix build requires

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1
- new version

* Wed Jan 26 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.63-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- new version

* Mon Sep 27 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.2-alt1
- new version

* Tue Aug 10 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.64-alt1
- 2.4.64

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.63-alt1
- 2.4.63

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.4-alt0.M51.1
- built for M51

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.4-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.3-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.3-alt1
- new version

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.1-alt0.M51.1
- build for M51

* Fri Apr 02 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.1-alt1
- new version

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.4.0.1-alt1
- new version

* Mon Feb 01 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.73-alt1
- new version

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.71.1070828-alt1
- 2.3.71 svn r1070828

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt4.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt5
- try to use redland backend in onto2vocabularyclass
  if sesame2 not found to don't break kde building

* Fri Nov 20 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt3.M51.1
- built for M51

* Fri Nov 20 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt4
- fix build requires

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt2.M51.1
- built for M51

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt3
- set default backend sesame2

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1.M51.1
- built for M51

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt2
- reversed sort plugins to prevent sesame2

* Fri Oct 02 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1
- new version
- split redland backend into separate package

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.69-alt1
- new version

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.2.3-alt1
- new version

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 2.2.2-alt1
- new version

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 2.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.67-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 2.1.64.895232-alt1
- new snapshot
- removed deprecated macroses from specfile

* Tue Oct 14 2008 Sergey V Turchin <zerg at altlinux dot org> 2.1.1-alt1
- new version

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 2.1-alt1
- new version

* Sun May 04 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.98-alt1
- new version

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.3-alt1
- new version

* Wed Feb 13 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt1
- built for ALT

