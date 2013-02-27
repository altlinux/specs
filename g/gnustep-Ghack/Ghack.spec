%set_verify_elf_method unresolved=strict

Name: gnustep-Ghack
Version: 0.1.8
Release: alt1
Summary: Graphical nethack
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
Minimal tile engine graphics support.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog HACKING README TODO
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

