%define plugin gtodo

Name: gkrellm-%plugin
Version: 0.2.4
Release: alt1

Summary: GKrellM gtodo plugin
License: GPL
Group: Monitoring
Url: http://voidtrance.home.comcast.net/
Source: http://voidtrance.home.comcast.net/software/files/gtodo/%name-%version.tar.gz

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Tue Dec 16 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
This GKrellM plugin allows the user to define
track and organize tasks and to-do items. 

%prep
%setup -q -n %name

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
%__mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 GLOBAL_INSTALL_PATH=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc BUGS CREDITS ChangeLog README TODO
%_libdir/gkrellm2/plugins/*.so


%changelog
* Tue Dec 16 2003 Alex Murygin <murygin@altlinux.ru> 0.2.4-alt1
- new version
- Merged upstream patches
  + gkrellm-gtodo-0.2.3-alt-i18n.patch
  + gkrellm-gtodo-0.2.3-alt-ru.patch
  + gkrellm-gtodo-0.2.3-alt-install.patch

* Mon Dec 01 2003 Alex Murygin <murygin@altlinux.ru> 0.2.3-alt1
- Built for ALTLinux

