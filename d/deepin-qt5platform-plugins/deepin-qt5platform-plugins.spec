%global repo qt5platform-plugins

Name: deepin-qt5platform-plugins
Version: 5.0.18
Release: alt1
Summary: Qt platform integration plugins for Deepin Desktop Environment
License: GPL-2.0+ and LGPL-3.0 and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt5platform-plugins
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
BuildRequires: gcc-c++ git-core libqt5-core qt5-x11extras-devel libcairo-devel libglvnd-devel libXi-devel libxcb-render-util-devel libxcbutil-image-devel libxcbutil-icccm-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libxkbcommon-devel libSM-devel libdbus-devel libmtdev-devel qt5-wayland-devel kf5-kwayland-devel
# for libQt5EdidSupport.a
BuildRequires: qt5-base-devel-static

%description
%repo is the
%summary.

%prep
%setup -n %repo-%version
# rm -r xcb/libqt5xcbqpa-dev wayland/qtwayland-dev
# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro

sed -i 's|error(Not support Qt Version: .*)|INCLUDEPATH += %_qt5_headerdir/QtXcb|' xcb/linux.pri

# https://github.com/linuxdeepin/qt5platform-plugins/pull/48
sed -i 's/xcbWindow-/window-/' xcb/windoweventhook.cpp

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_qt5_plugindir/platforms/libdxcb.so

%changelog
* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.16-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
