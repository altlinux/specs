%define photos_dir %_datadir/wallpapers
%define rname nordnature

Name: wallpapers-%rname
Version: 1
Release: alt1.2

Summary: Photo wallpapers from Russian Nord.
Summary(ru_RU.KOI8-R): Фото для фонов с Русского Севера
License: GPL
Group: Graphics
Url: http://memdoc.newmail.ru
Packager: Anatoly Yakushin <jaa@altlinux.ru>

Buildarch: noarch

Source: wallpapers-%rname-%version.tar.bz2

%description
Packaged as jpeg 

%description -l ru_RU.KOI8-R
Сжат как JPEG 

%prep
%setup -q

%build

%install
%__mkdir_p %buildroot/%photos_dir/%rname
%__install -m 0644 *.jpg %buildroot/%photos_dir/%rname


%files
%photos_dir/*
%doc README COPYING

%changelog
* Sun Nov 25 2007 Anatoly Yakushin <jaa@altlinux.ru> 1-alt1.2
- removed package intersection 

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1-alt1.1
- move to %%_datadir/wallpapers

* Mon Aug 25 2003 Anatoly Yakushin <jaa@altlinux.ru> 1-alt1
- add new pictures. Photo_dir path fix. 

* Sat Mar 8 2003 Anatoly Yakushin <jaa@altlinux.ru> 0.1-alt0.1
- build for ALT Linux

