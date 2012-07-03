%define origname tftp

Name: inquisitor-tftpd
Version: 0.48
Release: alt1

Summary: The server for the Trivial File Transfer Protocol (TFTP)
License: BSD
Group: System/Servers

Url: http://www.kernel.org/pub/software/network/tftp/
Source0: http://www.kernel.org/pub/software/network/tftp/tftp-hpa-%version.tar.gz
Source1: tftp.xinetd
Patch: tftp-hpa-0.48-inquisitor.patch
Patch1: tftp-0.28-malta.patch
Patch2: tftp-hpa-0.36-bcopy.patch
Packager: Michael Shigorin <mike@altlinux.org>

PreReq: shadow-utils
Requires: xinetd
Conflicts: tftpd tftp-server tftp-server-xinetd

# Automatically added by buildreq on Fri Apr 23 2004
BuildRequires: libreadline-devel libwrap-devel

%description
The Trivial File Transfer Protocol (TFTP) is normally used
for booting diskless systems.

This package includes only server side patched to please Inquisitor.

%prep
%setup -n tftp-hpa-%version
%patch0 -p1
%patch2 -p1

%build
%configure
subst '
    s,^CC=.*$,CC=cc,;
    s,^BINDIR=.*$,BINDIR=%_bindir,;
    s,^MANDIR=.*$,MANDIR=%_mandir,;
    s,^SBINDIR=.*$,SBINDIR=%_sbindir,;
    ' MCONFIG
%make_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_mandir/man{1,8},%_localstatedir/tftpboot}
%make_install install INSTALLROOT=%buildroot
ln -s in.tftpd %buildroot%_sbindir/tftpd
install -pDm640 %SOURCE1 %buildroot%_sysconfdir/xinetd.d/%origname

%post
%_sbindir/groupadd -rf %origname ||:
%_sbindir/useradd -r -g %origname -d /dev/null -s /dev/null -n %origname &>/dev/null ||:

%files
%config(noreplace) %_sysconfdir/xinetd.d/%origname
%_sbindir/*
%_man8dir/*
%dir %_localstatedir/tftpboot

%changelog
* Mon Nov 02 2009 Michael Shigorin <mike@altlinux.org> 0.48-alt1
- forked the package to include inquisitor logging patch
- dropped client subpackage, only server differs

* Fri Feb 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.48-alt1
- new version

* Mon Feb 20 2006 Anton Farygin <rider@altlinux.ru> 0.42-alt1
- new version

* Mon Jan 16 2006 Anton Farygin <rider@altlinux.ru> 0.41-alt1
- new version

* Mon Jun 27 2005 Anton Farygin <rider@altlinux.ru> 0.40-alt2
- summary fixed (#5597)

* Thu Oct 28 2004 Anton Farygin <rider@altlinux.ru> 0.36-alt2
- fixed possible remote buffer overflows

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 0.36-alt1
- new version (0.36)

* Sun May 04 2003 Rider <rider@altlinux.ru> 0.33-alt1
- new version

* Sun Nov 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt3
- Rebuilt with new shared libwrap
- Updated buildrequires

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt2
- Added malta patch from RH
- Rebuilt in new environment
- Moved /tftpboot to /var/lib/tftpboot

* Mon Jun 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt1
- 0.29
- Removed netkit client

* Fri Dec 07 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.17-ipl4mdk
- Changed xinet.d config file

* Wed Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.17-ipl3mdk
- Rebuild for Sisyphus
- New version of hpa (0.20)
- Added patch from Mandrake
- Some spec cleanup
- Added optimization

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl2mdk
- RE adaptions.

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.17-2mdk
- Add hpa version of tftp.
- Add xinetd support.
- Split server and client.

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.17-1mdk
- rebuild with shiny new version
- _sbindir_ macro

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.16-3mdk
- macros, BM, _spechelper_

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.16-2mdk
- fix changelog, blame me not Chris Molnar for damage...

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.16-1mdk
- version 0.16
- fixed Source URL
- added documentation

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.15-2mdk
- Fixed groups

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- 0.15
- Removed version dependencies from spec file
- Build Release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Apr  7 1999 Jeff Johnson <jbj@redhat.com>
- tftpd should truncate file when overwriting (#412)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
