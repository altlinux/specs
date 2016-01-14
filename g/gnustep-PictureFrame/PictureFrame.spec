%set_verify_elf_method unresolved=strict

Name: gnustep-PictureFrame
Version: 1.1.3
Release: alt6.1
Summary: Software for a digital picture frame
License: GPL
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/pictureframe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

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
BuildArch: noarch
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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ANNOUNCE ChangeLog PICTURE_FRAMES README
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files devel
%_includedir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt6.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt6
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt5
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt4
- Rebuilt with new gnustep-gui

* Fri Mar 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt3
- Added menu file (thnx kostyalamer@)

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2
- Set devel subpackage as noarch

* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

