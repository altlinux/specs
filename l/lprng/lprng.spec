Name: lprng
Version: 3.8.A
Release: alt3.1

Summary: The LPRng print spooler
License: %gpl2plus, %artistic_license
Group: System/Servers

Url: http://www.lprng.com
Packager: Yury Yurevich <anarresti@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: lpr
Conflicts: gtklp cups foomatic-db-engine
BuildRequires(pre): rpm-build-licenses
BuildRequires: gettext gawk procps libkrb5-devel libssl-devel openssl patch

%description
LPRng is an enhanced, extended, and portable implementation of the
Berkeley LPR print spooler functionality. LPRng provides the same
interface and meeting RFC1179 requirements, but the implementation is
completely new and provides support for the following features:
lightweight (no databases needed) lpr, lpc, and lprm programs; dynamic
redirection of print queues; automatic job holding; highly verbose
diagnostics; multiple printers serving a single queue; client programs
do not need to run SUID root; greatly enhanced security checks; and a
greatly improved permission and authorization mechanism.

LPRng is compatible with other print spoolers and network printers
that use the LPR interface and meet RFC1179 requirements. LPRng
provides emulation packages for the SVR4 lp and lpstat programs,
eliminating the need for another print spooler package. These
emulation packages can be modified according to local requirements, in
order to support vintage printing systems.

For users who require secure and/or authenticated printing support,
LPRng supports Kerberos V, MIT Kerberos IV Print Support, and PGP
authentication. Additional authentication support is extremely simple
to add.

%prep
%setup
%patch -p1

%build
%add_optflags -I/usr/include/krb5
PSHOWALL="-ax"; export PSHOWALL
%configure --prefix=/ \
           --exec-prefix=%_usr \
           --disable-rpath \
           --with-config_subdir=%name \
           --with-lockfile=%_var/run/%name/lpd \
           --libexecdir=%_libdir \
           --mandir=%_mandir \
           --with-unix_socket_path=%_var/run/%name/socket \
           --enable-kerberos_checks --enable-kerberos \
           --with-userid=lp \
           --with-groupid=lp \
           --with-filterdir=\$\{libdir\}/%name \
           --enable-lpd.conf.local
%make

%install

install -D -m 755 src/monitor %buildroot/%_usr/sbin/monitor
%makeinstall POSTINSTALL=NO
install -D -m 644 alt/lpd.perms %buildroot/%_sysconfdir/lprng/lpd.perms
install -D -m 644 alt/lpd.conf %buildroot/%_sysconfdir/lprng/lpd.conf
install -D -m 755 alt/lpd.init %buildroot/%_initdir/lpd
mkdir examples
mkdir -p %buildroot/%_var/run/%name
mkdir -p %buildroot/%_spooldir/lpd
mv %buildroot/%_sysconfdir/printcap.sample examples
mv %buildroot/%_sysconfdir/%name/*.sample examples

%post
%post_service lpd

%preun
%preun_service lpd

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/lpd.conf
%config(noreplace) %_sysconfdir/%name/lpd.perms
%config %_initdir/lpd
%_bindir/lpq
%_bindir/lprm
%_bindir/lpr
%_bindir/lpstat
%_bindir/lp
%_bindir/cancel
%_sbindir/lpc
%_sbindir/lpd
%_sbindir/checkpc
%_sbindir/monitor
%_sbindir/lprng_certs
%_sbindir/lprng_index_certs
%_libdir/%name/*
%_mandir/man*/cancel.*
%_mandir/man*/checkpc.*
%_mandir/man*/lp.*
%_mandir/man*/lpbanner.*
%_mandir/man*/lpc.*
%_mandir/man*/lpd.*
%_mandir/man*/lpf.*
%_mandir/man*/lpq.*
%_mandir/man*/lpr.*
%_mandir/man*/lprm.*
%_mandir/man*/lprng_certs.*
%_mandir/man*/lprng_index_certs.*
%_mandir/man*/lpstat.*
%_mandir/man*/monitor.*
%_mandir/man*/pclbanner.*
%_mandir/man*/psbanner.*
%_mandir/man*/printcap.*
%dir %attr(0770,root,lp) %_var/run/%name
%dir %attr(0770,root,lp) %_spooldir/lpd
%dir %_libdir/%name
%doc CHANGES CONTRIBUTORS COPYRIGHT INSTALL LICENSE
%doc README* 
%doc examples

%changelog
* Fri May 15 2009 Yury Yurevich <anarresti@altlinux.org> 3.8.A-alt3.1
- make /etc/lprng be owned by package

* Thu May 14 2009 Yury Yurevich <anarresti@altlinux.org> 3.8.A-alt3
- add conflicts
- fix filters path at x86_64

* Wed Apr 15 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.A-alt2
[ Yury Yurevich ]
- move filters to proper place - %%_libdir/%%name
- rename package LPRng to lprng
[ Vladimir V. Kamarzin ]
- upload package to Sisyphus by mentor

* Tue Apr 14 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.8.A-alt1
[ Yury Yurevich ]
- adapt spec to ALT Linux policies
- fix pidfile path
- make lprng be geared
[ Vladimir V. Kamarzin ]
- move filters to %%_bindir
- upload package to Sisyphus by mentor

* Tue Aug 21 2001 Patrick Powell <papowell@astart.com> 3.7.5-1
- new release for 3.7.5
- Note the aclocal, autoconf, etc. stuff added to make the various
- versions of gettext and libtool compatible with the RedHat version.

* Fri Aug 10 2001 Crutcher Dunnavant <crutcher@redhat.com> 3.7.4-28
- disabled gdbm support, changed CFLAGS; #41652

* Thu Aug  9 2001 Crutcher Dunnavant <crutcher@redhat.com> 3.7.4-27
- ownz /usr/libexec/filters; #51158
- make checkpc nonblocking on its tests; #37995

* Thu Aug  2 2001 Crutcher Dunnavant <crutcher@redhat.com> 3.7.4-26
- added gdbm-devel dep; #44885

* Fri Jun 29 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix build on s390

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Jun 07 2001 Crutcher Dunnavant <crutcher@redhat.com>
- setgroups droping patch

* Thu Mar 29 2001 Crutcher Dunnavant <crutcher@redhat.com>
- told checkpc to only Check_file() job files. (keeping it from zapping the master-filter)

* Fri Mar  9 2001 Crutcher Dunnavant <crutcher@redhat.com>
- applied elliot's patch (which i got idependently from the lprng list as well)
- that fixes a thinko that killed LPRng on 64 arches.

* Fri Mar  9 2001 Crutcher Dunnavant <crutcher@redhat.com>
- fixed the URLs for the LPRng project

* Thu Mar  8 2001 Crutcher Dunnavant <crutcher@redhat.com>
- reverted the shutdown call in Local_job to make device filters work.
- all your base are belong to us

* Wed Mar 07 2001 Philipp Knirsch <pknirsch@redhat.de>
- Removed the shutdown patch for common/linksupport:Link_close() as ii
generated a deadlock between lpr and lpd for none existing printers.

* Sun Feb 25 2001 Crutcher Dunnavant <crutcher@redhat.com>
- hacked out the shutdown(sock, 1) calls that killed stupid network printers.

* Wed Feb 15 2001 Crutcher Dunnavant <crutcher@redhat.com>
- tweak to ldp.init's display messages

* Fri Feb  9 2001 Crutcher Dunnavant <crutcher@redhat.com>
- man page tweak

* Thu Feb  8 2001 Crutcher Dunnavant <crutcher@redhat.com>
- (yet) further tweaks to lpd.init's display format.

* Tue Feb  6 2001 Crutcher Dunnavant <crutcher@redhat.com>
- further tweaks to lpd.init's display format.

* Tue Feb  6 2001 Crutcher Dunnavant <crutcher@redhat.com>
- cleaned up lpd.init to do translations correctly, and stop screwing up
- result values.

* Thu Feb  1 2001 Crutcher Dunnavant <crutcher@redhat.com>
- added lpd init back (ick!)

* Wed Jan 24 2001 Crutcher Dunnavant <crutcher@redhat.com>
- removed req for printconf (It should go the other way)

* Thu Jan 18 2001 Crutcher Dunnavant <crutcher@redhat.com>
- fixed file list

* Thu Jan 18 2001 Crutcher Dunnavant <crutcher@redhat.com>
- removed lpd.init, set requirement of printconf

* Thu Jan 11 2001 Crutcher Dunnavant <crutcher@redhat.com>
- upgraded to LPRng-3.7.4

* Tue Dec 12 2000 Crutcher Dunnavant <crutcher@redhat.com>
- rebuild for kerb

* Mon Oct 23 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Upgraded to LPRng-3.6.26
- Removed syslog patch, as .24 fixes the problem

* Mon Sep 25 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Patched use_syslog to avoid a format string exploit.
- Resolves bug #17756

* Mon Sep 18 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Upgraded to LPRng-3.6.24

* Mon Sep 11 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Added gettext to the BuildPreReq list

* Mon Sep 11 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Fixed lpd.init to use %_initdir//, instead of %_sysconfdir/init.d

* Mon Sep 11 2000 Crutcher Dunnavant <crutcher@redhat.com>
- changed the prereq: %_sysconfdir/init.d to: %_initdir/
- we are not changing that over (yet?)

* Mon Aug 14 2000 Crutcher Dunnavant <crutcher@redhat.com>
- removed the sticky bit from lpc

* Mon Aug 14 2000 Crutcher Dunnavant <crutcher@redhat.com>
- removed the sticky bit from the client programs (LPRng doesn't need them)

* Sat Aug 05 2000 Bill Nottingham <notting@redhat.com>
- condrestart fixes

* Fri Aug  4 2000 Bill Nottingham <notting@redhat.com>
- triggerpostun on lpr

* Sun Jul 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.6.22 (some fixes)

* Tue Jul 25 2000 Bill Nottingham <notting@redhat.com>
- fix prereq

* Sat Jul 22 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix bogus checkpc error messages when the lockfile doesn't exist because
  init scripts clear /var/run (#14472)

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix chkconfig comments in the init script

* Mon Jul 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- move the init script to %_initdir/
- fix perms on setuid binaries

* Fri Jul 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch checkpc to not complain when filter is executable and in the
  spool directory
- remove --disable-force_localhost from configure invocation for better
  compatibility with BSD LPR and rhs-printfilters
- change group back to lp, which is what printtool expects

* Thu Jul 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- change default group to 'daemon' to match 6.2
- enable NLS support
- remove Prefix: tag
- break init script out into a separate file
- fix up broken printcaps in post-install
- run checkpc -f at start-time

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.6.21
- get rid of the notypedef patch - gcc has been fixed at last.

* Mon Jun 26 2000 Preston Brown <pbrown@redhat.com>
- sample config files removed from /etc.
- initscript moved to %_sysconfdir/init.d

* Wed Jun 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.6.18

* Sat Jun 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.6.16
- adapt Kerberos and fixmake patches
- get rid of CFLAGS="-O"; gcc has been fixed
- fix build with glibc 2.2

* Mon Jun 05 2000 Preston Brown <pbrown@redhat.com>
- ifdef 0 is illegal, changed to if 0.
- work around compiler typdef bug.

* Thu Jun 01 2000 Preston Brown <pbrown@redhat.com>
- start, stop, and restart are functions not switch statements now.
  reduces overhead.
- patch to allow autoconf to choose which user/group to run as

* Wed May 31 2000 Preston Brown <pbrown@redhat.com>
- remove init.d symbolic links.
- remove txt/ps/info versions of the HOWTO from the pkg
- use new fhs paths

* Thu May 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- change free() to krb5_free_data_contents() when patching for Kerberos 5
- detect libcrypto or libk5crypto when looking for Kerberos 5

* Tue May 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable Kerberos support
- remove extra defattr in files list
- add --disable-force_localhost to configure invocation
- remove "-o root" at install-time

* Tue May 16 2000 Matt Wilson <msw@redhat.com>
- add Prereq of /sbin/chkconfig
- fix broken conflicting declaration on alpha

* Tue Apr 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial Red Hat packaging, fix up the spec file

* Mon Sep 13 1999 Patrick Powell <papowell@astart.com>
- resolved problems with symbolic links to %_sysconfdir/init.d
  files - used the chkconfig facility

* Sat Sep  4 1999 Patrick Powell <papowell@astart.com>
- did ugly things to put the script in the spec file

* Sat Aug 28 1999 Giulio Orsero <giulioo@tiscalinet.it>
- 3.6.8

* Fri Aug 27 1999 Giulio Orsero <giulioo@tiscalinet.it>
- 3.6.7 First RPM build.
