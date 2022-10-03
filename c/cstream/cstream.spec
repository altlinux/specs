Name: cstream
Version: 3.2.1
Release: alt1

Summary: General-purpose stream-handling tool
License: MIT
Group: File tools
Url: https://www.cons.org/cracauer/cstream.html
# https://www.cons.org/cracauer/download/%%name-%%version.tar.gz
Source: %name-%version.tar

Patch2: %name-%version-rh-Wextra.patch
Patch3: %name-%version-rh-double-assignment.patch
Patch5: %name-%version-rh-meh.patch
Patch6: %name-%version-rh-Werror=tautological-compare.patch

%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.

%prep
%setup
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc CHANGES COPYRIGHT README TODO

%changelog
* Tue Oct 04 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1, synced patches with Fedora.

* Wed Apr 17 2013 Dmitry V. Levin <ldv@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0, synced patches with Fedora.

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
