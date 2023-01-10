%def_disable clang

Name: deepin-calculator
Version: 6.0.0
Release: alt1
Summary: An easy to use calculator for ordinary users
License: GPL-2.0+ and GPL-3.0+

# 3rdparty: GPL-2.0+
# src: GPL-3.0+

Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-calculator
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake qt5-linguist qt5-base-devel qt5-svg-devel dtk5-widget-devel deepin-qt-dbus-factory-devel dtk5-common libgtest-devel libgmock-devel
Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/deepin-manual/manual-assets/application/%name/calculator/*/*

%changelog
* Tue Jan 10 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- New version (6.0.0).

* Fri Oct 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.7.22-alt1
- Fixed version tag (5.7.22).

* Tue Oct 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.7.21-alt2.gite1d1d55
- Git version (commit: e1d1d55db3045a552812c7a549960f16be53854b).
- Upstream:
  + fix build with dtk 5.6.

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.7.21-alt1
- New version (5.7.21).
- Checkout from dev to master branch.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.7.9-alt1
- New version (5.7.9).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.19-alt1
- New version (5.7.0.19) with rpmgs script.
- Fixed version tag.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.15-alt1
- New version (5.7.0.15) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.10-alt1
- New version (5.6.0.10) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.7-alt1
- New version (5.6.0.7) with rpmgs script.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.1-alt1
- New version (5.6.0.1) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.5.28-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
