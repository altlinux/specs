%define repo qt5integration

%def_disable clang

Name: deepin-qt5integration
Version: 5.5.20
Release: alt1
Summary: Qt platform theme integration plugins for DDE
# The entire source code is GPLv3+ except styles/ which is BSD,
# dstyleplugin/ which is GPLv3, dstyleplugin/dstyleanimation* which is LGPL
License: GPL-3.0-or-later and BSD-3-Clause and LGPL-2.1-or-later with Qt-LGPL-exception-1.1
Group: System/Libraries
Url: https://github.com/linuxdeepin/qt5integration
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: libatk-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-widget-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libgtk+2-devel
BuildRequires: glib2-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libICE-devel
BuildRequires: libinput-devel
BuildRequires: libudev-devel
BuildRequires: libpango-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: libqtxdg-devel >= 3.0.0
BuildRequires: qt5-x11extras-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrender-devel
BuildRequires: libxcb-devel
BuildRequires: libmtdev-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-base-common
BuildRequires: libgtest-devel
# for libQt5ThemeSupport.a
BuildRequires: qt5-base-devel-static
# Requires: deepin-qt5platform-plugins

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%setup -n %repo-%version

%build
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix
make -j1

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_qt5_plugindir/platformthemes/libqdeepin.so
%_qt5_plugindir/styles/libchameleon.so
%_qt5_plugindir/iconengines/libdsvgicon.so
%_qt5_plugindir/iconengines/libdtkbuiltin.so
%_qt5_plugindir/iconengines/libxdgicon.so
%_qt5_plugindir/imageformats/libdsvg.so

%changelog
* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.20-alt1
- New version (5.5.20).

* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.17-alt1
- New version (5.5.17).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.8-alt1
- New version (5.5.8).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.3-alt1
- New version (5.5.3).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.12-alt1
- New version (5.1.12) with rpmgs script.

* Fri Apr 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.11-alt2
- Disabled multithreaded build.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.11-alt1
- New version (5.1.11) with rpmgs script.

* Fri Apr 02 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.5-alt2.gitcb2a4e4
- Build from commit cb2a4e4c310b3749cd7e5e66de4c2ad3c5689550.

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.5-alt1
- New version (5.1.5) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.9-alt1
- New version (5.1.0.9) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.8-alt1
- New version (5.1.0.8) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
