%global _unpackaged_files_terminate_build 1
%global theme_name kanagawa
%global original_theme_name Kanagawa
%global theme_dirs Kanagawa*

Name: gtk-theme-%theme_name
Version: 20251023
Release: alt1
Summary: A GTK theme with the Kanagawa colour palette
License: GPL-3.0
Group: Graphical desktop/GNOME
URL: https://www.opendesktop.org/p/1810560
VCS: https://github.com/Fausto-Korpsvart/Kanagawa-GKT-Theme

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: sassc

Requires: gtk3-theme-%theme_name = %EVR
Requires: gtk4-theme-%theme_name = %EVR
Requires: icon-theme-%theme_name = %EVR

%description
Kanagawa is a GTK theme based on the Kanagawa colour scheme for Neovim.
This package contains its GTK3, GTK4, GNOME Shell, and icon-theme variants.

%package common
Summary: Common files for the %original_theme_name theme
Group: Graphical desktop/GNOME

%description common
Common files for the %original_theme_name theme.

%package -n gtk3-theme-%theme_name
Summary: %original_theme_name GTK3 and GNOME Shell theme
Group: Graphical desktop/GNOME
Requires: %name-common

%description -n gtk3-theme-%theme_name
%original_theme_name theme files for GTK3 and GNOME Shell.

%package -n gtk4-theme-%theme_name
Summary: %original_theme_name GTK4 theme
Group: Graphical desktop/GNOME
Requires: %name-common

%description -n gtk4-theme-%theme_name
%original_theme_name theme files for GTK4.

%package -n icon-theme-%theme_name
Summary: %original_theme_name icon theme
Group: Graphical desktop/GNOME
Requires: icon-theme-hicolor

%description -n icon-theme-%theme_name
%original_theme_name icon theme.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/themes %buildroot%_iconsdir
( cd themes
  ./install.sh --theme all --dest %buildroot%_datadir/themes
)
rm -rf %buildroot%_datadir/themes/%theme_dirs-hdpi
rm -rf %buildroot%_datadir/themes/%theme_dirs-xhdpi
for theme_dir in %buildroot%_datadir/themes/%theme_dirs; do
  rm -rf "$theme_dir/cinnamon" "$theme_dir/gtk-2.0" "$theme_dir/metacity-1" \
    "$theme_dir/plank" "$theme_dir/xfwm4"
done
cp -a icons/%original_theme_name %buildroot%_iconsdir

%files common
%dir %_datadir/themes/%theme_dirs
%_datadir/themes/%theme_dirs/index.theme

%files -n gtk3-theme-%theme_name
%_datadir/themes/%theme_dirs/gtk-3.0
%_datadir/themes/%theme_dirs/gnome-shell

%files -n gtk4-theme-%theme_name
%_datadir/themes/%theme_dirs/gtk-4.0

%files -n icon-theme-%theme_name
%_iconsdir/%original_theme_name

%changelog
* Mon Aug 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 20251023-alt1
- Initial build for ALT.
