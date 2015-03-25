%define	theme_name Adwaita

Name: metacity-theme-adwaita
Version: 3.14.2.3
Release: alt1

Summary: Metacity theme - Adwaita
License: GPL
Group: Graphical desktop/GNOME
Url: https://git.gnome.org/browse/gnome-themes-standard/
Source: %theme_name.tar
Buildarch: noarch
Conflicts: gnome-themes-standard-data < 3.15

%description
Metacity theme that can be used to fit Adwaita gtk theme
in environments that don\'t support gtk decorations e.g.
Cinnamon and Mate.

%prep
%setup -q -n %theme_name

%install
install -m755 -pd %{buildroot}%_datadir/themes/%theme_name/
cp -ar metacity-1 %{buildroot}%_datadir/themes/%theme_name/

%files
%_datadir/themes/%theme_name/metacity-1

%changelog
* Wed Feb 25 2015 Vladimir Didenko <cow@altlinux.org> 3.14.2.3-alt1
- Initial build
