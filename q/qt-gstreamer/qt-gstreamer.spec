Name:    qt-gstreamer
Version: 0.10.2
Release: alt2

Summary: C++ bindings for GStreamer with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/wiki/QtGStreamer

Requires: gst-plugins-base gst-plugins-good

Source0: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2

# fix LIB_INSTALL_DIR
Patch0:         qt-gstreamer-0.10.1-libdir.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: automoc
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer-devel >= 0.10.31
BuildRequires: gst-plugins-devel
BuildRequires: libqt4-devel
BuildRequires: doxygen kde-common-devel

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt applications.

%package devel
Summary:        Header files and development documentation for %name
Group:          Development/C++
Requires:       %name = %version-%release
Requires:       boost-devel
Requires:       gst-plugins-devel
Requires:       libqt4-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -q
#%patch0 -p1

%build
%Kbuild

%install
%Kinstall

%files
%doc COPYING README
%_libdir/gstreamer-0.10/libgst*.so
%_libdir/libQtGLib-2.0.so.0*
%_libdir/libQtGStreamer-0.10.so.0*
%_libdir/libQtGStreamerUi-0.10.so.0*
%_libdir/libQtGStreamerUtils-0.10.so.0*
%_qt4dir/imports/QtGStreamer/

%files devel
%doc HACKING
%_includedir/QtGStreamer
%_libdir/QtGStreamer
%_libdir/libQtGLib-2.0.so
%_libdir/libQtGStreamer-0.10.so
%_libdir/libQtGStreamerUi-0.10.so
%_libdir/libQtGStreamerUtils-0.10.so
%_libdir/pkgconfig/QtGLib-*.pc
%_libdir/pkgconfig/QtGStreamer*.pc


%changelog
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

