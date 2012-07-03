Name: ioping
Version: 0.3
Release: alt1
Summary: simple disk I/O latency monitoring tool

Group: File tools
License: GPLv3+
Url: http://code.google.com/p/ioping
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: ioping-%version.tar
Patch: %name.patch

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%prep
%setup
%patch -p2

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
%make_install install PREFIX=%prefix DESTDIR=%buildroot

%files
%attr(755,root,root) %_bindir/ioping
%attr(644,root,root) %_man1dir/ioping.1.*

%changelog
* Tue Jun 07 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- converted from Fedora by srpmconvert script
