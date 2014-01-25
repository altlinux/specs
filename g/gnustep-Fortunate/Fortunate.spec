%set_verify_elf_method unresolved=strict

Name: gnustep-Fortunate
Version: 3.0
Release: alt1
Summary: Fortunate displays a quotation in a window
License: Public domain / BSD
Group: Graphical desktop/GNUstep
Url: http://www.orange-carb.org/~csaldanh/software.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-pbxbuild

Requires: fortune

%description
Fortunate displays a quotation in a window. Fortunate is a
Cocoa/Objective-C graphical front-end to the command-line BSD fortune
(included) which, since the dawn of time, has been providing countless
seconds of fun each time a user logs in.

%prep
%setup

%build
pbxbuild -p Fortunate3.0.pbproj -g

%make_build -C pbxbuild \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std -C pbxbuild GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc CHANGES README.rtf
%_bindir/*
%_libdir/GNUstep

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

