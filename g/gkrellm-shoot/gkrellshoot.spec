%define sourcename gkrellshoot
%define plugin shoot

Name: gkrellm-%plugin
Version: 0.4.4
Release: alt1

Summary: GKrellM shoot plugin
Summary(ru_RU.CP1251): Плагин shoot для GKrellM
License: GPL
Group: Monitoring
Url: http://%sourcename.sourceforge.net/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: http://umn.dl.sourceforge.net/sourceforge/%sourcename/%sourcename-%version.tar.gz

Patch0: %sourcename-0.4.4-alt-i18n.patch
Patch1: %sourcename-0.4.1-alt-ru.patch
Patch2: %sourcename-0.4.1-alt-install.patch

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Requires: gkrellm >= 2.0

BuildPreReq: gkrellm-devel

%description
This GKrellM plugin gives you convenient one button access to initiating a
screen lock (screensaver) and screen shots. It also has charts with various
nice screensaver style animations.

%description -l ru_RU.CP1251
Этот GKrellM плагин позволяет удобно запирать экран и делать снимки
экрана с помощью одной кнопки. В нем также есть чарт с различными красивыми
анимациями.

%prep
%setup -q -n gkrellShoot-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build enable_nls=1  LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins

%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc ChangeLog README
%_libdir/gkrellm2/plugins/gkrell%plugin.so

%changelog
* Sat Sep 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 0.4.1-alt3
- renamed to gkrellm-{NAME}
- added russian summary, description

* Sat Mar 29 2003 Alex Murygin <murygin@altlinux.ru> 0.4.1-alt2
- Added i18n support
- Added russian translation

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 0.4.1-alt1
- Built for ALTLinux
