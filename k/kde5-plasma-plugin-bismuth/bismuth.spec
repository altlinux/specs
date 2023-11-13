Name: kde5-plasma-plugin-bismuth
Version: 3.1.4
Release: alt2.1

Summary: KDE Plasma extension that lets you tile your windows automatically

License: MIT and CC-BY-4.0 and LGPL-3.0+ and BSD-3-Clause
# cmake: BSD-3-Clause
# contrib, docs, external, scripts: MIT
# src: MIT and LGPL-3.0+ and CC-BY-4.0
Group: Graphical desktop/KDE
Url: https://bismuth-forge.github.io/bismuth

Source: https://github.com/Bismuth-Forge/bismuth/archive/%version/bismuth-%version.tar.gz
Patch1: bismuth-3.1.4-pull-458-swap-windows-when-focus-on-window0.patch
Patch2: bismuth-3.1.4-pull-480-fix-ignore-dialog.patch
Patch3: bismuth-3.1.4-pull-490-fix-windowid-is-undefined-in-wayland.patch

Provides: bismuth

BuildPreReq: rpm-build-kf5
BuildRequires: cmake extra-cmake-modules esbuild
BuildRequires: kf5-kconfigwidgets-devel qt5-base-devel
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: qt5-feedback-devel kf5-kcmutils-devel kf5-ki18n-devel kf5-kdeclarative-devel kf5-kpackage-devel
BuildRequires: plasma5-kdecoration-devel

%description
KDE Plasma extension, that lets you tile your windows automatically and manage
them via keyboard, just like in classical tiling window managers

%prep
%setup -n bismuth-%version
%autopatch -p1

%build
%K5init no_altplace
%K5build \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_NPM=OFF \
    -DUSE_TSC=OFF \
    -DDATA_INSTALL_DIR=%_K5data \
#

%install
%K5install

%files
%doc docs/* LICENSES/*
%_K5plug/kcms/kcm_bismuth.so
%_K5plug/org.kde.kdecoration2/bismuth_kdecoration.so
%_K5data/config.kcfg/bismuth_config.kcfg
%_K5icon/hicolor/16x16/status/bismuth*
%_K5icon/hicolor/32x32/status/bismuth*
%_K5icon/hicolor/22x22/categories/bismuth-kcm.svg
%_K5icon/hicolor/64x64/categories/bismuth-kcm.svg
%_K5icon/hicolor/scalable/apps/bismuth.svg
%_K5data/kconf_update/bismuth_old_conf_ui.sh
%_K5data/kconf_update/bismuth_old_conf_ui.upd
%_K5data/kconf_update/bismuth_new_logger.upd
%_K5data/kconf_update/bismuth_shortcuts_category.upd
%_K5data/kpackage/kcms/kcm_bismuth
%_K5srv/kcm_bismuth.desktop
%_K5data/kwin/scripts/bismuth
%dir %_K5qml/org/kde/bismuth/
%dir %_K5qml/org/kde/bismuth/core/
%_K5qml/org/kde/bismuth/core/libbismuth_core.so
%_K5qml/org/kde/bismuth/core/qmldir
%_datadir/qlogging-categories5/bismuth.categories

%changelog
* Mon Nov 13 2023 Leontiy Volodin <lvol@altlinux.org> 3.1.4-alt2.1
- Cleanup usage of %%K5* macros.
- Added provides to default name of project.

* Tue Aug 01 2023 Leontiy Volodin <lvol@altlinux.org> 3.1.4-alt2
- Applied fixes by project community.
- Enabled multiarch build.

* Mon Sep 26 2022 Leontiy Volodin <lvol@altlinux.org> 3.1.4-alt1
- New version (3.1.4).
- Upstream:
  + Use floating geometry to be compatible with KWin 5.26.

* Tue Jul 12 2022 Leontiy Volodin <lvol@altlinux.org> 3.1.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
