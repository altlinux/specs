%set_verify_elf_method unresolved=strict

Name: gnustep-FTP
Version: 0.4
Release: alt1
Summary: FTP is a compact and handy application for file transfers using the FTP protocol
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
Two-paned application, having on the left side a browser for the local
files and at right a browser for the remote host.

The application offers support for all three different connection modes
described in the RFC: active, passive and default (rarely used).

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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added menu files (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

