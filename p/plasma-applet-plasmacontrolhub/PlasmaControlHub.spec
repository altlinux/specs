%define nameL Plasma.Control.Hub
%define nameLC plasma_applet_%nameL

Name: plasma-applet-plasmacontrolhub
Version: 0.9.9.6
Release: alt1

Summary: Plasma-Control-Hub is a similar macos control center applet
License: GPL-3.0+
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2139890
Vcs: https://store.kde.org/p/2139890

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: gettext-tools

%description
Plasma-Control-Hub is a similar macos control center applet, created
especially for use in plasma. This widget is not a fork of Prayag2's
work, although some of its code was reused. It's still a work in progress,
it may not work.

%prep
%setup

%build
rm -r -v contents/locale

%install
for locale in ar bn de es fr hi it ja ko nl tr zh-cn zh-tw; do
 msgfmt translate/${locale}.po -o translate/${locale}.mo
 install -Dm 0644 translate/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done
install -d %buildroot%_datadir/plasma/plasmoids/%nameL
cp -p -r contents %buildroot%_datadir/plasma/plasmoids/%nameL
cp -a *.json %buildroot%_datadir/plasma/plasmoids/%nameL

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_datadir/plasma/plasmoids/%nameL

%changelog
* Fri Nov 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.9.9.6-alt1
- Initial build for ALT Linux.


