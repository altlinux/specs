Name: rcs
Version: 5.10.1
Release: alt1
Serial: 1

Summary: Revision Control System (RCS) file version management tools
Summary(ru_RU.UTF8): Revision Control System (RCS) - утилиты отслеживания версий файлов.
License: %gpl3plus
Group: Development/Other
Url: http://www.gnu.org/software/rcs/
Source: ftp://ftp.gnu.org/pub/gnu/rcs/%name-%version.tar
Patch1: rcs-rh-configure-c99.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: lzip diffutils ed groff-base texinfo

%description
The Revision Control System (RCS) manages multiple revisions of files.
RCS automates the storing, retrieval, logging, identification, and
merging of revisions. RCS is useful for text that is revised frequently,
for example programs, documentation, graphics, papers, and form letters.

%prep
%setup
%patch1 -p1

%build
%autoreconf
export \
       ac_cv_path_SENDMAIL=%_sbindir/sendmail
%configure --with-diffutils
%make_build

%install
%makeinstall man1dir=%buildroot%_man1dir man5dir=%buildroot%_man5dir

install -m 755 src/rcsfreeze %buildroot%_bindir

%check
make check XFAIL_TESTS="`tests/known-failures %{version}`"

%files
%doc ChangeLog COPYING THANKS NEWS README
%_bindir/*
%_mandir/man?/*
%_infodir/*

%changelog
* Sat Apr 19 2025 L.A. Kostis <lakostis@altlinux.ru> 1:5.10.1-alt1
- 5.10.1.
- Modernize .spec and build.
- Update -rh patches.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:5.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1:5.7-alt1
- Imported patches from FC rcs package.
- Cleaned up specfile.

* Tue Oct 21 2003 Nazar Yurpeak <phoenix@altlinux.org> 5.7-ipl7mdk
- updated BuildRequires
- fixed Source url
- fixed autoconf version

* Wed Oct 16 2002 Rider <rider@altlinux.ru> 5.7-ipl6mdk
- Russian summary
- rebuild (gcc 3.2)

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 5.7-ipl5mdk
- rebuild

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 5.7-ipl4mdk
- RE adaptions.

* Wed Aug 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.7-4mdk
- BM

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 5.7-3mdk
- New groups

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 10)

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file; added BuildRoot

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
