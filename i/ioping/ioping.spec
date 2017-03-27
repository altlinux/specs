Name: ioping
Version: 1.0
Release: alt1
Summary: simple disk I/O latency monitoring tool

Group: File tools
License: GPLv3+
Url: https://github.com/koct9i/ioping
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: ioping-%version.tar
Patch: %name-%version-%release.patch

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%prep
%setup
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
%make_install install PREFIX=%prefix DESTDIR=%buildroot

%files
%attr(755,root,root) %_bindir/ioping
%attr(644,root,root) %_man1dir/ioping.1.*

%changelog
* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- 1.0

* Mon Sep 14 2015 Denis Smirnov <mithraen@altlinux.ru> 0.9-alt2
- fix .gear/tags/list

* Tue Sep 08 2015 Denis Smirnov <mithraen@altlinux.ru> 0.9-alt1
- 0.9

* Tue Jan 07 2014 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- 0.8

* Tue Jun 07 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- converted from Fedora by srpmconvert script
