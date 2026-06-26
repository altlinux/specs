Name: greed
Version: 4.5
Release: alt2
Source: %name-%version.tar.gz
License: BSD-2-Clause
Group: Games/Puzzles
Summary: the board puzzle game of Greed
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Thu Dec 06 2007
BuildRequires: libncursesw-devel asciidoc-a2x
Patch: a2x.patch
Patch1: gcc15.patch

%description
The strategy game of Greed.  Try to eat as much as possible of the board
before munching yourself into a corner.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%make SFILE=%_localstatedir/games/%name.hs

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_man6dir %buildroot%_localstatedir/games
install %name %buildroot%_gamesbindir/
install %name.6 %buildroot%_man6dir/
install /dev/null %buildroot%_localstatedir/games/%name.hs

%files
%_man6dir/%name.6*
%doc *.adoc
%attr(664,root,games) %config(noreplace) %_localstatedir/games/%name.hs
%attr(2711,root,games) %_gamesbindir/%name

%changelog
* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 4.5-alt2
- Fix GCC15 build

* Tue Mar 31 2026 Fr. Br. George <george@altlinux.org> 4.5-alt1
- Autobuild version bump to 4.5

* Thu Dec 04 2025 Fr. Br. George <george@altlinux.org> 4.3-alt1
- Autobuild version bump to 4.3

* Sun Jul 16 2023 Fr. Br. George <george@altlinux.org> 4.2-alt2
- Rebuild with libncurses6

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Autobuild version bump to 4.2

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Autobuild version bump to 4.1

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 3.11-alt1
- Autobuild version bump to 3.11

* Tue Jun 03 2014 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10

* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 3.9-alt1
- Autobuild version bump to 3.9

* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 3.8-alt1
- Autobuild version bump to 3.8

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Autobuild version bump to 3.7

* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Initial build for ALT

