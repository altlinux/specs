#set_verify_elf_method unresolved=strict

Name: gnustep-ProjectManager
Version: 0.2
Release: alt5
Summary: Alternative Integrated Development Environment (IDE) for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://home.gna.org/pmanager/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu
Patch1: fix-undefined-sel_eq.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel doxygen
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-HighlighterKit-devel gnustep-WizardKit-devel

Requires: gnustep-HighlighterKit
Requires: gnustep-WizardKit
Requires: gnustep-back

%description
ProjectManager is an alternative Integrated Development Environment
(IDE) for GNUstep. It aims to provide a simple, but very usable
development environment for all a programmer's everyday needs.

%package docs
Summary: Documentation for ProjectManager
Group: Documentation
BuildArch: noarch

%description docs
ProjectManager is an alternative Integrated Development Environment
(IDE) for GNUstep. It aims to provide a simple, but very usable
development environment for all a programmer's everyday needs.

This package contains documentation for ProjectManager.

%prep
%setup
%patch1 -p2

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
doxygen

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc BUGS README TRICKS
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%doc Documentation/html/*

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.2-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt4.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added Requires: gnustep-HighlighterKit, Requires: gnustep-WizardKit
  and Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

