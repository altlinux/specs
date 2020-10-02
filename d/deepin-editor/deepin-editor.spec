Name: deepin-editor
Version: 5.6.28
Release: alt1
Summary: Simple editor for Linux Deepin
License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake libfreeimage-devel kf5-kcodecs-devel kf5-syntax-highlighting-devel dtk5-widget-devel libexif-devel libexif-devel libxcbutil-devel libXtst-devel libpolkitqt5-qt5-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-linguist
# Requires: deepin-session-shell deepin-qt5integration

%description
%summary.

%prep
%setup
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake_insource -GNinja -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_BUILD_TYPE=Release
%ninja_build

%install
%ninja_install

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/dedit
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
