Name: mutt
Version: 1.4.2.3
Release: alt4
Serial: 3

%def_without dotlock
%define docdir %_docdir/mutt-%version

Summary: A text mode mail and news user agent
License: GPL
Group: Networking/Mail
Url: http://www.mutt.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.mutt.org/pub/mutt/mutt-%version.tar.gz
Source: mutt-%version.tar
Source1: http://jblosser.firinn.org/pub/config/mutt/mutt-16.xpm
Source2: http://jblosser.firinn.org/pub/config/mutt/mutt-32.xpm
Source3: http://www.math.fu-berlin.de/~guckes/mutt/mutt-48.xpm
Source4: mutt.menu
Source5: http://www.fefe.de/muttfaq/faq.html
Source6: mutt-FAQ.ru.html
Source7: http://solidlinux.com/~justin/mutt/mutt-gnupg-howto.txt
# http://mutt.sourceforge.net/imap/
Source8: Mutt-and-IMAP.html
Source10: patchlist.sh

%define vvv_version 1.4.2.2
Patch11: http://mutt.kiev.ua/download/mutt-%vvv_version/mutt-%vvv_version-vvv-compressed.patch
Patch12: http://mutt.kiev.ua/download/mutt-%vvv_version/mutt-%vvv_version-vvv-initials.patch
Patch13: http://mutt.kiev.ua/download/mutt-%vvv_version/mutt-%vvv_version-vvv-nntp.patch
Patch14: http://mutt.kiev.ua/download/mutt-%vvv_version/mutt-%vvv_version-vvv-quote.patch

Patch16: mutt-1.4-headercache.patch 

Patch21: mutt-1.3.22.1-alt-no_dotlock.patch
Patch22: mutt-1.2.5-alt-8bitpgp.patch
Patch23: mutt-1.3.28-alt-flea.patch
Patch24: mutt-1.3.22.1-alt-altyesorno.patch
Patch25: mutt-1.3.22.1-alt-send_charset-koi8-r.patch
Patch26: mutt-1.3.22.1-alt-muttrc-show-docs.patch
Patch27: mutt-1.3.22.1-alt-compressed-hooks.patch
Patch28: mutt-1.4-alt-m4-fixes.patch
Patch29: mutt-1.4-owl-muttbug-tmp.patch
Patch30: mutt-1.4.2.1-owl-tmp.patch
Patch31: mutt-1.4-alt-tmp.patch
Patch32: mutt-1.4-alt-fixes.patch
Patch33: mutt-1.4-alt-gpg.patch
Patch34: mutt-1.4.2.1-alt-stat_check.patch
Patch35: mutt-1.4.2.1-owl-man.patch
Patch36: mutt-1.4.2.1-owl-bound.patch
Patch37: mutt-1.4.2.2i-alt-fixes.patch
Patch38: mutt-1.4.2.3-alt-bound.patch

Requires: MTA, urlview, mailcap

BuildPreReq: OpenSP groff-base libncursesw-devel libssl-devel sgml-tools

%description
Mutt is a feature-rich text-based mail user agent.  Mutt supports local
and remote mail spools (POP3 and IMAP, including with SSL), MIME, OpenPGP
(PGP/MIME) with GnuPG and PGP, colored display, threading, and a lot of
customization including arbitrary message headers, key remapping, colors,
and more.

%prep
%setup -q
install -pm755 %SOURCE10 .

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%patch16 -p1

%patch21 -p1
#%patch22 -p1
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
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

find -type f -name \*.orig -delete

%build
export ac_cv_path_GDB=/usr/bin/gdb
export ac_cv_path_ISPELL=/usr/bin/ispell
export ac_cv_path_SENDMAIL=/usr/sbin/sendmail
%if_without dotlock
export mutt_cv_worldwrite=no
export mutt_cv_groupwrite=no
%endif

# Correct manual name (#2710).
%__subst -p 's,/manual\.txt\\n,/manual.txt.bz2\\n,g' Muttrc.head.in

%add_optflags -D_GNU_SOURCE -fno-strict-aliasing
make -C m4 -f Makefile.am.in
autoreconf -fisv -I m4
%configure \
	--with-sharedir=%_sysconfdir \
	--with-docdir=%docdir \
	--enable-pop \
	--enable-imap \
	--enable-nntp \
	--disable-warnings \
	--with-ncurses \
	--disable-domain \
	--enable-nfs-fix \
	--with-charmaps \
	--with-ssl \
	--enable-compressed

make clean
make -C doc clean-real
%make_build

%install
%makeinstall sharedir=%buildroot%_sysconfdir docdir=%buildroot%docdir

# Icons.
install -pD -m644 %SOURCE1 %buildroot%_miconsdir/mutt.xpm
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/mutt.xpm
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/mutt.xpm

# Menu.
install -pD -m644 %SOURCE4 %buildroot%_menudir/mutt

# More docs.
install -p -m644 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 *.nntp \
	%buildroot%docdir/
find %buildroot%docdir/ \( -name \*.txt -or -iname changelog\* \) -size +8k -print0 |
	xargs -r0 bzip2 -9 --

# Fix configs.
find %buildroot%_sysconfdir -type f -print0 |
	xargs -r0 grep -FZl '%buildroot' |
	xargs -r0 %__subst -p 's|%buildroot||g' --

rm %buildroot%_sysconfdir/mime.types

%find_lang mutt

%files -f mutt.lang
%if_with dotlock
%attr(2711,root,mail) %_bindir/mutt_dotlock
%else
%exclude %_mandir/man?/*dotlock*
%endif
%config(noreplace) %_sysconfdir/Muttrc
%_bindir/flea
%_bindir/mutt
%_bindir/muttbug
%_bindir/pgp*
%_mandir/man?/*
%_menudir/mutt
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%docdir

%changelog
* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.3-alt4
- Added hooks to handle xzipped folders.
- Rebuilt with libssl.so.10.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.3-alt3
- Removed obsolete %%update_menus/%%clean_menus calls.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.3-alt2
- Requires: mailcap.

* Wed May 30 2007 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.3-alt1
- Updated to 1.4.2.3 (fixes CVE-2007-1558).

* Wed May 16 2007 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.2i-alt3
- mutt_gecos_name(): Fixed potential buffer overflow
  (CVE-2007-2683, patch from OpenBSD).
- mutt_expand_fmt(): Fixed potential read beyond buffer bounds.

* Mon Apr 02 2007 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.2i-alt2
- Fixed several bugs found by compiler.
- Linked with libncursesw.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.2i-alt1
- Updated to 1.4.2.2i.

* Tue Jun 27 2006 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt8
- Applied upstream fix for potential stack-based buffer overflow
  when processing an overly long namespace from the IMAP server.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt7
- Fixed build with new gcc compiler.

* Fri Mar 10 2006 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt6
- Relocated icons, compressed changelogs.

* Tue Aug 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt5
- Introduced extra buffer non-overflow safety for handler.c (Owl).
- Updated the SEE ALSO sections of all manpages (Owl).

* Thu Apr 14 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt4
- Fixed build with fresh autotools.

* Wed Feb 02 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt3
- Workaround STAT_CHECK bug.
- Do not package mutt_dotlock(1).
- Package one-page IMAP guide (fixes #5453).

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3:1.4.2.1i-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 03 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt2
- Reenabled forced 7bit pgp signed data conversion (#3764).
- Applied IMAP headers cache patch from Tudor Bosman at dwyn.net.

* Fri Feb 13 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.2.1i-alt1
- Updated to 1.4.2.1i (cvs-20020213-bound patch included into release).

* Mon Feb 09 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.1i-alt3
- Backported patch from CVS to fix Mutt crash on certain e-mails;
  this can occur when an UTF-8 locale is used on wide terminals.

* Thu Aug 28 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.1i-alt2
- Corrected manual filename entry (#2710).

* Sat Mar 22 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.1i-alt1
- Updated to 1.4.1i.
- Optimized by size "rr.compressed" and "vvv.nntp" patches.
- Enabled regeneration of manual.txt.
- Enabled compression of large text documentation files.
- Updated sample gpg.rc file.

* Fri Jan 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2:1.4i-alt3
- Improved the package description (Owl).
- Temporary files handling fixes (Owl).
- Additional temporary files handling fixes for rr/vvv patches.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.4i-alt2
- Fixed -I/usr/include compilation warnings.
- Explicitly use autoconf-2.13 and automake-1.4 for build.
- Use subst instead of perl for build.

* Thu May 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.4i-alt1
- 1.4i.

* Tue May 07 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.99i-alt1
- 1.3.99i.
- Don't use dotlocking for mailboxes, fcntl(2) should be enough.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.28i-alt2
- Fixed flea dependencies.
- Optimized and updated buildrequires.

* Fri Mar 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.28i-alt1
- 1.3.28i.
- Added mutt-FAQ.ru.html (mike).

* Mon Jan 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.27i-alt1
- 1.3.27i.
- Set default send_charset to
  "us-ascii:iso-8859-1:koi8-r:koi8-u:windows-1251:utf-8" (#405).

* Mon Jan 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.26i-alt1
- 1.3.26i.

* Fri Jan 04 2002 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.25i-alt1
- 1.3.25i (security).

* Mon Dec 10 2001 Dmitry V. Levin <ldv@altlinux.org> 1:1.3.24i-alt1
- 1.3.24i.

* Mon Nov 12 2001 Dmitry V. Levin <ldv@altlinux.org> 1:1.3.23.2i-alt1
- 1.3.23.2i.

* Thu Nov 01 2001 Dmitry V. Levin <ldv@altlinux.org> 1:1.3.23.1i-alt1
- 1.3.23.1i.

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.org> 1.3.22.1i-alt2
- Added more default keybindings for F1 key.
- Added default hooks for compressed folders.
- Added mutt-gnupg-howto.txt

* Tue Sep 18 2001 Dmitry V. Levin <ldv@altlinux.org> 1.3.22.1i-alt1
- 1.3.22.1i
- Added patches from http://mutt.kiev.ua/download/.

* Mon Jul 30 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.5i-ipl16mdk
- NNTP support fixed, NNTPPost added.
- Corrected mutt_dotlock permissions (ldv).
- Corrected requires (ldv).

* Wed Jul 25 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.5i-ipl15mdk
- NNTP support added. See mutt-nntp.html for details and configuration

* Fri Jun 29 2001 AEN <aen@logic.ru> 1.2.5i-ipl14mdk
- ru.po fixed

* Wed May 23 2001 Dmitry V. Levin <ldv@altlinux.org> 1.2.5i-ipl14mdk
- Fixed autodependencies.

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.org> 1.2.5i-ipl12mdk
- Modified 8bitpgp patch to fix build with new cpp (Mikhail Zabaluev <mhz@altlinux.ru>).

* Fri Mar 23 2001 Dmitry V. Levin <ldv@altlinux.org> 1.2.5i-ipl11mdk
- Added altyesorno patch (based on patch from Alexey Voinov <voins@voins.program.ru>).

* Tue Mar 20 2001 Dmitry V. Levin <ldv@altlinux.org> 1.2.5i-ipl10mdk
- Merged RH patches

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl9mdk
- Added special recognition for "iso-8859-1" charmap.

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl8mdk
- Cleanup pgp patch.
- Added special recognition for "ansi-x3-4-1968" charmap.

* Fri Jan 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl7mdk
- Added default charmap recognition.

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl6mdk
- Enabled ssl support.
- Disabled forced 7bit pgp signed data conversion.
- Fixed out $RPM_BUILD_ROOT from config file.

* Tue Oct 12 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl5mdk
- Addeded faq.html
- Automatically added BuildRequires.

* Wed Oct 04 2000 Daouda Lo <daouda@mandrakesoft.com> 1.2.5i-5mdk
- provide icons for menu

* Mon Sep 04 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.5i-ipl4mdk
- RE adaptions

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.5-3mdk
- automatically added BuildRequires

* Wed Aug  2 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.2.5i-2mdk
- some of us like docs and samples so put them back in
- fix docdir
- more macros

* Sat Jul 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.5i-1mdk
- new version
- macrosifications
- build for the BM

* Fri Jul 07 2000 DindinX <odin@mandrakesoft.com> 1.2.4i-2mdk
- merge Geoffrey Lee's spec changes
- remove /etc/mimes.types from %files which caused a conflit w/ mailcap

* Fri Jul 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.4i-1mdk
- new release (This version fixes a couple of problems present in 1.2.2, and
  one problem leading to crashes whose fix was missing from 1.2.3.)

* Mon Jun 26 2000 DindinX <odin@mandrakesoft.com> 1.2.2i-3mdk
- put the Serial: tag back

* Fri Jun 23 2000 DindinX <odin@mandrakesoft.com> 1.2.2i-2mdk
- fix the build as user the right way :)

* Thu Jun 22 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2.2i-1mdk
- 1.2.2i
- removed %%defattr which was causing readonly inboxes
- build with ncurses instead of slang to get colors working properly
- removed SSL support (won't compile due to keymaps bug)
- fixed build

* Tue Jun 20 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2i-2mdk
- enable charmaps in configure
- removed --enable-compressed (no patch)

* Mon Jun 19 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.2i-1mdk
- 1.2i
- enable SSL and NFS fixes in configure

* Wed Apr 27 2000 DindinX <odin@mandrakesoft.com> 1.0.1i-7mdk
- Recompile fix.
- fix the color scheme.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1i-6mdk
- By default active colors.
- Believe me or not, fix menu and %post.
- Use find_lang macros for locales.

* Tue Apr  4 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1i-5mdk
- Fix another chmousucks in menu (yes me too i can believe it).

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1i-4mdk
- Fix chmousucks in menu.
- Add icons in menu.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1i-3mdk
- Fix menu entry (don't only cp the meny entry from your debian box
  dindin ;)).

* Fri Mar 24 2000 DindinX <odin@mandrakesoft.com> 1.0.1i-2mdk
- Specs and group fixes
- Added menu support

* Sun Feb 06 2000 Andre Steden <andre@steden.de>
- 1.0.1
- add compressed folders patch
- add colour patch

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Thu Oct 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.0.

* Wed Oct  6 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 1.0pre3.

* Mon Aug 09 1999 Daouda LO <daouda@mandrakesoft.com>
 -0.95.7
 -added manual.sgml in documents.

* Sun May 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix bug of locales.

* Wed Apr 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Mandrake adaptations.
- update to 0.99.5.

* Mon Mar  8 1999 Bill Nottingham <notting@redhat.com>
-  update to 0.95.4 - fixes a /tmp race

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- the RETURN OF WMCONFIG! Aiyeee!

* Fri Feb 12 1999 Bill Nottingham <notting@redhat.com>
- 0.95.3 - fixes mailcap handling

* Mon Jan  4 1999 Bill Nottingham <notting@redhat.com>
- 0.95.1

* Sat Dec 12 1998 Bill Nottingham <notting@redhat.com>
- 0.95

* Fri Jul 31 1998 Bill Nottingham <notting@redhat.com>
- backport some 0.94.2 security fixes
- fix un-setgid
- update to 0.93.2

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- update to 0.93.1.
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
- Initial version for 0.81(e)
