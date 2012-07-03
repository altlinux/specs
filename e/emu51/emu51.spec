Name: emu51
Version: 0.0.3
Release: alt1.1
Group: Emulators
Summary: 8051 emulator
License: GPL
BuildPreReq: liballegro-devel gcc-c++
Source0: %name.tar
Packager: Yury A. Romanov <damned@altlinux.ru>

%description
Software Graphical 8051 Emulator, based on Allegro.

%prep
%setup -n %name

%build
%make_build LISTPATH=%_datadir/%name-%version

%install
%make_install DESTDIR=%buildroot LISTPATH=%_datadir/%name-%version install

%files
%_bindir/*
%_datadir/%name-%version/*

%changelog
* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.1
- Rebuilt with liballegro4.4

* Thu Jan 03 2008 Yury A. Romanov <damned@altlinux.ru> 0.0.3-alt1
- Initial build for Sisyphus
- Added Makefile for Linux
- Created spec

