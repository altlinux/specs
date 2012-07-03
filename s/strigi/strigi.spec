
Name: strigi
Version: 0.7.7
Release: alt3

Summary: The fastest and smallest desktop searching program
License: LGPL2+
Group: File tools
Url: http://strigi.sourceforge.net/

Requires: /usr/bin/pdftotext

Source0: %name-%version.tar.bz2
Source1: %name.watch
Source2: strigi-daemon.desktop
Source3: strigiclient.desktop

# FC
Patch1: strigi-0.7.7-xpmfix.patch

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
Requires: lib%name = %version

%description -n lib%name-devel
Strigi is a daemon which uses a very fast and efficient crawler that can
index data on your harddrive. Indexing operations are performed without
hammering your system, this makes Strigi the fastest and smallest
desktop searching program.

This package contains %name development library and headers.


%prep
%setup
pushd libstreamanalyzer
%patch1 -p1
popd

%build
%Kcmake \
    -DCMAKE_SKIP_RPATH=YES \
    -DCMAKE_BUILD_TYPE="Release" \
    -DENABLE_FFMPEG:BOOL=OFF \
    -DENABLE_CLUCENE:BOOL=ON \
    -DENABLE_CLUCENE_NG:BOOL=ON \
    -DENABLE_INOTIFY:BOOL=ON \
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
%dir %_libdir/libsearchclient/
%dir %_libdir/libstreamanalyzer/
%dir %_libdir/libstreams/
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
%_libdir/%name/*.cmake
%_libdir/libsearchclient/*.cmake
%_libdir/libstreamanalyzer/*.cmake
%_libdir/libstreams/*.cmake


%changelog
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
