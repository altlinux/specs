%define repo gio-qt

%def_enable doc

Name: libgio-qt
Version: 0.0.12
Release: alt1
Summary: Qt wrapper library of Gio
License: LGPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/gio-qt
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake libglibmm-devel qt5-base-devel
%if_enabled doc
BuildRequires: doxygen qt5-tools
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

%build
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
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
%_datadir/qt5/doc/%repo.qch
%endif

%changelog
* Wed Apr 12 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.12-alt1
- New version.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.11-alt1
- New version.

* Thu Jun 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.9-alt1
- Initial build for ALT Sisyphus.
