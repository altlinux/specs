Name:    ioping
Version: 1.3
Release: alt1
Summary: simple disk I/O latency monitoring tool

Group:    File tools
License:  %gpl3plus
Url:      https://github.com/koct9i/ioping
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%prep
%setup
%patch0 -p1

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/LICENSE) LICENSE

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
%make_install install PREFIX=%prefix DESTDIR=%buildroot

%files
%doc README.md changelog
%doc --no-dereference LICENSE

#%%attr(755,root,root) %_bindir/%name
#%%attr(644,root,root) %_man1dir/%{name}*
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Wed Feb 18 2026 Nikolay A. Fetisov <naf@altlinux.org> 1.3-alt1
- New version

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
