%define pypi_name psutils
%def_with check

Name: psutils
Version: 3.3.15
Release: alt1
Epoch: 2

Summary: PDF and PostScript document manipulation utilities
License: GPL-3.0-or-later
Group: Publishing

Url: https://github.com/rrthomas/psutils
VCS: https://github.com/rrthomas/psutils
Source: %name-%version.tar
Patch1: %name-3.3.14-alt-version-fallback.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-argparse-manpage
BuildRequires: python3-module-puremagic
BuildRequires: python3-module-pypdf
BuildRequires: paper

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-datafiles
BuildRequires: python3-module-wand
BuildRequires: ghostscript
BuildRequires: a2ps
%endif

Requires: paper

%description
PSUtils is a suite of utilities for manipulating PDF and PostScript
documents. You can select and rearrange pages, including arrangement into
signatures for booklet printing, combine multiple pages into a single page
for n-up printing, and resize, flip and rotate pages.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md COPYING
%_bindir/epsffit
%_bindir/extractres
%_bindir/includeres
%_bindir/psbook
%_bindir/psjoin
%_bindir/psnup
%_bindir/psresize
%_bindir/psselect
%_bindir/pstops
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}-%version.dist-info/
%_man1dir/*

%changelog
* Tue May 19 2026 Anton Farygin <rider@altlinux.org> 2:3.3.15-alt1
- 3.3.14 -> 3.3.15

* Tue Feb 04 2025 Anton Farygin <rider@altlinux.org> 2:3.3.14-alt1
- 2.10 -> 3.3.14
- upstream rewrote psutils in Python (was Perl + autotools)
- now supports PDF in addition to PostScript
- added version fallback patch for build time

* Sun Oct 15 2023 Michael Shigorin <mike@altlinux.org> 2:2.10-alt2
- fix build --without check

* Fri Oct 13 2023 Fr. Br. George <george@altlinux.org> 2:2.10-alt1
- 2.10

* Fri Nov 05 2021 Anton Farygin <rider@altlinux.ru> 2:2.07-alt1
- 2.07

* Thu Jul 08 2021 Anton Farygin <rider@altlinux.ru> 2:2.06-alt1
- 2.06

* Tue May 25 2021 Anton Farygin <rider@altlinux.ru> 2:2.05-alt1
- 1.23 -> 2.05
- fixed License tag

* Sun Nov 11 2018 Anton Farygin <rider@altlinux.ru> 2:1.23-alt2
- fixed URL

* Fri Oct 05 2018 Anton Farygin <rider@altlinux.ru> 2:1.23-alt1
- up to 1.23

* Thu Dec 28 2017 Anton Farygin <rider@altlinux.ru> 1:p17-alt3
- fixed build with  perl-5.26

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:p17-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Feb 27 2008 Fr. Br. George <george@altlinux.ru> 1:p17-alt2
- Pageflip patch

* Tue Feb 19 2008 Victor Forsyuk <force@altlinux.org> 1:p17-alt1
- Rebuild with 'alt' release prefix due to deprecation of ipl* releases.

* Wed Mar 02 2005 Victor Forsyuk <force@altlinux.ru> p17-ipl10mdk
- Manpage correction for psresize (Fedora).
- Support getting paper size from current locale (Fedora).

* Sat Oct 05 2002 Rider <rider@altlinux.ru> p17-ipl9mdk
- rebuild (gcc 3.2)
- specfile cleanup

* Mon Apr 15 2002 Rider <rider@altlinux.ru> p17-ipl8mdk
- rebuild

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Aug 30 2000 Etienne Faure <etienne@mandrakesoft.com> p17-6mdk
- rebuilt with new %%doc and _mandir macro

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> p17-5mdk
- Fix bad tag value.
- Fix ownership.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> p17-4mdk
- Fix group.

