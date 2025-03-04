%def_disable clang

Name: deepin-calculator
Version: 6.5.8
Release: alt1

Summary: An easy to use calculator for ordinary users

License: GPL-2.0+ and GPL-3.0+
# 3rdparty: GPL-2.0+
# src: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-calculator
Vcs: git://github.com/linuxdeepin/deepin-calculator.git

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake dqt6-base-devel dqt6-tools dqt6-svg-devel libdtk6widget-devel dtk6-common-devel libgtest-devel libgmock-devel
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
%DQ6build \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DVERSION=%version \
#

%install
%DQ6install
%find_lang --with-qt %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
# package outside find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
# ---
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%_datadir/deepin-manual/manual-assets/application/%name/

%changelog
* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.8-alt1
- New version 6.5.8.
- Switched to dqt6.
- Applied FindLang policy.

* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.4-alt1
- New version 6.5.4.

* Thu Dec 05 2024 Leontiy Volodin <lvol@altlinux.org> 6.5.2-alt1
- New version 6.5.2.
- Added vcs tag.
- Fixed post-install unowned files.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt2
- Built via separate qt5 instead system (ALT #48138).

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
