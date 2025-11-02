%define nameKDE org.kde.plasma.catwalk
%define nameLC plasma_applet_org.kde.plasma.catwalk 

Name: plasma-applet-catwalk
Version: 2.4
Release: alt1

Summary: A simple plasmoid showing the total CPU usage
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2137844
Vcs: https://store.kde.org/p/2137844

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%build
rm -r -v %nameKDE/translations
mv %nameKDE/contents/locale %_builddir/%name-%version/locale/

%install
install -d %buildroot%_datadir/plasma/plasmoids
mv %nameKDE %buildroot%_datadir/plasma/plasmoids/

for locale in ru uk_UA; do
 install -Dm 0644 locale/${locale}/LC_MESSAGES/%nameLC.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_datadir/plasma/plasmoids/%nameKDE

%changelog
* Sun Nov 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.4-alt1
- 2.3 -> 2.4

* Tue Jun 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3-alt1
- Initial build for ALT Linux.

