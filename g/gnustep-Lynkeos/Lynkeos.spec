%set_verify_elf_method unresolved=strict

Name: gnustep-Lynkeos
Version: 1.2
Release: alt5.1
Summary: Tool to process planetary astronomical images for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://packages.debian.org/jessie/lynkeos.app
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build -C Sources \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-DGNUSTEP -I%_includedir/libavcodec -I%_includedir/libavformat'

pushd Docs
doxygen
popd

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std -C Sources GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc Docs/TODO.rtf
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%doc Docs/html/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.2-alt5.1
- NMU: Rebuild with libgnutls30.

* Tue May 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5
- Fixed build

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

