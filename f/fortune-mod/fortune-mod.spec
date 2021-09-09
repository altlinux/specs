%define _unpackaged_files_terminate_build 1

Name: fortune-mod
Version: 2.28.0
Release: alt2

Summary: A program which will display a fortune
License: BSD-4-Clause-UC
Group: Games/Other
Url: https://github.com/shlomif/fortune-mod

Requires: fortune = %EVR
Requires: fortunes = %EVR

Source: %name-%version.tar
Patch0: fortune-dir-2.28.patch

BuildRequires: cmake gcc-c++ librecode-devel
BuildRequires: perl-autodie shlomif-cmake-modules rinutils

%description
Fortune-mod contains the ever-popular fortune program, which will
display quotes or witticisms. Fun-loving system administrators can add
fortune to users' .login files, so that the users get their dose of
wisdom each time they log in.

%package -n fortune
Summary: A program which will display a fortune
Group: Games/Other
Provides: %_datadir/%_gamesdir/fortune
Provides: %_datadir/%_gamesdir/fortune/off

%description -n fortune
Fortune-mod contains the ever-popular fortune program, which will
display quotes or witticisms. Fun-loving system administrators can add
fortune to users' .login files, so that the users get their dose of
wisdom each time they log in.

You may wish to install some fortunes-* packages.

%package -n fortunes
Summary: fortune-mod: fortunes
BuildArch: noarch
Group: Games/Other
PreReq: %_gamesdatadir/fortune

%description -n fortunes
Fortune-mod: standard fortunes

%package -n fortunes-offensive
Summary: fortune-mod: offensive fortunes
BuildArch: noarch
Group: Games/Other
PreReq: %_gamesdatadir/fortune/off

%description -n fortunes-offensive
Fortune-mod: offensive fortunes

Please, please, please request a potentially offensive fortune
if and only if you believe, deep in your heart, that you are
willing to be offended.  (And that you'll just quit using -o
rather than give us grief about it, okay?)

... let us keep in mind the basic governing philosophy of The
Brotherhood, as handsomely summarized in these words: we believe
in healthy, hearty laughter -- at the expense of the whole human
race, if needs be.  Needs be.
       --H. Allen Smith, "Rude Jokes"

%prep
%setup -q %name-%version
%patch0 -p1

%build
cd %name
%cmake -DNO_OFFENSIVE=FALSE

%cmake_build

%install
cd %name
%cmakeinstall_std
mv %{buildroot}/usr/games/fortune %{buildroot}/usr/bin/fortune

%files

%files -n fortune
%_bindir/*
%dir %_datadir/%_gamesdir/fortune
%dir %_datadir/%_gamesdir/fortune/off
%_man1dir/*
%_man6dir/*

%files -n fortunes
%_datadir/%_gamesdir/fortune/*
%exclude %_datadir/%_gamesdir/fortune/off

%files -n fortunes-offensive
%_datadir/%_gamesdir/fortune/off/*

%changelog
* Thu Sep 09 2021 Ilya Mashkin <oddity@altlinux.ru> 2.28.0-alt2
- NMU: rebuild with new recode

* Wed Jun 24 2020 Konstantin Rybakov <kastet@altlinux.org> 2.28.0-alt1
- Updated to upstream version 2.28.0

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.99.1-alt5.qa3
- NMU: added URL

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.99.1-alt5.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for fortunes-offensive
  * arch-dep-package-consists-of-usr-share for fortunes
  * postclean-03-private-rpm-macros for the spec file

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.99.1-alt5.qa1
- NMU: rebuilt for debuginfo.

* Thu Jun 10 2010 Alexey I. Froloff <raorn@altlinux.org> 1.99.1-alt5
- Fix segfault on x86_64 (closes: #23084)

* Sat Nov 08 2008 Sir Raorn <raorn@altlinux.ru> 1.99.1-alt4
- Make it compile with recent glibc

* Sun Jun 01 2008 Sir Raorn <raorn@altlinux.ru> 1.99.1-alt3
- Do not bail if offensive dir is empty

* Wed Apr 30 2008 Sir Raorn <raorn@altlinux.ru> 1.99.1-alt2
- Disabled crappy librecode support (back to iconv)

* Fri Apr 25 2008 Sir Raorn <raorn@altlinux.ru> 1.99.1-alt1
- [1.99.1] (closes: #14733)
- Package split to engine (fortune), standard fortune pack (fortunes)
  and offensive fortune pack (fortunes-offensive) (closes: #5677, #9582)
- fortune(6) moved to %%_bindir (die, ugly /usr/games, die, die, die!)
- This release was tested by hiddenman

* Fri May 14 2004 Sir Raorn <raorn@altlinux.ru> 1.0-ipl36mdk
- Rebuilt with new glibc (closes #4118)

* Fri Feb 27 2004 Sir Raorn <raorn@altlinux.ru> 1.0-ipl35mdk
- Fix race when using -m
- Spec cleanup

* Thu Dec 04 2003 Sir Raorn <raorn@altlinux.ru> 1.0-ipl34mdk
- New packager
- Recode fortune text when fortune(6) called with -m option (closes #2725)
- Move strfile and unstr from %%_sbindir to %%_bindir

* Sun Jun 01 2003 Sir Raorn <raorn@altlinux.ru> 1.0-ipl33mdk
- Keep fortune file in utf-8 encoding and use iconv for recoding
  to current codeset. Thanx to Alexander Bokovoy for iconv(3)
  examples
- Added Packager tag
- Some spec cleanups

* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl32mdk
- rebuild

* Wed Mar 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl31mdk
- Adopted for ALT

* Tue Jan 29 2002 Preston Brown <pbrown@redhat.com>
- more editorial work

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Dec 23 2001 Mike A. Harris <mharris@redhat.com> 1.0-17
- Added bofh-excuses and kernelnewbies fortune files

* Tue Sep  4 2001 Mike A. Harris <mharris@redhat.com> 1.0-16
- Remove an offensive remark.
- s/Copyright/License/
- Fix buildroot line.

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild; FHS stuff

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Jun 25 1999 Guido Flohr <gufl0000@stud.uni-sb.de>
- create fortune manpage without buildroot before installation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

