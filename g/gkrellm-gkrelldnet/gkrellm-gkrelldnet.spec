%define shortname gkrelldnet

Name: gkrellm-%shortname
Version: 0.14.2
Release: alt1.1

Summary: GKrellM monitor for Distributed.net client
License: GPL
Group: Monitoring
Url: http://gkrelldnet.sourceforge.net/

Source: %shortname-%version.tar.gz
Patch: gkrelldnet-0.14.2-alt-gcc4.7.patch

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig

%description
gkrelldnet is a monitoring system for Distributed.net client.
This plugin features (see also 'Info' in plugin config.)
  - monitor input/output work units
  - monitor current contest
  - monitor the crunch-o-meter (support both relative and absolute style)
  - start/stop the dnet client on left/right mouse button click
  - user configurable text output
  - user configurable command to start on every packet completion
      (like playing a sound)

%prep
%setup -n %shortname
%patch -p2
subst 's|^CFLAGS =.*|\0 %optflags|' Makefile

%build
%make

%install
mkdir -p %buildroot{%_bindir,%_libdir/gkrellm2/plugins}
install -m644 *.so %buildroot%_libdir/gkrellm2/plugins
install -m755 dnetw %buildroot%_bindir/

%files
%doc README TODO FAQ ChangeLog
%_libdir/gkrellm2/plugins/*.so
%_bindir/*

%changelog
* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.1
- Fixed build with gcc 4.7

* Mon Oct 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.2-alt1
- initial build

