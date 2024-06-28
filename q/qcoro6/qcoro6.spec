%define appname QCoro
%define rname qcoro
%define _cmake__builddir BUILD

%define qtmajor 6
%define sover 0
%define libqcorocore libqcoro%{qtmajor}core%sover
%define libqcorodbus libqcoro%{qtmajor}dbus%sover
%define libqcoronetwork libqcoro%{qtmajor}network%sover
%define libqcoroqml libqcoro%{qtmajor}qml%sover
%define libqcoroquick libqcoro%{qtmajor}quick%sover
%define libqcorowebsockets libqcoro%{qtmajor}websockets%sover

Name: qcoro%qtmajor
Version: 0.10.0
Release: alt1

Group: System/Libraries
Summary: C++ Coroutines for Qt%qtmajor
License: BSD-3-Clause
Url: https://github.com/danvratil/%rname

Source: %name-%version.tar

BuildRequires: cmake extra-cmake-modules qt%qtmajor-tools-devel
BuildRequires: qt%qtmajor-declarative-devel qt%qtmajor-websockets-devel

%description
The QCoro library provides set of tools to make use of the C++20 coroutines
in connection with certain asynchronous Qt actions.

The major benefit of using coroutines with Qt types is that it allows writing
asynchronous code as if it were synchronous and, most importantly, while the
coroutine is co_awaiting, the Qt event loop runs as usual, meaning that your
application remains responsive.

%package devel
Group: Development/KDE and QT
Summary: Development files for %appname
%description devel
This package contains libraries and header files for
developing applications that use %appname.

%package -n %libqcorocore
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcorocore
%name library

%package -n %libqcorodbus
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcorodbus
%name library

%package -n %libqcoronetwork
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcoronetwork
%name library

%package -n %libqcoroqml
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcoroqml
%name library

%package -n %libqcoroquick
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcoroquick
%name library

%package -n %libqcorowebsockets
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libqcorowebsockets
%name library

%prep
%setup

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STSTIC_LIBS=OFF \
    -DUSE_QT_VERSION:STRING=%qtmajor \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%_qt6_archdatadir/mkspecs/modules \
    -DBUILD_TESTING:BOOL=OFF \
    -DQCORO_BUILD_EXAMPLES:BOOL=OFF \
    -DQCORO_ENABLE_ASAN:BOOL=OFF \
    -DQCORO_WITH_QML:BOOL=ON \
    -DQCORO_WITH_QTDBUS:BOOL=ON \
    -DQCORO_WITH_QTNETWORK:BOOL=ON \
    -DQCORO_WITH_QTQUICK:BOOL=ON \
    -DQCORO_WITH_QTWEBSOCKETS:BOOL=ON \
    #
%cmake_build

%install
%cmake_install

%files devel
%_includedir/%rname%qtmajor/
%_libdir/cmake/QCoro%{qtmajor}*/
%_qt6_archdatadir/mkspecs/modules/*.pri
%_libdir/lib*.so

%files -n %libqcorocore
%_libdir/libQCoro%{qtmajor}Core.so.*
%_libdir/libQCoro%{qtmajor}Core.so.%sover
%files -n %libqcorodbus
%_libdir/libQCoro%{qtmajor}DBus.so.*
%_libdir/libQCoro%{qtmajor}DBus.so.%sover
%files -n %libqcoronetwork
%_libdir/libQCoro%{qtmajor}Network.so.*
%_libdir/libQCoro%{qtmajor}Network.so.%sover
%files -n %libqcoroqml
%_libdir/libQCoro%{qtmajor}Qml.so.*
%_libdir/libQCoro%{qtmajor}Qml.so.%sover
%files -n %libqcoroquick
%_libdir/libQCoro%{qtmajor}Quick.so.*
%_libdir/libQCoro%{qtmajor}Quick.so.%sover
%files -n %libqcorowebsockets
%_libdir/libQCoro%{qtmajor}WebSockets.so.*
%_libdir/libQCoro%{qtmajor}WebSockets.so.%sover

%changelog
* Fri Jun 28 2024 Sergey V Turchin <zerg@altlinux.org> 0.10.0-alt1
- initial build
