%set_verify_elf_method unresolved=strict

Name: gnustep-Stepulator
Version: 1.0
Release: alt1
Summary: Scientific calculator implementing RPN notation for GNUstep
License: BSD
Group: Graphical desktop/GNUstep
Url: http://packages.ubuntu.com/ru/lucid/stepulator.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
Stepulator is a scientific calculator implementing the RPN notation. It
is developed in Objective-C and is currently being maintained on GNUstep
and MacOS-X (cocoa).

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
%doc LICENSE README
%_bindir/*
%_libdir/GNUstep

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

