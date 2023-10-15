%def_with check

Name: psutils
Version: 2.10
Release: alt2
Epoch: 2

Summary: PostScript utilities
License: GPLv3
Group: Publishing

Url: https://github.com/rrthomas/psutils
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: gnulib help2man git-core
BuildRequires: paper
BuildRequires: perl(IPC/Run3.pm)

%add_perl_lib_path %_datadir/%name

%description
psutils contains some utilities for manipulating PostScript documents.
Page selections and rearrangement are supported, including arrengement
into signatures for booklet printing, and page merging for n-up printing.

%prep
%setup 

%build
./bootstrap --skip-git --gnulib-srcdir=/usr/share/gnulib
%configure
%make_build

%install
%makeinstall 

%check
%make check

%files
%doc COPYING README
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
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

* Fri Nov 12 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- Rebuilt for Oxygen.

* Fri Aug 27 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- Ajusted perl path in scripts.

* Fri Aug 13 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
