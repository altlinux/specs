%set_verify_elf_method unresolved=strict

Name: gnustep-AppWrapper
Version: 0.1
Release: alt2
Summary: GNUstep application wrapper
License: GPL
Group: Graphical desktop/GNUstep
Url: http://appwrapper.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
AppWrapper is a little GNUstep application I wrote to play around with
GNUstep in order to help myself learn the GNUstep development system and
a little bit of a couple of frameworks.

I also wanted a quick way to create application wrappers for non GNUstep
applications. So I could find GWorkspace more usefull in my envrionment.

Functionality: Current AppWrapper does not do much and it does not do it
as easily as I am sure it could.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

%files
%doc README TODO Documentation/ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

