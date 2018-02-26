%define photos_dir %_datadir/wallpapers
%define rname mike

Name: wallpapers-mike
Version: 20030214
Release: alt0.2.3

Summary: Photos for screen backgrounds
License: Distributable
Group: Graphics

Source: design-backgrounds-%rname-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Provides: design-backgrounds-mike = %version-%release
Obsoletes: design-backgrounds-mike < %version-%release

Summary(ru_RU.KOI8-R): Фото для фонов
Summary(uk_UA.KOI8-U): Фото для тла

%description
Photos made in 2001 in Kazakhstan
Packaged as 1024x768 and 1600x1200 JPEG

%description -l ru_RU.KOI8-R
Фото сделаны в 2001 г. в Казахстане
Сжаты как 1024x768 и 1600x1200 JPEG

%description -l uk_UA.KOI8-U
Фото зроблен╕ у 2001 р. в Казахстан╕
Пакування: 1024x768 та 1600x1200 JPEG

%prep
%setup -q -n design-backgrounds-%rname-%version

%build

%install
mkdir -p %buildroot/%photos_dir/%rname/{1024x768,1600x1200}
install -m 0644 1024x768/*.jpg %buildroot%photos_dir/%rname/1024x768
install -m 0644 1600x1200/*.jpg %buildroot%photos_dir/%rname/1600x1200

%files
%photos_dir/%rname/
%doc README.ALT

%changelog
* Mon Nov 26 2007 Michael Shigorin <mike@altlinux.org> 20030214-alt0.2.3
- s/Buildarch/BuildArch/
- removed invalid URL
- fixed Obsoletes:
- minor spec cleanup

* Sun Nov 25 2007 Michael Shigorin <mike@altlinux.org> 20030214-alt0.2.2
- don't include %photos_dir/
- spec macro abuse cleanup

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 20030214-alt0.2.1
- move to %%_datadir/wallpapers

* Mon Aug 18 2003 Sergey V Turchin <zerg at altlinux dot org> 20030214-alt0.2
- sync placement of pictures with ALT design

* Fri Feb 14 2003 Michael Shigorin <mike@altlinux.ru> 20030214-alt0.1
- built for ALT Linux

