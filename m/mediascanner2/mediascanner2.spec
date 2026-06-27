%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: mediascanner2
Version: 0.201
Release: alt1

Summary: Media Scanner 2.0
License: GPL-3.0-only AND LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/mediascanner2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(dbus-cpp)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(udisks2)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: qt5-declarative-devel
BuildRequires: gst-plugins-base1.0
BuildRequires: gst-plugins-good1.0
%endif

%description
Media Scanner 2.0 is a user session D-Bus services that scans files (and
detects changes) in the user's home directory relevant for media apps
(such as the gallery app, the music player app, the mediaplayer app,
etc.).

This package provides the media scanner D-Bus service.

%package -n lib%{name}
Group: System/Libraries
Summary: Access library for the media scanner's index

%description -n lib%{name}
This library provides convenient and safe access to the media scanner's
index files.

%package -n lib%{name}-devel
Group: Development/KDE and QT
Summary: Development files for libmediascanner
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Media Scanner 2.0 is a user session D-Bus services that scans files (and
detects changes) in the user's home directory relevant for media apps
(such as the gallery app, the music player app, the mediaplayer app,
etc.).

This package provides the infrastructure for using the media scanner's
access library in C++ based projects.

%prep
%setup

%build
export PATH=$PATH:/usr/share/qt5/bin
%cmake \
%if_with check
       -DENABLE_TESTS=ON
%else
       -DENABLE_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%check
export PATH=$PATH:/usr/share/qt5/bin
%ctest -j1 -VV

%files
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL HACKING
%_bindir/mediascanner-mountwatcher
%_bindir/mediascanner-query
%_bindir/mediascanner-service-2.0
%_bindir/mediascanner-watcher
%_userunitdir/mediascanner-2.0.service
%dir %_libexecdir/mediascanner-2.0
%_libexecdir/mediascanner-2.0/mediascanner-dbus-2.0
%_libexecdir/mediascanner-2.0/mediascanner-extractor
%_datadir/dbus-1/services/com.lomiri.MediaScanner2.Extractor.service
%_datadir/dbus-1/services/com.lomiri.MediaScanner2.service

%files -n lib%{name}
%_libdir/libmediascanner-2.0.so.4
%_libdir/libmediascanner-2.0.so.4.0.*
%dir %_qt5_qmldir/MediaScanner.0.1
%_qt5_qmldir/MediaScanner.0.1/libmediascanner-qml.so
%_qt5_qmldir/MediaScanner.0.1/plugin.qmltypes
%_qt5_qmldir/MediaScanner.0.1/qmldir

%files -n lib%{name}-devel
%dir %_includedir/mediascanner-2.0
%dir %_includedir/mediascanner-2.0/mediascanner
%_includedir/mediascanner-2.0/mediascanner/Album.hh
%_includedir/mediascanner-2.0/mediascanner/Filter.hh
%_includedir/mediascanner-2.0/mediascanner/MediaFile.hh
%_includedir/mediascanner-2.0/mediascanner/MediaFileBuilder.hh
%_includedir/mediascanner-2.0/mediascanner/MediaStore.hh
%_includedir/mediascanner-2.0/mediascanner/MediaStoreBase.hh
%_includedir/mediascanner-2.0/mediascanner/scannercore.hh
%_libdir/libmediascanner-2.0.so
%_pkgconfigdir/mediascanner-2.0.pc

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.201-alt1
- New version 0.201.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.200-alt1
- New version 0.200.

* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 0.118-alt1
- Initial build for Sisyphus
