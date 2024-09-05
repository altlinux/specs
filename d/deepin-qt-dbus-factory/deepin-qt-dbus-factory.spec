%define soname dframeworkdbus
%define repo   dde-qt-dbus-factory

%def_disable clang

Name: deepin-qt-dbus-factory
Version: 6.0.0
Release: alt3

Summary: A repository stores auto-generated Qt5 dbus code

# The entire source code is GPL-3.0+ except
# libdframeworkdbus/qtdbusextended/ which is LGPL-2.1+
License: GPL-3.0+ and LGPL-2.1+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-qt-dbus-factory

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-macros-dqt5
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: python3 libglvnd-devel dqt5-base-devel dtkcore

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%description
A repository stores auto-generated Qt5 dbus code.

%package -n libdframeworkdbus2
Summary: Library for %name
Group: Development/KDE and QT

%description -n libdframeworkdbus2
A repository stores auto-generated Qt5 dbus code.
Library for %name.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
%define optflags_lto %nil
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_dqt5_bindir:$PATH
%qmake_dqt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    QMAKE_RPATHDIR=%_dqt5_libdir \
    LIB_INSTALL_DIR=%_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdframeworkdbus2
%doc README.md CHANGELOG.md technology-overview.md
%doc LICENSE
%_libdir/lib%soname.so.2*

%files devel
%_includedir/lib%soname-2.0/
%_libdir/cmake/DFrameworkdbus/
%_pkgconfigdir/%soname.pc
%_libdir/lib%soname.so

%changelog
* Thu May 09 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt3
- Built via separate qt5 instead system (ALT #48138).

* Thu Feb 08 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt2
- Requires: libqt5-core = %%_qt5_version.
- Cleanup spec.

* Mon Feb 20 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- New version (6.0.0).

* Wed Mar 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.22-alt1
- New version (5.5.22).

* Mon Feb 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.5-alt1
- New version (5.5.5).

* Wed Feb 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20).

* Tue Aug 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt1
- New version (5.4.17).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10).

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Wed Mar 10 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.4-alt1
- New version (5.4.4) with rpmgs script.

* Tue Jan 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.35-alt1
- New version (5.3.35) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.34-alt1
- New version (5.3.0.34) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.20-alt1
- New version (5.3.0.20) with rpmgs script.
- Fixed compatibility with qt 5.15.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.19-alt1
- New version (5.3.0.19) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
