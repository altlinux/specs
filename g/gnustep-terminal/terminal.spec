%set_verify_elf_method unresolved=strict

Name: gnustep-terminal
Version: 0.9.8
Release: alt2
Summary: Terminal emulator for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/terminal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
Terminal is terminal emulator for GNUstep. Multiple windows, scroll
buffer and all the expected features are present. Furthermore it sports
terminal services.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles 
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Sun Jan 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt2
- Added menu file (thnx kostyalamer@)

* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

