%define shortname indi

Name: indilib
Version: 0.8.0
Release: alt3

Group: Development/C
Summary: Library to control astronomical devices
Url: http://indi.sourceforge.net/
License: LGPLv2+

Provides: %shortname = %version-%release
Conflicts: kde4edu-kstars < 4.1.60
Conflicts: kdeedu-kstars <= 3.5.10-alt2

Source: http://nchc.dl.sourceforge.net/sourceforge/indi/lib%{shortname}_%version.tar.gz
Patch1: 0.7.2-alt-fix-linking.patch

# Automatically added by buildreq on Wed Oct 05 2011 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel pkg-config zlib-devel
#BuildRequires: boost-devel-headers cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel-static
BuildRequires: boost-devel cmake gcc-c++ libcfitsio-devel libnova-devel libusb-compat-devel zlib-devel
BuildRequires: kde-common-devel

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n libsbigudrv
Summary: Librar file for INDI
Group: Development/C
%description -n libsbigudrv
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains library files of indilib.

%package -n lib%shortname
Group: System/Libraries
Summary: Library to control astronomical devices
%description -n lib%shortname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n lib%shortname-devel
Summary: INDI devellopment files
Group: Development/C
Requires: lib%shortname = %version-%release
Provides: %shortname-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release
%description -n lib%shortname-devel
  INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).
  This package contains files need to build applications using indilib.

%prep
%setup -q -n lib%{shortname}_%version
#%patch1 -p1
sed -i 's|lib\${LIB_POSTFIX}|lib\${LIB_SUFFIX}|' CMakeLists.txt

%build
%Kcmake
%Kmake

%install
%Kinstall


%files
%doc ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%shortname

%files -n lib%shortname
%doc ChangeLog NEWS README TODO
%_libdir/lib*.so.*

#%files -n libsbigudrv
#%_libdir/libsbigudrv.so.*

%files -n lib%shortname-devel
%doc ChangeLog README.*
#%doc src/examples
%_libdir/*.so
%_libdir/*.a
%_includedir/libindi
%_pkgconfigdir/libindi.pc

%changelog
* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt3
- rebuilt whith new libnova

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1.M60P.1
- built for M60P

* Wed Oct 05 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt2
- fix build requires

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M60P.1
- built for M60P

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt3
- rebuilt

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt2
- rebuilt

* Fri Aug 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Tue Nov 10 2009 Sergey V Turchin <zerg@altlinux.org> 0.6-alt4
- rebuilt with new libnova

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt3
- remove ExclusiveArch from specfile

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- fix conflicts

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- initial specfile

