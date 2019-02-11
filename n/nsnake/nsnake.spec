%define _unpackaged_files_terminate_build 1

Name: nsnake
Version: 3.0.1
Release: alt1.gitd018237
Summary: The classic snake game with textual interface
Url: https://github.com/alexdantas/nSnake
Source: %name-%version.tar
License: GPLv3+
Group: Games/Other

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: ncurses-devel

%description
nSnake is a implementation of the classic snake game with textual interface.
It is playable at command-line and uses the nCurses C library for graphics.

%prep
%setup -n %name-%version
sed -i -r 's/^VERSION =.*/VERSION = %version/' Makefile

%build
%make_build
%make_build doc

%install
%makeinstall_std

%files
%doc COPYING AUTHORS BUGS ChangeLog README.md TODO doc/html 
%_bindir/%name
%_man6dir/%name.6*
%_desktopdir/%name.desktop
%_gamesdatadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/%name.xpm

%changelog
* Sun Oct 21 2018 Vera Blagoveschenskaya <vercha@altlinux.org> 3.0.1-alt1.gitd018237
- Initial build for ALT
