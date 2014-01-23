%set_verify_elf_method unresolved=strict

Name: gnustep-NeXTGo
Version: 3.0
Release: alt1
Summary: NeXTGo is the classic Go game
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/nextgo/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
NeXTGo is the classic Go game originally written for the OPENSTEP/Mach
environment.

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
	GNUSTEP_SYSTEM_ROOT=%buildroot%_libdir/GNUstep

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/NeXTGo.app/NeXTGo \
	%buildroot%_bindir/

%files
%doc FAQ README* NeXTGoHelp.rtf
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

