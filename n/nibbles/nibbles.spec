# $Revision: 1.13 $, $Date: 2002/02/15 22:40:04 $
Summary: NCurses based nibbles game
Name: nibbles
Version: 0.0.4
Release: alt1.qa1
License: GPL
Group: Games/Arcade
Source0: http://www.earth.li/projectpurple/files/%name-v%version.tar.gz
Patch0: %name-Makefile.patch
Patch1: %name-window.patch
Patch2: %name-score.patch
Url: http://www.earth.li/projectpurple/progs/nibbles.html
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Wed Dec 16 2009
BuildRequires: libncurses-devel

%description
Nibbles is a remake of the classic Snake/Nibbles game in ncurses. I am
sure that better nibbles games exist, but I thought that I'd write an
ncurses one to learn how.

%prep
%setup -q -n %name-v%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make DATADIR=%_datadir

%install
install -d %buildroot{%_bindir,%_datadir/games,/var/games}

install nibbles %buildroot%_bindir
touch %buildroot/var/games/nibbles.score
cp -a nibbles.levels %buildroot%_datadir/games

%files
%defattr(644,root,root,755)
%attr(2711,root,games) %_bindir/nibbles
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/nibbles.score
%_datadir/games/nibbles.levels
%doc README TODO HISTORY CREDITS example.nibblerc

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for nibbles
  * postclean-05-filetriggers for spec file

* Wed Dec 16 2009 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Initial build from PLD

