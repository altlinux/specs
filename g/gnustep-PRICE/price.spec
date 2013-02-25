%set_verify_elf_method unresolved=strict

Name: gnustep-PRICE
Version: 1.2.0
Release: alt1
Summary: PRICE (Precision Raster Image Convolution Engine)
License: GPLv2+
Group: File tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

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

%files
%doc README
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

