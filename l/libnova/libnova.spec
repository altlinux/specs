
Name: libnova
Version: 0.14.0
Release: alt2

Summary: General purpose astronomy & astrodynamics library
Group: System/Libraries
License: LGPLv2+
Url: http://sourceforge.net/projects/libnova/

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz

BuildRequires: gcc-c++ gcc-fortran glibc-devel

%description
Libnova is a general purpose, double precision, celestial mechanics,
astrometry and astrodynamics library

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
%description devel
Contains library and header files for %name

%prep
%setup -q
%autoreconf

%build
%configure --disable-rpath --disable-static --enable-shared
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%make install DESTDIR=%buildroot


%files
%_libdir/libnova-*.so.*
%doc ChangeLog README AUTHORS NEWS

%files devel
%_bindir/libnovaconfig
%doc COPYING examples/*.c
%_includedir/libnova
%_libdir/libnova.so

%changelog
* Tue Dec 13 2011 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt2
- fix to build without rpath

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt0.M60P.1
- built for M60P

* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 0.14.0-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt2
- rebuilt

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.12.2-alt2
- fix requires

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.12.2-alt1
- initial specfile

