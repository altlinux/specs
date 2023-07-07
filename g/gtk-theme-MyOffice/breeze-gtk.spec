Name: gtk-theme-MyOffice
Version: 5.24.5
Release: alt1
%K5init no_altplace

Group: Graphical desktop/MATE
Summary: Breeze GTK2/3 theme (version for MyOffice Plus)
Url: http://www.kde.org
License: GPL-2.0-or-later

%define rname breeze-gtk
Source: %rname-%version.tar
Source1: index.theme

BuildArch: noarch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: gtk-engines-pixmap libgtk+3-devel pkg-config
BuildRequires: /usr/bin/sassc python3-module-pycairo plasma5-breeze plasma5-breeze-devel

%description
This is GTK2/3 port of default KDE Breeze style (version for MyOffice Plus).

%prep
%setup -n %rname-%version
subst 's/Breeze-Dark/MyOffice-Dark/' src/gtk-dark-3.0.css

%build
%K5build -DWITH_GTK3_VERSION=`pkg-config --modversion gtk+-3.0`

%install
%K5install
%K5install_move data kconf_update
mv %buildroot%_datadir/themes/Breeze %buildroot%_datadir/themes/MyOffice
mv %buildroot%_datadir/themes/Breeze-Dark %buildroot%_datadir/themes/MyOffice-Dark
install -Dpm 0644 %SOURCE1 %buildroot%_datadir/themes/MyOffice/index.theme

%files
%_datadir/themes/MyOffice
%_datadir/themes/MyOffice-Dark

%changelog
* Fri Jul 07 2023 Andrey Cherepanov <cas@altlinux.org> 5.24.5-alt1
- New theme MyOffice based on Breeze.
