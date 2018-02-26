Name: tcsh
Version: 6.18.01
Release: alt1

Summary: An enhanced version of csh, the C shell
License: BSD
Group: Shells

URL: http://www.tcsh.org/
Source: ftp://ftp.astron.com/pub/tcsh/tcsh-%version.tar.gz

Patch1: tcsh-6.15.00-closem.patch
Patch2: tcsh-6.17.00-alt-tinfo.patch
Patch3: tcsh-6.14.00-unprintable.patch

Patch5: tcsh-6.10.01-config-nodot.patch
Patch6: tcsh-6.17.00-alt-lscolors.patch

Patch8: tcsh-6.14.00-syntax.patch
Patch9: tcsh-6.13.00-memoryuse.patch
Patch10: tcsh-6.14.00-order.patch

Patch14: tcsh-6.17.00-glob-automount.patch

# Don't die on unknown LS_COLORS values
Patch100: tcsh-6.14.00-unknown_lscolors.patch

Patch101: tcsh-6.10.00-glibc_compat.patch

# To be rediffed, not applied for now
Patch300: tcsh-6.14.00-suse-owl-alt-shtmp.patch
Patch301: tcsh-6.10.01-deb-man.patch
Patch302: tcsh-6.10.01-alt-cleanups.patch

Provides: csh = %version

# Automatically added by buildreq on Sun Jan 15 2012
BuildRequires: groff-base libtinfo-devel

%description
Tcsh is an enhanced but completely compatible version of csh, the C shell. Tcsh
is a command language interpreter which can be used both as an interactive login
shell and as a shell script command processor. Tcsh includes a command line
editor, programmable word completion, spelling correction, a history mechanism,
job control and a C language like syntax.

%package doc
Summary: HTML doc files for tcsh
Group: Shells
Requires: tcsh = %version

BuildArch: noarch

%description doc
HTML doc files for tcsh.

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch5 -p1
%patch6 -p1

%patch8 -p1
%patch9 -p1
%patch10 -p1

%patch14 -p1

%patch100 -p1
%patch101 -p1

# To be rediffed:
#%patch300 -p1
#%patch301 -p1
#%patch302 -p1

cat > catalogs << _EOF
de ISO-8859-1 german
el ISO-8859-7 greek
en ISO-8859-1 C
es ISO-8859-1 spanish
et ISO-8859-1 et
fi ISO-8859-1 finnish
fr ISO-8859-1 french
it ISO-8859-1 italian
ja eucJP      ja
pl ISO-8859-2 pl
ru KOI8-R russian
uk KOI8-U ukrainian
_EOF

cat catalogs | while read lang charset language ; do
	if ! grep -q '^$ codeset=' nls/$language/set1 ; then
		echo '$ codeset='$charset	>  nls/$language/set1.codeset
		cat nls/$language/set1		>> nls/$language/set1.codeset
		cat nls/$language/set1.codeset	>  nls/$language/set1
		rm  nls/$language/set1.codeset
	fi
done

nroff -me eight-bit.me >eight-bit.txt

%build
# autoreconf needed for alt-tinfo patch
autoreconf
%configure --bindir=/bin
%make_build all
perl ./tcsh.man2html tcsh.man
%make_build -C nls catalogs

%install
install -pD -m755 tcsh %buildroot/bin/tcsh
install -pD -m644 tcsh.man %buildroot%_man1dir/tcsh.1
ln -s tcsh %buildroot/bin/csh
ln -s tcsh.1 %buildroot%_man1dir/csh.1

cat catalogs | while read lang charset language ; do
	dest=%buildroot%_datadir/locale/$lang/LC_MESSAGES
	if test -f tcsh.$language.cat ; then
		mkdir -p $dest
		install -m644 tcsh.$language.cat $dest/tcsh
		echo "%lang($lang) %_datadir/locale/$lang/LC_MESSAGES/tcsh"
	fi
done > tcsh.lang

%files -f tcsh.lang
/bin/csh
/bin/tcsh
%_man1dir/*
%doc NewThings FAQ Fixes complete.tcsh eight-bit.txt

%files doc
%doc tcsh.html/*

%changelog
* Tue Feb 28 2012 Victor Forsiuk <force@altlinux.org> 6.18.01-alt1
- 6.18.01

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 6.18.00-alt1
- 6.18

* Fri Jan 29 2010 Victor Forsyuk <force@altlinux.org> 6.17.00-alt1
- 6.17

* Mon Nov 24 2008 Victor Forsyuk <force@altlinux.org> 6.16.00-alt1
- 6.16
- Don't die on unknown LS_COLORS values.

* Fri Sep 28 2007 Victor Forsyuk <force@altlinux.org> 6.15.00-alt1
- 6.15

* Tue Nov 22 2005 Victor Forsyuk <force@altlinux.ru> 6.14.00-alt2
- Fix #8515
- Split big html docs into separate package.
- Fix NLS messages (adding ".mo" suffix was not right).
- Add patches from Fedora package.

* Thu Apr 07 2005 Victor Forsyuk <force@altlinux.ru> 6.14.00-alt1
- Fix URL.
- Package message localisation files.
- suse-owl-alt-shtmp.patch updated.

* Thu Oct 23 2003 Stanislav Ievlev <inger@altlinux.org> 6.12.00-alt2.1
- fix url (location of the sources)

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 6.12.00-alt2
- rebuild with gcc3

* Thu Aug 15 2002 Stanislav Ievlev <inger@altlinux.ru> 6.12.00-alt1
- 6.12.00

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 6.10.01-alt6
- Patched to link with libtinfo.
- Additional convention enforcement on patch file names.

* Thu May 23 2002 Stanislav Ievlev <inger@altlinux.ru> 6.10.01-alt5
- removed some SUXX.
- fixed package deps.

* Wed Feb 20 2002 Stanislav Ievlev <inger@altlinux.ru> 6.10.01-alt4
- added some Debian patches.

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.10.01-alt3
- Fixed URL.
- Added localization files and html documentation.

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.10.01-alt2
- Added mkstemp patch from Owl.

* Tue May 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.10.01-alt1
- 6.10.01

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 6.10-ipl2mdk
- Fixed build with glibc-2.2.2.

* Thu Dec 07 2000 Dmitry V. Levin <ldv@fandra.org> 6.10-ipl1mdk
- RE adaptions.

* Tue Nov 21 2000 Pixel <pixel@mandrakesoft.com> 6.10-1mdk
- new version

* Mon Nov 13 2000 Pixel <pixel@mandrakesoft.com> 6.09.04-1mdk
- new version

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 6.09.03-5mdk
- add man page for csh.1 (link to tcsh.1)

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 6.09.03-4mdk
- nicer %%post scripts

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 6.09.03-3mdk
- change the suffix of /etc/shells temporary file to remove rpmlint error

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 6.09.03-2mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Pixel <pixel@mandrakesoft.com> 6.09.03-1mdk
- new version

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 6.09.02-2mdk
- _mandir ization
- BM

* Thu Jul  6 2000 Pixel <pixel@mandrakesoft.com> 6.09.02-1mdk
- new version (cleanup of patches)

* Fri Jun 16 2000 Pixel <pixel@mandrakesoft.com> 6.09-4mdk
- new version
- merge with redhat

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 6.08.00-9mdk
- new group + cleanup

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies

* Thu Jan 27 2000 Jeff Johnson <jbj@redhat.com>
- append entries to spanking new /etc/shells.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- update to 6.09.
- fix strcoll oddness (#6000, #6244, #6398).

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh.
- Fix $shell to use --bindir(r)

* Sat Sep 25 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix $shell by using --bindir

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Wed Feb 24 1999 Cristian Gafton <gafton@redhat.com>
- patch for using PATH_MAX instead of some silly internal #defines for
  variables that handle filenames.

* Fri Nov  6 1998 Jeff Johnson <jbj@redhat.com>
- update to 6.08.00.

* Fri Oct 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 6.07.09 from the freebsd
- security fix

* Wed Aug  5 1998 Jeff Johnson <jbj@redhat.com>
- use -ltermcap so that /bin/tcsh can be used in single user mode w/o /usr.
- update url's

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 6.07; added BuildRoot
- cleaned up the spec file; fixed source url

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- added termios hacks for new glibc
- added /bin/csh to file list

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
 - Provides csh, adds and removes /bin/csh from /etc/shells if csh package
isn't installed.
