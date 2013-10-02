%set_verify_elf_method unresolved=strict

Name: gnustep-Zipper
Version: 1.5
Release: alt1
Summary: Tool for inspecting the contents of a compressed archive
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel

%description
Zipper consists only of a single window, displaying the contents of the
selected archive. Currently, you can view and extract .tar, .tar.gz,
.tar.bz2, .rar, .lha, .lhz and .zip archives.

Features:
* Multi-document
* ZIP, TAR (and BSD tar), LHA, 7Zip
* TAR creation
* GWorkspace integration

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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

