%define repo gio-qt

%def_enable doc

Name: libgio-qt
Version: 0.0.9
Release: alt1
Summary: Qt wrapper library of Gio
License: GPL-3.0+
# LGPL-3.0 in future
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
Group: Development/KDE and QT
BuildArch: noarch

%description doc
This package provides %name documantation for QtCreator.
%endif

%prep
%setup -n %repo-%version
%__subst 's|qhelpgenerator|qhelpgenerator-qt5|' CMakeLists.txt

%build
%cmake_insource \
    -GNinja \
%if_disabled doc
    -DBUILD_DOCS=OFF
%endif

%ninja_build

%install
%ninja_install

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
* Thu Jun 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.9-alt1
- Initial build for ALT Sisyphus.
