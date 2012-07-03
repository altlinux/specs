Name: greed
Version: 3.8
Release: alt1
Source: %name-%version.tar.gz
License: BSD-like
Group: Games/Puzzles
Summary: the board puzzle game of Greed
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Thu Dec 06 2007
BuildRequires: libncurses-devel

%description
The strategy game of Greed.  Try to eat as much as possible of the board
before munching yourself into a corner.

%prep
%setup

%build
%make SFILE=%_localstatedir/games/%name.hs

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_man6dir %buildroot%_localstatedir/games
install %name %buildroot%_gamesbindir/
install %name.6 %buildroot%_man6dir/
install /dev/null %buildroot%_localstatedir/games/%name.hs

%files
%_man6dir/%name.6*
%attr(664,root,games) %config(noreplace) %_localstatedir/games/%name.hs
%attr(2711,root,games) %_gamesbindir/%name

%changelog
* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 3.8-alt1
- Autobuild version bump to 3.8

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Autobuild version bump to 3.7

* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Initial build for ALT

