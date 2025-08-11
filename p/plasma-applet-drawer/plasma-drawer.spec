%define nameL p-connor.plasma-drawer
%define nameLC plasma_applet_%nameL

Name: plasma-applet-drawer
Version: 2.0.1
Release: alt1

Summary: A customizable fullscreen launcher widget for KDE Plasma
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Url: https://github.com/p-connor/plasma-drawer
Vcs: https://github.com/p-connor/plasma-drawer

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: kf5-kcoreaddons-devel

%description
A fullscreen customizable launcher with application directories and krunner-like search for KDE Plasma.

%prep
%setup
/usr/lib/kf5/bin/desktoptojson -i metadata.desktop -o metadata.json
mv contents/locale %_builddir/%name-%version/

%build
%install
install -d %buildroot%_datadir/plasma/plasmoids/%nameL
cp -p -r contents %buildroot%_datadir/plasma/plasmoids/%nameL/
cp -a *.json *.md %buildroot%_datadir/plasma/plasmoids/%nameL/
for locale in de ro ru uk; do
  install -Dm 0644 locale/${locale}/LC_MESSAGES/%nameLC.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_datadir/plasma/plasmoids/%nameL
%doc README.md

%changelog
* Mon Aug 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux.
