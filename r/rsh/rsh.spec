Name: rsh
Version: 0.17
Release: alt3
Serial: 1

Summary: Clients for remote access commands (rsh, rlogin, rcp)
Group: Networking/Remote access
License: BSD

Source0: netkit-rsh-%version.tar.gz
Source1: rexec.pam
Source2: rlogin.pam
Source3: rsh.pam
Source4: rexec-1.5.tar.bz2
Source5: rsh-xinetd
Source6: rlogin-xinetd
Source7: rexec-xinetd

Patch1: netkit-rsh-0.17-sectty.patch
# Make rexec installation process working
Patch2: netkit-rsh-0.17-rexec.patch
Patch3: netkit-rsh-0.10-stdarg.patch
# Improve installation process
Patch4: netkit-rsh-0.16-jbj.patch
Patch5: netkit-rsh-0.16-pamfix.patch
Patch6: netkit-rsh-0.16-jbj2.patch
Patch7: netkit-rsh-0.16-jbj3.patch
Patch8: netkit-rsh-0.16-jbj4.patch
Patch9: netkit-rsh-0.16-prompt.patch
Patch10: netkit-rsh-0.16-rlogin=rsh.patch
# Improve documentation
Patch11: netkit-rsh-0.16-nokrb.patch
Patch12: netkit-rsh-0.17-pre20000412-jbj5.patch
# RH #42880
Patch13: netkit-rsh-0.17-userandhost.patch
Patch14: netkit-rsh-0.17-strip.patch
# RH #67362
Patch15: netkit-rsh-0.17-lfs.patch
# RH #57392
Patch16: netkit-rsh-0.17-chdir.patch
# RH #63806
Patch17: netkit-rsh-0.17-pam-nologin.patch
Patch18: netkit-rsh-0.17-nohostcheck.patch
# RH #135643
Patch19: netkit-rsh-0.17-rexec-netrc.patch
# RH #68590
Patch20: netkit-rsh-0.17-pam-sess.patch
# RH #67361
Patch21: netkit-rsh-0.17-errno.patch
# RH #118630
Patch22: netkit-rsh-0.17-rexec-sig.patch
# RH #135827
Patch23: netkit-rsh-0.17-nohost.patch
# RH #122315
Patch24: netkit-rsh-0.17-ignchld.patch
# RH #146464
Patch25: netkit-rsh-0.17-checkdir.patch
Patch26: netkit-rsh-0.17-pam-conv.patch
# RH #174045
Patch27: netkit-rsh-0.17-rcp-largefile.patch
# RH #174146
Patch28: netkit-rsh-0.17-pam-rhost.patch
# RH #178916
Patch29: netkit-rsh-0.17-rlogin-linefeed.patch
Patch30: netkit-rsh-0.17-ipv6.patch
Patch31: netkit-rsh-0.17-pam_env.patch
Patch33: netkit-rsh-0.17-dns.patch
Patch34: netkit-rsh-0.17-nohostcheck-compat.patch
# RH #448904
Patch35: netkit-rsh-0.17-audit.patch
Patch36: netkit-rsh-0.17-longname.patch
# RH #440867
Patch37: netkit-rsh-0.17-arg_max.patch
Patch38: netkit-rsh-0.17-rh448904.patch
Patch39: netkit-rsh-0.17-rh461903.patch
Patch40: netkit-rsh-0.17-rh473492.patch
Patch41: netkit-rsh-0.17-rh650119.patch
Patch42: netkit-rsh-0.17-rh710987.patch
Patch43: netkit-rsh-0.17-rh784467.patch

Patch50: netkit-rsh-0.17-alt-warn.patch

# Automatically added by buildreq on Wed Jan 29 2003
BuildRequires: libncurses-devel libpam-devel libtinfo-devel

%description
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp).  All three of these commands
use rhosts style authentication.  This package contains the clients
needed for all of these services.

The rsh package should be installed to enable remote access to other
machines (but make sure you at least considered crypto approach
like openssh implements).

%package server
Summary: Servers for remote access commands (rsh, rlogin, rcp)
Group: System/Servers
Requires: pam >= 0.59

%description server
The rsh-server package contains a set of programs which allow users
to run commmands on remote machines, login to other machines and copy
files between machines (rsh, rlogin and rcp).  All three of these
commands use rhosts style authentication.  This package contains the
servers needed for all of these services.  It also contains a server
for rexec, an alternate method of executing remote commands.
All of these servers are run by xinetd and configured using
/etc/xinetd.d/ and PAM (but are disabled by default).

%prep
%setup -n netkit-rsh-%version -a 4
%patch1 -p1 -b .sectty
%patch2 -p1 -b .rexec
%patch3 -p1 -b .stdarg
%patch4 -p1 -b .jbj
# XXX patches {5,6,7} not applied
#patch5 -p1 -b .pamfix
#patch6 -p1 -b .jbj2
#patch7 -p1 -b .jbj3
%patch8 -p1 -b .jbj4
%patch9 -p1 -b .prompt
%patch10 -p1 -b .rsh
%patch11 -p1 -b .rsh.nokrb
%patch12 -p1 -b .jbj5
%patch13 -p1 -b .userandhost
%patch14 -p1 -b .strip
%patch15 -p1 -b .lfs
%patch16 -p1 -b .chdir
%patch17 -p1 -b .pam-nologin
#patch18 -p1 -b .nohostcheck
%patch19 -p1 -b .rexec-netrc
%patch20 -p1 -b .pam-sess
%patch21 -p1 -b .errno
%patch22 -p1 -b .rexec-sig
%patch23 -p1 -b .nohost
%patch24 -p1 -b .ignchld
%patch25 -p1 -b .checkdir
%patch26 -p1 -b .pam-conv
%patch27 -p1 -b .largefile
%patch28 -p1 -b .pam-rhost
%patch29 -p1 -b .linefeed
%patch30 -p1 -b .ipv6
%patch31 -p1 -b .pam_env
%patch33 -p1 -b .dns
%patch34 -p1 -b .compat
%patch35 -p1 -b .audit
%patch36 -p1 -b .longname
%patch37 -p1 -b .arg_max
%patch38 -p1 -b .rh448904
%patch39 -p1 -b .rh461903
%patch40 -p1 -b .rh473492
%patch41 -p1 -b .rh650119
%patch42 -p1 -b .rh710987
%patch43 -p1 -b .rh784467

# FIXME: needs rediff
#patch50 -p1 -b .warn

# No, I don't know what this is doing in the tarball.
rm -f rexec/rexec

%build
%_configure_script \
    --without-shadow \
    --prefix=/usr \
    --installroot=%buildroot \
    --binmode=0755 \
    --daemonmode=0711 \
    --suidmode=4711

perl -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%_bindir,;
    s,^MANDIR=.*$,MANDIR=%_mandir,;
    s,^SBINDIR=.*$,SBINDIR=%_sbindir,;
    ' MCONFIG

%make_build

%install
mkdir -p %buildroot/%_sysconfdir/{pam.d,xinetd.d}
mkdir -p %buildroot/{%_bindir,%_sbindir}
mkdir -p %buildroot/%_mandir/{man1,man8}

%make INSTALLROOT=%buildroot MANDIR=%_mandir install

install -pm644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/rexec
install -pm644 %SOURCE2 %buildroot/%_sysconfdir/pam.d/rlogin
install -pm644 %SOURCE3 %buildroot/%_sysconfdir/pam.d/rsh

install -pm644 %SOURCE5 %buildroot/%_sysconfdir/xinetd.d/rsh
install -pm644 %SOURCE6 %buildroot/%_sysconfdir/xinetd.d/rlogin
install -pm644 %SOURCE7 %buildroot/%_sysconfdir/xinetd.d/rexec

%files
%attr(4711,root,root) %_bindir/rcp
%attr(4711,root,root) %_bindir/rlogin
%attr(4711,root,root) %_bindir/rsh
%_bindir/rexec
%_mandir/man1/*
%doc README

%files server
%config(noreplace) %_sysconfdir/xinetd.d/*
%config(noreplace) %_sysconfdir/pam.d/*
%_mandir/man8/*
%_sbindir/in.*

%changelog
* Fri Jul 13 2012 Michael Shigorin <mike@altlinux.org> 1:0.17-alt3
- rebuilt for Sisyphus on request by Denis Nazarov
  + quote a percent sign in a 12 y old changelog record by jbj@
- applied fedora patches up to 0.17-68
  + netkit-rsh-0.17-nodns.patch and netkit-rsh-0.17-nohostcheck.patch
    are substituted by netkit-rsh-0.17-dns.patch
  + temporarily(tm) disabled ALT fixes for compiler warnings
    (the patch needs an update)
- pam configuration files made %%config(noreplace)
- dropped manpage optimizations (broken)
- dropped URL parts of Source{0,4} (unavailable by now)

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1:0.17-alt2
- fix PAM configuration for rsh and rlogin

* Fri Mar 07 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1:0.17-alt1
- add Serial and set package version to 0.17-alt
- add all patches from RH package rsh-0.17-29.1

* Wed Sep 24 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.17-ipl9mdk
- PAM configs fixed

* Tue Jan 28 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.17-ipl8mdk
- update netkit-rsh to real v0.17
- spec cleanup

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.17-ipl7mdk
- fixed suid/sgid file permissions

* Mon Feb  5 2001 Kostya Timoshenko <kt@petr.kz> 0.17-ipl5mdk
- rebuild for RE

* Tue Sep 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.17-4mdk
- Pamstackizification.

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.17-3mdk
- Xinetd support.
- Merge rh patch.
- Upgrade to the last pre of 0.17.

* Thu Aug 31 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.17-2mdk
- removed unused patch
- patch: all r-client command output a :
  "This command is deprecated, you should use ssh instead."

* Sat Aug 05 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.17-1mdk
- new and shiny version

* Wed Jun 28 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.16-3mdk
- Added UTF-8 patch from Alastair.McKinstry@compaq.com
- made man pages paths modular
- remove useless man pages compression and binary stripping sections
  (now done by spec-helper)

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.16-2mdk
- Fix bad tag value.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.16-1mdk
- 0.16-1mdk

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- mark pam config files as %%config.

* Fri Feb  4 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Sun Jan 30 2000 Bill Nottingham <notting@redhat.com>
- remove bogus rexec binary when building; it causes weirdness

* Fri Jan 28 2000 Jeff Johnson <jbj@redhat.com>
- Make sure that rshd is compiled with -DUSE_PAM.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- Fix bug in rshd (hangs forever with zombie offspring) (#8313).

* Wed Jan  5 2000 Jeff Johnson <jbj@redhat.com>
- fix the PAM fix yet again (#8133).

* Tue Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.
- dup setuid bits into files list.

* Fri Jul 30 1999 Jeff Johnson <jbj@redhat.com>
- update to rexec-1.5 client (#4262)

* Wed May 19 1999 Jeff Johnson <jbj@redhat.com>
- fix broken rexec protocol in in.rexecd (#2318).

* Tue May  4 1999 Justin Vallon <vallon@mindspring.com>
- rcp with error was tricked by stdarg side effect (#2300)

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- rlogin pam file was missing comment magic

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip rexec

* Fri Mar 26 1999 Jeff Johnson <jbj@redhat.com>
- rexec needs pam_set_item() (#60).
- clarify protocol in rexecd.8.
- add rexec client from contrib.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Sat Apr  5 1998 Marcelo F. Vianna <m-vianna@usa.net>
- Packaged for RH5.0 (Hurricane)

* Tue Oct 14 1997 Michael K. Johnson <johnsonm@redhat.com>
- new pam conventions

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
