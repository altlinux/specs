%set_verify_elf_method unresolved=strict

Name: gnustep-gmines
Version: 0.2
Release: alt1
Summary: The classic Minesweeper game 
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/gmines/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
The classic Minesweeper game for GNUstep.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

