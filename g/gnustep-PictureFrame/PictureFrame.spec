%set_verify_elf_method unresolved=strict

Name: gnustep-PictureFrame
Version: 1.1.3
Release: alt1
Summary: Software for a digital picture frame
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/pictureframe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
PictureFrame is an application meant to be run on your own home-built
digital picture frame (e.g. an old laptop you've taken apart and mounted
in a nice picture frame). Its a picture viewer for people who want more.
After all, if you have this big powerful computer in your picture frame,
it should be able to do more than just display photos! PictureFrame.app
does do more. At the bottom of the screen, it will display an
information frame containing a clock (digital or analog), information
about the photo being displayed and the current weather and forecast!
PictureFrame.app is expandable, and in the future, more features may be
added.

%package devel
Summary: Development files of PictureFrame
Group: Development/Objective-C
Requires: %name = %EVR

%description devel
PictureFrame is an application meant to be run on your own home-built
digital picture frame (e.g. an old laptop you've taken apart and mounted
in a nice picture frame). Its a picture viewer for people who want more.
After all, if you have this big powerful computer in your picture frame,
it should be able to do more than just display photos! PictureFrame.app
does do more. At the bottom of the screen, it will display an
information frame containing a clock (digital or analog), information
about the photo being displayed and the current weather and forecast!
PictureFrame.app is expandable, and in the future, more features may be
added.

This package contains development files of PictureFrame.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ANNOUNCE ChangeLog PICTURE_FRAMES README
%_bindir/*
%_libdir/GNUstep

%files devel
%_includedir/*

%changelog
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

