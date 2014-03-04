%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-devel
Version: 0.4.2
Release: alt1.git20140228
Summary: Package for build Etoile components
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
Etoile intends to be an innovative GNUstep based user environnement
built from the ground up on highly modular and light components with
project and document orientation in mind, in order to allow users to
create their own workflow by reshaping or recombining provided Services
(aka Applications), Components etc. Flexibility and modularity on both
User Interface and code level should allow us to scale from PDA to
computer environment.

This package contains root enitites for build Etoile.

%prep
%setup

%install
install -d %buildroot%_libdir/GNUstep/Etoile
install -m755 *.sh *.make %buildroot%_libdir/GNUstep/Etoile/

%files
%doc ANNOUNCE HACKING README INSTALL
%_libdir/GNUstep

%changelog
* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140228
- Initial build for Sisyphus

