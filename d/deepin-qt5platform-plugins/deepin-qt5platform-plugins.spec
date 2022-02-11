%define repo qt5platform-plugins

%def_disable clang

Name: deepin-qt5platform-plugins
Version: 5.0.46
Release: alt1
Summary: Qt platform integration plugins for Deepin Desktop Environment
License: GPL-2.0+ and LGPL-3.0 and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/qt5platform-plugins
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: git-core
BuildRequires: libqt5-core
BuildRequires: qt5-x11extras-devel
BuildRequires: libcairo-devel
BuildRequires: libglvnd-devel
BuildRequires: libXi-devel
BuildRequires: libxcb-render-util-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libxcbutil-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libSM-devel
BuildRequires: libdbus-devel
BuildRequires: libmtdev-devel
BuildRequires: qt5-wayland-devel
BuildRequires: kf5-kwayland-devel
# for libQt5EdidSupport.a
BuildRequires: qt5-base-devel-static

%description
%repo is the
%summary.

%prep
%setup -n %repo-%version
# Disable wayland for now: https://github.com/linuxdeepin/qt5platform-plugins/issues/47
sed -i '/wayland/d' qt5platform-plugins.pro

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    unix:LIBS+="-L/%_lib -ldl"
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc CHANGELOG.md README.md
%doc LICENSE
%_qt5_plugindir/platforms/libdxcb.so

%changelog
* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.46-alt1
- New version (5.0.46).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.40-alt1
- New version (5.0.40) with rpmgs script.

* Fri May 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.23-alt1
- New version (5.0.23) with rpmgs script.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt4.git5b86657
- Built from git.
- Disabled parallel build.

* Fri Apr 02 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt3.git76c1c3e
- Build from git.

* Thu Feb 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt2.git9a9450f
- Built from git (Qt 5.15.2 support).

* Tue Dec 01 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.21-alt1
- New version (5.0.21) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.16-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
