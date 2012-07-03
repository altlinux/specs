Name: diffstat
Version: 1.55
Release: alt1

Summary: An utility which provides statistics based on the output of diff
License: BSD-style
Group: Development/Other
Url: http://invisible-island.net/diffstat/
# ftp://invisible-island.net/diffstat/diffstat-%version.tgz
Source: diffstat-%version.tar

Requires: diffutils

%description
The diff command compares files line by line.  Diffstat reads the
output of the diff command and displays a histogram of the insertions,
deletions and modifications in each file.  Diffstat is commonly used
to provide a summary of the changes in large, complex patch files.

%prep
%setup

%build
%configure --with-warnings
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files
%_bindir/*
%_mandir/man?/*
%doc CHANGES README

%changelog
* Tue Jan 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.55-alt1
- Updated to 1.55.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1.54-alt1
- Updated to 1.54.

* Mon Aug 30 2010 Dmitry V. Levin <ldv@altlinux.org> 1.53-alt1
- Updated to 1.53 (closes: #19890).

* Wed Oct 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1.45-alt1
- Updated to 1.45.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.43-alt2
- Bump release.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.43-alt1
- Updated to 1.43.

* Tue Aug 30 2005 Ilya Evseev <evseev@altlinux.ru> 1.41-alt1
- update to new version

* Mon Feb 28 2005 Ilya Evseev <evseev@altlinux.ru> 1.38-alt1
- 1.38

* Sat Jan  8 2005 Ilya Evseev <evseev@altlinux.ru> 1.37-alt1
- Updated to 1.37
- Specfile: added russian description/summary, changed URL's

* Mon Jan 13 2003 Dmitry V. Levin <ldv@altlinux.org> 1.32-alt1
- Updated to 1.32

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 1.28-ipl3mdk
- rebuild (gcc 3.2)

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.28-ipl2mdk
- rebuild

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.28-ipl1mdk
- RE adaptions.

* Mon Dec 25 2000 Yves Duret <yduret@mandrakesoft.com> 1.28-1mdk
- new and shiny version 1.28
- macros
- added URL tag, fixed Source: tag
- added doc

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.27-12mdk
- BM, macros, spec-helper

* Thu Apr 4 2000 Denis Havlik <denis@mandrakesoft.com> 1.27-11mdk
- New group: Development/Other

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Sun Jul 18 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.27

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
