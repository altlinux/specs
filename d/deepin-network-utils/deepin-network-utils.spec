%def_disable clang

%define repo dde-network-utils

Name: deepin-network-utils
Version: 5.4.13
Release: alt3
Summary: Deepin desktop-environment - network utils
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-network-utils
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-network-utils-5.4.13-alt-fix-gtest-1.13.patch

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: deepin-qt-dbus-factory-devel dqt5-base-devel dqt5-linguist gsettings-qt-devel libgtest-devel
# BuildRequires: libgio-qt-devel

%description
Deepin desktop-environment - network utils.

%package -n libddenetworkutils
Summary: Library for %name
Group: Graphical desktop/Other

%description -n libddenetworkutils
Deepin desktop-environment - network utils.
Library for %name

%package -n libddenetworkutils-devel
Summary: Development package for %name
Group: Development/C++
Provides: deepin-network-utils-devel = %version-%release
Obsoletes: deepin-network-utils-devel < %version-%release

%description -n libddenetworkutils-devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%patch -p1
sed -i '/target.path/s|\$\$PREFIX/lib|%_libdir|' \
    dde-network-utils/dde-network-utils.pro

%build
export PATH=%_dqt5_bindir:$PATH
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%qmake_dqt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    QMAKE_RPATHDIR=%_dqt5_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libddenetworkutils
%doc README.md
%_libdir/lib%{repo}.so.1*
%_datadir/%repo/

%files -n libddenetworkutils-devel
%_includedir/libddenetworkutils/
%_pkgconfigdir/%repo.pc
%_libdir/lib%{repo}.so

%changelog
* Fri May 24 2024 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt3
- Built via separate qt5 instead system (ALT #48138).

* Thu Jan 26 2023 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt2
- Fix build with googletest 1.13.0.
- Renamed devel subpackage to libddenetworkutils-devel.

* Fri Feb 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13).

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.9-alt1
- New version (5.4.9).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.8-alt1
- New version (5.3.0.8) with rpmgs script.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- New version (5.3.0.5) with rpmgs script.

* Mon Jul 27 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
