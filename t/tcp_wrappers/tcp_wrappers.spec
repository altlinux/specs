Name: tcp_wrappers
Version: 7.6
Release: alt11
Epoch: 1

Summary: A security tool which acts as a wrapper for network services
License: BSD-style
Group: System/Servers
Url: http://ftp.porcupine.org/pub/security/

%define srcname tcp_wrappers_7.6
# ftp://ftp.porcupine.org/pub/security/%srcname.tar.gz
Source: %srcname.tar
Source1: ftp://ftp.porcupine.org/pub/security/tcp_wrappers_license

# ftp://ftp.porcupine.org/pub/security/tcpd-blacklist-patch
Patch0: %srcname-up-tcpd-blacklist.patch
Patch1: %srcname-owl-alt-makefile.patch
Patch2: %srcname-openbsd-owl-cleanups.patch
Patch3: %srcname-openbsd-owl-ip-options.patch
Patch4: %srcname-owl-safe_finger.patch
Patch5: %srcname-steveg-owl-match.patch
Patch6: %srcname-alt-fix_options.patch
Patch7: %srcname-alt-shared.patch
Patch8: %srcname-alt-hosts_ctl.patch
Patch9: %srcname-alt-drop-percent_m.patch

Patch10: %srcname-deb-man-quoting.patch
Patch11: %srcname-deb-man-typos.patch
Patch12: %srcname-deb-man_portability.patch
Patch13: %srcname-deb-man-fromhost.patch
Patch14: %srcname-deb-man-more-pages.patch
Patch15: %srcname-deb-restore-sigalarm.patch
Patch16: %srcname-deb-siglongjmp.patch

Requires: libwrap = %epoch:%version-%release

%package -n libwrap
Summary: Security wrapper access control shared library
Group: System/Libraries

%package -n libwrap-devel
Summary: Security wrapper access control development library
Group: Development/C
Provides: tcp_wrappers-devel = %version
Obsoletes: tcp_wrappers-devel
Requires: libwrap = %epoch:%version-%release

%package -n libwrap-devel-static
Summary: Security wrapper access control development static library
Group: Development/C
Provides: tcp_wrappers-devel-static = %version
Obsoletes: tcp_wrappers-devel-static
Requires: libwrap-devel = %epoch:%version-%release

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -n libwrap
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-devel
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-devel-static
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%prep
%setup -n %srcname
install -p -m644 %SOURCE1 LICENSE
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

find -type f -name \*.orig -delete
bzip2 -9k README CHANGES

%build
%add_optflags %optflags_shared -D_REENTRANT -Dlint
%make_build linux BUGS=

%install
mkdir -p %buildroot{/%_lib,%_libdir,%_sbindir,%_includedir,%_mandir/man{3,5,8}}

install -pm755 safe_finger tcpd tcpdchk tcpdmatch try-from \
	%buildroot%_sbindir/

cp -a libwrap.{a,so}* %buildroot%_libdir/

# Relocate shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f") || continue
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

install -pm644 tcpd.h %buildroot%_includedir/

install -pm644 hosts_access.3 %buildroot%_man3dir/
install -pm644 hosts_access.5 hosts_options.5 %buildroot%_man5dir/
ln -s hosts_access.5 %buildroot%_man5dir/hosts.allow.5
ln -s hosts_access.5 %buildroot%_man5dir/hosts.deny.5
install -p -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 %buildroot%_man8dir/

%files
%_sbindir/*
%_man8dir/*
%doc BLURB CHANGES.* README.* DISCLAIMER Banners.Makefile LICENSE

%files -n libwrap
/%_lib/*.so.*
%_man5dir/*

%files -n libwrap-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%files -n libwrap-devel-static
%_libdir/*.a

%changelog
* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt11
- Rebuilt for debuginfo.

* Mon Oct 18 2010 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt10
- Imported a few patches from Debian package.
- Rebuilt for soname set-versions.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt9
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt8
- Uncompressed tarball, cleaned up specfile.

* Wed Oct 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt7
- Additionally export some eval_* symbols (#8143).

* Mon Aug 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt6
- Restricted list of global symbols exported by the library.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt5
- Added multilib support (#4897).

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt4
- Relocated man5 documentation (#2588).
- Added hosts_ctl declaration (#2959).

* Thu Feb 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt3
- Relocated shared library from /usr/lib to /lib (#0002312).

* Fri Dec 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt2
- Handle error conditions with table matching,
  patch from Steve Grubb, imported from Owl.

* Sat Nov 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:7.6-alt1
- Reviewed patches; removed all but Owl's patches.
- Fixed compilation of fix_options.c via defining "struct ip_options". 
- Build libwrap shared library.
- Libificated.

* Thu Feb 21 2002 Stanislav Ievlev <inger@altlinux.ru> 7.6-ipl18mdk
- Merged Owl patches.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 7.6-ipl17mdk
- Merged RH patches:
  + fix gethostbyname to work better with dot "." notation (pb);
  + permit hosts.{allow,deny} to be assembled from included components (jbj).
  + permit '*' and '?' wildcard matches on hostnames (jbj).
  + security hardening (jbj).

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 7.6-ipl16mdk
- RE adaptions.

* Tue Sep 05 2000 Francis Galiegue <fg@mandrakesoft.com> 7.6-16mdk
- Removed setenv.o from libwrap.a

* Fri Jul 28 2000 Francis Galiegue <fg@mandrakesoft.com> 7.6-15mdk
- Spec file fixes
- %files list fixes
- permission fixes
- use links, not symlinks
- include doc in only one package, not both

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.6-14mdk
- fix %%clean
- Christian Zoffoli <czoffoli@linux-mandrake.com> :
	* fixed permission
	* removed %group
	* removed _sysconfdir
	* macroszifications
	* new IPv6 patch v1.9

* Fri Jun 23 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.6-13mdk
- compiled with IPv6 patch

* Sat Apr 08 2000 John Buswell <johnb@mandrakesoft.com> 7.6-12mdk
- split devel elements into devel package
- removed version number from spec file
- added docs to devel package

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 7.6-11mdk
- Fixed groups
- spec-helper

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- add netgroup support (r).

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- close setenv bug (problem #690)
- spec file cleanup

* Thu Jun 25 1998 Alan Cox <alan@redhat.com>
- Erp where did the Dec 05 patch escape to

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- don't build setenv.o module -- it just breaks things

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- upgrade to 7.6

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Upgraded to version 7.5
- Uses a build root
