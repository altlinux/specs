%set_verify_elf_method unresolved=strict

Name: gnustep-Yap
Version: 0.2
Release: alt1
Summary: Yap.app PostScript/PDF previewer
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Yap.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://debian.physik.uni-essen.de/misc/GNUstep/Apps/GPSText/Yap2.tgz
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back
Requires: a2ps ImageMagick ghostscript-classic

%description
A PostScript/PDF previewer and front end to the a2ps text formatting
tool.

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
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_bindir/*
%_libdir/GNUstep

%changelog
* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

