%define sourcename gkrellm_timers
%define plugin timers

Name: gkrellm-%plugin
Version: 1.2
Release: alt3

Summary: GKrellM timers plugin
Summary(ru_RU.CP1251): ѕлагин timers дл€ GKrellM
License: GPL
Group: Monitoring
Url: http://triq.net/%sourcename.html
Source: http://triq.net/%sourcename/%sourcename-%version.tar.gz

Patch0: %sourcename-1.2-alt-i18n.patch.gz
Patch1: %sourcename-1.2-alt-ru.patch.gz

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin lets you set multiple count down timers or stopwatches.
Commands can be executed when count down timers expire.

%description -l ru_RU.CP1251
Ётот GKrellM плагин позвол€ет устанавливать несколько счетчиков и секундомеров.
ћогут быть запущены команды при истечении времени.

%prep
%setup -q -n %sourcename-%version
%patch0 -p1
%patch1 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc ChangeLog README TODO
%_libdir/gkrellm2/plugins/gkrellm_%plugin.so

%changelog
* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 1.2-alt3
- renamed to gkrellm-{NAME}
- added russian summary, description

* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 1.2-alt2
- Added russian translation
- Added i18n support

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 1.2-alt1
- Built for ALTLinux
