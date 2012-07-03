%define sourcename gkrellkam
%define plugin kam

Name: gkrellm-%plugin
Version: 2.0.0
Release: alt3

Summary: GKrellM image watcher plugin
Summary(ru_RU.CP1251): Плагин GKrellM для просмотра изображений
License: GPL
Group: Monitoring
Url: http://gkrellkam.sourceforge.net/
Source: http://umn.dl.sourceforge.net/sourceforge/gkrellkam/%{sourcename}_%version.tar.gz
Patch0: gkrellkam-2.0.0-alt-i18n.patch.gz
Patch1: gkrellkam-2.0.0-alt-ru.patch.gz

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
The idea is that you can have a periodically updated image of whatever you
want, albeit squeezed into a little gkrellm panel. Each panel can watch a
single image, or cycle through a list of images, or run a script and use the
output of the script as the filename of an image. GKrellKam even knows how to
get images out on the internet- this is what allows you to watch webcams.

%description -l ru_RU.CP1251
Отображает картинки с file,http,script,dir источников с задаваемым периодом
обновления в gkrellm панели. Просмотр вебкамер, локальных коллекций изображений.

%prep
%setup -q -n %sourcename-%version
%patch0 -p1
%patch1 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
mkdir -p %buildroot/usr/share/man/man5
%make_install install enable_nls=1 DESTDIR=%buildroot PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files  -f %sourcename.lang
%doc COPYING Changelog INSTALL README Release Todo example.list
%_libdir/gkrellm2/plugins/gkrell%{plugin}2.so
%_man5dir/gkrellkam-list.5*


%changelog
* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt3
- renamed to gkrellm-{NAME}
- added russian summary, description

* Tue Mar 25 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt2
- Added russian translation.
- Added i18n support

* Sun Mar 16 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt1
- First build for Sisyphus.

