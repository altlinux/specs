%def_enable snapshot
%define _name pop
%define __name Pop
%define ver_major 5.5

%def_enable check

Name: %_name-gtk-theme
Version: %ver_major.1
Release: alt1

Summary: A GTK themes for Pop!_OS
License: CC-BY-SA-4.0 and GPL-3.0-or-later and LGPL-2.1-only
Group: Graphical desktop/Other
Url: https://github.com/pop-os/gtk-theme

BuildArch: noarch

Vcs: https://github.com/pop-os/gtk-theme.git

%if_disabled snapshot
Source: https://github.com/pop-os/gtk-theme/archive/v%version/%name-v%version.tar.gz
%else
Source: %name-%version.tar
%endif

Provides: %_name-backgrounds = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson sassc
BuildRequires: pkgconfig(glib-2.0)

%description
%summary

%package -n gtk-themes-%_name
Summary: Pop!_OS GTK themes
Group: Graphical desktop/Other

%description -n gtk-themes-%_name
This package provides GTK+2,3 GTK4 themes for Pop!_OS.

%package -n sound-theme-%_name
Summary: Pop!_OS sound theme
Group: Graphical desktop/Other
Provides: %_name-sound-theme = %EVR

%description -n sound-theme-%_name
This package provides sound theme for Pop!_OS.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -n gtk-themes-%_name -f %name.lang
%_datadir/themes/%__name/
%_datadir/themes/%__name-dark/
%exclude %_datadir/themes/%__name/gnome-shell
%doc README.*

%files -n sound-theme-%_name
%_datadir/sounds/%__name/
%doc README.*

# probably useless gnome-shell theme
%exclude %_datadir/themes/%__name/gnome-shell
%exclude %_datadir/gnome-shell/theme/%__name/
%exclude %_datadir/gnome-shell/theme/%__name-dark/
%exclude %_datadir/gnome-shell/theme/pop*.css

%changelog
* Fri Apr 25 2025 Yuri N. Sedunov <aris@altlinux.org> 5.5.1-alt1
- first build for Sisyphus (v5.5.1-7-g25ea85d9)
