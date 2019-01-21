%define theme_name Equilux
%define descr \
The Equilux Theme provides a couple of full-dark, neutral-gray theme for \
GNOME/GTK+ based desktop environments. It supports GTK+ 3, GTK+ 2, GNOME Shell, \
Budgie, MATE, Unity, LightDM, GDM, Chrome theme, etc. \
\
It is based on the Materia Theme.

Name:     gtk-theme-equilux
Version:  20181029
Release:  alt1

Summary:  A Material Design-like theme for GNOME/GTK+ based desktop environments.

License:  GPLv2
Group:    Graphical desktop/GNOME
Url:      https://github.com/ddnexus/equilux-theme

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

Requires: gtk2-theme-equilux
Requires: gtk3-theme-equilux
Requires: metacity-theme-equilux
Requires: xfwm4-theme-equilux
Requires: cinnamon-theme-equilux

BuildArch: noarch

%description
%descr

%package common
Summary: Common files for %theme_name GTK+ themes
Group: Graphical desktop/GNOME

%description common
%descr

Common files for %theme_name GTK+ themes.

%package -n gtk2-theme-equilux
Summary: %theme_name GTK+2 theme
Group: Graphical desktop/GNOME
Requires: %name-common = %EVR

%description -n gtk2-theme-equilux
%descr

Theme for GTK+2 as part of the %theme_name theme.

%package -n gtk3-theme-equilux
Summary: %theme_name GTK+3 theme
Group: Graphical desktop/GNOME
Requires: %name-common = %EVR

%description -n gtk3-theme-equilux
%descr

Theme for GTK+3 as part of the %theme_name theme.

%package -n metacity-theme-equilux
Summary: %theme_name Metacity themes
Group: Graphical desktop/GNOME
Requires: %name-common = %EVR

%description -n metacity-theme-equilux
%descr

Theme for Metacity as part of the %theme_name theme.

%package -n xfwm4-theme-equilux
Summary: %theme_name Xfwm4 theme
Group: Graphical desktop/XFce
Requires: %name-common = %EVR

%description -n xfwm4-theme-equilux
%descr

Theme for Xfwm4 as part of the %theme_name theme.

%package -n cinnamon-theme-equilux
Summary: %theme_name Cinnamon theme
Group: Graphical desktop/GNOME
Requires: %name-common = %EVR

%description -n cinnamon-theme-equilux
%descr

Theme for Cinnamon as part of the %theme_name theme.

%prep
%setup

%install
mkdir -p "%buildroot/usr/share/themes"
./install.sh -d "%buildroot/usr/share/themes"
rm -rf %buildroot/usr/share/themes/%theme_name/unity \
%buildroot/usr/share/themes/%theme_name-compact/unity

%files

%files common
%doc README.md COPYING
%dir %_datadir/themes/%theme_name/
%_datadir/themes/%theme_name/index.theme
%_datadir/themes/%theme_name-compact/index.theme

%files -n gtk2-theme-equilux
%_datadir/themes/%theme_name/gtk-2.0
%_datadir/themes/%theme_name-compact/gtk-2.0

%files -n gtk3-theme-equilux
%_datadir/themes/%theme_name/gtk-3.0
%_datadir/themes/%theme_name-compact/gtk-3.0
%_datadir/themes/%theme_name/gnome-shell
%_datadir/themes/%theme_name-compact/gnome-shell
%_datadir/themes/%theme_name/gtk-assets
%_datadir/themes/%theme_name-compact/gtk-assets

%files -n metacity-theme-equilux
%_datadir/themes/%theme_name/metacity-1
%_datadir/themes/%theme_name-compact/metacity-1

%files -n xfwm4-theme-equilux
%_datadir/themes/%theme_name/xfwm4
%_datadir/themes/%theme_name-compact/xfwm4

%files -n cinnamon-theme-equilux
%_datadir/themes/%theme_name/cinnamon
%_datadir/themes/%theme_name-compact/cinnamon

%changelog
* Fri Jan 18 2019 Grigory Ustinov <grenka@altlinux.org> 20181029-alt1
- Initial build for Sisyphus
