%define shortname timestamp

Name: gkrellm-%shortname
Version: 0.1.4
Release: alt2

Summary: GKrellM plugin which displays current UNIX timestamp
License: GPL
Group: Monitoring
Url: http://freshmeat.net/redir/timestamp/44588/url_homepage/gkrellm-timestamp

Source: %name-%version.tar.bz2

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig

%description
GkrellM Timestamp is a GkrellM plugin that shows the current UNIX
timestamp like the default clock.

%prep
%setup -q
%__subst 's|^CFLAGS =.*|\0 %optflags|' Makefile

%build
%make_build

%install
%makeinstall PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins/

%files
%_libdir/gkrellm2/plugins/*.so

%changelog
* Mon Oct 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.4-alt2
- use optflags when building

* Sat Sep 03 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.4-alt1
- initial build
