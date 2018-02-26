Name: adjtimex
Version: 1.21
Release: alt1

Summary: Utility to display or set the kernel time variables
License: GPL
Group: System/Kernel and hardware
Url: ftp://ftp.debian.org/debian/pool/main/a/adjtimex/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ibiblio.org/pub/Linux/system/admin/time/adjtimex-%version.tar.gz
Source: %name-%version-%release.tar

%description
This program gives you raw access to the kernel time variables.  For a
machine connected to the Internet, or equipped with a precision oscillator
or radio clock, the best way to keep the system clock correct is with
ntpd.  However, for a standalone or intermittently connected machine,
you may use adjtimex instead to at least correct for systematic drift.
adjtimex can optionally adjust the system clock using the CMOS clock as
a reference, and can log times for long-term estimation of drift rates.

%prep
%setup -q -n %name-%version-%release
bzip2 -9k ChangeLog

%build
%configure
%make_build

%install
install -pD -m755 adjtimex %buildroot%_sbindir/adjtimex
install -pD -m644 adjtimex.8 %buildroot%_man8dir/adjtimex.8

%files
%_sbindir/*
%_mandir/man?/*
%doc README* COPYRIGHT ChangeLog.bz2

%changelog
* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1.21-alt1
- Updated to 1.21

* Sat Jan 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1.16-alt1
- Updated to 1.16

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1.13-alt1
- 1.13

* Wed Apr 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.12-alt1
- 1.12

* Wed Dec 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.11-ipl1mdk
- RE adaptions.

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.11

* Sat Mar 18 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Tue Mar 17 2000 dam's <damien@mandrakesoft.com> 1.9-1mdk
- Update to 1.9

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Mandrake release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- builds on all architectures
