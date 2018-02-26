%define real_name oxygen-molecule
%define gtk2_prefix gtk2-theme

Name: %gtk2_prefix-%real_name
Version: 3.2
Release: alt1

Group: Graphical desktop/GNOME
Summary: Oxygen-Molecule GTK2 theme
Summary(ru_RU.UTF8): Тема Oxygen-Molecule для GTK2
URL: http://kde-look.org/content/show.php?content=103741
License: GPLv3

Requires: libgtk+2-common

BuildArch: noarch
Source0: %{gtk2_prefix}-%{real_name}-%{version}.tar.bz2

%description
This is GTK2 port of default KDE4 Oxygen style.

%description -l ru_RU.UTF8
Данная тема представляет собой порт на GTK2 стандартного
стиля графических элементов KDE4 - Oxygen.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/themes/%real_name
cp -r gtk-2.0 %buildroot/%_datadir/themes/%real_name/

%files
%_datadir/themes/%real_name

%changelog
* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 3.2-alt1
- initial build
