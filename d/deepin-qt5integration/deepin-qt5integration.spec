%global repo qt5integration

Name: deepin-qt5integration
Version: 5.1.0.8
Release: alt1
Summary: Qt platform theme integration plugins for DDE
# The entire source code is GPLv3+ except styles/ which is BSD,
# dstyleplugin/ which is GPLv3, dstyleplugin/dstyleanimation* which is LGPL
License: GPL-3.0-or-later and BSD-3-Clause and LGPL-2.1-or-later with Qt-LGPL-exception-1.1
Group: System/Libraries
Url: https://github.com/linuxdeepin/qt5integration
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: gcc-c++ libatk-devel dtk5-core-devel dtk5-widget-devel fontconfig-devel libfreetype-devel libgtk+2-devel glib2-devel libgdk-pixbuf-devel libICE-devel libinput-devel libudev-devel libpango-devel qt5-base-devel qt5-svg-devel libqtxdg-devel >= 3.0.0 qt5-x11extras-devel libX11-devel libXext-devel libXrender-devel libxcb-devel libmtdev-devel qt5-multimedia-devel
BuildRequires: qt5-base-common
# for libQt5ThemeSupport.a
BuildRequires: qt5-base-devel-static
# Requires: deepin-qt5platform-plugins

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%setup -n %repo-%version

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_qt5_plugindir/platformthemes/libqdeepin.so
# %_qt5_plugindir/styles/libdstyleplugin.so
%_qt5_plugindir/styles/libchameleon.so
%_qt5_plugindir/iconengines/libdsvgicon.so
%_qt5_plugindir/iconengines/libdtkbuiltin.so
%_qt5_plugindir/imageformats/libdsvg.so

%changelog
* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.8-alt1
- New version (5.1.0.8) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
