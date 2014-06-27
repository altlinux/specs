Name:    qt5-gstreamer1
Version: 1.1.90
Release: alt1

Summary: C++ bindings for GStreamer with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/modules/qt-gstreamer.html

Requires: gst-plugins-base1.0 gst-plugins-good1.0

Source: qt-gstreamer-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: automoc
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-quick1-devel
BuildRequires: libGL-devel libGLES-devel
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
Requires:       qt5-base-devel qt5-declarative-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -qn qt-gstreamer-%version

%build
%Kbuild \
    -DQT_VERSION=5 \
    -DQTGSTREAMER_STATIC=OFF \
    -DQTGSTREAMER_TESTS=OFF \
    -DQTGSTREAMER_EXAMPLES=OFF \
    -DQTGSTREAMER_CODEGEN=OFF \
    -DUSE_GST_PLUGIN_DIR=ON \
    -DUSE_QT_PLUGIN_DIR=ON \
    #

%install
%Kinstall

%files
%doc COPYING README
%_libdir/gstreamer-1.0/libgst*.so
%_libdir/libQt5GLib-2.0.so.0
%_libdir/libQt5GLib-2.0.so.1*
%_libdir/libQt5GStreamer-1.0.so.0
%_libdir/libQt5GStreamer-1.0.so.1*
%_libdir/libQt5GStreamerUi-1.0.so.0
%_libdir/libQt5GStreamerUi-1.0.so.1*
%_libdir/libQt5GStreamerUtils-1.0.so.0
%_libdir/libQt5GStreamerUtils-1.0.so.1*
%_libdir/libQt5GStreamerQuick-1.0.so.0
%_libdir/libQt5GStreamerQuick-1.0.so.1*
%_qt5_importdir/QtGStreamer/
%_qt5_archdatadir/qml/QtGStreamer/

%files devel
%doc HACKING
%_includedir/Qt5GStreamer
%_libdir/cmake/Qt5GStreamer
%_libdir/libQt5GLib-2.0.so
%_libdir/libQt5GStreamer-1.0.so
%_libdir/libQt5GStreamerUi-1.0.so
%_libdir/libQt5GStreamerUtils-1.0.so
%_libdir/libQt5GStreamerQuick-1.0.so
%_libdir/pkgconfig/Qt5GLib-*.pc
%_libdir/pkgconfig/Qt5GStreamer*.pc


%changelog
* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.90-alt1
- initial build
