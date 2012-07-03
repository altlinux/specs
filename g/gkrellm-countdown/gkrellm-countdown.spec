%define shortname countdown

Name: gkrellm-%shortname
Version: 0.1.2
Release: alt1

Summary: GKrellM plugin which provides a simple countdown clock
License: GPL
Group: Monitoring
Url: http://oss.pugsplace.net/

Source: %name-%version.tar.gz

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig

%description
GKrellM Countdown Plugin is a simple plugin for GKrellM 2.x that counts
down to a date and time with one-second accuracy. The target date and
time are easily set using GTK 2 calendar widgets. It can optionally
scroll the time.

%prep
%setup -q -n %name
%__subst 's|^FLAGS =.*|\0 %optflags|' Makefile

%build
%make_build

%install
%__mkdir -p %buildroot%_libdir/gkrellm2/plugins
%makeinstall DESTDIR=%buildroot PLUGIN_DIR=%_libdir/gkrellm2/plugins/

%files
%doc README ChangeLog
%_libdir/gkrellm2/plugins/*.so

%changelog
* Wed Apr 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.2-alt1
- 0.1.2
- update Url:

* Mon Oct 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.1-alt2
- use optflags when building

* Sat Sep 03 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.1-alt1
- initial build
