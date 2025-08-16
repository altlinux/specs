%define nameL Kde.mymemory.translator
%define nameLC plasma_applet_Kde.mymemory.translator

Name: plasma-applet-kde-mymemory-translator
Version: 0.6.9
Release: alt3

Summary: Mymemory translator
License: GPL-3.0-or-later
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2272210/
Vcs: https://store.kde.org/p/2272210/

Source0: %name-%version.tar
Source1: ru.po

BuildArch: noarch

BuildRequires: gettext-tools

%description
Simple plasmoid that provides translation using the mymemory translated api

%prep
%setup

rm -r %nameL/metadata.desktop
rm -r %nameL/contents/locale
mv %nameL/translate %_builddir/%name-%version/
cp -r -f %SOURCE1 translate/

#removed strange and unnecessary file
rm -r %nameL/contents/ui/components/GetAPI.qml

%build
%install
mkdir -p %buildroot%_datadir/plasma/plasmoids/%nameL
mv %nameL %buildroot%_datadir/plasma/plasmoids/

for locale in es fr hi it ru ja ko nl pt zh_CN zh_TW; do
 msgfmt translate/${locale}.po -o translate/${locale}.mo
 install -Dm 0644 translate/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_datadir/plasma/plasmoids/%nameL/*
%_datadir/locale/*/LC_MESSAGES/%nameLC.mo

%changelog
* Sat Aug 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt3
- new locale added

* Wed Jul 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt2
- new locales added

* Mon May 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt1
- 0.6.7 -> 0.6.9

* Sun May 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.7-alt1
- Initial build for ALT Linux.
- Created and added russian translate.
- Fixed upstream code for localizations to work.
