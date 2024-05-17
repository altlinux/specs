%define _name adwaita-icon-theme-legacy
%define ver_major 46
%define beta %nil

Name: icon-theme-adwaita-legacy
Version: %ver_major.2
Release: alt1%beta

Summary: Legacy Adwaita icons theme
License: CC-BY-SA-3.0 and LGPL-3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

Vcs: https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy.git

BuildArch: noarch
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

Provides: %_name = %version-%release
Conflicts: gnome-theme-standard < 3.13.0

Requires: icon-naming-utils
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson icon-naming-utils gtk4-update-icon-cache %_bindir/gtk-encode-symbolic-svg

%description
A fullcolor icon theme providing fallback for legacy apps. See [the
issue](https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/issues/288)
for more info.

%prep
%setup -n %_name-%version%beta

%build
%meson
%meson_build

%install
%meson_install

%find_lang %_name

%files -f %_name.lang
%_iconsdir/AdwaitaLegacy/
%_datadir/pkgconfig/%_name.pc
%doc NEWS COPYING README*

%changelog
* Fri May 17 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- first build for Sisyphus

