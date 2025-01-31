%define _name adwaita-fonts
%define ver_major 48
%define beta %nil

Name: fonts-ttf-adwaita
Version: %ver_major.2
Release: alt1%beta

Summary: Adwaita fonts
License: GPL-3.0-or-later and OFL-1.1
Group: System/Fonts/True type
Url: https://gitlab.gnome.org/GNOME/adwaita-fonts

Vcs: https://gitlab.gnome.org/GNOME/adwaita-fonts.git

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

Provides: %_name = %EVR

BuildRequires(pre): rpm-macros-meson rpm-macros-fonts
BuildRequires: meson

%description
Adwaita fonts for GNOME.

%prep
%setup -n %_name-%version%beta
sed -i 's|\(fontsdir = \).*|\1'"'%_ttffontsdir/Adwaita'"'|' meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
# mono
%_ttffontsdir/Adwaita/AdwaitaMono-Bold.ttf
%_ttffontsdir/Adwaita/AdwaitaMono-BoldItalic.ttf
%_ttffontsdir/Adwaita/AdwaitaMono-Italic.ttf
%_ttffontsdir/Adwaita/AdwaitaMono-Regular.ttf
# sans
%_ttffontsdir/Adwaita/AdwaitaSans-Italic.ttf
%_ttffontsdir/Adwaita/AdwaitaSans-Regular.ttf
%doc README*

%changelog
* Fri Jan 31 2025 Yuri N. Sedunov <aris@altlinux.org> 48.2-alt1
- first build for Sisyphus

