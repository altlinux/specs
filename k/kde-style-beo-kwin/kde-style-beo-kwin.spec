%define theme beo

Name: kde-style-%theme-kwin
Version: 0.1
Release: alt2

Summary: Beo theme for deKorator
License: GPL
Group: Graphical desktop/KDE
Url: http://www.kde-look.org/content/show.php/Oxygen+for+deKorator?content=81358

Packager: Konstantin Baev <kipruss@altlinux.org>

Requires: dekorator

BuildArch: noarch

Source: http://aerolinux.free.fr/Beo/%theme-theme.tar.bz2

%description
Beo theme for deKorator
A clean and dark theme based on deKorator and Domino

%prep
%setup -q -n %theme-theme

%install
mkdir -p %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
cp -r * %buildroot/%_datadir/apps/deKorator/themes/%theme-theme
find %buildroot/%_datadir/apps/deKorator/themes/%theme-theme -type f | xargs chmod 644

%files
%_datadir/apps/deKorator/themes/%theme-theme

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- removed set_strip_method macro

* Wed Aug 13 2008 Konstantin Baev <kipruss@altlinux.org> 0.1-alt1
- initial build for Sisyphus

