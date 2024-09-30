%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Summary: Terminal multiplexer
Name: tmux
Version: 3.5
Release: alt1
License: ISC and BSD-3-Clause and BSD-2-Clause
Group: Terminals
Url: https://tmux.github.io/
Vcs: https://github.com/tmux/tmux

Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: bash_completion_tmux.sh
BuildRequires: libevent-devel >= 2.0
BuildRequires: libncurses-devel
BuildRequires: libutempter-devel

%description
tmux is a terminal multiplexer: it enables a number of terminals to
be created, accessed, and controlled from a single screen. tmux may
be detached from a screen and continue running in the background, then
later reattached.

%prep
%setup
%autopatch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --enable-utempter
%make_build

%install
%makeinstall_std
install -Dpm 644 %SOURCE1 %buildroot%_datadir/bash-completion/completions/tmux

%files
%doc CHANGES README COPYING example_tmux.conf
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/tmux

%changelog
* Sun Sep 29 2024 Vitaly Chikunov <vt@altlinux.org> 3.5-alt1
- Update to 3.5 (2024-09-29).

* Wed Feb 14 2024 Vitaly Chikunov <vt@altlinux.org> 3.4-alt1
- Update to 3.4 (2024-02-14).

* Tue Feb 07 2023 Vitaly Chikunov <vt@altlinux.org> 3.3a-alt2
- (Fixes: CVE-2022-47016).

* Tue Jun 14 2022 Vitaly Chikunov <vt@altlinux.org> 3.3a-alt1
- Updated to 3.3a (2022-06-09).

* Wed Jun 01 2022 Vitaly Chikunov <vt@altlinux.org> 3.3-alt1
- Updated to 3.3 (2022-06-01).

* Sat Feb 19 2022 Vitaly Chikunov <vt@altlinux.org> 3.2a-alt1
- Updated to 3.2a (2021-06-10).
- Enable LFS on 32-bit architectures.
- Add simple bash-completion script.
- Fix License tag. Update Url, Vcs tags, and description.
- Enable libutempter.

* Fri Nov 06 2020 Fr. Br. George <george@altlinux.ru> 3.1c-alt1
- Autobuild version bump to 3.1c

* Thu Aug 27 2020 Fr. Br. George <george@altlinux.ru> 3.1b-alt1
- Autobuild version bump to 3.1b

* Sat Mar 28 2020 Fr. Br. George <george@altlinux.ru> 3.0a-alt1
- Update to 3.0a (thanks arei@)

* Thu Nov 07 2019 Fr. Br. George <george@altlinux.ru> 2.9a-alt2
- Fix build

* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 2.9a-alt1
- Autobuild version bump to 2.9a

* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 2.9-alt1
- Autobuild version bump to 2.9

* Wed Apr 03 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8-alt2
- fixed FTBFS: fixed build dependency

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Autobuild version bump to 2.8

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Autobuild version bump to 2.6

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4

* Mon Oct 17 2016 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3

* Thu Jun 02 2016 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Tue Oct 20 2015 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

* Sun May 10 2015 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 1.9-alt1
- Autobuild version bump to 1.9

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Wed Jul 20 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5

* Sun Jun 19 2011 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Wed Jul 28 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up

* Wed Mar 17 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up

* Tue Nov 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.9-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Initial build from MDV

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 0.8-1mdv2010.0
+ Revision: 371132
- Update to 0.8.

* Wed Feb 11 2009 Lev Givon <lev@mandriva.org> 0.7-1mdv2009.1
+ Revision: 339511
- Update to 0.7.

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 0.6-1mdv2009.1
+ Revision: 331825
- import tmux

