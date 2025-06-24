%define nameKDE org.kde.plasma.catwalk
%define nameLC plasma_applet_org.kde.plasma.catwalk 

Name: plasma-applet-catwalk
Version: 2.3
Release: alt1

Summary: A simple plasmoid showing the total CPU usage
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2137844
Vcs: https://store.kde.org/p/2137844

Source: %name-%version.tar

Patch0: config-2.3-alt-build.patch
Patch1: ConfigGeneral-2.3-alt-build.patch

BuildArch: noarch

%description
%summary

%prep
%setup
%autopatch -p0

%build
rm -r %nameKDE/translations
mv %nameKDE/contents/locale %_builddir/%name-%version/locale/

for locale in ar ar_DZ; do
 mv locale/${locale}/LC_MESSAGES/.mo locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%install
install -d %buildroot%_datadir/plasma/plasmoids
mv %nameKDE %buildroot%_datadir/plasma/plasmoids/

for locale in ar ar_DZ ru uk_UA; do
 install -Dm 0644 locale/${locale}/LC_MESSAGES/%nameLC.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%files
%_datadir/plasma/plasmoids/%nameKDE
%_datadir/locale/*/LC_MESSAGES/%nameLC.mo

%changelog
* Tue Jun 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3-alt1
- Initial build for ALT Linux.

