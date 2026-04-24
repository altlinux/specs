Name:		puzzle15
Version:	1.0.4
Release:	alt1
Summary:	puzzle15
Group:		Games/Puzzles
License:	GPLv3+
URL:		https://bitbucket.org/admsasha/puzzle15
Source0:	%{name}-%{version}.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires:	cmake 
BuildRequires:	gcc-c++
BuildRequires:	libSDL3-devel libSDL3_ttf-devel libSDL3_image-devel libSDL3_mixer-devel

%description
The 15 Puzzle is a classic sliding tile puzzle.
One space is left empty, allowing the tiles to be moved.
The goal is to arrange the tiles in numerical order by sliding 
them into the vacant spot, using the fewest moves possible.

%prep
%setup -q

%build
cd desktop
%cmake
%cmake_build

%install
cd desktop
%cmake_install


%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Apr 23 2026 Alexander Danilov <admsasha@altlinux.org> 1.0.4-alt1
- Initial package.
