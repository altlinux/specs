%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tig
Version: 2.5.8
Release: alt1

Summary: Text-mode interface for git
License: GPLv2+
Group: Development/Other

URL: https://jonas.github.io/tig/
VCS: https://github.com/jonas/tig.git
Source: %name-%version.tar

Requires: git-core

BuildRequires: asciidoc
BuildRequires: hardlink
BuildRequires: libncursesw-devel
BuildRequires: libpcre-devel
BuildRequires: libreadline-devel
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:
BuildRequires: /dev/pts
BuildRequires: git-core
BuildRequires: util-linux
}}

%description
Tig is an ncurses-based text-mode interface for git. It functions mainly
as a Git repository browser, but can also assist in staging changes
for commit at chunk level and act as a pager for output from various
Git commands.

%prep
%setup

%build
export C_INCLUDE_PATH=/usr/include/pcre
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build V=1 src/tig doc-man

%install
install -pD -m755 src/tig %buildroot%_bindir/tig
install -pD -m755 contrib/tig-pick %buildroot%_bindir/tig-pick
install -pD -m644 doc/tig.1 %buildroot%_man1dir/tig.1
install -pD -m644 doc/tigrc.5 %buildroot%_man5dir/tigrc.5
install -pD -m644 doc/tigmanual.7 %buildroot%_man7dir/tigmanual.7
mkdir -p %buildroot%_datadir/tig
install -p -m644 contrib/*.tigrc %buildroot%_datadir/tig/
install -pD -m644 contrib/tig-completion.bash %buildroot%_datadir/bash-completion/completions/tig
install -pD -m644 contrib/tig-completion.bash %buildroot%_datadir/zsh/site-functions/tig-completion.bash
install -pD -m644 contrib/tig-completion.zsh  %buildroot%_datadir/zsh/site-functions/_tig
hardlink -v %buildroot%_datadir

%check
src/tig -v
export C_INCLUDE_PATH=/usr/include/pcre
script -e -c 'make test' /dev/null

%files
%doc COPYING NEWS.adoc README.adoc doc/manual.adoc
%_bindir/tig
%_bindir/tig-pick
%_man1dir/tig.1*
%_man5dir/tigrc.5*
%_man7dir/tigmanual.7*
%_datadir/tig
%_datadir/bash-completion/completions/tig
%_datadir/zsh/site-functions/_tig
%_datadir/zsh/site-functions/tig-completion.bash

%changelog
* Wed Feb 08 2023 Vitaly Chikunov <vt@altlinux.org> 2.5.8-alt1
- Update to tig-2.5.8 (2023-02-04).

* Fri Aug 26 2022 Vitaly Chikunov <vt@altlinux.org> 2.5.7-alt1
- Update to tig-2.5.7 (2022-08-25).

* Fri Jul 15 2022 Vitaly Chikunov <vt@altlinux.org> 2.5.6-alt2
- Package tig-completion.bash for zsh completion.

* Wed Jul 13 2022 Vitaly Chikunov <vt@altlinux.org> 2.5.6-alt1
- Update to tig-2.5.6 (2022-07-11).

* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 2.5.5-alt3
- Fix install perms of tig-pick.
- Do not use libpcre2 (there is already POSIX regex support).

* Sat Apr 30 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.5.5-alt2
- Rebuilt against libpcre2.

* Fri Jan 14 2022 Vitaly Chikunov <vt@altlinux.org> 2.5.5-alt1
- Updated to tig-2.5.5 (2022-01-11).

* Sun Dec 19 2021 Vitaly Chikunov <vt@altlinux.org> 2.5.4-alt2
- Packaged tig-pick, completions, tigrc examples, and manual.
- Fixed lfs=strict build on 32-bit systems.

* Tue Jun 15 2021 Alexey Tourbin <at@altlinux.ru> 2.5.4-alt1
- 2.5.3 -> 2.5.4

* Tue Apr 27 2021 Alexey Tourbin <at@altlinux.ru> 2.5.3-alt1
- 2.5.2 -> 2.5.3

* Wed Feb 17 2021 Alexey Tourbin <at@altlinux.ru> 2.5.2-alt1
- 2.5.0 -> 2.5.2

* Sat Nov 23 2019 Alexey Tourbin <at@altlinux.ru> 2.5.0-alt1
- 2.4.0 -> 2.5.0

* Sun Jul 22 2018 Alexey Tourbin <at@altlinux.ru> 2.4.0-alt1
- 2.3.2 -> 2.4.0

* Wed Dec 27 2017 Alexey Tourbin <at@altlinux.ru> 2.3.2-alt1
- 2.3.1 -> 2.3.2

* Mon Dec 18 2017 Alexey Tourbin <at@altlinux.ru> 2.3.1-alt1
- 2.3.0 -> 2.3.1

* Thu Oct 05 2017 Alexey Tourbin <at@altlinux.ru> 2.3.0-alt2
- built with readline

* Wed Oct 04 2017 Alexey Tourbin <at@altlinux.ru> 2.3.0-alt1
- 2.2.2 -> 2.3.0

* Fri Aug 18 2017 Alexey Tourbin <at@altlinux.ru> 2.2.2-alt1
- 1.1 -> 2.2.2

* Wed Oct 24 2012 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1

* Fri Sep 21 2012 Alexey Tourbin <at@altlinux.ru> 1.0-alt2
- packaged tigmanual(7)

* Fri May 11 2012 Alexey Tourbin <at@altlinux.ru> 1.0-alt1
- tig-1.0

* Tue Feb 14 2012 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- tig-0.18

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt2
- tig-0.17-43-gcc3ca7c

* Sun Mar 20 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- tig-0.17

* Mon Nov 22 2010 Alexey Tourbin <at@altlinux.ru> 0.16.2-alt1
- tig-0.16.2

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- tig-0.16

* Fri Dec 04 2009 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- tig-0.15

* Mon Jul 20 2009 Alexey Tourbin <at@altlinux.ru> 0.14.1-alt2
- tig-0.14.1-29-g1e69632

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 0.14.1-alt1
- 0.14 -> 0.14.1

* Sat Feb 14 2009 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- packaged NEWS.html

* Sat Feb 14 2009 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.12.1 -> 0.14

* Sat Oct 11 2008 Alexey Tourbin <at@altlinux.ru> 0.12.1-alt1
- 0.12 -> 0.12.1

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.11 -> 0.12

* Tue Apr 15 2008 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.10.1 -> 0.11

* Fri Mar 21 2008 Alexey Tourbin <at@altlinux.ru> 0.10.1-alt1
- 0.9.1 -> 0.10.1
- built with libncursesw

* Sun Oct 28 2007 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt1
- updated to tig-0.9.1

* Sat Jul 21 2007 Alexey Tourbin <at@altlinux.ru> 0.8-alt1
- updated to tig-0.8-12-g56b6ea5

* Sat Jun 16 2007 Alexey Tourbin <at@altlinux.ru> 0.7-alt1
- updated to tig-0.7-18-gd1858de

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 0.6-alt1
- updated to tig-0.6-1-ga1d2855

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 0.5-alt5
- updated to tig-0.5-16-ge15ec88 (improved handling of remotes)

* Sun Jan 07 2007 Alexey Tourbin <at@altlinux.ru> 0.5-alt4
- updated to tig-0.5-g337d737

* Tue Oct 31 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt3
- new snapshot, fixes SEGV in tree view

* Wed Oct 18 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt2
- in main view, fix handling of headlines that start with whitespace

* Tue Oct 03 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt1
- new version

* Sat Sep 09 2006 Alexey Tourbin <at@altlinux.ru> 0.4-alt1
- new snapshot

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- initial revision
