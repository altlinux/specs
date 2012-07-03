%define sourcename gkrellaclock
%define plugin aclock

Name: gkrellm-%plugin
Version: 0.3.2
Release: alt3

Summary: GKrellM aclock plugin
Summary(ru_RU.CP1251): Аналоговые часы для GKrellM 
License: GPL
Group: Monitoring
Url: http://www.geocities.com/m_muthukumar/gkrellaclock.html
Source: http://www.geocities.com/m_muthukumar/%sourcename-%version.tar.gz

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Patch0: gkrellaclock-0.3.2-alt-i18n.patch.gz
Patch1: gkrellaclock-0.3.2-alt-ru.patch.gz
Patch2: gkrellaclock-0.3.2-alt-install.patch.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin displays analog clock. 

%description -l ru_RU.CP1251
Плагин GKrellM отображающий аналоговые часы.

%prep
%setup -q -n gkrellAclock-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc ChangeLog README
%_libdir/gkrellm2/plugins/gkrell%plugin.so

%changelog
* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 0.3.2-alt3
- renamed to gkrellm-{NAME}
- added russian summary, description

* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 0.3.2-alt2
- Added russian translation
- Added i18n support

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 0.3.2-alt1
- Built for ALTLinux
