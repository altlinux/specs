%define _unpackaged_files_terminate_build 1
%define theme_name otis
%define original_theme_name Otis

Name: gtk-theme-%theme_name
Version: 20250522
Release: alt1

Summary: An elegant dark theme for gnome
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://github.com/EliverLara/otis
Vcs: https://github.com/EliverLara/otis
Source: %name-%version.tar

BuildRequires: sassc

Requires: cinnamon-theme-%theme_name
Requires: gtk2-theme-%theme_name
Requires: gtk3-theme-%theme_name
Requires: gtk4-theme-%theme_name
Requires: metacity-theme-%theme_name
Requires: xfwm4-theme-%theme_name

BuildArch: noarch

%description
%summary.

%package common
Summary: Common files for %original_theme_name theme
Group: Graphical desktop/GNOME

%description common
%summary.

%package -n cinnamon-theme-%theme_name
Summary: %original_theme_name Cinnamon theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n cinnamon-theme-%theme_name
%summary.

%package -n gtk2-theme-%theme_name
Summary: %original_theme_name GTK2 theme
Group: Graphical desktop/GNOME

Requires: %name-common
Requires: gtk2-themes-murrine

%description -n gtk2-theme-%theme_name
%summary.

%package -n gtk3-theme-%theme_name
Summary: %original_theme_name GTK3 theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n gtk3-theme-%theme_name
%summary.

%package -n gtk4-theme-%theme_name
Summary: %original_theme_name GTK4 theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n gtk4-theme-%theme_name
%summary.

%package -n metacity-theme-%theme_name
Summary: %original_theme_name Metacity theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n metacity-theme-%theme_name
%summary.

%package -n xfwm4-theme-%theme_name
Summary: %original_theme_name Xfwm theme
Group: Graphical desktop/XFce

Requires: %name-common

%description -n xfwm4-theme-%theme_name
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/themes/%original_theme_name
cp -r assets index.theme cinnamon gnome-shell gtk-* metacity-1 xfwm4 %buildroot%_datadir/themes/%original_theme_name

%files common
%_datadir/themes/%original_theme_name/index.theme
%_datadir/themes/%original_theme_name/assets
%doc README.md

%files -n cinnamon-theme-%theme_name
%_datadir/themes/%original_theme_name/cinnamon

%files -n gtk2-theme-%theme_name
%_datadir/themes/%original_theme_name/gtk-2.0

%files -n gtk3-theme-%theme_name
%_datadir/themes/%original_theme_name/gnome-shell
%_datadir/themes/%original_theme_name/gtk-3.0

%files -n gtk4-theme-%theme_name
%_datadir/themes/%original_theme_name/gtk-4.0

%files -n metacity-theme-%theme_name
%_datadir/themes/%original_theme_name/metacity-1

%files -n xfwm4-theme-%theme_name
%_datadir/themes/%original_theme_name/xfwm4
%exclude %_datadir/themes/%original_theme_name/xfwm4/render-assets.sh
%exclude %_datadir/themes/%original_theme_name/xfwm4/render_assets.fish

%changelog
* Thu Jul 08 2025 David Sultaniiazov <x1z53@altlinux.org> 20250522-alt1
- Initial build
