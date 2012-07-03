%define photos_dir %_datadir/wallpapers
%define rname lav

Name: wallpapers-lav
Version: 20030331
Release: alt2

Summary: Photos for screen backgrounds
Summary(ru_RU.KOI8-R): Фото для фонов
Summary(uk_UA.KOI8-U): Фото для тла
License: Distributable
Group: Graphics
#Url: 
Packager: Vitaly Lipatov <lav@altlinux.ru>

Buildarch: noarch
Provides: design-backgrounds-lav = %version-%release
Obsoletes: design-backgrounds-lav <= %version-%release
Source: design-backgrounds-%rname-%version.tar

%description
Collection of author's work
Packaged as 1024x768 JPEG

%description -l ru_RU.KOI8-R
Коллекция авторских работ
Сжаты как 1024x768 JPEG

%prep
%setup -q -n design-backgrounds-%rname-%version

%build

%install

%__install -d %buildroot/%photos_dir/%rname
%__install -m 0644 *.jpg %buildroot/%photos_dir/%rname

%files
%photos_dir/*
%doc READ.ME

%changelog
* Fri Oct 19 2007 Vitaly Lipatov <lav@altlinux.ru> 20030331-alt2
- fix filesystem intersection

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 20030331-alt1.1
- move to %%_datadir/wallpapers

* Sun Jan 04 2004 Vitaly Lipatov <lav@altlinux.ru> 20030331-alt1
- rebuild

* Mon Mar 31 2003 Vitaly Lipatov <lav@altlinux.ru> 20030331-alt0.1
- build for Sisyphus (thanks to Michael Shigorin for his spec) 
