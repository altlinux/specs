Name:		hexglass
Version:	1.2.1
Release:	alt1
Source:		%{name}-%{version}.tar.gz
Summary:	Tetris-like puzzle game
Group:		Games/Puzzles
License:	GPLv3

# Automatically added by buildreq on Thu Feb 17 2011
BuildRequires: gcc-c++ libmpc libqt4-devel

%description
The HexGlass is a Tetris-like puzzle game where
10 different types of blocks continuously fall
from above and you must arrange them to make
horizontal rows of hexagonal bricks.
Completing any row causes those hexagonal blocks
to disappear and the rest above move downwards.
The blocks above gradually fall faster and the
game is over when the screen fills up and blocks
can no longer fall from the top.

%prep
%setup

%build
qmake-qt4
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc README CHANGES MANIFEST 
%_qt4dir/bin/*

%changelog
* Thu Feb 17 2011 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Initial build from scratch

