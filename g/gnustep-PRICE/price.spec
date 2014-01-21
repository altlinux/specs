%set_verify_elf_method unresolved=strict

Name: gnustep-PRICE
Version: 1.2.0
Release: alt3
Summary: PRICE (Precision Raster Image Convolution Engine)
License: GPLv2+
Group: File tools
Url: http://sourceforge.net/projects/price/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
PRICE is a high quality image manipulation and enhancement application
and supports the image formats supported by GNUstep. It allows various
manipulations like simple rotating and flipping up to edge tracing or
noise reduction. Custom convolutions are supported.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

