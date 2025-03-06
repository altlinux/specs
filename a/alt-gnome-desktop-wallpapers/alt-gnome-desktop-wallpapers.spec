%define _unpackaged_files_terminate_build 1

Name: alt-gnome-desktop-wallpapers
Version: 1.0.1
Release: alt1

Summary: Background images for ALT Linux with GNOME
License: Proprietary
Group: Graphical desktop/Other

Url: http://www.basealt.ru
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
Background images for ALT Linux distributions with
the GNOME graphical environment, compiled taking into account
the packaging features of wallpaper for GNOME.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/backgrounds/alt-gnome-desktop/*.jxl
%_datadir/backgrounds/alt-gnome-desktop/*.jpg
%_datadir/gnome-background-properties/alt-gnome-desktop-alt-*.xml

%changelog
* Mon Mar 03 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.1-alt1
- replace: .jxl nature photo with .jpg

* Mon Feb 10 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.0-alt1
- Initial build
