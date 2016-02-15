Name:    qt-gstreamer1
Version: 1.2.0
Release: alt4

Summary: C++ bindings for GStreamer with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/modules/qt-gstreamer.html

Obsoletes: qt-gstreamer < %version-%release
Requires: gst-plugins-base1.0 gst-plugins-good1.0

Source: %name-%version.tar
Patch1: alt-ext-glib.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: automoc
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libqt4-devel libGL-devel libGLES-devel
BuildRequires: qt4-glib-devel
BuildRequires: doxygen kde-common-devel

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt applications.

%package qml
Group:   System/Libraries
Summary: QML bindings for GStreamer with a Qt-style API
Provides: qt-gstreamer-qml = %version-%release
Conflicts: qt-gstreamer0-qml
%description qml
QML bindings for GStreamer with a Qt-style API

%package devel
Summary:        Header files and development documentation for %name
Group:          Development/C++
Requires:       %name = %version-%release
Requires:       qt4-glib-devel
Requires:       boost-devel
Requires:       gst-plugins1.0-devel
Requires:       libqt4-devel
Conflicts: qt-gstreamer-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -q
%patch1 -p1

rm -rf src/QGlib
ln -s /usr/include/QtGStreamer/QGlib src/QGlib

%build
%Kcmake \
    -DQT_VERSION=4 \
    -DQTGSTREAMER_STATIC=OFF \
    -DQTGSTREAMER_TESTS=OFF \
    -DQTGSTREAMER_EXAMPLES=OFF \
    -DQTGSTREAMER_CODEGEN=OFF \
    -DUSE_GST_PLUGIN_DIR=ON \
    -DUSE_QT_PLUGIN_DIR=ON \
    #
for subd in src elements/gstqtvideosink
do
pushd $subd
if [ ! -e %_includedir/gstreamer-1.0/gst/gstconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gstconfig.h ]
then
    mkdir -p gst
    [ -e gst/gstconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gstconfig.h gst/gstconfig.h
fi
if [ ! -e %_includedir/gstreamer-1.0/gst/gl/gstglconfig.h -a -e %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h ]
then
    mkdir -p gst/gl
    [ -e gst/gl/gstglconfig.h ] || \
       ln -s %_libdir/gstreamer-1.0/include/gst/gl/gstglconfig.h gst/gl/gstglconfig.h
fi
popd
done
%Kmake

%install
%Kinstall

%files
%doc README
%_libdir/gstreamer-1.0/libgst*.so
%_libdir/libQtGStreamer-1.0.so.0
%_libdir/libQtGStreamer-1.0.so.1*
%_libdir/libQtGStreamerUi-1.0.so.0
%_libdir/libQtGStreamerUi-1.0.so.1*
%_libdir/libQtGStreamerUtils-1.0.so.0
%_libdir/libQtGStreamerUtils-1.0.so.1*

%files qml
%_qt4dir/imports/QtGStreamer/

%files devel
%doc HACKING
%_includedir/QtGStreamer
%_libdir/cmake/QtGStreamer
%_libdir/libQtGStreamer-1.0.so
%_libdir/libQtGStreamerUi-1.0.so
%_libdir/libQtGStreamerUtils-1.0.so
%_libdir/pkgconfig/QtGStreamer*.pc


%changelog
* Mon Feb 15 2016 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt4
- obsolete qt-gstreamer

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt3
- fix against ugly gstreamer includes placement

* Fri Sep 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt2
- fix requires

* Thu Sep 04 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.90-alt1
- initial build
