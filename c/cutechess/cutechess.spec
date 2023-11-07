Name:    cutechess
Version: 1.3.1
Release: alt1

Summary: Cute Chess is a graphical user interface, command-line interface and a library for playing chess
License: GPL-3.0
Group:   Other
Url:     https://github.com/cutechess/cutechess

Packager: Leonid Znamenok <respublica@altlinux.org>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Core5Compat)

%description
Cute Chess is a set of cross-platform tools for working with chess engines.

It consists of:
cutechess - a graphical user interface.
cutechess-cli - a command-line interface for automating chess engine matches.

Cute Chess is developed using C++ and Qt.
The project has been in development since
May 2008 and is currently in active development.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc *.md COPYING AUTHORS
%_bindir/cutechess
%_bindir/cutechess-cli
%_desktopdir/%name.desktop
%_iconsdir/application/*/apps/%name.*
%_man5dir/*
%_man6dir/*

%changelog
* Fri Oct 06 2023 Leonid Znamenok <respublica@altlinux.org> 1.3.1-alt1
- New release 1.3.1

* Tue Jul 11 2023 Leonid Znamenok <respublica@altlinux.org> 1.3.0-alt0.beta4
- Initial build for Sisyphus
