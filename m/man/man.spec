# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: man
Version: 1.6f
Release: alt14

Summary: Programs for formating and displaying the manual pages
License: GPL
Group: System/Base
Url: http://primates.ximian.com/~flucifredi/man/
Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: http://primates.ximian.com/~flucifredi/%name/%name-%version.tar.gz
Source3: makewhatis
Source4: whatis.filetrigger

Patch0: man-1.5m2-cvs-fixes.patch
Patch1: man-1.6f-alt-add-less-R.patch
Patch2: man-1.5m2-alt-makefile.patch
Patch3: man-alt-bzip2.patch
Patch4: man-alt-usage_fix.patch
Patch5: man-1.5k-alt-conf.patch

Patch7: man-alt-apropos.patch
Patch8: man-alt-man-makewhatis.patch
Patch9: man-1.5k-alt-msgs.patch
Patch10: man-1.5m2-alt-manpath.patch
Patch11: man-alt-recode.patch
Patch12: man-alt-recode2.patch
Patch13: man-alt-unlatin1.patch
Patch15: man-1.5m2-alt-utf8whatis.patch
Patch16: man-1.5m2-alt-my_xsprintf.patch
Patch17: man-1.6f-alt-call-pic-tbl-inside-groff.patch
Patch18: man-1.6f-alt-add-tty-tmac.patch
Patch19: man-1.6f-alt-man-unpack.patch
Patch20: man-1.6f-alt-add-man-show-source.patch
Patch21: man-1.6f-alt-safer-mode.patch
Patch22: man-1.6f-remove-unsafe.patch

# Automatically added by buildreq on Wed Mar 12 2003
BuildRequires: groff-base less su lzma-utils ncompress

PreReq: shadow-utils
Requires: mktemp >= 1:1.3.1
Requires: getopt less iconv lzma-utils

# After fixing bug #9364 file /usr/share/man/$LANG/.charset supplied
# by man package
Conflicts: man-pages-ru <= 0.98-alt11
Conflicts: man-pages-uk <= 20030816-alt1

# Because we use nroff with -D option
Requires: groff-base >= 1.19.3-alt3.20081215
# Because man -t required this
Requires: groff-ps >= 1.19.3-alt3.20081215

Provides: man-base
Obsoletes: man-base < %version-%release

%description
This package contains the man system which is formats and displays
on-line manual pages about commands or functions on your system.

%package whatis
Summary: Tools for finding documentation about Linux system
Group: System/Base
BuildArch: noarch
Requires: %name = %version-%release

%description whatis
This package contains parts of the man system which is used for
finding information and/or documentation about your Linux system:
apropos and whatis.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1

%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

%build

# FIXME:
# Don't install messages for Russian, because they in koi8-r charsets
# and not displayed properly in CP1251 and UTF-8 locales.
INSTALL_LANGUAGES=`grep ^LANGUAGES configure | cut -d\" -f2 | sed 's|,ru||'`
./configure -default -confdir /etc +sgid +fsstnd +fhs +lang "$INSTALL_LANGUAGES"
#./configure -default -confdir /etc +sgid +fsstnd +fhs +lang all

# SMP-incompatible build.
%make CC="%__cc %optflags -D_GNU_SOURCE" LDFLAGS=

%install
%makeinstall_std

install -Dp -m755 %SOURCE4 %buildroot%_rpmlibdir/whatis.filetrigger

# Symlinks for manpath
ln -snf %name %buildroot%_bindir/manpath
ln -snf %name.1 %buildroot%_man1dir/manpath.1

mkdir -p %buildroot{%_cachedir/man/{{,{local,perl,X11R6}/}cat{1,2,3,4,5,6,7,8,9,n},tmp},%_lockdir/makewhatis}
for f in %buildroot%_cachedir/man/{,{local,perl,X11R6}/}whatis; do echo >"$f"; done

find %buildroot%_mandir -type f -print0 |
	xargs -r0 chmod 644 --

# See bug ALT#27372 for details
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
cat > %buildroot%_sysconfdir/tmpfiles.d/man.conf <<EOF
D %_lockdir/makewhatis 0700 root root -
EOF

# See bug ALT#9364 for details
mkdir -p %buildroot%_mandir/{ru,uk}
echo "KOI8-R" > %buildroot%_mandir/ru/.charset
echo "KOI8-U" > %buildroot%_mandir/uk/.charset

# Replace makewhatis with ALT-specific script.
rm %buildroot%_sbindir/makewhatis
install -pD -m754 %SOURCE3 %buildroot%_sbindir/makewhatis

%find_lang %name --with-man

for man in man.conf apropos whatis; do
	%find_lang "$man" \
		--output="%name.lang" \
		--append \
		--with-man \
		--without-mo
done

%pre
/usr/sbin/useradd -r -g man -d %_cachedir/man -s /dev/null -n cacheman >/dev/null 2>&1 ||:

%triggerpostun -- %name < 1.5m2-alt2
echo -n 'Rebuilding whatis database... '
su -l cacheman -s /bin/sh -c '/usr/sbin/makewhatis'
echo done.

%files -f %name.lang
%_mandir/ru/.charset
%_mandir/uk/.charset
%config(noreplace) %_sysconfdir/%name.conf
%config %_sysconfdir/tmpfiles.d/man.conf
%_bindir/*
%_man1dir/manpath.1.*
%_man1dir/man2html.1.*

%exclude %_bindir/whatis
%exclude %_bindir/apropos
%exclude %_man1dir/whatis.1.*
%exclude %_man1dir/apropos.1.*
%exclude %_man8dir/makewhatis.8.*

%attr(3775,root,man) %dir %_cachedir/man
%attr(3775,root,man) %dir %_cachedir/man/local
%attr(3775,root,man) %dir %_cachedir/man/perl
%attr(3775,root,man) %dir %_cachedir/man/X11R6

%defattr(644,root,man,2775)
%_cachedir/man/cat*
%_cachedir/man/local/cat*
%_cachedir/man/perl/cat*
%_cachedir/man/X11R6/cat*

%files whatis
%attr(754,root,man) %_sbindir/makewhatis
%_bindir/whatis
%_bindir/apropos
%_man1dir/whatis.1.*
%_man1dir/apropos.1.*
%_man8dir/makewhatis.8.*

%_rpmlibdir/whatis.filetrigger

%attr(700,cacheman,man) %dir %_cachedir/man/tmp
%attr(644,cacheman,man) %ghost %_cachedir/man/whatis
%attr(644,cacheman,man) %ghost %_cachedir/man/local/whatis
%attr(644,cacheman,man) %ghost %_cachedir/man/perl/whatis
%attr(644,cacheman,man) %ghost %_cachedir/man/X11R6/whatis

%changelog
* Tue Jun 26 2012 Dmitry V. Levin <ldv@altlinux.org> 1.6f-alt14
- Merged man-base subpackage back to man subpackage; man-whatis
  subpackage is no longer required by man subpackage
  (by Mikhail Efremov; closes: #27501).

* Wed Jun 20 2012 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt13
- Replace makewhatis with ALT-specific script and move whatis in
  subpackage (ALT#21793) (thx Mikhail Efremov).

* Fri Jun 08 2012 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt12
- Create /var/lock/makewhatis before use it (ALT#27372).

* Thu Apr 30 2009 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt11
- Fix a loss of the last line (ALT#19806).

* Thu Apr 16 2009 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt10
- Fix package requires (ALT#18473).
- Fix bugs (ALT#3011, ALT#16879, ALT#19034).

* Mon Apr 06 2009 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt9
- Fix '-t' option.

* Wed Dec 17 2008 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt8
- Don't hardcode -Tutf8 for nroff.

* Sun Nov 16 2008 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt7
- Call gpic inside groff.
- man-source: Fix minor bugs.

* Sat Sep 20 2008 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt6
- man-source: Fix unbound variable (ALT#17216).

* Thu Sep 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt5
- Add man-show-source utility.
- Use groff safer mode.

* Wed Sep 03 2008 Alexey Gladkov <legion@altlinux.ru> 1.6f-alt4
- Call gtbl inside groff (ALT#16879).
- Add lzma support.
- Supply .charset files for backward compatibility.
- Add man-source utility:
  + Add support for preconv (part of groff-base package) (ALT#16680);
  + Allow use .so directive (ALT#3011).
- Update makewhatis:
  + Add support for mans charset;
  + Add backward compatibility with .charset scheme;
  + Use man-source to unpack man-page;
  + Remove obsolete code.

* Thu Aug 28 2008 Slava Semushin <php-coder@altlinux.ru> 1.6f-alt3
- Changed scheme of man page preparation for groff (Closes: #16879)

* Mon Aug 25 2008 Slava Semushin <php-coder@altlinux.ru> 1.6f-alt2
- Call nroff with -Tutf8 option (Closes: #16680)
- Don't supply .charset files (not needed any more)
- Requires last groff-base version

* Fri Feb 08 2008 Slava Semushin <php-coder@altlinux.ru> 1.6f-alt1
- Updated to 1.6f ('Flying Fox')
- Don't run cron scripts under fake environment (#11488)
- Added su to BuildRequires (and auto-generated Requires)

* Sun Dec 30 2007 Slava Semushin <php-coder@altlinux.ru> 1.6e-alt1
- Updated to 1.6e (#7681, also fixes #9018)
- Corrected behavior of --help option (#9045)
- Supply .charset files for ru and uk (#9364)
- Added iconv to Requires (#13315)
- New maintainer
- Disabled installation of messages for Russian, because they in
  koi8-r charsets and not displayed properly in CP1251 and UTF-8
  locales
- Spec cleanup:
  + Don't use %%name macros in Summary
  + Update url in Source tag
  + s/%%setup -q/%%setup/
  + Use %%__cc macros instead of gcc command
  + Correct find usage
  + Don't use macros for mkdir and chmod commands
  + Use %%find_land macros instead of self written commands
- Enable _unpackaged_files_terminate_build

* Tue Nov 28 2006 Dmitry V. Levin <ldv@altlinux.org> 1.5m2-alt4
- Added "less" to package requirements.
- Removed %%__* macros abuse from specfile.
- Replaced $RPM_* variables with appropriate macros.
- Added URL (#7680).

* Thu Jun 02 2005 Dmitry V. Levin <ldv@altlinux.org> 1.5m2-alt3
- Fixed "static data free" bug (closes #5802).
- Moved recode after nroff, disabled nroff de'latin1'isation,
  (closes #6988 but probably raises new issues).

* Fri May 28 2004 Alexey Voinov <voins@altlinux.ru> 1.5m2-alt2
- man2dvi patch [fix for #2031]
- utf8whatis patch [fix for #2872]
  (whatis files converted to utf-8 if iconv is present.)
- trigger running makewhatis on upgrade from older versions

* Tue May 25 2004 Alexey Voinov <voins@altlinux.ru> 1.5m2-alt1
- new version(1.5m2)
- lot of patches updated
- de-latin1-isation

* Sun Apr 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.5k-alt3
- Changed %_cachedir/man/{,local,perl,X11R6} permissions
  from %%attr(2775,cacheman,man) to %%attr(3775,root,man).
- Changed %_cachedir/man/{,local,perl,X11R6}/cat* permissions
  from %%attr(2775,cacheman,man) to %%attr(2775,root,man).
- Updated cron scripts to avoid changing %_cachedir/man permissions.

* Wed Mar 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.5k-alt2
- Backported few fixes from 1.5l.

* Sun Nov 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5k-alt1
- 1.5k, updated and redone patches.
- When calculating manpath, honor LC_MESSAGES category only.
- Use "nroff -mandoc" (no -T driver), requires recent nroff.
- Added recode support (based on patch from corwin@micom.net.ru).

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.5i2-alt4
- Set LC_CTYPE together with LC_MESSAGES (rh).
- Updated makewhatis script.
- cron scripts: exit if DURING_INSTALL set.
- Updated package requires.

* Wed Sep 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5i2-alt3
- Automatically updated requires.

* Tue Aug 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5i2-alt2
- nroff -Tlatin1 for manpages for a while.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5i2-alt1
- 1.5i2
- Shutup catopen.
- Relocated translation files.

* Fri May 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5i-alt1
- 1.5i
- Fixed "makewhatis -u".

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5h1-ipl12mdk
- Fixed recent fix.

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5h1-ipl11mdk
- Fixes permissions of manpages installed with this package.
- Security fix for cron scripts (method of running makewhatis).

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5h1-ipl10mdk
- Security fix for cron scripts (method of creating lockfile).

* Tue Mar 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.5h1-ipl9mdk
- Merged with makewhatis code from man-pages-ru.

* Mon Mar 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.5h1-ipl8mdk
- Fixed compatibility hack in makewhatis script (again).

* Mon Feb 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.5h1-ipl7mdk
- Fixed compatibility hack in makewhatis script.

* Mon Feb 12 2001 Dmitry V. Levin <ldv@fandra.org> 1.5h1-ipl6mdk
- Fixed typo in makewhatis script.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.5h1-ipl5mdk
- Removed sgid=man from %_bindir/man.
- Fixed cron scripts a bit.
- Fixed makewhatis and apropos scripts.
- Fixed whatis database building when /usr mounted readonly.
- Merged RH patches.

* Mon Aug 21 2000 Dmitry V. Levin <ldv@fandra.org> 1.5h1-ipl4mdk
- FHS-2.1
- RE adaptions.

* Sun Jul 09 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.5h1-3mdk
- Fix typo.

* Thu Jun 29 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.5h-2mdk
- security fix for makewhatis

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.5h-1mdk
- new release
- remove useless loop & manpath patch
- remove a chunk of make patch which is now usefull

* Mon May 15 2000 Pixel <pixel@mandrakesoft.com> 1.5g-15mdk
- build as non root fix

* Thu Mar 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- build for new environnment (new group naming)
- heavy use of spechelper

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh patchs.

* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- By default in latin1.

* Tue May 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Makewhatis make the database with $LANG.
- Fix bug, if parsing files with -0 size.

* Mon May 24 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Fix up makewhatis bzip2/$LANG support
- 1.5g

* Tue Apr 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch to makewhatis support bzip2 pages.
- Add patch to makewhatis to $LANG pages.

* Sun Apr 11 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- Mandrake adaptions
- restore de, fr, tr locales from 5.2
- Add support for {bzip2|bzip|tzip} compressed manpages
- bzip2 man pages

* Thu Feb 18 1999 Jeff Johnson <jbj@redhat.com>
- add manpath symlinks (#1138).

* Fri Feb 12 1999 Michael Maher <mike@redhat.com>
- fixed bug #792
- added man2html files

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- upgraded to 1.5e
- properly buildrooted

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- enable fsstnd organization
- change /var/catman/X11 to X11R6
- %post/%preun to clean up cat litter

* Tue Jun 02 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- you can't do free(malloc(10) + 4) <sigh>

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5d

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.5a

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- uses a build root

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to man-1.4j, which fixes some security problems; release 1 is
  for RH 4.2, release 2 is for glibc

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added /usr/lib/perl5/man to default manpath
