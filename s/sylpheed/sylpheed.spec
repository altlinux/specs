Name: sylpheed
Version: 3.1.3
Release: alt1

Summary: a GTK+ based, lightweight, and fast e-mail client
License: GPLv2+
Group: Networking/Mail
URL: http://sylpheed.sraoss.jp/en/

%def_enable ldap
%def_enable jpilot
%def_enable gtkspell

Source: %name-%version.tar

Source1: %{name}_icons.tar
Source5: %name-README.actions

Patch0: %name-0.6.4-colorder.patch
Patch1: %name-2.2.4-alt-mboxlock.patch
Patch2: %name-0.9.1-alt-nullpass.patch
Patch3: %name-2.2.4-alt-nntperr.patch
Patch4: %name-0.8.5-alt-ldapcriteria.patch
Patch5: %name-2.2.4-alt-noincludedir.patch
Patch6: %name-2.2.4-alt-qpfix.patch
Patch7: %name-2.2.4-alt-quoteformat-default.patch
Patch8: %name-2.2.4-alt-passphrase-grab.patch
Patch9: %name-2.2.4-alt-jpilotcharset.patch
Patch10: %name-2.2.5-alt-final_newline_fix.patch
Patch11: %name-2.2.5-alt-gtkspell-enchant.patch

Patch21: %name-3.1.0-alt-desktop.patch
Patch22: %name-3.1.0-alt-icons.patch
Patch23: %name-3.1.2-alt-glib2-2.32.0.patch

# old patches - not applied, should be obsolete now
Patch1000: %name-0.9.3cvs9-alt-wm_race.patch

Requires: mailcap
Requires: libgpgme >= 1.0.0

%{?_enable_ldap:BuildPreReq: libldap-devel}
%{?_enable_jpilot:BuildPreReq: libpilot-link-devel}
%{?_enable_gtkspell:BuildPreReq: libenchant-devel libgtkspell-devel}

# Automatically added by buildreq on Mon May 29 2006,
# then manually edited to remove libldap-devel and libpilot-link-devel
# (conditional dependencies) and other crap
BuildRequires: flex fontconfig glib2-devel libatk-devel libcompface-devel libgpg-error-devel libgpgme-devel libgtk+2-devel libpango-devel libssl-devel pkg-config

#BuildRequires: libdbus-glib-devel

%description
Sylpheed is an e-mail client (and news reader) based on GTK+, running on
X Window System, and aiming for
 * Quick response
 * Graceful, and sophisticated interface
 * Easy configuration, intuitive operation
 * Abundant features
The appearance and interface are similar to some popular e-mail clients
for Windows, such as Outlook Express, Becky!, and Datula. The interface
is also designed to emulate the mailers on Emacsen, and almost all
commands are accessible with the keyboard.

The messages are managed by MH format, and you will be able to use it
together with another mailer based on MH format (like Mew). You can
also utilize fetchmail or/and procmail, and external programs on
receiving (like inc or imget).
%if_enabled ldap
This version of Sylpheed is built with LDAP support, so you can get
address book information from a LDAP server.
%endif #enabled ldap
%if_enabled jpilot
This version of Sylpheed includes pilot-link support, so you can use the
address book from your Pilot in Sylpheed.
%endif #enabled jpilot

%package devel
Summary: Development files for sylpheed
Group: Development/Other
Requires: sylpheed = %version-%release

%description devel
Sylpheed - lightweight and user-friendly e-mail client.

This package contains development files.


%prep
%setup -a1
#patch0 -p0
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
#patch8 -p1
#patch9 -p1
#patch10 -p1
#patch11 -p1

#patch21 -p2
%patch22 -p2
%patch23 -p2

cp -a %SOURCE5 README.actions
bzip2 -9fk ChangeLog

%build
#rm -f missing
aclocal -I ac
libtoolize --force --copy
autoheader
automake --gnu --add-missing --copy
autoconf

# --disable-shared is for noinst_LTLIBRARIES = libsylph.la
%configure \
	--enable-gpgme \
	--enable-ssl \
	--enable-fcntl \
	--enable-flock \
	--disable-shared \
	%{subst_enable ldap} \
	%{subst_enable jpilot} \
	%{subst_enable gtkspell}

%make_build

%install
%makeinstall_std
#install -pD -m644 %{name}_16.xpm $RPM_BUILD_ROOT%_miconsdir/%name.xpm
#install -pD -m644 %{name}_32.xpm $RPM_BUILD_ROOT%_niconsdir/%name.xpm

%find_lang %name


%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
#_miconsdir/%name.xpm
#_niconsdir/%name.xpm
%_liconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%doc COPYING AUTHORS ChangeLog.bz2 NEWS README TODO README.actions

%files devel
%doc PLUGIN.txt
%_includedir/sylpheed/

%changelog
* Sat Apr 21 2012 Egor Vyscrebentsov <evyscr@altlinux.org> 3.1.3-alt1
- new version: 3.1.3

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.1
- Fixed with new glib2

* Thu Sep 15 2011 Egor Vyscrebentsov <evyscr@altlinux.org> 3.1.2-alt1
- new version: 3.1.2

* Sun Apr 24 2011 Egor Vyscrebentsov <evyscr@altlinux.org> 3.1.0-alt2
- removed xorg-devel from build requirements

* Sat Feb 26 2011 Egor Vyscrebentsov <evyscr@altlinux.org> 3.1.0-alt1
- new version: 3.1.0
- spec cleanup

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt0.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun Sep 05 2010 Ilya Mashkin <oddity@altlinux.ru> 3.0.3-alt0.1
- 3.0.3
- dropped all patches
- cleanup spec
- add desktop file
- add devel package

* Tue Mar 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6.0-alt0.1
- 2.6.0

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.9-alt1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.9-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Oct 19 2006 Sergey Vlasov <vsu@altlinux.ru> 2.2.9-alt1
- Version 2.2.9.
- Updated ru.po.

* Fri Jun 09 2006 Sergey Vlasov <vsu@altlinux.ru> 2.2.6-alt1
- Version 2.2.6.
- Fixed icon paths for new locations.
- Added --disable-shared to %%configure options to avoid compiling useless PIC
  objects for libsylph.la (which is currently used only as a static library).
- Removed old patches:
  - cvs-gmail-smtp-workaround (fixed upstream)
  - cvs-clearsign-no-encoding (fixed upstream)
  - cvs-gpg-fix (fixed upstream)
  - ldap_utf8 (obsolete - the internal encoding is always UTF-8 now)
  - alt-reeditsig (unable to reproduce the bug)
  - alt-gpg_utf8 (obsolete - the internal encoding is always UTF-8 now)
  - cvs-revert-jpilot-ja (obsolete)
  - alt-iso_conv_fix (obsolete)
  - alt-wm_race (unable to reproduce the bug, probably it does not happen with
    GTK2)
- Updated patches: alt-mboxlock, alt-nntperr, alt-noincludedir, alt-qpfix,
  alt-quoteformat-default, alt-jpilotcharset, alt-final_newline_fix.
- Added alt-passphrase-grab patch: fix input grabbing for the GPG passphrase
  prompt (the unpatched code always fails at least with libgtk+2-2.8.7-alt2 and
  fvwm-2.5.16-alt1).
- Added alt-gtkspell-enchant patch: obtain spell dictionary list from
  libenchant instead of libaspell to match hacked libgtkspell in Sisyphus
  (which is patched to use libenchant).
- Updated ru.po.
- Reenabled X-Face support.
- Removed obsolete BuildPreReq: imlib-devel.
- Updated BuildRequires.
- Enabled gtkspell support (can be disabled with --disable gtkspell).

* Thu Jun 09 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.4-alt1
- 1.0.4 release.
- Moved auto* calls from %%prep to %%build.
- Updated alt-mboxlock, alt-nntperr, alt-final_newline_fix, alt-gpg_utf8
  patches.
- Added cvs-gmail-smtp-workaround patch: consider EOF right after QUIT
  successful; ignore some EOFs which in theory violate the SSL protocol
  (workaround for Gmail SMTP server).
- Added cvs-clearsign-no-encoding patch: do not use MIME encoding for
  clearsigned text.
- Added cvs-gpg-fix patch: fix crashes in GPG support code.
- Added cvs-revert-jpilot-ja patch: reverted the JPilot addressbook Japanese
  support patch from upstream (charset conversion support is already included
  in the alt-jpilotcharset patch, the only missing thing is locale-dependent
  first/last-name order).
- Added alt-quoteformat-default patch: do not show email address in the default
  quote format to avoid feeding spambots.
- Removed obsolete patches: cvs-conv_unmime_header, cvs-unmime-buffer-overflow,
  cvs-fix-reedit-crash, cvs-fix-smtp-auth.
- Updated ru.po.
- Updated BuildRequires.

* Thu Mar 31 2005 Sergey Vlasov <vsu@altlinux.ru> 0.9.10-alt4
- Added cvs-unmime-buffer-overflow patch: fix possible buffer overflow when
  displaying a message with attachments which have MIME-encoded filenames
- Added cvs-fix-reedit-crash patch: fix possible crash when reediting a message
- Added cvs-fix-smtp-auth patch: fix SMTP AUTH capability checking

* Fri Mar 18 2005 Sergey Vlasov <vsu@altlinux.ru> 0.9.10-alt3
- Added cvs-conv_unmime_header patch: CAN-2005-0667

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.10-alt2.1.1
- Rebuilt with openldap-2.2.18-alt3.

* Tue Oct 19 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.10-alt2.1
- Updated build dependencies (libgpgme-compat-devel).

* Wed May 12 2004 Sergey Vlasov <vsu@altlinux.ru> 0.9.10-alt2
- Rebuild with new openssl.
- Removed faces support.

* Tue Mar 02 2004 Sergey Vlasov <vsu@altlinux.ru> 0.9.10-alt1
- 0.9.10 release.
- Removed cvs-format_string_fix patch (upstream).
- Updated alt-iso_conv_fix patch.
- Updated ru.po.
- Removed temporary BuildRequires workaround for #2976.

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.6-alt1.1
- Rebuilt.

* Sun Oct 12 2003 Sergey Vlasov <vsu@altlinux.ru> 0.9.6-alt1
- 0.9.6 release.
- Removed obsolete patches: alt-imapflagsfix.
- Disabled alt-thread patch.
- Added alt-wm_race patch - workaround for the problem with cancelling a
  password prompt with some window managers.
- Added format_string_fix patch (from CVS) - fix format string bug.
- Updated ru.po.
- Added more BuildRequires as a workaround for missing Requires in
  libldap-devel (see #2976).

* Fri Jun 06 2003 Sergey Vlasov <vsu@altlinux.ru> 0.9.2-alt1
- 0.9.2 release.

* Thu Jun 05 2003 Sergey Vlasov <vsu@altlinux.ru> 0.9.1-alt2
- Fixed alt-threads patch (builtin POP3 receive was broken).

* Sun Jun 01 2003 Sergey Vlasov <vsu@altlinux.ru> 0.9.1-alt1
- 0.9.1 release.
- Updated BuildPreReq (s/openldap-devel/libldap-devel).
- Updated patches: alt-thread, alt-nullpass, alt-nntperr.
- Updated ru.po.

* Thu Apr 10 2003 Sergey Vlasov <vsu@altlinux.ru> 0.8.11-alt2
- Added patch to fix adding final newline to messages (which broken
  the GnuPG signature check in some cases).
- Added patch to fix ISO-8859-* conversion (restored the previous (0.8.8)
  behavior).

* Fri Mar 07 2003 Sergey Vlasov <vsu@altlinux.ru> 0.8.11-alt1
- 0.8.11 release.
- Removed obsolete patches:
   + 0.8.3cvs8-canon (fixed upstream)
   + 0.8.8-0.8.9-enchdrfix (fixed upstream)
   + 0.8.8-alt-qpwrapfix (fixed upstream)
   + 0.8.8-alt_ml-regexp2fix (fixed upstream)
   + 0.8.8-alt_cvs-enchdr_crash_fix (fixed upstream)
- Removed libjconv check - no longer used.
- Updated ru.po.

* Fri Feb 07 2003 Sergey Vlasov <vsu@altlinux.ru> 0.8.8-alt3
- Added patch to fix second filter regexp handling (from mailing list).
- Added patch to fix crash in header encoding conversion (backport from CVS).

* Thu Jan 23 2003 Sergey Vlasov <vsu@altlinux.ru> 0.8.8-alt2
- Added patch to fix header linewrapping problems (backport from 0.8.9).
- Added patch to fix Quoted-Printable encoding (fixes bug #2017).
- Added patch to fix Quoted-Printable header wrapping (lost spaces in Subject).

* Wed Dec 25 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.8-alt1
- 0.8.8 release.
- Updated ru.po.

* Mon Dec 23 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.7-alt1
- 0.8.7 release.
- Removed obsolete patches:
  + alt-fixpartialcite;
  + alt-systemname;
  + alt-fontenc;
  + alt-utf8fix;
  + alt-popupfix.
- Updated patches:
  + alt-gpg_utf8.
- Updated ru.po.

* Sun Nov 17 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.6-alt1
- 0.8.6 release.
- Abort build if libjconv is not found by configure.
- Updated fixpartialcite patch.
- Removed obsolete patches (reeditfix).
- Patch to remove $(includedir) from INCLUDES
  (caused compiler warnings about -I/usr/include).
- Patch to set system name from build_alias instead of target_alias
  (fixes empty system name with new rpm and autoconf versions).
- Patch to fix problems with font encodings due to recent upstream
  changes.
- Patch to fix message display in UTF-8 locales.
- Patch to add charset conversion for JPilot address book data.
- Patch to avoid window shift with some window managers when starting
  a second copy of Sylpheed (which should just show and raise the
  existing window).
- Updated menu file (added genericname="Mail Client").
- Updated ru.po.

* Thu Oct 17 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.5-alt3
- Rebuild with new pilot-link.
- Fixed translation bug (#0001397).

* Fri Oct 04 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.5-alt2
- Patch to convert GnuPG userid from UTF-8 (fixes bug #693).
- Patch to fix flag handling with IMAP (fixes bug #1080).
- Patch to change default LDAP search criteria (fixes bug #1096).
- bzip2 ChangeLog.

* Thu Oct 03 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.5-alt1
- 0.8.5 release.
- Patch to avoid wrong citation header when quoting selected part of text.
- Patch to fix line endings in reedit.
- Patch to remove signature and main text parts from attach list when doing
  reedit, forward or redirect.

* Tue Oct 01 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.4-alt1
- 0.8.4 release.
- Cleaned up conditional build (now uses enable/disable rpm logic);
  this change in 0.8.2-alt2 was accidentally lost in 0.8.3-alt1.
- Patch to canonicalize the message text correctly (fixes problems with
  verifying PGP/MIME signatures from Sylpheed in Evolution 1.0.3).
- Updated ru.po.
- Fixed %%doc list (-INSTALL, +AUTHORS, +NEWS, +TODO).
- Added some documentation about user-definable actions.

* Wed Sep 18 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.3-alt1
- 0.8.3 release.
- Removed obsolete patches (cp1251).
- Updated thread patch.
- Updated ru.po.

* Thu Aug 29 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.2-alt1
- 0.8.2 release.
- Removed obsolete patches (micalg).
- Updated mbox locking patch.
- Require new libgpgme-compat.

* Wed Jul 31 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.1-alt1
- 0.8.1 release.
- Updated ru.po.
- Patch to handle null passwords correctly.
- Patch to fix NNTP error handling.

* Tue Jul 16 2002 Sergey Vlasov <vsu@altlinux.ru> 0.8.0-alt1
- 0.8.0 release.
- Updated menu icons.
- Updated ru.po.

* Tue Jun 25 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.8-alt2
- Fixed BuildRequires (libjconv-devel).

* Fri Jun 21 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.8-alt1
- 0.7.8 release.
- Updated ru.po.

* Tue May 21 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.6-alt2
- Use fcntl for spool mailbox locking (ALT policy).
- Use flock in addition to fcntl (compatibility with broken software).

* Tue May 14 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.6-alt1
- 0.7.6 release.
- Removed obsolete patches.
- Updated ru.po.

* Mon Mar 11 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.4-alt1
- 0.7.4 release.
- Removed obsolete patches.
- Updated ru.po.

* Fri Feb 22 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.2-alt1
- 0.7.2 release.
- Removed obsolete patches.
- Updated ru.po.

* Wed Feb 13 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.1-alt3
- Patch to fix problems with quoting selected part of message.

* Tue Feb 12 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.1-alt2
- Patch from CVS to fix problems with reading GnuPG encrypted messages.
- Patch to use the correct namespace separator with APPEND on IMAP server.
- Requires: mailcap

* Mon Feb 11 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.1-alt1
- 0.7.1 release.
- Removed obsolete patches.
- Updated SMTP AUTH patch.
- Removed ancient pre-ALT changelog entries with no useful information

* Thu Jan 24 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.0-alt2
- Patch to update message count in outbox after sending.

* Wed Jan 23 2002 Sergey Vlasov <vsu@altlinux.ru> 0.7.0-alt1
- 0.7.0 release
- Updated ru.po
- Fixed segfault on closing LDIF import window

* Fri Jan 04 2002 Sergey Vlasov <vsu@altlinux.ru> 0.6.6-alt2
- Fixed image scrolling (closes bug #239)
- Use UTF-8 encoding for LDAP (closes bug #253)
- Fixed thread problems (gdk_thread_enter/leave and init order)

* Sat Dec 15 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.6-alt1
- 0.6.6 release

* Thu Nov 22 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.5-alt2
- Fixed windows-1251 charset name (was CP1251).

* Thu Nov 08 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.5-alt1
- 0.6.5 release
- updated SMTP AUTH patch

* Sun Oct 21 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.4-alt1
- 0.6.4 release
- updated SMTP AUTH patch
- updated ru.po
- patch to restore old ordering of columns

* Thu Oct 11 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.3-alt3
- Patch to add separate username/password settings for SMTP AUTH.
- Disabled dynamic loading of LDAP libraries - doesn't work yet.

* Tue Oct 09 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.6.3-alt2
- Build with libpilot-link by default.

* Mon Oct 08 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.3-alt1
- 0.6.3 release
- updated ru.po
- build with LDAP by default

* Wed Sep 19 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.2-alt1
- 0.6.2 release
- require libgpgme-compat (important bugfixes)
- patch to fix problems with background POP3 mail retrieval
- patch from Werner Koch to write micalg for signatures

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.6.1-alt1
- 0.6.1 release.

* Fri Aug 31 2001 Sergey Vlasov <vsu@altlinux.ru> 0.6.0-alt1
- 0.6.0 release
- build with SSL support
- removed obsolete patches
- updated ru.po

* Wed Aug 15 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.3-alt1
- 0.5.3 release
- removed obsolete patches
- patch to fix crash when trying to delete from an empty folder
- patch to fix summary view updating after receiving messages
- patch to avoid unneeded updating of the summary view
- updated ru.po

* Tue Aug 14 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.2-alt3
- patch to correctly enable toolbar buttons after receiving messages

* Sat Aug 11 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.2-alt2
- patch to fix folder updatind after "Get all" from spool only
- patch to keep position in the displayed message after receiving new mail

* Sat Aug  4 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.2-alt1
- 0.5.2 release
- updated ru.po

* Sat Jul 28 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.1-alt1
- 0.5.1 release
- removed obsolete patches

* Sat Jul  7 2001 Sergey Vlasov <vsu@altlinux.ru> 0.5.0-alt1
- 0.5.0 release
- removed obsolete bugfix patches
- updated ru.po
- requires libgpgme-compat

* Sat Jun 16 2001 Sergey Vlasov <vsu@altlinux.ru> 0.4.99-alt1
- 0.4.99 release
- removed obsolete patches
- patch to fix iso-8859-* encodings
- patch to fix base64 decoder
- updated ru.po

* Wed May 23 2001 Sergey Vlasov <vsu@altlinux.ru> 0.4.66-alt2
- iso-8859-{5,7} code conversion fix

* Tue May  8 2001 Sergey Vlasov <vsu@altlinux.ru> 0.4.66-alt1
- 0.4.66 release
- patch to disable GnuPG warning message
- patch to disable GnuPG signature popup
- updated ru.po

* Tue Apr 24 2001 Sergey Vlasov <vsu@altlinux.ru> 0.4.65-alt0.7
- 0.4.65cvs7
- updated ru.po
- new add-sender-to-addressbook patch

* Fri Mar 16 2001 AEN <aen@logic.ru> 0.4.63-ipl4
- mimedecode patch from Sergey Vlasov <vsu@mivlgu.murom.ru>

* Thu Mar 15 2001 AEN <aen@logic.ru> 0.4.63-ipl3
- ru.po patch from Sergey Vlasov <vsu@mivlgu.murom.ru>

* Sun Mar 12 2001 AEN <aen@logic.ru> 0.4.62-ipl2
- custom headers patch

* Sun Mar 11 2001 AEN <aen@logic.ru> 0.4.62-ipl1
- 0.4.62 release
- patch from Sergey Vlasov <vsu@mivlgu.murom.ru>

* Fri Mar 02 2001 Dmitry V. Levin <ldv@fandra.org> 0.4.62-ipl0.6
- Applied new SMTP Authentication patch.

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 0.4.62-ipl0.5
- Do not apply SMTP Authentication patch (broken yet).
- Patched some security issues.
- Fixed specfile for correct build from cvs tree.

* Tue Feb 27 2001 AEN <aen@logic.ru> 0.4.62-ipl0.4
- sources form cvs
- completion-list, add-sender & smtp-auth patches

* Tue Feb 20 2001 AEN <aen@logic.ru> 0.4.61-ipl4
- %%file fixed -- menu & icons added
* Tue Feb 20 2001 AEN <aen@logic.ru> 0.4.61-ipl2
- russian translation added

* Mon Feb 19 2001 AEN <aen@logic.ru> 0.4.1-ipl1
- build old version for testing purposes

* Mon Feb 19 2001 AEN <aen@logic.ru> 0.4.61-ipl1
- RE adaptation
- first build for Sisyphus
