Name: dlint
Version: 1.4.1
Release: alt1
Serial: 1

Summary: A DNS zone verification utility
License: GPLv2+
Group: Networking/DNS
Url: http://www.domtools.com/dns/dlint.shtml
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

# http://www.domtools.com/pub/dlint%version.tar.gz
Source: dlint%version.tar
Patch: dlint-1.4.0-alt-tmp.patch

%description
This program analyzes any DNS zone you specify, and reports any problems
it finds by displaying errors and warnings.  Then it descends recursively
to examine all zones below the given one (this can be disabled with a
command- line option).  Designed for Unix, dlint is written in Bourne
Shell and Perl.

%prep
%setup -q -n dlint%version
%patch -p1

%build
sed -i 's|/usr/local/bin/|%_datadir/%name/|g' dlint

%install
install -pD -m755 digparse %buildroot%_datadir/%name/digparse
install -pD -m755 dlint %buildroot%_bindir/%name
install -pD -m644 dlint.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_datadir/%name
%_mandir/man?/*
%doc README CHANGES BUGS TESTCASES COPYRIGHT

%changelog
* Mon Mar 31 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.1-alt1
- Updated to 1.4.1 (fixes coreutils old-style options usage).

* Tue Aug 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.0-alt1
- Updated GROUP tag (#4734).

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-ipl2
- Fixed tmp files handling.
- Relocated digparse helper to %_datadir/%name/.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.0-ipl1
- 1.4.0

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.4-1ipl
- 1.3.4
- RE adaptions.

* Wed Nov 10 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
