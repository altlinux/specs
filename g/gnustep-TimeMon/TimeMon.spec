%set_verify_elf_method unresolved=strict

Name: gnustep-TimeMon
Version: 4.1
Release: alt1
Summary: CPU time usage monitor
License: Permission to use, copy, modify, and distribute without fee
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
TimeMon gives a graphical representation of where the CPU cycles are
going. It's coarse, but better than nothing. The best feature is that it
runs in an icon on your dock, so that you never lose it.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ChangeLog README.rtf
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Initial build for Sisyphus

