
Name: strigi
Version: 0.7.8
Release: alt2

Summary: The fastest and smallest desktop searching program
License: LGPL2+
Group: File tools
Url: http://strigi.sourceforge.net/

Requires: /usr/bin/pdftotext
Requires: lib%name = %EVR

Source0: %name-%version.tar.bz2
Source1: %name.watch
Source2: strigi-daemon.desktop
Source3: strigiclient.desktop

# SuSE
Patch101: bug_304439.diff


BuildRequires: boost-devel bzlib-devel cmake cppunit-devel dbus-tools-gui gcc-c++ libattr-devel
BuildRequires: libclucene-core-devel libexiv2-devel libqt4-devel phonon-devel xml-utils libxml2-devel
BuildRequires: libexpat-devel kde-common-devel
#BuildRequires: libffmpeg-devel

%description 
Strigi is a daemon which uses a very fast and efficient crawler that can
index data on your harddrive. Indexing operations are performed without
hammering your system, this makes Strigi the fastest and smallest
desktop searching program.


%package -n lib%name
Summary: %name shared library
Group: System/Libraries
%description -n lib%name
Strigi is a daemon which uses a very fast and efficient crawler that can
index data on your harddrive. Indexing operations are performed without
hammering your system, this makes Strigi the fastest and smallest
desktop searching program.

This package contains %name shared library.


%package -n lib%name-devel
Summary: %name development library and headers
Group: Development/C++
Requires: lib%name = %EVR
%description -n lib%name-devel
Strigi is a daemon which uses a very fast and efficient crawler that can
index data on your harddrive. Indexing operations are performed without
hammering your system, this makes Strigi the fastest and smallest
desktop searching program.

This package contains %name development library and headers.


%prep
%setup
%patch101 -p1
#patch102 -p1

%build
%Kcmake \
    -DCMAKE_SKIP_RPATH=YES \
    -DENABLE_FFMPEG:BOOL=OFF \
    -DENABLE_CLUCENE:BOOL=ON \
    -DENABLE_CLUCENE_NG:BOOL=ON \
    -DENABLE_INOTIFY:BOOL=ON \
    -DENABLE_FAM=OFF \
    -DENABLE_DBUS:BOOL=ON
%Kmake

%install
%Kinstall

mkdir -p %buildroot/{%_desktopdir,%_sysconfdir/xdg/autostart}
install -m0644 %SOURCE2 %buildroot/%_sysconfdir/xdg/autostart/
install -m0644 %SOURCE3 %buildroot/%_desktopdir/


%files
%_bindir/*
%_datadir/dbus-1/services/*
%_datadir/%name/
%dir %_libdir/%name/
%_libdir/%name/*.so
#%_sysconfdir/xdg/autostart/*.desktop
%_desktopdir/*.desktop
%doc AUTHORS ChangeLog README* TODO*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name/
%_pkgconfigdir/*.pc
%dir %_libdir/%name/
%_libdir/cmake/LibSearchClient/
%_libdir/cmake/LibStreamAnalyzer/
%_libdir/cmake/LibStreams/
%_libdir/cmake/Strigi/



%changelog
* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt2
- rebuild with new exiv2

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Fri Jan 25 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt7
- fix requires

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt6
- rebuilt whith new exiv2

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt4.M60P.1
- built for M60P

* Wed Oct 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt5
- don't show strigi-client in KDE settings menu section

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt3.M60P.1
- built for M60P

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt4
- merge upstream and FC patches

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt2.M60P.1
- built for M60P

* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt3
- fix requires

* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt2
- rebuilt with clucene-core

* Fri Feb 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt0.M60P.2
- rebuilt with new exiv2

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt0.M60P.1
- built for M60P

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.7.7-alt1
- new version

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.5-alt2
- rebuilt with new exiv2

* Mon Sep 26 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.5-alt0.M60P.1
- built for M60P

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.5-alt1
- new version

* Thu May 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt4
- don't autostart strigidaemon

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt3
- rebuilt

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt2
- rebuilt with new exiv2

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt0.M51.1
- build for M51

* Mon Feb 08 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.0.1070828-alt1
- svn r1070828

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.7-alt1
- rebuilt with new exiv2

* Mon Jul 27 2009 Sergey V Turchin <zerg@altlinux.org> 0.7-alt0.2
- rebuilt with new exiv2

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.7-alt0.1
- 0.7-RC1

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.95-alt1
- 0.6.95 svn 974206

* Fri Jul 03 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt1.M50.1
- built for M50

* Fri Jul 03 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt2
- add desktop-files for autostart and menu entry

* Fri May 08 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt1
- new version

* Tue Mar 17 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt2
- don't force to build with inotify support

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6.4-alt1
- new version

* Thu Jan 15 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6.3-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6.1.895463-alt1
- new snapshot
- remove deprecated macroses from specfile

* Mon Jun 02 2008 Sergey V Turchin <zerg at altlinux dot org> 0.5.10-alt1
- new version

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 0.5.9-alt1
- new version

* Sun Mar 30 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.5.7-alt4
- rebuild with new libexiv2

* Wed Feb 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.5.7-alt3
- package %_libdir/%name/ (#14347)

* Sat Jan 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.5.7-alt2
- use optflags
- add watch file

* Sat Jan 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.5.7-alt1
- initial build
