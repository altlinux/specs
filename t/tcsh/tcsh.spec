Name: tcsh
Version: 6.20.00
Release: alt2
Summary: An enhanced version of csh, the C shell
License: BSD
Group: Shells
URL: http://www.tcsh.org
Source0: ftp://ftp.astron.com/pub/tcsh/tcsh-%version.tar.gz
Source1: tcsh.login
Source2: tcsh.cshrc
Source3: tcshrc.skel
Patch0: tcsh-%version-alt-build.diff
Patch1: tcsh-%version-alt-closem-nosocket.diff
Patch2: tcsh-%version-alt-maxwidth.diff
Patch3: tcsh-%version-alt-tinfo.diff
Patch4: tcsh-%version-owl-config.diff
Patch5: tcsh-%version-owl-lscolors.diff
Patch6: tcsh-%version-owl-no-TIOCSTI.diff
Patch7: tcsh-%version-owl-strnxxx.diff
Patch8: tcsh-%version-owl-tmp.diff
Patch9: tcsh-%version-owl-warnings.diff
Conflicts: setup < 2.2.14-alt2
Provides: csh = %version

# Automatically added by buildreq on Sun Jan 15 2012
BuildRequires: groff-base libtinfo-devel

%description
tcsh is an enhanced but completely compatible version of csh, the C
shell.  tcsh is a command language interpreter which can be used both
as an interactive login shell and as a shell script command processor.
tcsh includes a command line editor, programmable word completion,
spelling correction, a history mechanism, job control and a C language
like syntax.

%package doc
Group: Shells
Summary: Optional documentation for %name
BuildArch: noarch
Requires: %name = %EVR

%description doc
This package contains optional documentation for %name.

%prep
%setup
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

%define _bindir	/bin

%build
%configure \
  --disable-rpath
%__make all
test -x %__perl && %__perl tcsh.man2html tcsh.man || :
%__make -C nls catalogs

%install
install -pm 755 -D tcsh %buildroot/bin/tcsh
install -pm 644 -D tcsh.man %buildroot%_man1dir/tcsh.1
ln -sf tcsh %buildroot/bin/csh
ln -sf tcsh.1 %buildroot%_man1dir/csh.1

install -pm 644 -D %_sourcedir/tcshrc.skel %buildroot/etc/skel/.tcshrc
install -pm 644 %_sourcedir/tcsh.login %buildroot/etc/csh.login
install -pm 644 %_sourcedir/tcsh.cshrc %buildroot/etc/csh.cshrc

while read lang language; do
	dest=%buildroot%_datadir/locale/$lang/LC_MESSAGES
	if test -f nls/$language.cat; then
		install -pm 644 -D nls/$language.cat $dest/tcsh.mo
	fi
done << EOF
en C
et et
fi finnish
fr french
de german
el greek
it italian
ja ja
pl pl
ru russian
es spanish
uk ukrainian
EOF

%find_lang tcsh

%post
# do not edit /etc/shells on upgrades
if [ $1 -eq 1 ]; then
	grep -Fqx /bin/csh /etc/shells || echo /bin/csh >> /etc/shells
	grep -Fqx /bin/tcsh /etc/shells || echo /bin/tcsh >> /etc/shells
fi

%preun
# do not edit /etc/shells on upgrades
if [ $1 -eq 0 ]; then
	sed -i -e '/^\/bin\/t\?csh$/d' /etc/shells
fi

%files -f tcsh.lang
%config(noreplace) /etc/csh.*
%config(noreplace) /etc/skel/.tcshrc
/bin/csh
/bin/tcsh
%_man1dir/*.*

%files doc
%doc NewThings FAQ complete.tcsh Fixes tcsh.html

%changelog
* Thu Aug 24 2017 Dmitry V. Levin <ldv@altlinux.org> 6.20.00-alt2
- Fixed and cleaned up spec, resurrected %%changelog.

* Tue Jul 25 2017 Alexey V.Vissarionov <gremlin@altlinux.org> 6.20.00-alt1
- Updated to 6.20.00.
- Disabled TIOCSTI (avoid CVE-2017-5226 issues).
- Moved documentation to separate subpackage.

* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.18.01-alt2.qa1
- Fixed build with glibc >= 2.24.

* Sun Sep 06 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.18.01-alt2
- Fixed infinite loop when built with gcc5.

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
