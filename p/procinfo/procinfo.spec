Name: procinfo
Version: 18
Release: alt1
Serial: 1

Packager: Dmitry V. Levin <ldv@altlinux.org>

Summary: A tool for gathering and displaying system information.
License: GPL
Group: Monitoring

Source: ftp://ftp.cistron.nl/pub/people/svm/%name-%version.tar.bz2
Patch1: %name-14-rh-makefile.patch
Patch2: %name-17-rh-uptime.patch 
Patch3: %name-17-rh-lsdev.patch
Patch4: %name-18-rh-mharris-use-sysconf.patch
# Automatically added by buildreq on Mon Jun 24 2002
BuildRequires: libtinfo-devel

%description
The %name command gets system data from the /proc directory
(the kernel filesystem), formats it and displays it on standard
output.  You can use %name to acquire information about your
system from the kernel as it is running.

Install %name if you'd like to use it to gather and display
system data.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%__subst 's/install -/\$(INSTALL) -/g' Makefile

%build
%make_build LDLIBS=-ltinfo

%install
%makeinstall
for f in *.8; do
	install -pD -m644 "$f" "$RPM_BUILD_ROOT%_man8dir/$f"
done

%files
%_bindir/*
%_mandir/man?/*
%doc README CHANGES

%changelog
* Tue Jun 08 2004 Stanislav Ievlev <inger@altlinux.org> 1:18-alt1
- rebuild in hasher
- added patch from RH to use sysconf for retrieving number of system processors
  (it's more portable)

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 18-ipl4mdk
- 

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 18-ipl3mdk
- Fixed to link with libtinfo.

* Thu Mar 21 2002 Stanislav Ievlev <inger@altlinux.ru> 18-ipl2mdk
- Added some RH pathes
- Rebuilt

* Wed Mar 07 2001 Dmitry V. Levin <ldv@fandra.org> 18-ipl1mdk
- Release 18.

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 17-ipl5mdk
- RE adaptions.

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 17-4mdk
- BM
- use new macros
- let spechelper compress 'n strip

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 17-3mdk
- fix bad tag value.

* Mon Mar 20 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 17-2mdk
- Updated to procinfo 17
- removed the jbj architecture patch cause it has been included in the procinfo
  tree.

* Fri Nov 26 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP build
- build as non root

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- patched to work with kernels with LOTS of IRQs. (bug 1616)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Mar 12 1999 Michael Maher <mike@redhat.com>
- updated to version 16
- closed bug 1349

* Fri Nov 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 15 to fix bugzilla 70.

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- calculate time per-cent on non-{alpha,i386} correctly.

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 14
- fixed the spec file

* Thu Apr 30 1998 Donnie Barnes <djb@redhat.com>
- updated from 0.11 to 13
- added socklist program

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 0.11

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
