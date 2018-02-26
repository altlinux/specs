%define sover 0
%define sover_qt4 1
%define sover_glib 2
%define sover_gobject 1
%define libname libntrack%sover
%define libname_qt4 libntrack%{sover_qt4}-qt4
%define libname_glib libntrack%{sover_glib}-glib
%define libname_gobject libntrack%{sover_gobject}-gobject

Name: ntrack
Version: 016
Release: alt1
Epoch: 1

Group: System/Libraries
Summary: Network Connectivity Tracking library for Desktop Applications
Url: https://launchpad.net/ntrack
License: LGPLv3

%setup_python_module sip

Source: %name-%version.tar.gz
Patch1: ntrack-011-alt-fix-pkgconfig.patch

# Automatically added by buildreq on Thu Jan 27 2011 (-bi)
#BuildRequires: gcc-c++ glibc-devel-static libnl-devel libqt4-devel python-module-pygobject-devel rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel libnl-devel libqt4-devel python-module-pygobject-devel

%description
ntrack aims to be a lightweight and easy to use library for application
developers that want to get events on network online status changes such
as online, offline or route changes.

%package -n libntrack-devel
Group: Development/Other
Summary: Network Connectivity Tracking library for Desktop Applications
#Requires: %libname = %epoch:%version
%description -n libntrack-devel
Development files (headers and libraries) for ntrack

%package -n %libname
Group: System/Libraries
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n %libname
ntrack aims to be a lightweight and easy to use library for application
developers that want to get events on network online status changes such
as online, offline or route changes.

%package -n libntrack-qt4-devel
Group: Development/Other
#Requires: %libname_qt4 = %epoch:%version
Requires: libntrack-devel = %epoch:%version
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n libntrack-qt4-devel
Development files (headers and libraries) for ntrack

%package -n %libname_qt4
Group: System/Libraries
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n %libname_qt4
ntrack aims to be a lightweight and easy to use library for application
developers that want to get events on network online status changes such
as online, offline or route changes.

%package -n libntrack-gobject-devel
Group: Development/Other
#Requires: %libname_gobject = %epoch:%version
Requires: libntrack-devel = %epoch:%version
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n libntrack-gobject-devel
Development files (headers and libraries) for ntrack

%package -n %libname_gobject
Group: System/Libraries
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n %libname_gobject
ntrack aims to be a lightweight and easy to use library for application
developers that want to get events on network online status changes such
as online, offline or route changes.

%package -n libntrack-glib-devel
Group: Development/Other
#Requires: %libname_glib = %epoch:%version
Requires: libntrack-devel = %epoch:%version
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n libntrack-glib-devel
Development files (headers and libraries) for ntrack

%package -n %libname_glib
Group: System/Libraries
Summary: Network Connectivity Tracking library for Desktop Applications
%description -n %libname_glib
ntrack aims to be a lightweight and easy to use library for application
developers that want to get events on network online status changes such
as online, offline or route changes.

%package -n python-module-ntrack
Group: System/Libraries
Summary: Python bindings for %name
%description -n python-module-ntrack
Python bindings for %name

%prep
%setup -q -n %name-%version
%patch1 -p1
%autoreconf

%build
%configure \
    --enable-shared \
    --disable-static \
    --disable-rpath \
    --with-glib2 \
    --with-gobject \
    --with-qt4
%make


%install
%make install DESTDIR=%buildroot


%files -n libntrack-devel
%dir %_includedir/ntrack
%_includedir/ntrack/common
%_libdir/pkgconfig/libntrack.pc
%_libdir/libntrack.so

%files -n %libname
%doc ChangeLog AUTHORS NEWS README
%dir %_libdir/ntrack
%dir %_libdir/ntrack/modules
%_libdir/ntrack/modules/ntrack-*.so
%_libdir/libntrack.so.%sover
%_libdir/libntrack.so.%sover.*

%files -n libntrack-qt4-devel
%_includedir/ntrack/qt4
%_libdir/pkgconfig/libntrack-qt4.pc
%_libdir/libntrack-qt4.so

%files -n %libname_qt4
%_libdir/libntrack-qt4.so.%sover_qt4
%_libdir/libntrack-qt4.so.%sover_qt4.*

%files -n libntrack-gobject-devel
%_includedir/ntrack/gobject
%_libdir/pkgconfig/libntrack-gobject.pc
%_libdir/libntrack-gobject.so

%files -n %libname_gobject
%_libdir/libntrack-gobject.so.%sover_gobject
%_libdir/libntrack-gobject.so.%sover_gobject.*

%files -n libntrack-glib-devel
%_includedir/ntrack/glib
%_libdir/pkgconfig/libntrack-glib.pc
%_libdir/libntrack-glib.so

%files -n %libname_glib
%_libdir/libntrack-glib.so.%sover_glib
%_libdir/libntrack-glib.so.%sover_glib.*

%files -n python-module-ntrack
%python_sitelibdir/*ntrack*.so

%changelog
* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 1:016-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:011-alt2.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 1:011-alt2
- revert to 011

* Mon Apr 04 2011 Sergey V Turchin <zerg@altlinux.org> 014-alt1
- new version

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 011-alt1
- initial build
