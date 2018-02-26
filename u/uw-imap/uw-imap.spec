Name: uw-imap
Version: 2004g
Release: alt3.1

Summary: Server daemons for IMAP and POP network mail protocols
License: BSD
Group: System/Servers
Url: http://www.washington.edu/imap/

###########################################
# Relations with other POP3/IMAP server pkgs (like courier-imap)

# Provide the abstract service names (which are virtual pkg names),
# specify their origin (our pkg name as the epoch + version-release):
Provides: IMAPD = %name:%version-%release
Provides: POP3D = %name:%version-%release

# Conflict with all other real pkgs which provide the same services
# (they should specify the origin the same way, so the epoch-version-release
# of the virtual pkgs POP3D & IMAPD will always differ from that of ours if
# they are provided by a different real pkg):
Conflicts: IMAPD < %name:%version-%release
Conflicts: IMAPD > %name:%version-%release
Conflicts: POP3D < %name:%version-%release
Conflicts: POP3D > %name:%version-%release

Conflicts: courier-imap
Conflicts: cyrus-imapd

# End of the statements to describe relations with other POP3/IMAP server pkgs
########################################

# Renaming the pkg between 2000c-ipl3mdk and 2001a-alt1
Obsoletes: imap < 1:2001a-alt1

# Otherwise we get too many unimportant warnings
%define optflags_warnings -Wall -Wno-parentheses

%define WithSSL 1
%if_without ssl
%define WithSSL 0
%endif

%define WithMaildir 0
%if_with maildir
%define WithMaildir 1
%endif

# Fallback values if openssl-config is not available:
%define _ssldir %_localstatedir/ssl
%define _pemdir %_ssldir/certs

%if %WithSSL

# for openssl-config:
BuildPreReq: libssl-devel
%define _ssldir %(openssl-config --openssldir)
%define _pemdir %_ssldir/certs

# the location of certificates is hardcoded into the binaries (hence Requires),
# and we require the location exists on installation (hence PreReq):
Requires: /var/lib/ssl
PreReq(post): /var/lib/ssl

%endif #WithSSL

Requires: pam >= 0.72-ipl11mdk

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: ftp://ftp.cac.washington.edu/mail/imap-%version.tar.bz2
Source1: imap.pamd
Source2: uw-imap.xinetd
Source3: uw-pop3.xinetd
Source4: uw-pop2.xinetd
Source5: uw-imaps.xinetd
Source6: uw-pop3s.xinetd
Source12: uw-simap.xinetd
Source13: uw-spop3.xinetd
Source8: imap-c-client-maildir.tar.bz2
Source9: uw-imap-2001a-README.IMAPS.ALT

Patch: uw-imap-2001a-alt8-openssl.patch

Patch1: uw-imap-2001a-alt7-ALT-custom.patch
Patch4: uw-imap-2001a-alt7-flocksim.patch

Patch9: uw-imap-2001a-glibc-time.patch
Patch10: uw-imap-2001a-debian-portability.patch
Patch11: uw-imap-2001a-debian-nonull.patch
Patch12: uw-imap-2001a-debian-blackbox-inbox.patch
Patch13: uw-imap-2001a-overflow.patch
Patch14: uw-imap-2001a-IMAP4-overflow.patch

# The maildir support (turned on by %WithMaildir)
# is supplied by three source pieces:
# the tarball (Source8) with the module and README,
# a general patch that embeds the maildir module into the build
# process, and a patch special for Pine client (not the imap server).
# The last piece is only included in pine.src.rpm
Patch20:uw-imap-2001a-maildir-embed.patch
# for glibc 2.2.2
Patch22: imap-maildir-glibc-time.patch

# Automatically added by buildreq on Wed Dec 05 2001
BuildRequires: libpam-devel

%if %WithSSL
BuildRequires: libssl-devel
%endif

%package -n lib%name
Summary: Shared library for IMAP applications
Group: System/Libraries

%package devel
Summary: Static library and headers for developing IMAP applications
Group: Development/C

##############################
# Keep in sync with uw-imap main pkg version
# (no Requires: is required here)
Conflicts: %name < %version-%release
Conflicts: %name > %version-%release
# End of statements to keep in sync.
##############################

######################################
# Compatibility with future: we are going to rename (and probably split)
# the ...-devel subpkg to libc-client-devel & libc-client-devel-static
# (see No. 0001557 at bugs.altlinux.ru; we do not rename now because of
# the pre-Master 2.2 freeze)
Provides: libc-client-devel = %version-%release
# End of the statements for Compatibility with future
#########################################

%description
The %name package provides server daemons for both the IMAP (Internet
Message Access Protocol) and POP (Post Office Protocol) mail access
protocols.  The POP protocol uses a "post office" machine to collect mail
for users and allows users to download their mail to their local machine
for reading. The IMAP protocol provides the functionality of POP, but
allows a user to read mail on a remote machine without downloading it to
their local machine.

Install the %name package if you need a server to support the IMAP or the
POP mail access protocols.

These programs were developed at UW (University of Washington).

%description -n lib%name
The lib%name package contains the shared library for running programs
will use the UW IMAP (University of Washington's Internet Message Access Protocol) library.

%description devel
The %name-devel package contains the header files and static libraries for
developing programs which will use the UW IMAP library
(University of Washington's Internet Message Access Protocol library).

%prep
echo Using release number %release
%setup -q -n imap-%version
ln -s . imap
tar jxvf %SOURCE8

#patch9 -p1 -b .glibc-time
#patch0 -p1 -b .ssl
%patch1 -p1 -b .ALT
%patch10 -p1 -b .deb-port
%patch11 -p1 -b .deb-nonull
#patch12 -p1 -b .deb-blackbox
%patch13 -p1 -b .overflow
#patch14 -p1 -b .imap4
%patch4 -p1 -b .flock

%if %WithMaildir
%patch20 -p1 -b .maildir
%patch22 -p1 -b .glibc-time-maildir
%endif

# RH says:
# It looks like this is required by the license (see COPYRIGHT), so here goes....
%__subst 's/^(char \*version = ".+)(";)/${1}alt$2/g' \
  src/i{mapd/imap,popd/ipop{2,3}}d.c

%build
%add_optflags %optflags_shared
%make_build \
%if %WithSSL
    SSLTYPE=unix.nopwd \
%else
    SSLTYPE=none \
%endif
%if %WithMaildir
    EXTRADRIVERS=maildir \
%else
    EXTRADRIVERS= \
%endif
    EXTRASPECIALS='MAILSPOOL=%_var/mail SSLDIR=%_ssldir SSLINCLUDE=%_includedir SSLLIB=%_libdir SSLCERTS=%_pemdir' \
    lnp

#cd c-client
#gcc -shared -o lib%name.so.%version -Wl,-soname=lib%name.so.%%major \
#        `ar t lib%name.a` -L/usr/X11R6/lib -ldl -lpam -lcrypto

%install
mkdir -p %buildroot%_man8dir
install -p -m644 src/*/*.8 %buildroot%_man8dir

mkdir -p %buildroot%_sbindir
install -p -m755 ipopd/ipop{2,3}d imapd/imapd %buildroot%_sbindir
ln -s imapd %buildroot%_sbindir/rimapd

mkdir -p %buildroot%_libdir
#install -p -m755 c-client/lib%name.so.%version %buildroot%_libdir
#ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so

# docs:
install -p -m0644 %SOURCE9 README.IMAPS
# remove the not-patched file:
rm -f docs/SSLBUILD.ssl
# we don't wnat it in the main pkg:
mv docs/internal.txt .

#devel
mkdir -p %buildroot%_includedir/%name
install -p -m644 ./c-client/*.h %buildroot%_includedir/%name
install -p -m644 ./src/osdep/tops-20/shortsym.h %buildroot%_includedir/%name
install -p -m644 ./c-client/c-client.a %buildroot%_libdir/libc-client.a

install -p -m640 -D %SOURCE1 "%buildroot%_sysconfdir/pam.d/imap"
install -p -m640 -D %SOURCE1 "%buildroot%_sysconfdir/pam.d/pop"

for f in %SOURCE2 %SOURCE3 %SOURCE12 %SOURCE13 %SOURCE4 \
%if %WithSSL
%SOURCE5 %SOURCE6 \
%endif
; do
	d=${f##*/}
	d=${d%%.xinetd}
	install -p -m640 -D "$f" "%buildroot%_sysconfdir/xinetd.d/$d"
done

%if %WithSSL
# Generate ghost *.pem files
mkdir -p %buildroot%_pemdir
touch %buildroot%_pemdir/{imapd,ipop3d}.pem
chmod 600 %buildroot%_pemdir/{imapd,ipop3d}.pem
%endif

%post
%if %WithSSL
# If no cert, migrate stunnel.pem, or generate a new cert
pushd %_pemdir &> /dev/null || :

ANCESTOR=stunnel.pem
for CERT in imapd.pem ipop3d.pem; do
   if [ ! -e "$CERT" ]; then
      if [ -e "$ANCESTOR" ]; then
         echo -n "%name: Installing your $ANCESTOR certificate as $CERT "
         install -p -m0600 "$ANCESTOR" "$CERT" \
          && echo "succeeded." || echo "failed."
      elif [ -e make-dummy-cert ]; then
         echo "%name: Generating new certificate for $CERT."
        sh -s "$CERT" < make-dummy-cert
      else
        echo "%name: Remember to read docs and make $(pwd)/$CERT!" >&2
      fi
   fi
done || :

popd &> /dev/null || :
%endif

/sbin/service xinetd condreload || :

%postun
if [ $1 = 0 ]; then
	/sbin/service xinetd condreload || :
fi

#%files -n lib%name
#%_libdir/*.so.*

%files devel
#%_libdir/*.so
%_libdir/*.*a
%_includedir/*
%doc internal.txt

%files
%config(noreplace) %_sysconfdir/*.d/*
%_sbindir/*
%_man8dir/*
%doc README CPYRIGHT docs/*
%if %WithSSL
%doc README.IMAPS
%endif

%if %WithSSL
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %_pemdir/*.pem
%endif

%changelog
* Thu Oct 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2004g-alt3.1
- rebuild (with the help of girar-nmu utility)

* Tue Nov 24 2009 Denis Smirnov <mithraen@altlinux.ru> 2004g-alt3
- cleanup spec
- fix build

* Thu Dec 11 2008 Denis Smirnov <mithraen@altlinux.ru> 2004g-alt2
- add conflicts to courier-imap and cyrus-imapd
- cleanup spec

* Sun Sep 10 2006 Denis Smirnov <mithraen@altlinux.ru> 2004g-alt1
- update from 2001a to 2004g version
- update must patches

* Sun Jul 02 2006 Denis Smirnov <mithraen@altlinux.ru> 2001a-alt10
- fix building

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2001a-alt9.1.1
- Rebuilt with openssl-0.9.7d.

* Fri Feb  7 2003 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt9.1
- built once more -- the previous release seems to have been lost :-(,
  no changes

* Thu Feb  6 2003 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt9
- deps:
  + provide abstract IMAPD & POP3D service (as virtual pkgs) and describe
    the relations with other such pkgs (fixes No. 0002154 at bugs.altlinux.ru);
  + %name-devel doesn't depend on %name anymore; other deps improvements
    (No. 0001557).

* Fri Oct 18 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt8
- follow the SSLDIR relocation:
  (Make sure you moved your certs to the new location before you upgrade!)
  + set %%_ssldir according openssl-config output (/var/lib/ssl now)
  + fix docs
- use %_var/mail/ as the mailbox directory (instead of /var/spool/mail/)
  as FHS requires

* Thu Oct 17 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt7
- Fixed:
  + locking on reiserfs (#0001400 at bugs.altlinux.ru): make the locking
    routine work on all kinds of FS through fcntl(2), and make it not silently
    be a no-op (always issue a warning if locking is disabled)
  + client address logging in server_init() (thanks to Andrey Khavryuchenko
    <akhavr at kds.com.ua> and RH: #60290 at bugzilla.redhat.com)
  + libc-client's support for a certain IMAP extension
    (not supported by UW imapd yet; more info inside patch16)
- post: clean up the certificate creation script a bit
- spec-file (no impact on the binaries):
  + pass SSLCERTS directory in %%build
  + -DIGNORE_LOCK_EACCESS_ERRORS is not valid anymore, removed (boguswarning
    patch substitutes this setting)
  + pass EXTRADRIVERS (with mbox turned off) in %%build, not as a patch
    (was a part of uw-imap-2001a-ALT-custom.patch)
  + remove EXTRACFLAGS=-DDISABLE_POP_PROXY=1 from %%build (done by a patch)

* Wed May 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2001a-alt6
- Replaced "xinetd reload" with "xinetd condreload" (#0000924).
- PreReq: xinetd >= 2.3.4-alt3 (for correct reload).

* Tue May 14 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt5
- apply the fix for an overflow for IMAP4 reported in Bugtraq (anyway, IMAP4
  support is not compiled in, so this could be only important for people
  who build the server themselves);
- spec-file:
    + change the %%With* macros a bit;
    + enable defining %%release in command line;

* Tue May  7 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt4
- now, when the locking scheme has been cleaned, we drop the "bogus"
  warning about locking;

* Tue May  7 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt3
- code fixes:
  + use flock simulation via fcntl to be consistent with the other part
    of ALT Linux system, fcntl's error processing changed (patch4: flocksim);
  + two potential SegFaults (in message parsing -- patch13;
    and working with a specific blackbox config -- patch11);
- more ALT Linux (and RedHat- and Debian-like, FHS complaint) system specific
  customization (several patches merged):
  + change paths to the server binaries in configuration and docs;
  + add %_sbindir/rimapd (symlink);

* Tue Dec 18 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt2
- xinetd config files changed:
  + renamed (added uw- prefix);
  + uw-{imaps,pop3s} reflect the fact that the servers now support SSL internally, no stunnel is required;
  + uw-{simap,pop3} use the conventional stunnel scheme;
- install time scripts:
  + SSL certificates for the servers are generated at install time (the scripts based on RedHat's);
  + xinetd configuration reloaded;
- files:
  + inernal.txt moved to -devel subpkg;
  + other minor fixes in paths.

* Mon Dec 3 2001 Ivan Zakharyaschev <imz@altlinux.ru> 2001a-alt1
- new mainstream version (2001a);
- changed name: imap -> uw-imap;
- SSL/TLS are not just plain words any longer: it really works;
- for packagers:
  + synced with Pine patches; still need the openssl-paths patch for Makefile;
  + "flock" patches not applied;
  + "vfs" patch thrown away;
  + "boguswarning" patch replaced by setting Make-variables
     in the commandline in %%build;
  + "security" patch merged mainstream;
  + "glibc-time" patch adds \#include <utime.h>;
  + SSL devel locations specified in %%build;
  + "setcred" pacth for PAM not needed any more;
  + custom %%optflags_warnings -- otherwise really important warnings
    are hard too find.

* Thu Jun 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2000c-ipl3mdk
- Security fixes (mdk).

* Fri Mar 02 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 2000c-ipl2mdk
- the devel subpackage renamed back to imap-devel (was libimap-devel
  for a short while, but that name was misleading since there was no libimap pkg)
- fix build on glibc 2.2.2

* Fri Feb 02 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 2000c-ipl1mdk
- new source, patches redone:
    + flock
    + ssl -> openssl
    + setcred (pam related) not needed any more
    + sparc thrown away (already applied in the source)
    + version thrown away: now there is a more flexible substitution
      performed by perl in the prep-section

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 2000-ipl2mdk
- RE adaptions.
- Split subpackages.

* Thu Jan 11 2001 David BAUDENS <baudens@mandrakesoft.com> 2000-2mdk
- Don't apply sparc patch on non sparc archs (so, fix PPC build)
- %%config(noreplace)
- Macros

* Fri Nov 10 2000 Vincent Danen <vdanen@mandrakesoft.com> 2000-1mdk
- 2000
- change -devel description
- include SSL support
- fixed xinetd support for ipop2 (was using ipop3 for ipop2 incorrectly)

* Tue Sep 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.7c2-4mdk
- Pamstackizification.

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.7c2-3mdk
- Correct xinetd scripts.
- Add xinetd support for imap.

* Sun Sep 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.7c2-2mdk
- Fix bad link.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.7c2-1mdk
- BM.
- xinetd support.
- Merge rh patches.
- 4.7c2.
- Clean up sepcs.

* Sun Apr 02 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 4.7b_virtual-2mdk
- fixed group

* Thu Mar 02 2000 Jean-Michel Dault <jmdault@netrevolution.com> 4.7b_virtual-1mdk
- updated to 4.7b

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 4.7a_virtual-3mdk
- A fix for crashes caused by certain unusual tokens in message headers.
- updated patch

* Mon Feb 28 2000 Jean-Michel Dault <jmdault@netrevolution.com> 4.7a_virtual-2mdk
- moved docs in main package instead of devel

* Mon Feb 28 2000 Jean-Michel Dault <jmdault@netrevolution.com> 4.7a_virtual-1mdk
- upgraded to 4.7a
- added phall virtual patch for Linuxconf

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Wed Dec 31 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuild for Mandrake 7

* Sat Dec 12 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- Took mandrake adaptations (except SMP build) from 4.5-6mdk and updated to
  4.7. Now we have imap-devel
- Merged and re-made patch files

* Thu May 20 1999 Brian Bruns <bruns@magenet.com>
- Built on RH 5.2

* Thu May 20 1999 Henri Gomez <gomez@slib.fr>
- added devel package and libimap support

* Fri May 14 1999 Brian Bruns <bruns@magenet.com>
- Update to IMAP 4.6 beta

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- ipop3d service name was changed to "pop" now. Clearly somebody that hasn't
  got a clue about PAM stuff is messing around with the source.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Sat Mar 13 1999 Cristian Gafton <gafton@redhat.com>
- verson 4.5
- loose the noflock patch

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- added a -vfs patch because sys/statvfs on glibc 2.1 is different from what
  is available on the sun...
- build against glibc 2.1

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- use only fcntl locking.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.4.
- removed g+s bit to imapd.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- updated to 4.2.
- added g+s bit to imapd so that lock files can be created.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- Updated to the latest imap as of today...

* Wed Dec 10 1997 Cristian Gafton <gafton@redhat.com>
- Updated to the latest imap as of today...
- Updated the pam patch to reflect the new directory organization

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fix patch for new PAM spec compliance.

* Thu Oct 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Comply with change in PAM spec.
- Use a buildroot.

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved from pam.conf to pam.d

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Fixed buffer overrun in server_login().

