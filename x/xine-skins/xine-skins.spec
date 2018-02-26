Name: xine-skins
Version: 1.0.2
Release: alt4

Summary: Xine skins
License: GPL
Group: Sound
Url: http://www.altlinux.ru/
BuildArchitectures: noarch

Source: %name.tar.bz2
Requires: xine-ui

Prefix: %prefix

%description
Skins for xine. Install this package; at next startup, xine will see all the
skins.

%description -l ru_RU.KOI8-R
Шкурки для xine. Устанавливаем пакет и при следующем запуске xine в настройках
будут доступны новые шкурки cosmic-*.

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/xine

bzcat %SOURCE0 |tar xf - -C $RPM_BUILD_ROOT%_datadir/xine

%files
%_datadir/xine/skins

%changelog
* Wed Mar 30 2005 Ilya A Krawez <sadist at altlinux dot ru> 1.0.2-alt4
- Update skins for new version

* Tue May 20 2003 Ilya A Krawez <sadist at altlinux dot ru> 1.0.1-alt2
- Contarst

* Wed Apr 23 2003 Ilya A Krawez <sadist at altlinux dot ru> 1.0.0-alt1
- First build for ALT 

