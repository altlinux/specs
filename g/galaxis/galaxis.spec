Name: galaxis
Version: 1.8
Release: alt1
Url: http://www.catb.org/~esr/galaxis/
Source0: %name-%version.tar.gz
License: GPL
Group: Games/Arcade
Summary: Curses-based clone of the nifty little Macintosh game
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Thu Dec 06 2007
BuildRequires: libncurses-devel

%description
A UNIX-hosted, curses-based clone of the nifty little Macintosh
freeware game Galaxis.

%prep
%setup

%build
make
make %name.6

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_man6dir
install -m755 %name %buildroot%_gamesbindir/
install %name.6 %buildroot%_man6dir/

%files
%doc README COPYING
%_man6dir/%name.6*
%_gamesbindir/%name

%changelog
* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Initial build for ALT

* Mon Dec 29 2003 Eric S. Raymond <esr@snark.thyrsus.com> 1.7
- Mac OSX port fix.

* Fri Dec 26 2003 Eric S. Raymond <esr@snark.thyrsus.com> 1.6
- Cleanup fixes to RPM packaging machinery.

* Mon Dec 15 2003 Eric S. Raymond <esr@snark.thyrsus.com> 1.5
- Minor bug fix from James Hiller.

* Tue Jul 30 2002 Eric S. Raymond <esr@thyrsus.com> 1.4
- Moved documentation to XML.

* Sat Apr 20 2002 Eric S. Raymond <esr@thyrsus.com> 1.3
- Applied James Hiller's fix for multiple-reprobe bug.

* Fri Jul 28 2000 Eric S. Raymond <esr@thyrsus.com> 1.2
- Update to modern RPM tools.

RPM seems to choke on changelog entry dates older than 1997...

Sun Oct 23 1994 Eric S. Raymond <esr@thyrsus.com> 1.1
- Original release.
