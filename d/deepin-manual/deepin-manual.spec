%set_verify_elf_method relaxed

Name: deepin-manual
Version: 5.7.0.7
Release: alt1
Summary: Help files for DDE
License: GPL-3.0+ and (BSD-3-Clause and Qt.Commercial) and ISC
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-manual
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-manual_5.7.0.7_alt_qt5.15.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-tools-devel qt5-webchannel-devel dtk5-widget-devel qt5-x11extras-devel qt5-webengine-devel

%description
%summary.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other

%description data
Data files for %name.

%prep
%setup
%patch -p2
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/dman
%_bindir/dman-search
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Manual.Open.service
%_datadir/dbus-1/services/com.deepin.Manual.Search.service
%_iconsdir/hicolor/scalable/apps/%name.svg

%files data
%_datadir/%name/

%changelog
* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.7-alt1
- Initial build for ALT Sisyphus.
