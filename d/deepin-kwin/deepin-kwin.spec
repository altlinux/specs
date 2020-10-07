%set_verify_elf_method unresolved=no

%define repo dde-kwin

Name: deepin-kwin
Version: 5.2.0.2
Release: alt2
%K5init altplace

Summary: KWin configuration for Deepin Desktop Environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-kwin
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

# archlinux patches
Patch1: %name-added-functions-from-their-forked-kwin.patch
Patch2: %name-tabbox-chameleon-rename.patch
Patch3: %name-build-fix.patch
Patch4: %name-unload-blur.patch
Patch5: deepin-kwin-qt5.15.patch
Patch6: kwin-5.19.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ninja
BuildRequires: gcc-c++ cmake extra-cmake-modules qt5-tools qt5-tools-devel qt5-base-devel plasma5-kdecoration-devel qt5-x11extras-devel qt5-declarative-devel kf5-kwindowsystem-devel kf5-kcoreaddons-devel dtk5-gui-devel kf5-kconfig-devel kf5-kglobalaccel-devel kf5-ki18n-devel gsettings-qt-devel plasma5-kwin-devel plasma5-kwayland-server-devel kf5-kwayland-devel
BuildRequires: zlib-devel bzlib-devel libpng-devel libpcre-devel libbrotli-devel libuuid-devel libexpat-devel

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%patch1 -R -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%__subst 's|lrelease|lrelease-qt5|' plugins/platforms/plugin/translate_generation.sh
%__subst 's|${CMAKE_INSTALL_PREFIX}/share/kwin/scripts|%_K5data/kwin/scripts/|' scripts/CMakeLists.txt
%__subst 's|${CMAKE_INSTALL_PREFIX}/share/kwin/tabbox|%_K5data/kwin/tabbox|' tabbox/CMakeLists.txt

%build
%K5cmake \
    -GNinja \
    -DCMAKE_INSTALL_LIBDIR=%_K5lib
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
chmod +x %buildroot%_bindir/kwin_no_scale

%files
%doc CHANGELOG.md LICENSE
%_sysconfdir/xdg/*
%_bindir/deepin-wm-dbus
%_bindir/kwin_no_scale
%_K5lib/libkwin-xcb.so.*
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/interfaces/*.xml
%_K5data/kwin/scripts/*
%_K5data/kwin/tabbox/*
%dir %_datadir/dde-kwin-xcb/
%dir %_datadir/dde-kwin-xcb/translations/
%_datadir/dde-kwin-xcb/translations/%repo-xcb*.qm
%dir %_K5plug/platforms/
%_K5plug/platforms/lib%repo-xcb.so
%_K5plug/platforms/lib%repo-wayland.so
%dir %_K5plug/kwin/
%dir %_K5plug/kwin/effects/
%dir %_K5plug/kwin/effects/plugins/
%_K5plug/kwin/effects/plugins/libblur.so
# Bad elfs detected.
%exclude %_K5plug/kwin/effects/plugins/libmultitasking.so
%_K5plug/kwin/effects/plugins/libscissor-window.so
%_K5plug/org.kde.kdecoration2/libdeepin-chameleon.so

%files devel
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_K5lib/libkwin-xcb.so

%changelog
* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt2
- Fixed file locations.

* Wed Sep 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
