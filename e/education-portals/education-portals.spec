Name: education-portals
Version: 0.02
Release: alt2
Summary: Links to various Russian educations portals
Summary(ru_RU.UTF-8): Ссылки на российские образовательные порталы для школьников
License: GPLv3
Group: Education
URL: http://www.altlinux.org
Packager: Alexei Mezin <alexvm@altlinux.org>
Vendor: ALT Linux Team

Source: %name-%version.tar.gz

Requires: filesystem icon-theme-hicolor altlinux-freedesktop-menu-common
BuildArch: noarch

%description
System menu entries with links to Russian Educational Portals for schoolkids.

%description -l ru_RU.UTF-8
Ссылки на российские Образовательные Порталы для школьников в системное меню. Можно использовать для
удобного добавления ярлыков со ссылками на рабочий стол.

%prep
%setup

%build

%install
# menu entry
install -D -m0644 altlinux-education-webportals.menu  %buildroot/%_sysconfdir/xdg/menus/applications-merged/altlinux-education-webportals.menu
install -D -m0644 altlinux-education-webportals.directory %buildroot/%_datadir/desktop-directories/altlinux-education-webportals.directory
install -D -m0644 education-webportals_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/education-webportals.png
install -D -m0644 education-webportals_48x48.png %buildroot/%_liconsdir/education-webportals.png


# www.childrenscience.ru
install -D -m0644 childrenscience.desktop %buildroot/%_desktopdir/childrenscience.desktop
install -D -m0644 childrenscience_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/childrenscience.png
install -D -m0644 childrenscience_48x48.png %buildroot/%_liconsdir/childrenscience.png

# www.interneturok.ru
install -D -m0644 interneturok.desktop %buildroot/%_desktopdir/interneturok.desktop
install -D -m0644 interneturok_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/interneturok.png
install -D -m0644 interneturok_48x48.png %buildroot/%_liconsdir/interneturok.png

# www.iqsha.ru
install -D -m0644 iqsha.desktop %buildroot/%_desktopdir/iqsha.desktop
install -D -m0644 iqsha_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/iqsha.png
install -D -m0644 iqsha_48x48.png %buildroot/%_liconsdir/iqsha.png

# www.uchi.ru
install -D -m0644 uchiru.desktop %buildroot/%_desktopdir/uchiru.desktop
install -D -m0644 uchiru_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/uchiru.png
install -D -m0644 uchiru_48x48.png %buildroot/%_liconsdir/uchiru.png

# www.yaklass.ru
install -D -m0644 yaklass.desktop %buildroot/%_desktopdir/yaklass.desktop
install -D -m0644 yaklass_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/yaklass.png
install -D -m0644 yaklass_48x48.png %buildroot/%_liconsdir/yaklass.png

# education.yandex.ru
install -D -m0644 yandex-education.desktop %buildroot/%_desktopdir/yandex-education.desktop
install -D -m0644 yandex-education_96x96.png %buildroot/%_iconsdir/hicolor/96x96/apps/yandex-education.png
install -D -m0644 yandex-education_48x48.png %buildroot/%_liconsdir/yandex-education.png

# school.mos.ru
install -D -m0644 mesh.desktop %buildroot/%_desktopdir/mesh.desktop
install -D -m0644 mesh_256x256.png %buildroot/%_iconsdir/hicolor/256x256/apps/mesh.png
install -D -m0644 mesh.svg %buildroot/%_iconsdir/hicolor/scalable/apps/mesh.svg
install -D -m0644 mesh_48x48.png %buildroot/%_liconsdir/mesh.png



%files
%_sysconfdir/xdg/menus/applications-merged/*
%_iconsdir/hicolor/*/apps/*
%_datadir/desktop-directories/*
%_desktopdir/*

%changelog
* Sun Dec 05 2021 Alexei Mezin <alexvm@altlinux.org> 0.02-alt2
- Minor spec fixes

* Sun Dec 05 2021 Alexei Mezin <alexvm@altlinux.org> 0.02-alt1
- Initial build for Sisyphus
- Add school.mos.ru portal
- Fix icons

* Fri Dec 06 2019 Alexei Mezin <alexei@nanoscantech.com> 0.01-alt1
- Initial build.


