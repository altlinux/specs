# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: which
Version: 2.20
Release: alt2

Summary: Displays where a particular program in your path is located
License: GPLv3
Group: System/Base
URL: http://www.xs4all.nl/~carlo17/which/
Packager: Slava Semushin <php-coder@altlinux.ru>

# ftp://ftp.gnu.org/gnu/which/which-%version.tar.gz
Source: which-%version.tar
Patch1: which-alt-texinfo.patch
Patch2: which-rh-alt-fixes.patch

%description
The which command shows the full pathname of a specified program,
if the specified program is in your PATH.

%prep
%setup
%patch1 -p2
%patch2 -p2

%build
%configure
%make_build --silent --no-print-directory CFLAGS="%optflags -Werror"

%install
%makeinstall --silent --no-print-directory
rm -f -- %buildroot%_infodir/dir

%files
%doc AUTHORS EXAMPLES NEWS
%_bindir/%name
%_man1dir/%name.1.*
%_infodir/%name.info.*

%changelog
* Sat May 30 2009 Slava Semushin <php-coder@altlinux.ru> 2.20-alt2
- Removed obsolete %%install_info/%%uninstall_info calls

* Fri Mar 27 2009 Slava Semushin <php-coder@altlinux.ru> 2.20-alt1
- 2.20 (Closes: #19290)
- New maintainer
- License changed to GPLv3
- Enabled _unpackaged_files_terminate_build
- Using -Werror flag for compiler by default

* Wed Dec 26 2007 Slava Semushin <php-coder@altlinux.ru> 2.18-alt1
- 2.18

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2.16-alt3
- Rebuilt.

* Tue Jun 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.16-alt2
- Specfile cleanup.

* Tue Oct 21 2003 Stanislav Ievlev <inger@altlinux.ru> 2.16-alt1
- 2.16

* Mon Mar 17 2003 Stanislav Ievlev <inger@altlinux.ru> 2.14-alt3
- added patch (rh-broken) from RH: fix some broken code

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 2.14-alt2
- rebuild with gcc3

* Thu Aug 01 2002 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt1
- 2.14

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt1
- 2.13

* Tue Nov 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.12-ipl1mdk
- 2.12

* Wed Jun 28 2000 Dmitry V. Levin <ldv@fandra.org> 2.11-ipl1mdk
- 2.11
- RE adaptions.

* Wed Apr  5 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 2.9-4mdk
- new group System/Base
- updated BuildRoot

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Wed Aug 18 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add defattr

* Sun Aug 08 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 2.8 :
	* aclocal.m4 was missing from the tar, resulting in
	  a build failure if autoconf isn't installed.

* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Upgrade to the offical version of Gnu project.
- Rewriting the spec-files.
- 2.7 :
    * Support for aliases
    * Configure/compile fix in the `tilde' directory.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- handle RPM_OPT_FLAGS
- Makefiles and source code are NOT docs.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
