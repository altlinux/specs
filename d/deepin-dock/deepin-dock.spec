%global repo dde-dock
%global start_logo start-here
# %%global __provides_exclude_from ^%%_libdir/%%repo/.*\\.so$

Name: deepin-dock
Version: 5.2.0.14
Release: alt1
Summary: Deepin desktop-environment - Dock module
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-dock_archlinux_qt5.15.patch
Patch1: deepin-dock_archlinux_fix-build.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake libdbusmenu-qt5-devel deepin-network-utils-devel dtk5-widget-devel deepin-qt-dbus-factory-devel >= 2.0 gsettings-qt-devel libgtk+2-devel qt5-base-devel qt5-x11extras-devel qt5-svg-devel libX11-devel libXtst-devel libXext-devel libxcb-devel libxcbutil-icccm-devel libxcbutil-image-devel qt5-linguist
# Requires: deepin-daemon deepin-launcher deepin-menu deepin-qt5integration onboard icon-theme-deepin
#Requires: fedora-logos

%description
Deepin desktop-environment - Dock module.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%patch -p1
%patch1 -p1

%__subst '/TARGETS/s|lib|%_lib|' plugins/*/CMakeLists.txt
sed -E '35d;/dpkg-architecture|EXIT/d' CMakeLists.txt
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DARCHITECTURE=%_arch \
    -DDOCK_TRAY_USE_NATIVE_POPUP=YES
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
%doc LICENSE
%_sysconfdir/%repo/
%_bindir/%repo
%_libdir/%repo/
%_datadir/%repo/
%_datadir/dbus-1/services/*.service
%_datadir/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml

%files devel
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.14-alt1
- New version (5.2.0.14) with rpmgs script.

* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
