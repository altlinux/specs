%define shortname timestamp

Name: gkrellm-%shortname
Version: 0.1.4
Release: alt2.1

Summary: GKrellM plugin which displays current UNIX timestamp
License: GPL
Group: Monitoring
Url: http://freshmeat.net/redir/timestamp/44588/url_homepage/gkrellm-timestamp

Source: %name-%version.tar.bz2
Patch: gkrellm-timestamp-0.1.4-alt-gcc4.7.patch

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig

%description
GkrellM Timestamp is a GkrellM plugin that shows the current UNIX
timestamp like the default clock.

%prep
%setup
%patch -p2
subst 's|^CFLAGS =.*|\0 %optflags|' Makefile

%build
%make_build

%install
%makeinstall PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins/

%files
%_libdir/gkrellm2/plugins/*.so

%changelog
* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt2.1
- Fixed build with gcc 4.7

* Mon Oct 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.4-alt2
- use optflags when building

* Sat Sep 03 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.4-alt1
- initial build
