%def_enable snapshot
%define _name phosh
%define ver_major 0.41
%define beta %nil

%def_enable check

Name: %_name-wallpapers
Version: %ver_major.0
Release: alt1%beta

Summary: Phosh wallpapers and other artwork
License: CC-BY-SA-4.0 and CC0-1.0 and GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/guidog/phosh-wallpapers

BuildArch: noarch

Vcs: https://gitlab.gnome.org/guidog/phosh-wallpapers.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/guidog/%name/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

Provides: %_name-backgrounds = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary

%package -n plymouth-theme-%_name
Summary: Phosh theme for Plymouth
Group: Graphical desktop/GNOME

%description -n plymouth-theme-%_name
This package provides Plymouth theme for mobile devices using Phosh.

%package -n sound-theme-%_name
Summary: Phosh sound theme
Group: Graphical desktop/GNOME

%description -n sound-theme-%_name
This package provides sound theme for Phosh.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_datadir/gnome-background-properties/%_name-byzantium-abstract.xml
%_datadir/gnome-background-properties/%_name-logo.xml
%_datadir/%_name/backgrounds/*
%doc README.* NEWS

%files -n plymouth-theme-%_name
%_datadir/plymouth/themes/%_name/
%doc README.* NEWS

%files -n sound-theme-%_name
%_datadir/sounds/%_name/
%doc README.* NEWS

%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- 0.41.0.rc1

* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- first build for Sisyphus
