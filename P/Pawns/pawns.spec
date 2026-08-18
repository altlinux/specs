%define _unpackaged_files_terminate_build 1

Name: Pawns
Version: 1.0.0
Release: alt1

Summary: A feature-rich chess application built with C++ and Qt6
License: GPL-3.0-or-later
Group: Games/Boards
Url: https://github.com/alamahant/Pawns
Vcs: https://github.com/alamahant/Pawns.git

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel qt6-multimedia-devel
BuildRequires: libminiupnpc-devel
Requires: stockfish

%description
A feature-rich chess application built with C++ and Qt6. Play against
Stockfish, challenge friends locally or remotely, or watch engines
battle it out.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

install -D -m0644 io.github.alamahant.%name.desktop %buildroot%_desktopdir/%name.desktop
install -D -m0644 io.github.alamahant.%name.png %buildroot%_pixmapsdir/io.github.alamahant.%name.png

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/io.github.alamahant.%name.png

%changelog
* Tue Aug 18 2026 Mikhail Nogin <joycap@altlinux.org> 1.0.0-alt1
- Initial built for Sisyphus.
