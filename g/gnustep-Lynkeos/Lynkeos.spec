%set_verify_elf_method unresolved=strict

Name: gnustep-Lynkeos
Version: 1.2
Release: alt2
Summary: Tool to process planetary astronomical images for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/jessie/lynkeos.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel doxygen
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: libfftw3-devel libavcodec-devel libavformat-devel
BuildPreReq: libtiff-devel libswscale-devel

Requires: gnustep-back

%description
This is an application dedicated to the processing of astronomical
(mainly planetary) images taken with a webcam through a telescope.

%package docs
Summary: Documentation for Lynkeos
Group: Documentation
BuildArch: noarch

%description docs
This is an application dedicated to the processing of astronomical
(mainly planetary) images taken with a webcam through a telescope.

This package contains documentation for Lynkeos.

%prep
%setup

%build
%make_build -C Sources \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -I%_includedir/libavcodec -I%_includedir/libavformat' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd Docs
doxygen
popd

%install
%makeinstall_std -C Sources GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc Docs/TODO.rtf
%_bindir/*
%_libdir/GNUstep

%files docs
%doc Docs/html/*

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

