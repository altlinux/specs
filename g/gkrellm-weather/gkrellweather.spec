%define sourcename gkrellweather
%define plugin weather

Name: gkrellm-%plugin
Version: 2.0.8
Release: alt3

Summary: GKrellM weather plugin
Summary(ru_RU.UTF-8): Плагин GKrellM для отображения погоды
License: GPL-2.0-or-later
Group: Monitoring
Url: https://sites.google.com/site/makovick/gkrellm-plugins
Source0: %name-%version.tar

Patch0: %sourcename-alt-install.patch
Patch1: %sourcename-alt-fix_url.patch
Patch2: %sourcename-2.0.8-alt-fix-GrabWeather.patch

Provides: %sourcename = %version
Obsoletes: %sourcename < %version

Requires: wget gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin grab weather for your location from NOAA server and display
it.

Location should be set as METAR code.

%description -l ru_RU.UTF-8
Этот GKrellM плагин скачивает информацию о погоде для указанного места с
сервера NOAA и отображает ее.

Местоположение должно быть представлено в виде METAR кода.

%prep
%setup
%autopatch -p1
subst 's|^CFLAGS =.*|\0 %optflags|' Makefile

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale PREFIX=%_prefix

%install
mkdir -p %buildroot%_bindir
install -D -m755 GrabWeather %buildroot%_bindir/
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc COPYING ChangeLog README
%_libdir/gkrellm2/plugins/gkrell%plugin.so
%_bindir/GrabWeather

%changelog
* Tue Jan 27 2026 L.A. Kostis <lakostis@altlinux.ru> 2.0.8-alt3
- Update description.
- Use SPDX tag for license.
- Get rid of ugly GrabWeather patches.

* Wed Mar 01 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.0.8-alt2
- fixed plugin initialization (ALT #33160)

* Wed Mar 01 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.0.8-alt1
- new version - 2.0.8

* Wed Mar 01 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.0.6-alt2
- spec cleanup
- added patch to update the URL source of weather

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 2.0.6-alt1
- renamed to gkrellm-{NAME}
- new version
- removed internationalisation patches (merged to upstream)
- rediffed patches
- added russian summary, description

* Wed Apr 02 2003 Alex Murygin <murygin@altlinux.ru> 2.0.5-alt4
- removed GrabWeather from requires

* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 2.0.5-alt3
- GrabWeather conflicts with wmWeather (move to /usr/lib/gkrellm2/)

* Fri Mar 28 2003 Alex Murygin <murygin@altlinux.ru> 2.0.5-alt2
- Added i18n support
- Added Russian translation
- Fix 2436 bug (GrabWeather path)

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 2.0.5-alt1
- Built for ALTLinux
