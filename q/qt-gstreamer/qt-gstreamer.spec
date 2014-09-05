Name:    qt-gstreamer
Version: 0.10.3
Release: alt3

Summary: C++ bindings for GStreamer with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/modules/qt-gstreamer.html

Requires: gst-plugins-base gst-plugins-good

Source0: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2

Patch1: alt-ext-glib.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: automoc
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer-devel >= 0.10.31
BuildRequires: gst-plugins-devel
BuildRequires: libqt4-devel libGL-devel libGLES-devel
BuildRequires: qt4-glib-devel
BuildRequires: doxygen kde-common-devel

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt applications.

%package -n qt-gstreamer0-qml
Group:   System/Libraries
Summary: QML bindings for GStreamer with a Qt-style API
Provides: qt-gstreamer-qml = %version-%release
Conflicts: qt-gstreamer1-qml
%description -n qt-gstreamer0-qml
QML bindings for GStreamer with a Qt-style API

%package devel
Summary:        Header files and development documentation for %name
Group:          Development/C++
Requires:       %name = %version-%release
Requires:       qt4-glib-devel
Requires:       boost-devel
Requires:       gst-plugins-devel
Requires:       libqt4-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -q
%patch1 -p1

rm -rf src/QGlib
ln -s /usr/include/QtGStreamer/QGlib src/QGlib

%build
%Kcmake
%Kmake VERBOSE=1

%install
%Kinstall

%files
%doc COPYING README
%_libdir/gstreamer-0.10/libgst*.so
%_libdir/libQtGStreamer-0.10.so.0*
%_libdir/libQtGStreamerUi-0.10.so.0*
%_libdir/libQtGStreamerUtils-0.10.so.0*

%files -n qt-gstreamer0-qml
%_qt4dir/imports/QtGStreamer/

%files devel
%doc HACKING
%_includedir/QtGStreamer
%_libdir/cmake/QtGStreamer
%_libdir/libQtGStreamer-0.10.so
%_libdir/libQtGStreamerUi-0.10.so
%_libdir/libQtGStreamerUtils-0.10.so
%_libdir/pkgconfig/QtGStreamer*.pc


%changelog
* Fri Sep 05 2014 Sergey V Turchin <zerg@altlinux.org> 0.10.3-alt3
- package QML module separately

* Thu Sep 04 2014 Sergey V Turchin <zerg@altlinux.org> 0.10.3-alt2
- package QtGlib separately

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 0.10.3-alt0.M70P.1
- built for M70P

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.10.3-alt1
- new version

* Fri May 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt4
- fix package url

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt3
- rebuild

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt2
- fix requires

* Sat Apr 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt0.M60P.1
- build for M60P

* Fri Apr 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt1
- new version

* Fri Apr 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.1-alt1.M60P.1
- build for M60P

* Fri Apr 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.1-alt2
- fix requires

* Wed Feb 22 2012 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- Initial build in Sisyphus

