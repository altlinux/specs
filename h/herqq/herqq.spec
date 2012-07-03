Name: herqq
Version: 1.0.0
Release: alt3

Group: System/Libraries
Summary: A software library for building UPnP devices and control points
# test app GPLv3 (don't packaged)
License: LGPLv3+
Url: http://herqq.org/

Source: %name-%version.tar
# Upstream
Patch0: herqq-r129.patch
# FC
Patch1: herqq-1.0.0-qtsoap-library.patch
# ALT
Patch100: herqq-1.0.0-alt-constructor.patch
Patch101: herqq-1.0.0-alt-check-pointer.patch

# Automatically added by buildreq on Wed Sep 21 2011 (-bi)
# optimized out: elfutils libqt4-core libqt4-devel libqt4-network libqt4-xml libstdc++-devel
#BuildRequires: gcc-c++ glibc-devel-static phonon-devel qtsoap-devel
BuildRequires: gcc-c++ glibc-devel phonon-devel qtsoap-devel libqt4-devel

%description
Herqq UPnP (HUPnP) is a software library for building UPnP
devices and control points conforming to the UPnP Device
Architecture version 1.1.

%package -n libhupnp
Group: System/Libraries
Summary: A software library for building UPnP devices and control points
Obsoletes: cagibi < 0.2.1
%description -n libhupnp
Herqq UPnP (HUPnP) is a software library for building UPnP
devices and control points conforming to the UPnP Device
Architecture version 1.1.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
#Requires: %name = %version-%release
Provides: hupnp-devel = %version-%release
%description devel
Header files for developing applications using %name.

%prep
%setup
%patch0 -p1
%patch1 -p1 -b .qtsoap-library
%patch100 -p1
%patch101 -p1

%build
qmake-qt4 PREFIX=%prefix -config DISABLE_QTSOAP \
  -config DISABLE_TESTAPP -config USE_QT_INSTALL_LOC \
  'QMAKE_CFLAGS+=%optflags' 'QMAKE_CXXFLAGS+=%optflags'
%make_build

%install
%make INSTALL_ROOT=%buildroot install

%files -n libhupnp
%doc hupnp/ChangeLog
%_libdir/libHUpnp.so.1*

%files devel
%_libdir/libHUpnp.so
%_includedir/qt4/HUpnpCore/


%changelog
* Thu Nov 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt3
- built for sisyphus (ALT#26572)

* Wed Nov 09 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1.M60T.1
- fix possible crash

* Wed Sep 28 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- obsolete cagibi

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.M60P.1
- built for M60P

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
