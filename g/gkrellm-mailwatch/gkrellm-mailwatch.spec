%define plugin mailwatch

Name: gkrellm-%plugin
Version: 2.4.2
Release: alt1

Summary: GKrellM mailwatch plugin
License: GPL
Group: Monitoring
Url: http://gkrellm.luon.net/mailwatch.phtml
Source: http://gkrellm.luon.net/files/%name-%version.tar.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Sun Mar 30 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin has separate displays for multiple mailboxes.

%prep
%setup -q -n %name

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc Changelog README
%_libdir/gkrellm2/plugins/%plugin.so

%changelog
* Sat Jun 28 2003 Alex Murygin <murygin@altlinux.ru> 2.4.2-alt1
- new version

* Sun May 11 2003 Alex Murygin <murygin@altlinux.ru> 2.4.1-alt1
- new version
- removed i18n&russian patch

* Sun Mar 30 2003 Alex Murygin <murygin@altlinux.ru> 2.3.1-alt1
- Added russian translation
- Added i18n support

* Mon Mar 03 2003 Alex Murygin <murygin@altlinux.ru> 2.2.2-alt1
- Built for ALTLinux
