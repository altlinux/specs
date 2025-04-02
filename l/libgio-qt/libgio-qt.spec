%define repo gio-qt6
%define sover 0

%def_enable doc

Name: libgio-qt
Version: 0.0.14
Release: alt1
Summary: Qt wrapper library of Gio
License: LGPL-3.0+
Group: System/Libraries
Url: https://github.com/linuxdeepin/gio-qt
Vcs: https://github.com/linuxdeepin/gio-qt.git
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/gio-qt-%version.tar.gz
Patch: gio-qt-0.0.14-alt-fix-detection-dqt6-pkgconfig.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: gcc-c++ cmake libglibmm-devel dqt6-base-devel
%if_enabled doc
BuildRequires: doxygen dqt6-tools
%endif

%description
This is a glib/glibmm wrapper mainly focused on GIO module. This library is designed to be exception-free and avoid Qt application developer do direct access to glib/glibmm.

%package -n lib%{repo}_%sover
Summary: Qt wrapper library of Gio
Group: System/Libraries

%description -n lib%{repo}_%sover
This package provides %repo library.

%package -n lib%repo-devel
Summary: Qt wrapper library of Gio
Group: Development/KDE and QT
Provides: libgio-qt-devel
Obsoletes: libgio-qt-devel

%description -n lib%repo-devel
This package provides development files for %repo library.

%package -n lib%repo-doc
Summary: %name documantation for QtCreator
Group: Documentation
BuildArch: noarch
Provides: %name-doc
Obsoletes: %name-doc

%description -n lib%repo-doc
This package provides %name documantation for QtCreator.

%prep
%setup -n gio-qt-%version
%autopatch -p1
sed -i '/qt5.cmake/d' \
  gio-qt/CMakeLists.txt \
  qgio-tools/CMakeLists.txt
sed -i '/DOXYGEN_QHG_LOCATION/s|qhelpgenerator|%_dqt6_libexecdir/qhelpgenerator|' \
  CMakeLists.txt
sed -i 's|qt5/doc|doc/dqt6|' \
  CMakeLists.txt

%build
%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
%if_disabled doc
  -DBUILD_DOCS=OFF \
%endif
#

%install
%DQ6install

%files -n lib%{repo}_%sover
%_libdir/lib%repo.so.%{sover}*

%files -n lib%repo-devel
%_libdir/lib%repo.so
%_includedir/gio-qt/
%_pkgconfigdir/%repo.pc

%files -n lib%repo-doc
%doc README.md LICENSE
%if_enabled doc
%_datadir/doc/dqt6/gio-qt.qch
%endif

%changelog
* Wed Mar 26 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.14-alt1
- New version 0.0.14.
- Added vcs tag.
- Switched to dqt6.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.12-alt2
- Built via separate qt5 instead system (ALT #48138).

* Wed Apr 12 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.12-alt1
- New version.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.11-alt1
- New version.

* Thu Jun 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.9-alt1
- Initial build for ALT Sisyphus.
