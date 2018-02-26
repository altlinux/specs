%define sourcename gkrellweather
%define plugin weather

Name: gkrellm-%plugin
Version: 2.0.6
Release: alt1

Summary: GKrellM weather plugin
Summary(ru_RU.CP1251): Плагин GKrellM для отображения погоды
License: GPL
Group: Monitoring
Url: http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/index.html
Source: http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/%sourcename-%version.tgz

Patch0: %sourcename-2.0.6-alt-install.patch.gz

Provides: %sourcename = %version
Obsoletes: %sourcename < %version

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin grab weather for your location from server and display it.

%description -l ru_RU.CP1251
Этот GKrellM плагин скачивает информацию о погоде для указанного места.
с сервера и отображает ее.

%prep
%setup -q -n %sourcename-%version
%patch0 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins

install -D -m755 GrabWeather %buildroot%_libdir/gkrellm2/GrabWeather
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc COPYING ChangeLog README
%_libdir/gkrellm2/plugins/gkrell%plugin.so
%_libdir/gkrellm2/GrabWeather

%changelog
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
