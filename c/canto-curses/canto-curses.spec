Name: canto-curses
Version: 0.9.0
Release: alt1.alpha1.git20140904
Summary: Curses frontend for Canto daemon
License: GPLv2
Group: Networking/News
Url: http://codezen.org/canto-ng/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/themoken/canto-curses.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-modules-curses
BuildPreReq: libreadline-devel libncursesw-devel

Requires: canto-next

%description
Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*
%_man1dir/*

%changelog
* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.alpha1.git20140904
- Initial build for Sisyphus

