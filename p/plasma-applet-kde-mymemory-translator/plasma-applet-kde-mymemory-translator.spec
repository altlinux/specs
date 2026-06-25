%define _unpackaged_files_terminate_build 1
%define nameL Kde.mymemory.translator
%define nameLC plasma_applet_Kde.mymemory.translator

Name: plasma-applet-kde-mymemory-translator
Version: 0.8
Release: alt2

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
#removed broken file
rm -v translate/hi.po

%build
%install
mkdir -p %buildroot%_datadir/plasma/plasmoids/%nameL
mv %nameL %buildroot%_datadir/plasma/plasmoids/

for locale in translate/*.po; do
 dirname=$(basename "$locale" .po)
 msgfmt translate/${dirname}.po -o translate/${dirname}.mo
 install -Dm 0644 translate/${dirname}.mo %buildroot%_datadir/locale/$dirname/LC_MESSAGES/%nameLC.mo
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_datadir/plasma/plasmoids/%nameL/*
%_datadir/locale/*/LC_MESSAGES/%nameLC.mo

%changelog
* Thu Jun 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8-alt2
- fixed FTBFS

* Thu Feb 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8-alt1
- 0.7.5.3 -> 0.8

* Wed Oct 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.5.3-alt1
- 0.7.5.2 -> 0.7.5.3

* Tue Sep 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.5.2-alt1
- 0.7.5.1 -> 0.7.5.2

* Mon Sep 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.5.1-alt1
- 0.6.9 -> 0.7.5.1

* Mon Aug 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt5
- new locale added

* Wed Aug 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.9-alt4
- new locale added

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
