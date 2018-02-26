%define plugin reminder

Name: gkrellm-%plugin
Version: 2.0.0
Release: alt2

Summary: GKrellM reminder plugin
License: GPL
Group: Monitoring
Url: http://web.wt.net/~billw/gkrellm/Plugins/
Source: http://web.wt.net/~billw/gkrellm/Plugins//%name-%version.tar.gz

Patch0: gkrellm-reminder-2.0.0-alt-i18n.patch.gz
Patch1: gkrellm-reminder-2.0.0-alt-ru.patch.gz
Patch2: gkrellm-reminder-2.0.0-alt-install.patch.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin lets you set multiple reminders.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc COPYING ChangeLog INSTALL README
%_libdir/gkrellm2/plugins/%plugin.so

%changelog
* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt2
- Added russian translation
- Added i18n support

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 2.0.0-alt1
- Built for ALTLinux
