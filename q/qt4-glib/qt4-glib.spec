Name:    qt4-glib
Version: 1.2.0
Release: alt1

Summary: C++ bindings for Glib with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/modules/qt-gstreamer.html

Source: qt4-glib-%version.tar
Source1: cmake.add
Patch1: alt-install-private-headers.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: automoc
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: libqt4-devel libGL-devel libGLES-devel
BuildRequires: doxygen kde-common-devel

%description
QtGStreamer provides C++ bindings for GLib with a Qt-style API

%package -n libqt4-glib
Group:   System/Libraries
Summary: C++ bindings for Glib with a Qt-style API
Conflicts: qt-gstreamer <= 0.10.3-alt1
%description -n libqt4-glib
QtGStreamer provides C++ bindings for GLib with a Qt-style API


%package devel
Group:          Development/C++
Summary:        Header files and development documentation for %name
Requires:       libqt4-glib = %EVR
Requires:       libqt4-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -q
%patch1 -p0
cat %SOURCE1 >> src/QGlib/CMakeLists.txt

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
pushd BUILD-*/src/QGlib
%make
popd

%install
pushd BUILD-*/src/QGlib
%make install DESTDIR=%buildroot
popd
ln -s libQtGLib-2.0.so %buildroot/%_libdir/libQtGLib.so


%files -n libqt4-glib
%doc README
%_libdir/libQtGLib-2.0.so.0*
%_libdir/libQtGLib-2.0.so.1*

%files devel
%doc HACKING
%_includedir/QtGStreamer/QGlib/
%_libdir/libQtGLib.so
%_libdir/libQtGLib-2.0.so
%_libdir/pkgconfig/QtGLib-*.pc


%changelog
* Thu Sep 04 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- initial build
