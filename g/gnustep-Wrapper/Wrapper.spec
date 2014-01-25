%set_verify_elf_method unresolved=strict

Name: gnustep-Wrapper
Version: 0.1.0
Release: alt1
Summary: Create GNUstep app-wrappers of non-GNUstep applications
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://www.freshports.org/deskutils/gnustep-wrapper
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
GNUstepWrapper provides an easy way to create GNUstep app-wrappers of
non-GNUstep applications. It is the most useful in conjunction with
Enrico Sersale's GWorkspace environment.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-L$PWD/libGSWrapper/obj' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep

%files
%doc AUTHORS NEWS README TODO
%_bindir/*
%_libdir/GNUstep
%_libdir/*.so.*

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

