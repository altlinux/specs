Name: wallpapers-alt-mobile
Version: 0.1.0
Release: alt1

Summary: Wallpapers for the ALT Mobile
License: CC-BY-SA-4.0
Group: Graphical desktop/GNOME

Url: https://github.com/alt-gnome/wallpapers-alt-mobile-sisyphus
Vcs: https://github.com/alt-gnome/wallpapers-alt-mobile-sisyphus
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.50.0

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/gnome-background-properties/alt-mobile-hex-black.xml
%_datadir/wallpapers/alt-mobile/hex-black-ld.png

%changelog
* Mon Feb 10 2025 Oleg Shchavelev <oleg@altlinux.org> 0.1.0-alt1
- Initial build
