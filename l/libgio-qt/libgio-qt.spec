%define repo gio-qt

%def_enable doc

Name: libgio-qt
Version: 0.0.12
Release: alt2
Summary: Qt wrapper library of Gio
License: LGPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/gio-qt
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: gio-qt-0.0.12-upstream-fix-use-QElapsedTimer-instead-QTime.patch
Patch1: gio-qt-0.0.12-alt-fix-detection-dqt5-pkgconfig.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
BuildRequires: gcc-c++ cmake libglibmm-devel dqt5-base-devel
%if_enabled doc
BuildRequires: doxygen dqt5-tools
%endif

%description
This is a glib/glibmm wrapper mainly focused on GIO module. This library is designed to be exception-free and avoid Qt application developer do direct access to glib/glibmm.

%package devel
Summary: Qt wrapper library of Gio
Group: Development/KDE and QT

%description devel
This package provides development files for %repo library.

%if_enabled doc
%package doc
Summary: %name documantation for QtCreator
Group: Documentation
BuildArch: noarch

%description doc
This package provides %name documantation for QtCreator.
%endif

%prep
%setup -n %repo-%version
%patch -p1
%patch1 -p1
sed -i 's|qt5/doc|doc/dqt5|' \
  CMakeLists.txt

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
%if_disabled doc
    -DBUILD_DOCS=OFF
%endif

cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%_libdir/lib%repo.so.*

%files devel
%_libdir/lib%repo.so
%_includedir/%repo
%_pkgconfigdir/%repo.pc

%if_enabled doc
%files doc
%_datadir/doc/dqt5/%repo.qch
%endif

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.12-alt2
- Built via separate qt5 instead system (ALT #48138).

* Wed Apr 12 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.12-alt1
- New version.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.11-alt1
- New version.

* Thu Jun 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.9-alt1
- Initial build for ALT Sisyphus.
