# vim: set ft=spec: -*- rpm-spec -*-

%def_disable debug
#def_enable Werror

%define oname mutt
%define branch 1.5
Name: %oname%branch
Version: 1.5.21
Release: alt2
Serial: 3

%def_without dotlock
%define docdir %_docdir/%name-%version

Summary: A text mode mail and news user agent
Group: Networking/Mail
License: GPL
Url: http://www.mutt.org/

Packager: Sir Raorn <raorn@altlinux.ru>

Source: ftp://ftp.%oname.org/%oname/devel/%oname-%version.tar
Patch: %oname-%version-%release.patch

# http://jblosser.firinn.org/pub/config/mutt/ (DEAD)
Source1: %oname-16.xpm
# http://jblosser.firinn.org/pub/config/mutt/ (DEAD)
Source2: %oname-32.xpm
# http://www.math.fu-berlin.de/~guckes/mutt/ (DEAD)
Source3: %oname-48.xpm
Source4: %name.desktop
Source5: http://www.fefe.de/%{oname}faq/faq.html
Source6: mutt-FAQ.ru.html
# http://solidlinux.com/~justin/mutt/ (DEAD)
Source7: %oname-gnupg-howto.txt
# http://mutt.sourceforge.net/imap/
Source8: Mutt-and-IMAP.html

Requires: urlview

Conflicts: %oname

# Automatically added by buildreq on Mon Jun 02 2008
BuildRequires: OpenSP docbook-dtds docbook-style-xsl libgdbm-devel libgpgme-devel libidn-devel libncursesw-devel libsasl2-devel libssl-devel lynx mailcap xsltproc zlib-devel

%description
Mutt is a feature-rich text-based mail user agent.  Mutt supports local
and remote mail spools (POP3 and IMAP, including with SSL), MIME, OpenPGP
(PGP/MIME) with GnuPG and PGP, colored display, threading, and a lot of
customization including arbitrary message headers, key remapping, colors,
and more.

%prep
%setup -q -n %oname-%version
%patch -p1

%build
export ac_cv_path_GDB=/usr/bin/gdb
export ac_cv_path_ISPELL=/usr/bin/ispell
export ac_cv_path_SENDMAIL=/usr/sbin/sendmail
%if_without dotlock
export mutt_cv_worldwrite=no
export mutt_cv_groupwrite=no
%endif

%add_optflags -std=c99
%autoreconf -I m4
%configure \
	--with-docdir=%docdir \
	--enable-gpgme \
	--enable-pop \
	--enable-imap \
	--enable-smtp \
	--enable-nntp \
	%{subst_enable debug} \
	--enable-nfs-fix \
	--enable-compressed \
	--enable-hcache \
	--with-curses \
	--with-gss \
	--with-ssl \
	--with-sasl \
	--with-idn \
	#

%make clean
%make_build

%install
%make_install DESTDIR=%buildroot install

# Icons.
install -pD -m644 %_sourcedir/%oname-16.xpm %buildroot%_miconsdir/%oname.xpm
install -pD -m644 %_sourcedir/%oname-32.xpm %buildroot%_niconsdir/%oname.xpm
install -pD -m644 %_sourcedir/%oname-48.xpm %buildroot%_liconsdir/%oname.xpm

# Menu.
install -pD -m644 %_sourcedir/%name.desktop %buildroot%_desktopdir/%name.desktop

# More docs.
install -p -m644 %_sourcedir/{faq.html,mutt-FAQ.ru.html,%oname-gnupg-howto.txt,Mutt-and-IMAP.html} *.nntp \
	%buildroot%docdir/
find %buildroot%docdir/ \( -name \*.txt -o -name ChangeLog\* \) -size +8k -print0 |
	xargs -r0 bzip2 -9 --

# HACK
[ -f %buildroot%docdir/manual.txt.bz2 ] || exit 1

# Fix configs.
find %buildroot%_sysconfdir -type f -print0 |
	xargs -r0 grep -FZl "%buildroot" |
	xargs -r0 sed -i "s|%buildroot||g" --

# Don't package flea, use ALT bugzilla
cat <<EOF > %buildroot%_bindir/flea
#!/bin/sh

exec >&2
cat <<EOS
\${0##*/}: Don't panic!

You are using heavily patched unstable version of Mutt mail client.
Mutt authors are not responsible for anything, that could be broken
in this build, so don't bother them.  Instead, visit ALT Linux
Bugzilla on https://bugzilla.altlinux.org/ and fill a bug report
against %name package.

You are using %name-%version-%release RPM package.

So Long, and Thanks for All the Fish.
EOS
exit 1
EOF

%find_lang %oname

%files -f %oname.lang
%if_with dotlock
%attr(2711,root,mail) %_bindir/mutt_dotlock
%endif
%config(noreplace) %_sysconfdir/Muttrc
%_bindir/flea
%_bindir/mutt
%_bindir/muttbug
%_bindir/pgp*
%_bindir/smime_keys
%_mandir/man?/*
%_desktopdir/%name.desktop
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%docdir

%changelog
* Thu Nov 18 2010 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.21-alt2
- hg snapshot 20101013 AKA 57568da7d9aa

* Wed Sep 15 2010 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.21-alt1
- [1.5.21]
  + $mail_check_recent controls whether all unread mail or only new mail
    since the last mailbox visit will be reported as new
  + %D format expando for $folder_format

* Sat Aug 14 2010 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt6
- hg snapshot 20100813 AKA 78b6f4b914c8
  ! $thorough_search defaults to yes
  + imap-logout-all closes all open IMAP connections
- Dropped obsolete altyesno patch (mutt uses locale information for
  yes/no questions since 1.3.8)

* Sun Aug 08 2010 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt5
- hg snapshot 20100807 AKA cc881d855f05

* Sat Jan 02 2010 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt4
- hg snapshot 20091229 AKA 31881f38ca1e
- Fixed NULL-pointer dereference while reading IMAP mailbox (closes: #21040)

* Tue Nov 10 2009 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt3
- hg snapshot 20091029 AKA 89fb586edda2
  ! header/body cache paths are always UTF-8
  + $wrap_headers to control outgoing message's header length
  + send-hooks now run in batch mode; previously only send2-hooks ran

* Wed Jun 24 2009 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt2
- hg snapshot 20090623 AKA f467353f5657
  + all text/* parts can be displayed inline without mailcap
  + fix atime/mtime screwage for mbox folders

* Sun Jun 21 2009 Alexey I. Froloff <raorn@altlinux.org> 3:1.5.20-alt1
- [1.5.20] (closes: #20476)
  ! $fcc_attach is a quadoption now
  + $honor_disposition to honor Content-Disposition headers
  + $search_context specifies number of context lines for search results
    in pager/page-based menus
  ! ssl_use_sslv2 defaults to no
  + uncolor works for header + body objects, too
  + the "flagged" and "replied" flags are enabled/supported for
    POP when built with header caching
  ! browser correctly displays maildir's mtime
  + <set-flag> and <clear-flag> work in the pager, too
  + ~x pattern also matches against In-Reply-To
  + lower case patterns for string searches perform case-insensitive
    search as regex patterns do (except IMAP)
  + $ssl_verify_dates controls whether mutt checks the validity period of
    SSL certificates
  + $ssl_verify_hostname controls whether mutt will accept certificates whose
    host names do not match the host name in the folder URL.
- Removed dependency on perl(timelocal.pl) (closes: #7061)

* Wed Feb 04 2009 Sir Raorn <raorn@altlinux.ru> 3:1.5.19-alt1
- [1.5.19]
  + support for SSL certificate chains
  + <what-key> function works in pager, too
  + support for tokyocabinet (qdbm successor)
- Dropped obsolete %%update_menus/%%clean_menus calls

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 3:1.5.18-alt4
- hg snapshot 20081030 AKA c2439fc68cd6
 ! $move now defaults to "no" instead of "ask-no"
 + $imap_pipeline_depth controls the number of commands that mutt can issue
   to an IMAP server before it must collect the responses
 + $ssl_client_cert available with gnutls as well as openssl
 + 'mime_lookup application/octet-stream' added to system Muttrc
- Make it compile with recent gcc

* Tue Jun 17 2008 Sir Raorn <raorn@altlinux.ru> 3:1.5.18-alt3
- Now code really updated to match changelog:
 + Fixed build with --enable debug (reported by kas@)
 + Also install UPDATING
 + Fixed segfault when viewing some attachements with non-sane
   mailcap entry (reported by kas@)

* Wed Jun 11 2008 Sir Raorn <raorn@altlinux.ru> 3:1.5.18-alt2
- Fixed build with --enable debug (reported by kas@)
- Also install UPDATING
- Fixed segfault when viewing some attachements with non-sane
  mailcap entry (reported by kas@)

* Tue Jun 03 2008 Sir Raorn <raorn@altlinux.ru> 3:1.5.18-alt1
- [1.5.18] (hg snapshot 20080530 AKA f467353f5657)
- Fixed index_color message highlighting when limit is set
- Added "modern" <F1> sequence alias for brain-damaged terminal emulators

* Mon Dec 10 2007 Sir Raorn <raorn@altlinux.ru> 3:1.5.17-alt1
- [1.5.17]

* Tue Sep 11 2007 Sir Raorn <raorn@altlinux.ru> 3:1.5.16-alt2
- Don't package vendor-supplied flea(1), print a message about
  ALT bugzilla (closes: #12741)
- Use compressed manual in <F1> keybindings (lost in upgrade)

* Thu Sep 06 2007 Sir Raorn <raorn@altlinux.ru> 3:1.5.16-alt1
- [1.5.16]

* Tue Mar 20 2007 Sir Raorn <raorn@altlinux.ru> 3:1.5.14-alt1
- [1.5.14]

* Mon Dec 11 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.13-alt1.3
- Fixed non-japaneese 8-bit output

* Mon Dec 11 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.13-alt1.2
- Enabled SMTP support

* Mon Dec 11 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.13-alt1.1
- Fixed typo in filechooser code.

* Mon Dec 11 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.13-alt1
- [1.5.13]
- Updated build deps
- Added patches:
  + dgc.uncollapsenew.1 (from http://home.uchicago.edu/~dgc/mutt/)
  + mutt-ng.attach_remind (from http://developer.berlios.de/patch/?func=detailpatch&patch_id=581&group_id=2853)
  + bc.smtp.14 (from http://mutt.kublai.com/)
- Removed patches:
  + aw.jumptagged
  + dgc.attach (merged upstream)
  + dgc.isalias
  + ats.parent_match
  + cb.chdir
  + cb.tag-invert
  + tg.mutt-thread (merged upstream)
  + cd.source_multiple
  + nr.crypt-autohook
  + sde.libesmtp (replaced by bc.smtp)
  + rr.compressed.ranty-fix (merged upstream)
  + alt-imap-complete (merged upstream)

* Sat Jun 03 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.11-alt3
- Built with libncursesw

* Sat Mar 18 2006 Sir Raorn <raorn@altlinux.ru> 3:1.5.11-alt2
- Fixed segfault in imap completion (closes: #9257, mutt bugs #2079 and #2112)
- Icons moved to right places

* Mon Oct 03 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.11-alt1
- [1.5.11]
- Regenerated all patches for 1.5.11
- Documented sec.pager_status_on_top patch (closes: #7109)
- Added patches:
  + dgc.flagsafe (from http://home.uchicago.edu/~dgc/sw/mutt/)
  + dgc.xlabel_sort (from http://home.uchicago.edu/~dgc/sw/mutt/)
- Updated patches:
  + owl-bound (latest revision from Owl CVS)
  + dgc.attach (v6 for 1.5.11, soon-to-be-included in upstream)
  + dgc.xlabel_ext (v7 from http://home.uchicago.edu/~dgc/sw/mutt/)
- Removed patches:
  + 1.4-alt-fixes (not needed)
  + tamo.namequot (closes: #8052)
  + ab+tg+tamo.menu (problem fixed in upstream)
  + mutt-ng.imap_reconnect (applied patch was incomplete, see also
    http://marc.theaimsgroup.com/?l=mutt-dev&m=112657531026080)
- Replaced patches msyk.iconvhook, mt.slanglib, tamo.pgp_charsethack,
  tt.assumed_charset, tt.attach_charset, tt.create_rfc2047_params,
  tt.linear_white_space, tt.tree_width and tt.wcwidth
  with cumulative mutt-j.multi-charset patch, fixed WC_FUNCS ifdef's

* Tue Aug 23 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.10i-alt3
- Do not use buffer overflow patch from pvalchev, adopted
  mutt-1.4.2.1-owl-bound.diff from Owl
- Do not build "complete documentaion".  Patch from Debian package

* Mon Aug 22 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.10i-alt2
- Removed dependency on perl(timelocal.pl) (closes: #7061)
- Fixed buffer overflow in handler.c (muttbug#2033, patch by Peter Valchev)

* Sun Aug 21 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.10i-alt1
- [1.5.10i]
- Updated FAQ to 1.0 patchlevel 18 (Source5)
- Links to icons and mutt-gnupg-howto seems to be dead, URLs removed
- Fixed manual.txt generation
- Compile mutt without warnings, however -Werror breaks some
  configure tests (alt-fixes.patch)
- Updated ALT patches:
  + alt-altyesorno.patch
  + alt-owl-tmp.patch
- Major spec cleanup, reviewed all mutt patches (for more information
  see spec). Complete patchlist:
  + aw (http://www.wolfermann.org/mutt.html)
   - jumptagged
   - timeouthook
  + dgc (http://home.uchicago.edu/~dgc/mutt/)
   - attach
   - deepif
   - fmtpipe
   - isalias
   - markmsg
   - xlabel_ext
  + ats (http://www.schrab.com/aaron/mutt/)
   - date_conditional
   - parent_match
  + cb (http://www.df7cb.de/projects/mutt/)
   - mutt-thread
   - chdir
   - reverse_reply
   - tag-invert
  + cd (http://cedricduval.free.fr/mutt/patches/)
   - pattern_broken
   - ifdef
   - source_multiple
   - trash_folder
   - purge_message
   - signatures_menu
  + dw (http://www.woolridge.org/mutt/)
   - crypt-hook-both
   - crypt-autoselectkey
   - mbox-hook
  + gj (http://www.spocom.com/users/gjohnson/mutt/patches.html)
   - attach_sanitize
   - sigontop_space_fix
   - stuff_all_quoted
  + greek0 (http://www.greek0.net/~greek0/mutt/)
   - indexcolor
  + nr (http://www.rachinsky.de/nicolas/mutt.html)
   - crypt-autohook
  + reh (http://www.plumlocosoft.com/software/)
   - imap-fcc-status
  + rr (http://www.spinnaker.de/mutt/)
   - compressed
  + sde (http://www.deez.info/sengelha/projects/mutt/)
   - libesmtp
   - void_passphrase_on_failed_sign
  + sec (http://www.42.org/~sec/mutt/)
   - pager_status_on_top
   - previous_jump
  + tt (http://www.emaillab.org/mutt/download1510.html)
   - iconvhook
   - slanglib
   - pgp_charsethack
   - assumed_charset
   - attach_charset
   - create_rfc2047_params
   - linear_white_space
   - tree_width
   - wcwidth
  + vvv (http://mutt.org.ua/download/1.5.10/)
   - initials
   - nntp
   - quote
   - ru
  + tamo (http://www.momonga-linux.org/~tamo/)
   - mutt-dev-msg01444
   - unbind
   - menu
   - namequot
  + lpr (http://debian.lpr.ch/Mutt/)
   - collapse_flagged
   - signin
   - signoff
  + mutt-ng (http://svn.berlios.de/viewcvs/mutt-ng/)
   - imap_reconnect
   - msgid_format
  + Debian (http://packages.debian.org/unstable/source/mutt)
   - pgp_verbose_mime
   - xtitles
   - compressed.ranty-fix
   - fix-bug-266493

* Fri Jul 22 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.9i-alt1
- [1.5.9i] (CVS snapshot 20050717)
- Updated patches:
  + header-cache
  + rr.compressed
  + vvv.nntp
  + vvv.initials
  + vvv.quote
- Removed patches:
  + vvv.ru (merged upstream)

* Mon Feb 14 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.8i-alt1
- [1.5.8i] (CVS snapshot 20050213)
- Updated patches:
  + rr.compressed
  + vvv.nntp
  + vvv.initials
  + vvv.quote
  + vvv.ru
- Removed patches:
  + ddm.pgp-auto-decode (partially merged upstream)
  + cb.menu_context (partially merged upstream)
  + tt.adjust_line (merged upstream)

* Tue Feb 08 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.7i-alt0.1
- [1.5.7i] (CVS snapshot 20050205)
- gpgme support enabled
- Updated patches:
  + rr.compressed
  + vvv.nntp
  + vvv.initials
  + vvv.quote
  + header-cache
- Added patches:
  + vvv.ru
  + gj.attach_sanitize
  + gj.stuff_all_quoted

* Sat Jan 15 2005 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.8
- CVS snapshot 20050115
- Rebuilt with new ncurses
- Updated patches:
  + header-cache.25
  + aw.timeouthook.1
  + rr.compressed.1+CVS
  + vvv.nntp
- Removed patches:
  + alt-flea.patch
  + owl-muttbug-tmp.patch

* Wed Nov 03 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.7
- CVS snapshot 20041102
- Added patches:
  + imap-fcc-status
  + header-cache.23
  + dgc.fmtpipe.1
  + sde.libesmtp.3
  + cd.signatures_menu.2.1
  + cb+tg.thread_pattern.2
  + tt.adjust_edited_file.1
  + tt.adjust_line.3
  + tt.assumed_charset.1
  + tt.create_rfc2047_params.1
- Removed patches:
  + headercache
  + maildir-header-cache.8
  + nr.threadcomplete

* Tue Oct 12 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.6
- CVS snapshot 20040929

* Thu Jul 15 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.5
- CVS snapshot 20040715

* Wed Jun 23 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.4
- CVS snapshot 20040623

* Wed May 26 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.3
- Rebuilt with new libssl

* Mon May 03 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.2
- Reverted patch-1.5.4.aw.listreply.1

* Tue Apr 20 2004 Sir Raorn <raorn@altlinux.ru> 3:1.5.6i-alt0.1
- CVS snapshot 20040413
- LOTS of patches from mutt's WiKi

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

