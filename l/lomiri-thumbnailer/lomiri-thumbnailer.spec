%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

%define _libexecdir %_prefix/libexec

Name: lomiri-thumbnailer
Version: 3.1.2
Release: alt1

Summary: D-Bus service for out of process thumbnailing
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-thumbnailer

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(libpersistent-cache-cpp)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: /usr/bin/xvfb-run
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: ayatana-cmake-modules
BuildRequires: python3(tornado)
%endif

%description
Lomiri Thumbnailer is an API for the Lomiri operating environment to
create and cache image thumbnails for local and remote media.

This package provides thumbnailer D-Bus service that can provide
thumbnails on behalf of another process.

%package -n lib%{name}
Group: System/Libraries
Summary: Qt/C++ API to obtain thumbnails

%description -n lib%{name}
Lomiri Thumbnailer is an API for the Lomiri operating environment to
create and cache image thumbnails for local and remote media.

Library providing a client API for obtaining thumbnails from the DBus
service.

%package -n lib%{name}-devel
Group: Development/KDE and QT
Summary: Qt/C++ API to obtain thumbnails (development files)
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Lomiri Thumbnailer is an API for the Lomiri operating environment to
create and cache image thumbnails for local and remote media.

Library providing a client API for obtaining thumbnails from the DBus
service.

This package provides the development files for the library.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -DGSETTINGS_LOCALINSTALL=ON \
       -DGSETTINGS_COMPILE=ON \
       -DENABLE_UBUNTU_COMPAT=ON \
%if_with check
       -DBUILD_TESTING=ON \
       -Dskip-dbus-tests=OFF \
       -Dslowtests=ON
%else
       -DBUILD_TESTING=OFF \
       -Dskip-dbus-tests=ON \
       -Dslowtests=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -VV

%files
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL HACKING
%_bindir/lomiri-thumbnailer-admin
%_man1dir/lomiri-thumbnailer-admin.1.*
%_man1dir/thumbnailer-service.1.*
%_man5dir/thumbnailer-settings.5.xz
%exclude /usr/etc/apport/report-ignore/lomiri-thumbnailer
%dir %_qt5_qmldir/Lomiri/Thumbnailer.0.1
%_qt5_qmldir/Lomiri/Thumbnailer.0.1/libLomiriThumbnailer-qml.so
%_qt5_qmldir/Lomiri/Thumbnailer.0.1/qmldir
%dir %_qt5_qmldir/Ubuntu/Thumbnailer.0.1
%_qt5_qmldir/Ubuntu/Thumbnailer.0.1/LomiriThumbnailerLoader.qml
%_qt5_qmldir/Ubuntu/Thumbnailer.0.1/qmldir
%_libexecdir/lomiri-thumbnailer/thumbnailer-service
%_libexecdir/lomiri-thumbnailer/vs-thumb
%_datadir/dbus-1/services/com.lomiri.Thumbnailer.service
%_datadir/glib-2.0/schemas/com.lomiri.Thumbnailer.gschema.xml

%files -n lib%{name}
%_libdir/liblomiri-thumbnailer-qt.so.1*

%files -n lib%{name}-devel
%_includedir/lomiri-thumbnailer-qt-1.0/lomiri/thumbnailer/qt/lomiri-thumbnailer-qt.h
%_pkgconfigdir/liblomiri-thumbnailer-qt.pc
%_libdir/liblomiri-thumbnailer-qt.so

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.2-alt1
- New version 3.1.2.

* Sat May 23 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- New version 3.1.1.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.0-alt1
- New version 3.1.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.5-alt1
- New version 3.0.5.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus
