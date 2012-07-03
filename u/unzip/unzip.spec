Name: unzip
Version: 6.0
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: An utility for unpacking zip archives
License: distributable (BSD-based)
Group: Archiving/Compression

Url: http://www.info-zip.org/
%define src_ver	%(echo %version|sed "s/\\.//"g)
Source: http://downloads.sourceforge.net/infozip/unzip%src_ver.tar.gz
Patch1: unzip-6.0-alt-natspec.patch

# Automatically added by buildreq on Mon Aug 10 2009
BuildRequires: libnatspec-devel

%description
The unzip utility is used to list, test, or extract files from a zip archive.
Zip archives are commonly found on MS-DOS systems. The zip utility, included in
the zip package, creates zip archives. Zip and unzip are both compatible with
archives created by PKWARE(R)'s PKZIP for MS-DOS, but the programs' options and
default behaviors do differ in some respects.

%prep
%setup -n unzip%src_ver
%patch1 -p1
ln -s unix/Makefile .

%__subst 's/1L/1/g' man/*.1

# Let configure emit link flag required for our build instead of useless strip option:
%__subst 's/"-s"/"-lnatspec"/' unix/configure
# Tweak to build with our optimizations and defines:
%define _optlevel 3
%__subst 's/CFLAGS_OPT=.-O3./CFLAGS_OPT="%optflags -DNO_WORKING_ISPRINT -DDATE_FORMAT=DF_YMD"/g' unix/configure
# -DNO_WORKING_ISPRINT fixes ALT bug #21137.

%build
# TODO: build with bzip2 compression method support
#
# We will use `generic' make target instead of ready made `linux' or `linux_noasm`
# This target allows us to use flags and defines produced by unzip's configure
# script at build time instead of hardcoded for linux target.
%make flags
%make_build -e generic
%make test

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -p -m755 %name f%name %{name}sfx unix/zipgrep %buildroot%_bindir
install -p -m644 man/*.1 %buildroot%_man1dir/
ln -s unzip %buildroot%_bindir/zipinfo

%files
%_bindir/*
%_man1dir/*
%doc BUGS LICENSE

%changelog
* Mon Sep 21 2009 Victor Forsyuk <force@altlinux.org> 6.0-alt2
- Fix ALT #21137.

* Mon Aug 10 2009 Victor Forsyuk <force@altlinux.org> 6.0-alt1
- 6.0
- Man pages in section 1, not 1L. Fixed.
- Correct branding: "by ALT Linux Team.  Original by Info-ZIP.".
- Built using DATE_FORMAT=DF_YMD so that unzip -l show dates in ISO format.

* Tue Mar 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt5
- fix CVE-2008-0888

* Wed Aug 01 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt4
- workaround for stupid incoming, nothing else.

* Mon Jul 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt3
- use libnatspec instead iconv + some guesses (fix bug #12313) tnx lav@
- small cleanup spec: use SMP build, use man1dir only

* Tue Apr 10 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt2
- fix CAN-2005-2475
- fix CVE-2005-4667

* Tue May 17 2005 Alexey Voinov <voins@altlinux.ru> 5.52-alt1
- new version (5.52)
- iconv patch updated
- ddottrav patch disabled

* Tue Dec 14 2004 Alexey Voinov <voins@altlinux.ru> 5.50-alt4
- added iconv patch (by Dmitry Vukolov <dav@altlinux.org>)
  [fixes #4871]

* Wed Jul 02 2003 Alexey Voinov <voins@altlinux.ru> 5.50-alt3
- Fixed '../' directory traversal for filenames which include
  quote and/or control characters.
- Spec cleanup.

* Mon Sep 30 2002 Dmitry V. Levin <ldv@altlinux.org> 5.50-alt2
- Fixed summaries, description and url.
- Fixed build to:
  + honor $RPM_OPT_FLAGS properly, define _GNU_SOURCE;
  + avoid implicit strip during buiuld.
- Enabled "unshrinking" algorithm (i.e. LZW decompression).
- Build without assembly, it doesn't seem to increase performance.

* Fri Mar 22 2002 Rider <rider@altlinux.ru> 5.50-alt1
- 5.50

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 5.42-alt1
- 5.42

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 5.41-ipl3mdk
- RE adaptions.
- FHSification.

* Thu Apr 20 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Sun Nov 28 1999 Pixel <pixel@linux-mandrake.com>
- non-intel adaptation (thanks to Stefan van der Eijk)
- cleanup (was it really mandrake adapted?!)

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- build release.

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 5.40
- ix86 optimizations and various spec cleanings

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
