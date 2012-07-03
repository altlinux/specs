Name: cstream
Version: 2.7.6
Release: alt1

Summary: General-purpose stream-handling tool
License: MIT
Group: File tools
Url: http://www.cons.org/cracauer/cstream.html
Packager: Dmitry V. Levin <ldv@altlinux.org>
Source: cstream-%version.tar
Patch: cstream-2.7.6-rh-Wextra.patch

%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.

%prep
%setup -q
%patch -p1

%build
%configure
%make_build 
%make check

%install
%make_install install DESTDIR="%buildroot"
%make installcheck DESTDIR="%buildroot"

%files
%_bindir/*
%_man1dir/*
%doc CHANGES COPYRIGHT README TODO

%changelog
* Sun Feb 08 2009 Dmitry V. Levin <ldv@altlinux.org> 2.7.6-alt1
- Packaged for ALT Linux.

* Sat Dec 20 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.6-1
- Update to upstream's 2.7.6 release.

* Sat Feb 09 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.5-1
- Update to upstream's 2.7.5 release.

* Sat Feb 09 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-4
- Add %%{?dist} to Release:

* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-3
- More compile warnings (-Wall -Wextra -Werror).
- Redacted description down to the most important points.

* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-2
- Spec file cleanups (use install target, get rpmlint to shut up).

* Fri Feb 08 2008 Mike Weisenborn <mike@weisenborn.com> - 2.7.4-1
- Initial package
