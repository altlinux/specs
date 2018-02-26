%define sourcename gkrellmlaunch
%define plugin launch

Name: gkrellm-%plugin
Version: 0.5
Release: alt3

Summary: GKrellM launch plugin
Summary(ru_RU.CP1251): Плагин launch для GKrellM
License: GPL
Group: Monitoring
Url: http://gkrellmlaunch.sourceforge.net/
Source: http://umn.dl.sourceforge.net/sourceforge/gkrellmlaunch/%sourcename-%version.tar.gz

Patch0: gkrellmlaunch-0.5-alt-i18n.patch.gz
Patch1: gkrellmlaunch-0.5-alt-ru.patch.gz
Patch2: gkrellmlaunch-0.5-alt-install.patch.gz

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin gives you some buttons you can configure to launch 
some of your frequently used apps.

%description -l ru_RU.CP1251
Этот GKrellM плагин позволяет создавать кнопки запуска любимых приложений.

%prep
%setup -q -n %sourcename-%version
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
%doc COPYING CHANGELOG LICENSE README updateconfig.sh
%_libdir/gkrellm2/plugins/gkrellm%plugin.so

%changelog
* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 0.5-alt3
- renamed to gkrellm-{NAME}
- added russian summary, description

* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 0.5-alt2
- Added russian translation
- Added i18n support

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 0.5-alt1
- Built for ALTLinux
