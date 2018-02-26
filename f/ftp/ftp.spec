# Spec file for ftp package

%define rname    netkit-ftp
%define rversion 0.18-pre1

Name: ftp
Version: 0.18
Release: alt0.pre1.1

Summary: The standard UNIX FTP (file transfer protocol) client

License: BSD
Group: Networking/File transfer
URL: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit-devel/
#URL: http://www.hcs.harvard.edu/~dholland/computers/netkit.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit-devel/%rname-%rversion.tar

Patch1: %rname-0.17-alt-configure.patch
Patch2: %rname-0.17-alt-tinfo.patch

Patch10: %rname-0.18-pre1-alt-usagi-ipv6.patch

Patch11: %rname-0.17-acct.patch
Patch12: %rname-0.17-pre20000412.pasv-security.patch 
Patch13: %rname-0.17-fedora-arg_max.patch

Patch14: %rname-0.17-fedora-segv.patch
Patch15: %rname-0.17-fedora-volatile.patch
Patch16: %rname-0.17-fedora-runique_mget.patch
Patch17: %rname-0.17-fedora-locale.patch
Patch18: %rname-0.17-fedora-printf.patch
Patch19: %rname-0.17-fedora-longint.patch
Patch20: %rname-0.17-fedora-vsftp165083.patch
Patch21: %rname-0.17-fedora-C-Frame121.patch
Patch22: %rname-0.17-fedora-data.patch
Patch23: %rname-0.17-fedora-multihome.patch
Patch24: %rname-0.17-fedora-longnames.patch
Patch25: %rname-0.17-fedora-multiipv6.patch
Patch26: %rname-0.17-fedora-nodebug.patch
Patch27: %rname-0.17-fedora-stamp.patch
Patch28: %rname-0.17-fedora-sigseg.patch
Patch29: %rname-0.17-fedora-size.patch
Patch30: %rname-0.17-fedora-fdleak.patch
Patch31: %rname-0.17-fedora-bitrate.patch
Patch32: %rname-0.17-fedora-case.patch
Patch33: %rname-0.17-fedora-chkmalloc.patch
Patch34: %rname-0.17-fedora-fprintf.patch

# Automatically added by buildreq on Sat Dec 13 2008
BuildRequires: libreadline-devel libtinfo-devel

%description
The %name package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

If your system is on a network, you should install %name in order to do
file transfers.

%prep
%setup -q -n %rname-%rversion
%patch1 -p1
%patch2 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1

%build
CFLAGS=$RPM_OPT_FLAGS BINDIR=%_bindir MANDIR=%_mandir ./configure --enable-ipv6
%make_build

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man{1,5}}

%make_install INSTALLROOT=$RPM_BUILD_ROOT install

%files
%_bindir/*
%_mandir/man?/*
%doc README BUGS

%changelog
* Sat Dec 13 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.18-alt0.pre1.1
- New version 0.18-pre1
- Rivives from orphaned

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.17-ipl5mdk.1
- Rebuilt with libreadline.so.5.

* Wed Oct 30 2002 Stanislav Ievlev <inger@altlinux.ru> 0.17-ipl5mdk
- rebuild with gcc3

* Sun Jun 30 2002 Dmitry V. Levin <ldv@altlinux.org> 0.17-ipl4mdk
- Patched to link with libtinfo.

* Mon Mar 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.17-ipl3mdk
- Rebuilt

* Tue Aug 15 2000 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl2mdk
- RE adaptions.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.17-2mdk
- automatically added BuildRequires

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.17-1mdk
- rebuild for new version

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.16-1mdk
- 0.16
  - y2k patch now integrated
  - ewt and readline patch no more necessary
- BM
- macros

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 0.10-8mdk
- rebuild for new readline
- cleanup

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 0.10-7mdk
- relocate group

* Tue Dec 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix possible y2k misunderstand (i told you it's a minimal
  possibility).

* Mon Dec 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Use readline.

* Wed Nov 03 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
