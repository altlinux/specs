#set_verify_elf_method unresolved=strict

Name: gnustep-ProjectManager
Version: 0.2
Release: alt3
Summary: Alternative Integrated Development Environment (IDE) for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://home.gna.org/pmanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
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

%files
%doc BUGS README TRICKS
%_bindir/*
%_libdir/GNUstep

%files docs
%doc Documentation/html/*

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added Requires: gnustep-HighlighterKit, Requires: gnustep-WizardKit
  and Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

